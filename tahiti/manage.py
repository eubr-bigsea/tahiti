# -*- coding: utf-8 -*-
import logging
import signal
import sys

from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager

from tahiti.factory import create_app, create_babel_i18n
from tahiti.models import Operation, OperationTranslation, OperationCategory, \
    OperationForm, OperationFormTranslation, OperationPort, \
    OperationPortInterface, OperationPortTranslation, OperationFormField, db, \
    Platform
import collections

app = create_app(log_level=logging.WARNING)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

babel = create_babel_i18n(app)


def signal_handler(s, frame):
    print('You pressed Ctrl+C! Exiting')
    sys.exit(0)


def required_ok(_, v):
    return v is not None and v.strip() != ''


def in_list_ok(options, v):
    return v in options.get('values', [])


def current_order(index):
    return index


create_op_fields = [
    ["name", {"validation": required_ok, 'label': 'Name (EN):'}],
    ["name_pt", {"validation": required_ok, 'label': 'Name (PT):'}],
    ["slug", {"validation": required_ok, 'label': 'Slug:'}],
    ["description", {"validation": required_ok, 'label': 'Description (EN):'}],
    ["description_pt",
     {"validation": required_ok, 'label': 'Description (PT):'}],
    ["type",
     {"validation": in_list_ok, 'values': ['TRANSFORMATION'],
      'label': 'Type:',
      'default': 'TRANSFORMATION'}],
    ["icon", {"validation": required_ok, 'label': 'Icon:'}],
]

create_port_fields = [
    ['type',
     {'validation': in_list_ok, 'values': ['OUTPUT', 'INPUT'],
      'label': 'Port type:',
      'default': 'INPUT'}],
    ['name', {'validation': required_ok, 'label': 'Port name (EN):',
              'default': lambda
                  t: 'input data' if t == 'INPUT' else 'output data'}],
    ['name_pt', {'validation': required_ok, 'label': 'Port name (PT):',
                 'default': lambda
                     t: 'dados de entrada' if t == 'INPUT' else 'dados de saída'}],
    ['description', {'validation': required_ok, 'label': 'Description (EN):',
                     'default': lambda
                         t: 'Input data' if t == 'INPUT' else 'Output data'}],
    ['description_pt',
     {'validation': required_ok, 'label': 'Description (PT):',
      'default': lambda
          t: 'Dados de entrada' if t == 'INPUT' else 'Dados de saída'}],
    ['order', {'validation': required_ok, 'label': 'Order:', 'default': '1'}],
    ['multiplicity',
     {'validation': in_list_ok, 'values': ['MANY', 'ONE'],
      'label': 'multiplicity',
      'default': lambda t: 'ONE' if t == 'INPUT' else 'MANY'}],
]

create_form_field_fields = [
    ['name', {'validation': required_ok, 'label': 'Field name:'}],
    ['label', {'validation': required_ok, 'label': 'Label (EN):'}],
    ['label_pt', {'validation': required_ok, 'label': 'Label (PT):'}],
    ['help', {'validation': required_ok, 'label': 'Help (EN):'}],
    ['help_pt', {'validation': required_ok, 'label': 'Help (PT):'}],
    ['required', {'validation': in_list_ok, 'values': ['1', '0'],
                  'label': 'Required? (1=Yes, 0=No)'}],

    ['type',
     {'validation': in_list_ok,
      'values': ['LAT_LONG', 'DOUBLE', 'DECIMAL', 'FLOAT', 'CHARACTER', 'LONG',
                 'DATETIME', 'TEXT', 'TIME', 'DATE', 'INTEGER'],
      'label': 'Field type:', 'default': 'TEXT'}],

    ['suggested_widget', {'validation': in_list_ok,
                          'values': ['suggested_widget', 'attribute-function',
                                     'attribute-selector',
                                     'checkbox', 'color', 'decimal', 'dropdown',
                                     'expression', 'integer',
                                     'lookup', 'percentage', 'range', 'tag',
                                     'text', 'textarea'],
                          'label': 'Suggested widget:', 'default': 'text'}],
]


