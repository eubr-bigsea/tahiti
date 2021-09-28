# -*- coding: utf-8 -*-}
import itertools
import locale
import unicodedata
import logging
from functools import reduce, cmp_to_key

from flask import request, current_app, g
from flask_restful import Resource
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import bindparam, text

from tahiti.app_auth import requires_auth, requires_permission
from tahiti.cache import cache
from tahiti.schema import *
from tahiti.models import *

log = logging.getLogger(__name__)


def handle_conflicts(v1, v2):
    result = v2
    if isinstance(v1, list) and isinstance(v2, list):
        result = []
        result.extend(v1)
        result.extend(v2)

    return result


def deep_merge(d1, d2, in_conflict=lambda v1, v2: v2):
    """ merge d2 into d1. using in conflict function to
    resolve the leaf conflicts """
    for k in d2:
        if k in d1:
            if isinstance(d1[k], dict) and isinstance(d2[k], dict):
                deep_merge(d1[k], d2[k], in_conflict)
            elif d1[k] != d2[k]:
                d1[k] = in_conflict(d1[k], d2[k])
        else:
            d1[k] = d2[k]
    return d1


def optimize_operation_query(operations, only_translation=False):
    current_translation = db.aliased(Operation.current_translation,
                                     name='operation_translation')
    # fallback_translation = db.aliased(Operation.fallback_translation)
    op = operations \
        .join(current_translation).options(joinedload('current_translation'))
    # .options(db.contains_eager(Operation.current_translation,
    #                           alias=current_translation))
    if not only_translation:
        op = op.options(joinedload('forms.current_translation')) \
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
    return op


