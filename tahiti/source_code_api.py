import math
import logging

from tahiti.app_auth import requires_auth, requires_permission

from flask import request
from flask_restful import Resource
from http import HTTPStatus

from tahiti.schema import (SourceCodeCreateRequestSchema, partial_schema_factory,
                           SourceCodeItemResponseSchema,
                           SourceCodeListResponseSchema)
from tahiti.models import SourceCode, db
from flask_babel import gettext

log = logging.getLogger(__name__)
# region Protected\s*
# endregion


class SourceCodeListApi(Resource):
    """ REST API for listing class SourceCode """

    def __init__(self):
        self.human_name = gettext('SourceCode')

    @requires_auth
    def get(self):
        """
        Retrieve a list of instances of class SourceCode.

        :return: A JSON object containing the list of SourceCode instances data.
        :rtype: dict
        """
        if request.args.get('fields'):
            only = [f.strip() for f in request.args.get('fields').split(',')]
        else:
            only = ('id', ) if request.args.get(
                'simple', 'false') == 'true' else None
        enabled_filter = request.args.get('enabled')
        if enabled_filter:
            source_codes = SourceCode.query.filter(
                SourceCode.enabled == (enabled_filter != 'false'))
        else:
            source_codes = SourceCode.query

        ids_filter = request.args.get('ids')
        if ids_filter:
            ids = [int(x) for x in ids_filter.split(',')]
            source_codes = source_codes.filter(SourceCode.id.in_(ids))

        sort = request.args.get('sort', 'name')
        if sort not in ['name']:
            sort = 'name'
        sort_option = getattr(SourceCode, sort)
        if request.args.get('asc', 'true') == 'false':
            sort_option = sort_option.desc()
        source_codes = source_codes.order_by(sort_option)

        page = request.args.get('page') or '1'
        if page is not None and page.isdigit():
            page_size = int(request.args.get('size', 20))
            page = int(page)
            pagination = source_codes.paginate(page, page_size, True)
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
                    source_codes)}

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Listing %(name)s', name=self.human_name))
        return result

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def post(self):
        """
        Add a single instance of class SourceCode.

        :return: A JSON object containing a success message.
        :rtype: dict
        """
        result = {'status': 'ERROR',
                  'message': gettext("Missing json in the request body")}
        return_code = HTTPStatus.BAD_REQUEST

        if request.json is not None:
            request_schema = SourceCodeCreateRequestSchema()
            response_schema = SourceCodeItemResponseSchema()
            source_code = request_schema.load(request.json)

            if log.isEnabledFor(logging.DEBUG):
                log.debug(gettext('Adding %s'), self.human_name)
            source_code = source_code
            db.session.add(source_code)
            db.session.commit()
            result = response_schema.dump(source_code)
            return_code = HTTPStatus.CREATED
        return result, return_code


class SourceCodeDetailApi(Resource):
    """ REST API for a single instance of class SourceCode """

    def __init__(self):
        self.human_name = gettext('SourceCode')

    @requires_auth
    def get(self, source_code_id):
        """
        Retrieve a single instance of class SourceCode.

        :param source_code_id: The ID of the SourceCode instance to retrieve.
        :type source_code_id: int
        :return: A JSON object containing the SourceCode instance data.
        :rtype: dict
        """

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Retrieving %s (id=%s)'), self.human_name,
                      source_code_id)

        source_code = SourceCode.query.get(source_code_id)
        return_code = HTTPStatus.OK
        if source_code is not None:
            result = {
                'status': 'OK',
                'data': [SourceCodeItemResponseSchema().dump(
                    source_code)]
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext(
                    '%(name)s not found (id=%(id)s)',
                    name=self.human_name, id=source_code_id)
            }

        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def delete(self, source_code_id):
        """
        Delete a single instance of class SourceCode.

        :param source_code_id: The ID of the SourceCode instance to delete.
        :type source_code_id: int
        :return: A JSON object containing a success message.
        :rtype: dict
        """

        return_code = HTTPStatus.NO_CONTENT
        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Deleting %s (id=%s)'), self.human_name,
                      source_code_id)
        source_code = SourceCode.query.get(source_code_id)
        if source_code is not None:
            db.session.delete(source_code)
            db.session.commit()
            result = {
                'status': 'OK',
                'message': gettext('%(name)s deleted with success!',
                                   name=self.human_name)
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext('%(name)s not found (id=%(id)s).',
                                   name=self.human_name, id=source_code_id)
            }
        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def patch(self, source_code_id):
        """
        Update a single instance of class SourceCode.

        :param source_code_id: The ID of the SourceCode instance to update.
        :type source_code_id: int
        :return: A JSON object containing a success message.
        :rtype: dict
        """
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Updating %s (id=%s)'), self.human_name,
                      source_code_id)
        if request.json:
            request_schema = partial_schema_factory(
                SourceCodeCreateRequestSchema)
            response_schema = SourceCodeItemResponseSchema()
            # Ignore missing fields to allow partial updates

            data = request.json

            source_code = request_schema.load(data, partial=True)
            source_code.id = source_code_id
            source_code = db.session.merge(source_code)

            db.session.commit()

            if source_code is not None:
                return_code = HTTPStatus.OK
                result = {
                    'status': 'OK',
                    'message': gettext(
                        '%(n)s (id=%(id)s) was updated with success!',
                        n=self.human_name,
                        id=source_code_id),
                    'data': [response_schema.dump(
                        source_code)]
                }
        return result, return_code