@manager.option('-c', '--config', help='Config file')
def create_op(config):
    # Appearance form
    appearance_form = OperationForm.query.filter_by(category='appearance')
    qos_form = OperationForm.query.filter_by(category='infrastructure')
    logging_form = OperationForm.query.filter_by(category='logging')
    security_form = OperationForm.query.filter_by(category='security')

    associated_forms = []
    if not all([appearance_form, qos_form, logging_form, security_form]):
        print('At least one required form does not exist')
        return
    else:
        associated_forms.extend(appearance_form)
        associated_forms.extend(qos_form)
        associated_forms.extend(logging_form)
        associated_forms.extend(security_form)

    print('#' * 20)
    print('1 - Create a new operation')
    print('#' * 20)
    result = {}
    for name, options in create_op_fields:
        while True:
            v = input(
                '{}\n({}) > '.format(options['label'],
                                     options.get('default'))).decode('utf8')
            valid = options['validation'](options, v)

            if not valid:
                default = options.get('default')
                if all([any([v is None, v.strip() == '']), default is not None,
                        default != ""]):
                    result[name] = default
                    break
                else:
                    print('Invalid value for {}'.format(name))
            else:
                result[name] = v
                break
    constructor_params = [pair for pair in iter(result.items()) if pair[0] in ['name', 'description', 'slug', 'type', 'icon']]

    print('Creating operation')
    operation = Operation(enabled=True, **dict(constructor_params))
    db.session.add(operation)
    db.session.flush()
    print('Operation received Id={}'.format(operation.id))

    print('Updating operation translation')
    op_translation_en = OperationTranslation.query.get((operation.id, 'en'))
    op_translation_en.name = result['name']
    op_translation_en.description = result['description']

    op_translation_pt = OperationTranslation.query.get((operation.id, 'pt'))
    op_translation_pt.name = result['name_pt']
    op_translation_pt.description = result['description_pt']

    db.session.add(op_translation_en)
    db.session.add(op_translation_pt)
    db.session.flush()

    print('Creating form')
    form = OperationForm(name='Execution',
                         enabled=True, order=1, category='execution')

    db.session.add(form)
    db.session.flush()

    print('Inserting form translation')
    form_translation_en = OperationFormTranslation.query.get((form.id, 'en'))
    form_translation_en.name = 'Execution'

    form_translation_pt = OperationFormTranslation.query.get((form.id, 'pt'))
    form_translation_pt.name = 'Execução'

    db.session.add(form_translation_en)
    db.session.add(form_translation_pt)
    db.session.flush()

    print('Associating forms (including common ones) to operation')
    associated_forms.append(form)

    operation.forms.extend(associated_forms)
    db.session.add(operation)
    db.session.flush()

    db.session.commit()
    define_op_platform(None, operation.id)
    define_op_categ(None, operation.id)
    if input('Would you like to add ports? \n (y, N) >').lower() == 'y':
        define_op_ports(None, operation.id)

    print('DONE!')


@manager.option('-c', '--config', help='Config file')
@manager.option('--op_id', help='Operation id')
def define_op_platform(config, op_id):
    operation = Operation.query.get(op_id)
    platforms = Platform.query.all()
    if operation:
        print('-' * 40)
        print('Platforms')
        all_platforms = {}
        for c in platforms:
            all_platforms[c.id] = c
            print('{} - {}'.format(c.id, c.name))
        print('-' * 40)
        c = input('Inform ids separated by comma and press ENTER\n> ')
        ids = [x.strip() for x in c.split(',')]
        for _id in ids:
            if _id.isdigit():
                plat_id = int(_id)
                if plat_id in all_platforms:
                    operation.platforms.append(all_platforms[plat_id])

        db.session.add(operation)
        db.session.commit()
        print('DONE!')
    else:
        print("Operation {} does not exist".format(op_id))


@manager.option('-c', '--config', help='Config file')
@manager.option('--op_id', help='Operation id')
def define_op_categ(config, op_id):
    operation = Operation.query.get(op_id)
    categories = OperationCategory.query.all()
    if operation:
        print('-' * 40)
        print('Categories')
        all_categ = {}
        for c in categories:
            all_categ[c.id] = c
            print('{} - {} ({})'.format(c.id, c.name, c.type))
        print('-' * 40)
        c = input('Inform ids separated by comma and press ENTER\n> ')
        ids = [x.strip() for x in c.split(',')]
        for _id in ids:
            if _id.isdigit():
                cat_id = int(_id)
                if cat_id in all_categ:
                    operation.categories.append(all_categ[cat_id])

        db.session.add(operation)
        db.session.commit()
        print('DONE!')
    else:
        print("Operation {} does not exist".format(op_id))