class OperationListApi(Resource):
    """ REST API for listing class Operation """

    @staticmethod
    @requires_auth
    def get():
        @cache.memoize(3600 * 24, make_name=lambda f: request.url)
        def result():
            config = current_app.config['TAHITI_CONFIG']

            simple = request.args.get('simple', 'false') == 'true'
            if request.args.get('fields'):
                only = [x.strip() for x in
                        request.args.get('fields').split(',')]
            else:
                only = ('id', 'name', 'slug') \
                    if simple else None

            exclude = []

            if simple:
                operations = Operation.query
                operations = operations.options(
                    joinedload('current_translation'))
            elif request.args.get('partial') in ('true', 1, '1'):
                operations = optimize_operation_query(Operation.query, True)\
                    .options(joinedload('categories.current_translation')) \
                    .options(joinedload('categories'))

                exclude = ['forms', 'ports', 'platforms']
            else:
                operations = optimize_operation_query(Operation.query)

            # if only:
            #     current_translation = Operation.current_translation
            #     names = {'id': 'operation.id',
            #     'name': 'operation_translation.name'}
            #     operations = operations.join(current_translation).with_entities(
            #         *[column(c) for c in only])
            #     import pdb; pdb.set_trace()

            disabled_filter = request.args.get('disabled')
            if not disabled_filter:
                operations = operations.filter(Operation.enabled)

            subset_filter = request.args.get('subset')
            if subset_filter and subset_filter.isdigit():
                sub_query = OperationSubset.query\
                    .join(OperationSubset.operations).filter(
                        OperationSubset.id == subset_filter)\
                    .with_entities(Operation.id).subquery()
                operations = operations.filter(Operation.id.in_(sub_query))

            platform = request.args.get('platform', None)
            if platform:
                if platform.isdigit():
                    operations = operations.filter(
                        Operation.platforms.any(enabled=True, id=int(platform)))
                else:
                    operations = operations.filter(
                        Operation.platforms.any(enabled=True, slug=platform))
            else:
                operations = operations.filter(
                    Operation.platforms.any(enabled=True))

            workflow = request.args.get('workflow', None)
            if workflow:
                tasks = db.session.query(Task.operation_id).filter(
                    Task.workflow_id == int(workflow)).subquery()
                operations = operations.filter(Operation.id.in_(tasks))

            ids = request.args.getlist('ids[]')
            if ids:
                operations = operations.filter(Operation.id.in_(
                    [int(x) for x in ids]))

            name = request.args.get('name', '')
            # SqlAlchemy-i18n is not working when a filter
            # is used in where clause with a translation table field.
            # In order to optimize the query, I'm using text() query here
            # to write SQL. Notice that the name operation_translation
            # is generated by SqlAlchemy and it is hard coded here.
            if name is not None and name.strip():
                param_name = bindparam('param_name',
                                       '%%{}%%'.format(name),
                                       Unicode)
                operations = operations.filter(text(
                    'operation_translation.name LIKE :param_name').bindparams(
                        param_name=f'%%{name}%%'))
                #operations = operations.filter(OperationTranslation.name.ilike(
                #    '%' + name + '%'))

            current_locale = g.user.locale

            if platform == '5':  # FIXME hard coded
                bindparam('param_locale', 'en', Unicode)
            else:
                bindparam('param_locale', locale, Unicode)

            operations = operations.filter(text(
                'operation_translation.locale = :param_locale').bindparams(
                    param_locale=current_locale))

            exclude.extend(['platforms.icon',
                            'platforms.description'])

            category = request.args.get('category')
            if category:
                operations = operations.join(Operation.categories).filter(
                    OperationCategory.type == category)

            page = request.args.get('page')

            # Operations disabled in config file
            disabled_ops = set(config.get(
                'operations', {}).get('disabled', []))
            if page is not None and page.isdigit():
                page_size = int(request.args.get('size', 20))
                page = int(page)
                try:
                    s = request.args.get('sort')
                    if s == 'name':
                        s = 'operation_translation.name'
                    else:
                        s = '1'
                    if request.args.get('asc') == 'true':
                        s += ' ASC '
                    else:
                        s += ' DESC'
                    operations = operations.order_by(text(s))
                    pagination = operations.paginate(page, page_size, True)
                    items = pagination.items
                    for item in items:
                        if item.id in disabled_ops:
                            item.enabled = False
                    results = {
                        'data': OperationListResponseSchema(many=True,
                                                            exclude=exclude,
                                                            only=only).dump(
                            items),
                        'pagination': {'page': page, 'size': page_size,
                                       'total': pagination.total,
                                       'pages': pagination.total / page_size + 1
                                       }}
                except Exception as e:
                    raise
            else:
                operations = operations.order_by(
                    text('operation_translation.name'))
                items = operations
                for item in items:
                    if item.id in disabled_ops:
                        db.session.expunge(item)
                        item.enabled = False

                data = OperationListResponseSchema(
                    many=True, only=only, exclude=exclude).dump(items)

                # Group forms with same type
                if only is None or 'forms' in only:
                    for op in data:
                        groups = itertools.groupby(
                            sorted(op.get('forms', {}),
                                   key=lambda f: f.get('category')),
                            lambda f: f.get('category'))

                        op['forms'] = []

                        for key, group in groups:
                            merged = reduce(
                                lambda v1, v2: deep_merge(v1, v2,
                                                          handle_conflicts),
                                group, {})
                            op['forms'].append(merged)
                results = {'data': data}

            return results

        return result()


class OperationDetailApi(Resource):
    """ REST API for a single instance of class Operation """

    @staticmethod
    @requires_auth
    def get(operation_id):
        @cache.memoize(600, make_name=lambda f: request.url)
        def result():
            operation = optimize_operation_query(
                Operation.query.filter_by(
                    id=operation_id)).first()
            if operation is not None:
                return OperationItemResponseSchema().dump(operation)
            else:
                return dict(status="ERROR", message="Not found"), 404

        return result()

    @staticmethod
    @requires_auth
    @requires_permission('ADMINISTRATOR')
    def patch(operation_id):
        result = dict(status="ERROR", message="Insufficient data")
        result_code = 400

        if request.json:
            request_schema = partial_schema_factory(
                OperationCreateRequestSchema)
            form = request_schema.load(request.json)
            response_schema = OperationItemResponseSchema()
            if not form.errors:
                try:
                    form.id = operation_id
                    operation = db.session.merge(form)
                    db.session.commit()

                    if operation is not None:
                        result, result_code = dict(
                            status="OK", message="Updated",
                            data=response_schema.dump(operation)), 200
                        cache.clear()
                    else:
                        result = dict(status="ERROR", message="Not found")
                except Exception as e:
                    log.exception('Error in PATCH')
                    result, result_code = dict(status="ERROR",
                                               message="Internal error"), 500
                    if current_app.debug:
                        result['debug_detail'] = e.message
                    db.session.rollback()
            else:
                result = dict(status="ERROR", message="Invalid data",
                              errors=form.errors)
        return result, result_code


