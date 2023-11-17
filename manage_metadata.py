import argparse
import logging
import sys
from copy import deepcopy
from difflib import Differ
from itertools import chain
from pprint import pprint
from typing import List

import yaml
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.collections import InstrumentedList

from tahiti.app import app
from tahiti.models import *

# logging.getLogger('sqlalchemy.engine.Engine').setLevel(logging.WARN)


def deep_diff(x, y, parent_key=None, exclude_keys=[], epsilon_keys=[]):
    """
    Take the deep diff of JSON-like dictionaries

    No warranties when keys, or values are None

    """
    EPSILON = 0.5
    rho = 1 - EPSILON

    if x == y:
        return None

    if parent_key in epsilon_keys:
        xfl, yfl = float_or_None(x), float_or_None(y)
        if xfl and yfl and xfl * yfl >= 0 and rho * xfl <= yfl and rho * yfl <= xfl:
            return None

    if type(x) != type(y) or type(x) not in [list, dict]:
        return x, y

    if type(x) == dict:
        d = {}
        for k in x.keys() ^ y.keys():
            if k in exclude_keys:
                continue
            if k in x:
                left = deepcopy(x[k])
                if left is not None:
                    d[k] = (left, None)
            else:
                right = deepcopy(y[k])
                if right is not None:
                    d[k] = (None, right)

        for k in x.keys() & y.keys():
            if k in exclude_keys:
                continue

            next_d = deep_diff(x[k], y[k], parent_key=k, 
                               exclude_keys=exclude_keys, 
                               epsilon_keys=epsilon_keys)
            if next_d is None:
                continue

            d[k] = next_d

        return d if d else None

    # assume a list:
    d = [None] * max(len(x), len(y))
    flipped = False
    if len(x) > len(y):
        flipped = True
        x, y = y, x

    for i, x_val in enumerate(x):
        d[i] = deep_diff(y[i], x_val, parent_key=i, exclude_keys=exclude_keys, 
                         epsilon_keys=epsilon_keys) if flipped else \
        deep_diff(x_val, y[i], parent_key=i, exclude_keys=exclude_keys, 
                  epsilon_keys=epsilon_keys)

    for i in range(len(x), len(y)):
        d[i] = (y[i], None) if flipped else (None, y[i])

    return None if all(map(lambda x: x is None, d)) else d

# We need this helper function as well:
def float_or_None(x):
    try:
        return float(x)
    except ValueError:
        return None