@manager.option('-c', '--config', help='Config file')
@manager.option('--op_id', help='Operation id')
@manager.option('--cat', help='Form category')
def define_form_field(config, op_id, cat='execution'):
    operation = Operation.query.get(op_id)
    forms = [f for f in operation.forms if f.category == cat]
    if len(forms) == 1:
        print('-' * 40)
        print('Adding fiels for operation {}- {}'.format(operation.id,
                                                         operation.name))
        print('-' * 40)
        form = forms[0]

        counter = 1
        while True:
            result = {}
            for name, options in create_form_field_fields:
                while True:
                    values = ', '.join(options.get('values', []))

                    v = input('{}\n({})[{}] > '.format(
                        options['label'], options.get('default'),
                        values)).decode('utf8')
                    valid = options['validation'](options, v)

                    if not valid:
                        default = options.get('default')
                        if all([any([v is None, v.strip() == '']),
                                default is not None,
                                default != ""]):
                            result[name] = default
                            break
                        else:
                            print('Invalid value for {}'.format(name))
                    else:
                        result[name] = v
                        break

            constructor_params = [pair for pair in iter(result.items()) if pair[0] not in ['label_pt',
                                             'help_pt']]

            field = OperationFormField(**dict(constructor_params))
            field.scope = 'EXECUTION'
            field.order = counter
            for lang in ['en', 'pt']:
                field.translations['en'].label = result['label']
                field.translations['en'].help = result['help']
                field.translations['pt'].label = result['label_pt']
                field.translations['pt'].help = result['help_pt']

            field.form = form
            counter += 1
            db.session.add(field)
            db.session.flush()
            db.session.commit()

            if input('Add another field?\n (Y,n)> ') in ['n', 'N']:
                break
    else:
        print("Form for operation {} execution is not configured correctly".format(
            operation.name))


@manager.option('-c', '--config', help='Config file')
@manager.option('--op_id', help='Operation id')
def define_op_ports(config, op_id):
    operation = Operation.query.get(op_id)
    if operation:
        print('-' * 40)
        print('Adding ports for operation {} - {}'.format(operation.id,
                                                          operation.name))
        print('-' * 40)
        result = {}

        while True:
            for name, options in create_port_fields:
                while True:
                    d = options.get('default')
                    default = d(result['type']) if isinstance(d, collections.Callable) else d
                    v = input(
                        '{}\n({}) > '.format(options['label'],
                                             default)).decode(
                        'utf8')
                    valid = options['validation'](options, v)

                    if not valid:
                        if all([any([v is None, v.strip() == '']),
                                default is not None,
                                default != ""]):
                            result[name] = default
                            break
                        else:
                            print('Invalid value for {}'.format(name))
                    else:
                        result[name] = v
                        break

            constructor_params = [pair for pair in iter(result.items()) if pair[0] not in ['name', 'description', 'name_pt',
                                             'description_pt']]

            print('Creating port {}'.format(result['name']))
            port = OperationPort(**dict(constructor_params))

            port.operation = operation
            db.session.add(port)
            db.session.flush()

            print('Inserting port translation')
            port_en = OperationPortTranslation.query.get((port.id, 'en'))
            port_en.name = result['name']
            port_en.description = result['description']

            port_pt = OperationPortTranslation.query.get((port.id, 'pt'))
            port_pt.name = result['name_pt']
            port_pt.description = result['description_pt']

            db.session.add(port_en)
            db.session.add(port_pt)
            db.session.flush()

            print('Port interfaces')
            interfaces = OperationPortInterface.query.all()
            print('-' * 40)

            all_interfaces = {}
            for i in interfaces:
                all_interfaces[i.id] = i
                print('{} - {}'.format(i.id, i.name))
            print('-' * 40)

            ids = [x.strip() for x in
                   input('Which interfaces does the port support? Inform a '
                             'list of ids, separated by comma\n> ').split(',')]

            for _id in ids:
                if _id.isdigit():
                    interface_id = int(_id)
                    if interface_id in all_interfaces:
                        port.interfaces.append(
                            all_interfaces[interface_id])

            db.session.add(port)
            db.session.flush()
            db.session.commit()
            if input('Add another port?\n (Y,n)> ') in ['n', 'N']:
                break
    else:
        print("Operation {} does not exist".format(op_id))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    manager.run()
