# -*- coding: utf-8 -*-}
import logging

from flask import request, current_app, g
from flask_babel import gettext
from flask_restful import Resource
from http import HTTPStatus
from marshmallow.exceptions import ValidationError

from tahiti.app_auth import requires_auth, requires_permission
from tahiti.schema import *
from tahiti.models import *
from tahiti.util import translate_validation

log = logging.getLogger(__name__)

class SourceCodeListApi(Resource):
    """ REST API for listing class SourceCode """

    def __init__(self):
        self.human_name = gettext('SourceCode')

    @requires_auth
    def get(self):
        all_sourcecodes = request.args.get('all') in ["true", 1, "1"]
        only = None

        description_filter = request.args.get('description')
        if description_filter:
            sourcecodes = SourceCode.query.filter(
                SourceCode.description == (description_filter != 'false'))
        else:
            sourcecodes = SourceCode.query

        page = request.args.get('page') or '1' 
        if page is not None and page.isdigit():
            page_size = int(request.args.get('size', 20))
            page = int(page)
            pagination = sourcecodes.paginate(page, page_size, True)
            result = {
                'data': SourceCodeListResponseSchema(
                    many=True, only=only).dump(pagination.items),
                'pagination': {
                    'page': page, 'size': page_size,
                    'total': pagination.total,
                    'pages': int(math.ceil(1.0 * pagination.total / page_size))}
            }
        else:
            result = {
                'data': SourceCodeListResponseSchema(
                    many=True, only=only).dump(
                    sourcecodes)}

        return result

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def post():
        result = {'status': 'ERROR',
                  'message': gettext("Missing json in the request body")}
        return_code = HTTPStatus.BAD_REQUEST
        
        if request.json is not None:
            request_schema = SourceCodeCreateRequestSchema()
            response_schema = SourceCodeItemResponseSchema()
            sourcecode = request_schema.load(request.json)
            try:
                if log.isEnabledFor(logging.DEBUG):
                    log.debug(gettext('Adding %s'), self.human_name)
                sourcecode = sourcecode
                db.session.add(sourcecode)
                db.session.commit()
                result = response_schema.dump(sourcecode)
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


class SourceCodeDetailApi(Resource):
    """ REST API for a single instance of class SourceCode """

    def __init__(self):
            self.human_name = gettext('SourceCode')

    @requires_auth
    def get(self, sourcecode_id):

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Retrieving %s (id=%s)'), self.human_name,
                      sourcecode_id)

        sourcecode = SourceCode.query.get(sourcecode_id)
        return_code = HTTPStatus.OK
        if sourcecode is not None:
            result = {
                'status': 'OK',
                'data': [SourceCodeItemResponseSchema().dump(
                    sourcecode)]
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext(
                    '%(name)s not found (id=%(id)s)',
                    name=self.human_name, id=sourcecode_id)
            }

        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def delete(self, sourcecode_id):
        return_code = HTTPStatus.NO_CONTENT
        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Deleting %s (id=%s)'), self.human_name,
                      sourcecode_id)
        sourcecode = SourceCode.query.get(sourcecode_id)
        if sourcecode is not None:
            try:
                db.session.delete(sourcecode)
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
                                   name=self.human_name, id=sourcecode_id)
            }
        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def patch(self, sourcecode_id):
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Updating %s (id=%s)'), self.human_name,
                      sourcecode_id)
        if request.json:
            request_schema = partial_schema_factory(
                SourceCodeCreateRequestSchema)
            # Ignore missing fields to allow partial updates
            sourcecode = request_schema.load(request.json, partial=True)
            response_schema = SourceCodeItemResponseSchema()
            try:
                sourcecode.id = sourcecode_id
                sourcecode = db.session.merge(sourcecode)
                db.session.commit()

                if sourcecode is not None:
                    return_code = HTTPStatus.OK
                    result = {
                        'status': 'OK',
                        'message': gettext(
                            '%(n)s (id=%(id)s) was updated with success!',
                            n=self.human_name,
                            id=sourcecode_id),
                        'data': [response_schema.dump(
                            sourcecode)]
                    }
            except ValidationError as e:
                result= {
                   'status': 'ERROR', 
                   'message': gettext('Invalid data for %(name)s (id=%(id)s)',
                                      name=self.human_name,
                                      id=sourcecode_id),
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