# define a custom representer for strings
def quoted_presenter(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

def sa_vars(row, translation=False):
    if isinstance(row, InstrumentedList):
        row = row[0]
    def _get_t_value(col, r):
        v = col.type.python_type(getattr(r, col.name))
        if translation:
            # import pdb; pdb.set_trace()
            return v if (v and v != 'None') else 'null'
        else:
            return v
    return {
        column.name: _get_t_value(column, row)
        for column in row.__table__.columns
        if (not column.foreign_keys and 
            column.type.python_type(getattr(row, column.name)) is not None and
            'None' != column.type.python_type(getattr(row, column.name)))

    }
def get_interfaces(p):
    result = []
    for interface in p.interfaces:
        result.append({'id': interface.id, 'name': interface.name})
    return result

def dump_platform(platform: Platform):
    d = platform.__dict__
    d = sa_vars(platform)
    d['translations'] = [
       sa_vars(platform.translations['pt']),
       sa_vars(platform.translations['en']),
    ]
    d['translations'] = {
       'pt': sa_vars(platform.translations['pt'], True),
       'en': sa_vars(platform.translations['en'], True),
    }

    return d

def dump_platforms(out=sys.stdout):
    with app.app_context():
        platforms = (Platform
            .query
            .options(joinedload('translations')))
        for platform in platforms:
            dump = dump_platform(platform)
            with open(f'metadata/platforms/{platform.id}.yaml', 'w') as f:
                print(yaml.dump(dump, indent=1, sort_keys=False, 
                    default_flow_style=False), file=f)

def compare_platforms():
    with app.app_context():
        platforms = (Platform
            .query
            .options(joinedload('translations')))
        for platform in platforms:
            dump = dump_platform(platform)
            with open(f'metadata/platforms/{platform.id}.yaml') as f:
                source = yaml.load(f, Loader=yaml.FullLoader)

            diff = deep_diff(dump, source)
            if diff is not None:
                print('*' * 20)
                #print(platform.id)
                #print('*' * 20)
                pprint(diff)
                #print(dump)
                print('*' * 20)

def compare_operations():
    with app.app_context():
        ops = (Operation
            .query
            .options(joinedload('forms.current_translation')) 
            .options(joinedload('ports.current_translation')) 
            .options(joinedload('ports.interfaces.current_translation')) 
            .options(joinedload('forms.fields.current_translation')) 
            .options(joinedload('categories.current_translation')) 
            .options(joinedload('forms')) 
            .options(joinedload('platforms')) 
            .options(joinedload('platforms.current_translation')) 
            .options(joinedload('ports')) 
            .options(joinedload('ports.interfaces')) 
            .options(joinedload('forms.fields')) 
            .options(joinedload('categories'))
            .options(joinedload('scripts'))
            .options(joinedload('translations')))
        for op in ops:
            dump = dump_op(op)
            with open(f'metadata/operations/{op.id}.yaml') as f:
                source = yaml.load(f, Loader=yaml.FullLoader)

            diff = deep_diff(dump, source)
            if diff is not None:
                print('*' * 20)
                #print(platform.id)
                #print('*' * 20)
                pprint(diff)
                #print(dump)
                print('*' * 20)
            
 

def dump_form(form: OperationForm):
    d = form.__dict__
    d = sa_vars(form)
    d['fields'] = [
        dict(chain.from_iterable(
            d.items() for d in (
                sa_vars(p), 
                {'translations': {
                   'pt': sa_vars(p.translations['pt']),
                   'en': sa_vars(p.translations['en']),
                }},
            )
         )) 
        for p in form.fields]
    # import pdb; pdb.set_trace()
    d['translations'] = {
       'pt': sa_vars(form.translations['pt'], True),
       'en': sa_vars(form.translations['en'], True),
    }
    return d
   
def dump_forms(out=sys.stdout, ids=None):
    with app.app_context():
        forms = (OperationForm
            .query
            .options(joinedload('fields'))
            .options(joinedload('fields.current_translation'))
            .options(joinedload('fields.fallback_translation'))
            .options(joinedload('translations'))
            )
        if ids:
            forms = forms.filter(OperationForm.id.in_(ids))
        dd = []
        for form in forms:
            dump = dump_form(form)
            with open(f'metadata/forms/{form.id}.yaml', 'w') as f:
                print(yaml.dump(dump, indent=1, sort_keys=False, 
                    default_flow_style=False), file=f)

def dump_op(op):
    d = op.__dict__
    d = sa_vars(op)
    d['scripts'] = [sa_vars(p) for p in op.scripts]
    d['ports'] = [
        dict(chain.from_iterable(
            d.items() for d in (
                sa_vars(p), 
                {'interfaces': get_interfaces(p)},
                {'translations': {
                   'pt': sa_vars(p.translations['pt'], True),
                   'en': sa_vars(p.translations['en'], True),
                }
             }
            )
         )) 
        for p in op.ports]
    # import pdb; pdb.set_trace()
    d['translations'] = {
       'pt': sa_vars(op.translations['pt'], True),
       'en': sa_vars(op.translations['en'], True),
    }
    d['platforms'] = [{'id': p.id, 'slug': p.slug} for p in op.platforms]
    d['categories'] = [{'id': p.id, 'type': p.type} for p in op.categories]
    d['forms'] = [f.id for f in op.forms]
    return d

def dump_ops(out=sys.stdout, ids=None):
    with app.app_context():
        ops = Operation.query #.limit(1000)
        ops = ops.options(joinedload(Operation.current_translation))

        # .options(db.contains_eager(Operation.current_translation,
        #                           alias=current_translation))
        ops = ops.options(joinedload('forms.current_translation')) \
            .options(joinedload('ports.current_translation')) \
            .options(joinedload('ports.interfaces.current_translation')) \
            .options(joinedload('forms.fields.current_translation')) \
            .options(joinedload('categories.current_translation')) \
            .options(joinedload('forms')) \
            .options(joinedload('platforms')) \
            .options(joinedload('platforms.current_translation')) \
            .options(joinedload('ports')) \
            .options(joinedload('ports.interfaces')) \
            .options(joinedload('forms.fields')) \
            .options(joinedload('categories'))
        if ids:
            ops = ops.filter(Operation.id.in_(ids))
        for op in ops:
            dump = dump_op(op)
            with open(f'metadata/operations/{op.id}.yaml', 'w') as f:
                print(yaml.dump(dump, indent=1, sort_keys=False, 
                    default_flow_style=False), file=f)

def sync(forms: List[int], ops: List[int]):
    sync_forms(forms)
    sync_ops(ops)
    print('Done.')

def sync_ops(ops: List[int]):
    if ops is None or len(ops) == 0:
        print('No operation specified. Sync all operations? ')
        answer = input('(Y/n) > ')
        if answer not in ('y', 'Y'):
            print('Operation sync ignored')
            return 
    for op_id in ops:
        with open(f'metadata/operations/{op_id}.yaml') as f:
            d = yaml.load(f, Loader=yaml.FullLoader)
        d['translations'] = {k: OperationTranslation(**v)
            for k, v in d.get('translations', {}).items()}
        d['scripts'] = [
            OperationScript(**s) for s in d.get('scripts', [])
        ]
        def get_operation_port(s):
            s['translations'] = {k: OperationPortTranslation(**v)
                for k, v in s.get('translations', {}).items()}
            s['interfaces'] = [
                OperationPortInterface(**s) for s in s.get('interfaces', [])
            ]
            port = OperationPort(**s)
            return port

        d['ports'] = [
            get_operation_port(s) for s in d.get('ports', [])
        ]
        d['platforms'] = [
            Platform(**s) for s in d.get('platforms', [])
        ]
        d['categories'] = [
            OperationCategory(**s) for s in d.get('categories', [])
        ]
        d['forms'] = [
            OperationForm(id=s) for s in d.get('forms', [])
        ]
        op = Operation(**d)
        db.session.merge(op)

def sync_forms(forms: List[int]):
    if forms is None or len(forms) == 0:
        print('No form specified. Sync all forms? ')
        answer = input('(Y/n) > ')
        if answer not in ('y', 'Y'):
            print('Form sync ignored')
            return

    for form_id in forms:
        with open(f'metadata/forms/{form_id}.yaml') as f:
            d = yaml.load(f, Loader=yaml.FullLoader)
        d['translations'] = {k: OperationFormTranslation(**v)
            for k, v in d.get('translations', {}).items()}

        def get_fields(s):
            # translations = {k: v for item in s.get('translations', []) for k, v in item.items()}
            #s['translations'] = {k: OperationFormFieldTranslation(**v)
            #    for k, v in translations.items()}
            s['translations'] = {k: OperationFormFieldTranslation(**v)
                for k, v in s.get('translations', {}).items()}
            field = OperationFormField(**s)
            return field
        # import pdb; pdb.set_trace()
        d['fields'] = [get_fields(s) for s in d.get('fields', [])]
        form = OperationForm(**d)
        db.session.merge(form)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a', "--action", type=str, default='dump', required=False,
        help="action to be performed [dump|compare|sync]")
    
    parser.add_argument(
        '-o', "--ops", type=int, nargs='+', required=False,
        help='list of ids of operations, space-separated')
    parser.add_argument(
        '-f', "--forms", type=int, nargs='+', required=False,
        help='list of ids of forms, space-separated')
    args = parser.parse_args()
    if args.action == 'dump':
        #dump_ops(ids=args.ops)
        #dump_platforms()
        dump_forms(ids=args.forms)
    elif args.action == 'compare':
        #compare_platforms()
        compare_operations()
    elif args.action == 'sync':
        with app.app_context():
            sync(args.forms, args.ops)
            db.session.commit()