class OperationClearCacheApi(Resource):
    # noinspection PyMethodMayBeStatic
    @staticmethod
    @requires_auth
    def post():
        cache.clear()
        return '{"msg": "Cache cleaned"}', 200


class OperationTreeApi(Resource):
    @staticmethod
    # @requires_auth
    def get(platform_id):
        operations = Operation.query.filter(Operation.enabled).filter(
            Operation.platforms.any(enabled=True, id=platform_id))
        current_translation = db.aliased(Operation.current_translation)
        operations = operations \
            .join(current_translation) \
            .options(db.contains_eager(Operation.current_translation,
                                       alias=current_translation)) \
            .options(joinedload('categories.current_translation')) \
            .options(joinedload('categories'))

        def extract_group(c): return {
            'id': c.id, 'name': c.name, 'order': c.order or c.default_order}

        def filter_group(c): return c.type == 'group'
        def filter_subgroup(c): return c.type == 'subgroup'

        ops = []
        for op in operations:
            group = next(map(extract_group, filter(
                filter_group, op.categories)), None)
            subgroup = next(map(extract_group, filter(
                filter_subgroup, op.categories)), None)
            item = {
                'group_id': group['id'] if group is not None else None,
                'subgroup_id': subgroup['id'] if subgroup is not None else None,
                'group': group['name'] if group is not None else None,
                'operation': {'id': op.id, 'name': op.name, 'slug': op.slug},
                'subgroup': subgroup['name'] if subgroup is not None else None,
                'order': group['order'] if group is not None else None,
                'subgroupOrder': subgroup['order'] if subgroup is not None else None
            }
            ops.append(item)

            def cmp_groups(a, b):
                if a['order'] is None:
                    return -1
                if b['order'] is None:
                    return 1
                if a['order'] < b['order']:
                    return -1
                if a['order'] > b['order']:
                    return 1
                text_cmp = locale.strcoll(unicodedata.normalize('NFC', a['group'] or ''),
                                          unicodedata.normalize('NFC', b['group'] or ''))
                if text_cmp != 0:
                    return text_cmp
                text_cmp = locale.strcoll(
                    unicodedata.normalize('NFC', a['subgroup'] or ''),
                    unicodedata.normalize('NFC', b['subgroup'] or ''))
                if text_cmp != 0:
                    return text_cmp
                return locale.strcoll(
                    unicodedata.normalize('NFC', a['operation']['name']),
                    unicodedata.normalize('NFC', b['operation']['name']))

            ops = sorted(ops, key=cmp_to_key(cmp_groups))
            groups = []
            for k, g in itertools.groupby(ops, key=lambda x: x['group_id']):
                for i, nested in enumerate(g):
                    if i == 0:
                        g = {'id': nested['group_id'],
                             'name': nested['group'], 'operations': []}
                        groups.append(g)
                    g['operations'].append(nested['operation'])

        only = None
        exclude = ['forms', 'platforms', 'ports']
        result = OperationListResponseSchema(
            many=True, only=only, exclude=exclude).dump(operations)

        return groups, 200

# class OperationSubsetApi(Operation):
#     human_name = 'OperationSubset'

#     def post():
#         result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
#         return_code = 400

#         if request.json:
#             try:
#                 op_id = request.json.get('operation_id')
#                 subset_id = request.json.get('subset_id')
#                 if op_id and subset_id:
#                     op = Operation.filter.get(op_id)
#                     subset = OperationSubset.query.get(subset_id)

#                     if op.platform.id == subset.platform_id:
#                         oso = OperationSubsetOperation(operation=op, subset=subset)
#                         db.session.add(oso)
#                         db.session.commit();
#                         result = {
#                             'status': 'OK',
#                             'message': gettext(
#                                 '%(n)s (id=%(id)s) was updated with success!',
#                                 n=self.human_name,
#                                 id=platform_id)
#                         }
#             except Exception as e:
#                 result = {'status': 'ERROR',
#                               'message': gettext("Internal error")}
#                 return_code = 500
#                 db.session.rollback()

#         return result, return_code
