# -*- coding: utf-8 -*-}
from tahiti.app_auth import requires_auth, requires_permission
from flask import request, current_app, g as flask_globals
from flask_restful import Resource
from sqlalchemy import or_

import math
import logging
from tahiti.schema import *
from flask_babel import gettext
from tahiti.util import translate_validation

log = logging.getLogger(__name__)

# region Protected\s*
# endregion


class OperationSubsetListApi(Resource):
    """ REST API for listing class OperationSubset """

    def __init__(self):
        self.human_name = gettext('OperationSubset')

    @requires_auth
    def get(self):
        if request.args.get('fields'):
            only = [f.strip() for f in request.args.get('fields').split(',')]
        else:
            only = ('id', ) if request.args.get(
                'simple', 'false') == 'true' else None
        operation_subsets = OperationSubset.query.all()

        page = request.args.get('page') or '1'
        if page is not None and page.isdigit():
            page_size = int(request.args.get('size', 20))
            page = int(page)
            pagination = operation_subsets.paginate(page, page_size, True)
            result = {
                'data': OperationSubsetListResponseSchema(
                    many=True, only=only).dump(pagination.items).data,
                'pagination': {
                    'page': page, 'size': page_size,
                    'total': pagination.total,
                    'pages': int(math.ceil(1.0 * pagination.total / page_size))}
            }
        else:
            result = {
                'data': OperationSubsetListResponseSchema(
                    many=True, only=only).dump(
                    operation_subsets).data}

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Listing %(name)s', name=self.human_name))
        return result

    @requires_auth
    @requires_permission('ADMINISTRATOR')
    def post(self):
        result = {'status': 'ERROR',
                  'message': gettext("Missing json in the request body")}
        return_code = 400
        
        if request.json is not None:

            request_schema = OperationSubsetCreateRequestSchema()
            response_schema = OperationSubsetItemResponseSchema()
            form = request_schema.load(request.json)
            if form.errors:
                result = {'status': 'ERROR',
                          'message': gettext("Validation error"),
                          'errors': translate_validation(form.errors)}
            else:
                try:
                    form.data.platform = Platform.query.get(request.json.get(
                        'platform').get('id'))
                    
                    if log.isEnabledFor(logging.DEBUG):
                        log.debug(gettext('Adding %s'), self.human_name)
                    operation_subset = form.data
                    db.session.add(operation_subset)
                    db.session.commit()
                    result = response_schema.dump(operation_subset).data
                    return_code = 200
                except Exception as e:
                    result = {'status': 'ERROR',
                              'message': gettext("Internal error")}
                    return_code = 500
                    if current_app.debug:
                        result['debug_detail'] = str(e)

                    log.exception(e)
                    db.session.rollback()

        return result, return_code


class OperationSubsetDetailApi(Resource):
    """ REST API for a single instance of class OperationSubset """
    def __init__(self):
        self.human_name = gettext('OperationSubset')

    @requires_auth
    def get(self, subset_id):

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Retrieving %s (id=%s)'), self.human_name,
                      subset_id)
        import pdb; pdb.set_trace()
        operation_subset = OperationSubset.query.get(subset_id)
        return_code = 200
        if operation_subset is not None:
            result = {
                'status': 'OK',
                'data': [OperationSubsetItemResponseSchema().dump(
                    operation_subset).data]
            }
        else:
            return_code = 404
            result = {
                'status': 'ERROR',
                'message': gettext(
                    '%(name)s not found (id=%(id)s)',
                    name=self.human_name, id=subset_id)
            }

        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR')
    def delete(self, subset_id):
        return_code = 200
        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Deleting %s (id=%s)'), self.human_name,
                      subset_id)
        operation_subset = OperationSubset.query.get(subset_id)
        if operation_subset is not None:
            try:
                db.session.delete(operation_subset)
                db.session.commit()
                result = {
                    'status': 'OK',
                    'message': gettext('%(name)s deleted with success!',
                                       name=self.human_name)
                }
            except Exception as e:
                result = {'status': 'ERROR',
                          'message': gettext("Internal error")}
                return_code = 500
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
        else:
            return_code = 404
            result = {
                'status': 'ERROR',
                'message': gettext('%(name)s not found (id=%(id)s).',
                                   name=self.human_name, id=subset_id)
            }
        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR')
    def patch(self, subset_id):
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = 404

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Updating %s (id=%s)'), self.human_name,
                      subset_id)
        if request.json:
            request_schema = partial_schema_factory(
                OperationSubsetCreateRequestSchema)
            # Ignore missing fields to allow partial updates
            form = request_schema.load(request.json, partial=True)
            response_schema = OperationSubsetItemResponseSchema()
            if not form.errors:
                try:
                    form.data.id = subset_id
                    operation_subset = db.session.merge(form.data)
                    db.session.commit()

                    if operation_subset is not None:
                        return_code = 200
                        result = {
                            'status': 'OK',
                            'message': gettext(
                                '%(n)s (id=%(id)s) was updated with success!',
                                n=self.human_name,
                                id=subset_id),
                            'data': [response_schema.dump(
                                operation_subset).data]
                        }
                except Exception as e:
                    result = {'status': 'ERROR',
                              'message': gettext("Internal error")}
                    return_code = 500
                    if current_app.debug:
                        result['debug_detail'] = str(e)
                    db.session.rollback()
            else:
                result = {
                    'status': 'ERROR',
                    'message': gettext('Invalid data for %(name)s (id=%(id)s)',
                                       name=self.human_name,
                                       id=subset_id),
                    'errors': form.errors
                }
        return result, return_code

class OperationSubsetOperationApi(Resource):
    @requires_auth
    @requires_permission('ADMINISTRATOR')
    def delete(self, subset_id, operation_id):
        return_code = 200
        operation_subset = OperationSubset.query.get(subset_id)
        if operation_subset is not None:
            try:
                operation_subset.operations = [op for op in 
                        operation_subset.operations if op.id != operation_id]
                db.session.add(operation_subset)
                db.session.commit()
                result = { 'status': 'OK', }
            except Exception as e:
                result = {'status': 'ERROR',
                          'message': gettext("Internal error")}
                return_code = 500
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
        else:
            return_code = 404
            result = {
                'status': 'ERROR',
                'message': gettext('%(name)s not found (id=%(id)s).',
                                   name=self.human_name, id=subset_id)
            }
        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR')
    def post(self, subset_id, operation_id):
        return_code = 200

        operation_subset = OperationSubset.query.get(subset_id)
        operation = Operation.query.get(operation_id)
        if operation_subset is not None or operation is not None:
            try:
                operation_subset.operations.append(operation)
                db.session.add(operation_subset)
                db.session.commit()
                result = { 'status': 'OK', }
            except Exception as e:
                result = {'status': 'ERROR',
                          'message': gettext("Internal error")}
                return_code = 500
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
        else:
            return_code = 404
            result = {
                'status': 'ERROR',
                'message': gettext('%(name)s not found (id=%(id)s).',
                                   name=self.human_name, id=subset_id)
            }
        return result, return_code

