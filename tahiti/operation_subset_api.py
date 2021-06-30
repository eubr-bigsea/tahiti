# -*- coding: utf-8 -*-}
import math
import logging

from tahiti.app_auth import requires_auth, requires_permission
from flask import request, current_app, g as flask_globals
from flask_restful import Resource
from sqlalchemy import or_
from http import HTTPStatus
from marshmallow.exceptions import ValidationError

from tahiti.schema import *
from tahiti.util import translate_validation
from flask_babel import gettext

log = logging.getLogger(__name__)
# region Protected
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
                    many=True, only=only).dump(pagination.items),
                'pagination': {
                    'page': page, 'size': page_size,
                    'total': pagination.total,
                    'pages': int(math.ceil(1.0 * pagination.total / page_size))}
            }
        else:
            result = {
                'data': OperationSubsetListResponseSchema(
                    many=True, only=only).dump(
                    operation_subsets)}

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Listing %(name)s', name=self.human_name))
        return result

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def post(self):
        result = {'status': 'ERROR',
                  'message': gettext("Missing json in the request body")}
        return_code = HTTPStatus.BAD_REQUEST
        
        if request.json is not None:
            request_schema = OperationSubsetCreateRequestSchema()
            response_schema = OperationSubsetItemResponseSchema()
            operation_subset = request_schema.load(request.json)
            try:
                if log.isEnabledFor(logging.DEBUG):
                    log.debug(gettext('Adding %s'), self.human_name)
                operation_subset = operation_subset
                db.session.add(operation_subset)
                db.session.commit()
                result = response_schema.dump(operation_subset)
                return_code = HTTPStatus.CREATED
            except ValidationError as e:
                result= {
                   'status': 'ERROR', 
                   'message': gettext('Invalid data for %(name)s.)',
                                      name=self.human_name),
                   'errors': translate_validation(e.messages)
                }
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
    def get(self, operation_subset_id):

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Retrieving %s (id=%s)'), self.human_name,
                      operation_subset_id)

        operation_subset = OperationSubset.query.get(operation_subset_id)
        return_code = HTTPStatus.OK
        if operation_subset is not None:
            result = {
                'status': 'OK',
                'data': [OperationSubsetItemResponseSchema().dump(
                    operation_subset)]
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext(
                    '%(name)s not found (id=%(id)s)',
                    name=self.human_name, id=operation_subset_id)
            }

        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def delete(self, operation_subset_id):
        return_code = HTTPStatus.NO_CONTENT
        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Deleting %s (id=%s)'), self.human_name,
                      operation_subset_id)
        operation_subset = OperationSubset.query.get(operation_subset_id)
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
                return_code = HTTPStatus.INTERNAL_SERVER_ERROR
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext('%(name)s not found (id=%(id)s).',
                                   name=self.human_name, id=operation_subset_id)
            }
        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def patch(self, operation_subset_id):
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Updating %s (id=%s)'), self.human_name,
                      operation_subset_id)
        if request.json:
            request_schema = partial_schema_factory(
                OperationSubsetCreateRequestSchema)
            # Ignore missing fields to allow partial updates
            operation_subset = request_schema.load(request.json, partial=True)
            response_schema = OperationSubsetItemResponseSchema()
            try:
                operation_subset.id = operation_subset_id
                operation_subset = db.session.merge(operation_subset)
                db.session.commit()

                if operation_subset is not None:
                    return_code = HTTPStatus.OK
                    result = {
                        'status': 'OK',
                        'message': gettext(
                            '%(n)s (id=%(id)s) was updated with success!',
                            n=self.human_name,
                            id=operation_subset_id),
                        'data': [response_schema.dump(
                            operation_subset)]
                    }
            except ValidationError as e:
                result= {
                   'status': 'ERROR', 
                   'message': gettext('Invalid data for %(name)s (id=%(id)s)',
                                      name=self.human_name,
                                      id=operation_subset_id),
                   'errors': translate_validation(e.messages)
                }
            except Exception as e:
                result = {'status': 'ERROR',
                          'message': gettext("Internal error")}
                return_code = 500
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
        return result, return_code
