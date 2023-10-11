import math
import logging

from http import HTTPStatus
from flask import request, g
from flask_restful import Resource
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import text
from flask_babel import gettext
from tahiti.app_auth import (requires_auth, requires_permission)
from tahiti.schema import (PlatformCreateRequestSchema, 
                           PlatformItemResponseSchema, 
                           PlatformListResponseSchema, 
                           partial_schema_factory
                           )
from tahiti.models import Platform, PlatformTranslation, db

log = logging.getLogger(__name__)
# region Protected
# endregion


class PlatformListApi(Resource):
    """ REST API for listing class Platform """

    def __init__(self):
        self.human_name = gettext('Platform')

    @requires_auth
    def get(self):
        all_platforms = request.args.get('all') in ["true", 1, "1"]
        only = None

        if all_platforms:
            platforms = Platform.query
        else:
            only = ('id', 'slug', 'name',) \
                if request.args.get('simple', 'false') == 'true' else None
        enabled_filter = request.args.get('enabled')
        if enabled_filter:
            platforms = Platform.query.filter(
                Platform.enabled == (enabled_filter != 'false'))
        else:
            platforms = Platform.query

        sort = request.args.get('sort', 'name')
        current_translation = db.aliased(Platform.current_translation,
                                         name='platform_translation')
                    
        platforms = platforms.join(Platform.subsets, isouter=True)
        platforms = platforms.join(current_translation)\
            .options(joinedload('current_translation'))\
                .options(joinedload('subsets'))

        if sort not in ['name', 'id', 'slug'] or sort == 'name':
            sort_option = PlatformTranslation.name
        else:
            sort_option = getattr(Platform, sort)

        if request.args.get('asc', 'true') == 'false':
            sort_option = sort_option.desc()

        locale = g.user.locale
        platforms = platforms.filter(text(
            'platform_translation.locale = :param_locale').bindparams(
            param_locale=locale))

        platforms = platforms.order_by(sort_option)

        # Pagination
        page = request.args.get('page', type=int, default=1)
        page_size = request.args.get('size', type=int, default=20)
        pagination = platforms.paginate(page, page_size, True)

        return {
            'data': PlatformListResponseSchema(
                many=True, only=only).dump(pagination.items),
            'pagination': {
                'page': page, 'size': page_size,
                'total': pagination.total,
                'pages': int(math.ceil(1.0 * pagination.total / page_size))}
        }


class PlatformDetailApi(Resource):
    """ REST API for a single instance of class Platform """

    def __init__(self):
        self.human_name = gettext('Platform')

    @requires_auth
    def get(self, platform_id):

        return_code = HTTPStatus.OK

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Retrieving %s (id=%s)'), self.human_name,
                      platform_id)

        platform = Platform.query
        
        current_translation = db.aliased(Platform.current_translation,
                                         name='platform_translation')
        
        platform = platform.join(Platform.subsets, isouter=True)
        platform = platform.join(current_translation)\
            .options(joinedload('current_translation'))\
                .options(joinedload('subsets'))
        platform = platform.filter(Platform.id==platform_id).first()
            
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
            response_schema = PlatformItemResponseSchema()
            # Ignore missing fields to allow partial updates
            platform = request_schema.load(request.json, partial=True)
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
        return result, return_code
