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

class PlatformListApi(Resource):
    """ REST API for listing class Platform """

    def __init__(self):
        self.human_name = gettext('Platform')

    @requires_auth
    def get(self):
        if request.args.get('fields'):
            only = [f.strip() for f in request.args.get('fields').split(',')]
        else:
            only = ('id', ) if request.args.get(
                'simple', 'false') == 'true' else None
        enabled_filter = request.args.get('enabled')
        if enabled_filter:
            platforms = Platform.query.filter(
                Platform.enabled == (enabled_filter != 'false'))
        else:
            platforms = Platform.query

        sort = request.args.get('sort', 'name')
        if sort not in ['name']:
            sort = 'name'
        platforms = platforms.join(Platform.current_translation)
        sort_option = getattr(PlatformTranslation, sort)
        if request.args.get('asc', 'true') == 'false':
            sort_option = sort_option.desc()
        platforms = platforms.order_by(sort_option)

        page = request.args.get('page') or '1'
        if page is not None and page.isdigit():
            page_size = int(request.args.get('size', 20))
            page = int(page)
            pagination = platforms.paginate(page, page_size, True)
            result = {
                'data': PlatformListResponseSchema(
                    many=True, only=only).dump(pagination.items),
                'pagination': {
                    'page': page, 'size': page_size,
                    'total': pagination.total,
                    'pages': int(math.ceil(1.0 * pagination.total / page_size))}
            }
        else:
            result = {
                'data': PlatformListResponseSchema(
                    many=True, only=only).dump(
                    platforms)}

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Listing %(name)s', name=self.human_name))
        return result


class PlatformDetailApi(Resource):
    """ REST API for a single instance of class Platform """
    def __init__(self):
        self.human_name = gettext('Platform')

    @requires_auth
    def get(self, platform_id):

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Retrieving %s (id=%s)'), self.human_name,
                      platform_id)

        platform = Platform.query.get(platform_id)
        return_code = HTTPStatus.OK
        if platform is not None:
            result = {
                'status': 'OK',
                'data': [PlatformItemResponseSchema().dump(
                    platform)]
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext(
                    '%(name)s not found (id=%(id)s)',
                    name=self.human_name, id=platform_id)
            }

        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def patch(self, platform_id):
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Updating %s (id=%s)'), self.human_name,
                      platform_id)
        if request.json:
            request_schema = partial_schema_factory(
                PlatformCreateRequestSchema)
            # Ignore missing fields to allow partial updates
            platform = request_schema.load(request.json, partial=True)
            response_schema = PlatformItemResponseSchema()
            try:
                platform.id = platform_id
                platform = db.session.merge(platform)
                db.session.commit()

                if platform is not None:
                    return_code = HTTPStatus.OK
                    result = {
                        'status': 'OK',
                        'message': gettext(
                            '%(n)s (id=%(id)s) was updated with success!',
                            n=self.human_name,
                            id=platform_id),
                        'data': [response_schema.dump(
                            platform)]
                    }
            except ValidationError as e:
                result= {
                   'status': 'ERROR', 
                   'message': gettext('Invalid data for %(name)s (id=%(id)s)',
                                      name=self.human_name,
                                      id=platform_id),
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
