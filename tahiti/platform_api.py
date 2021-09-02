# -*- coding: utf-8 -*-}
import logging
import math

from flask import request, g
from flask_restful import Resource
from sqlalchemy.sql.expression import bindparam, text
from flask_babel import gettext
from tahiti.app_auth import requires_auth
from tahiti.schema import *
from marshmallow import ValidationError

log = logging.getLogger(__name__)


class PlatformListApi(Resource):
    """ REST API for listing class Platform """

    @staticmethod
    @requires_auth
    def get():
        only = ('id', 'slug', 'name') \
            if request.args.get('simple', 'false') == 'true' else None
        all_platforms = request.args.get('all') in ["true", 1, "1"]
        if all_platforms:
            platforms = Platform.query
        else:
            platforms = Platform.query.filter(Platform.enabled)

        sort = request.args.get('sort', 'name')
        if sort not in ['name', 'id', 'slug'] or sort == 'name':
            current_translation = db.aliased(Platform.current_translation,
                                             name='platform_translation')
            sort_option = PlatformTranslation.name
            platforms = platforms.join(current_translation)
        else:
            sort_option = getattr(Workflow, sort)

        if request.args.get('asc', 'true') == 'false':
            sort_option = sort_option.desc()

        locale = (str(g.get('locale') or 'en'))[:2]
        platforms = platforms.filter(text(
            'platform_translation.locale = :param_locale').bindparams(
            param_locale=locale))

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

        return result


class PlatformDetailApi(Resource):
    """ REST API for a single instance of class Platform """
    human_name = 'Platform'

    @staticmethod
    @requires_auth
    def get(platform_id):
        platform = Platform.query.get(platform_id)
        if platform is not None:
            return {
                'status': 'OK',
                'data': [PlatformItemResponseSchema().dump(
                    platform)]
            }
        else:
            return dict(status="ERROR", message="Not found"), 404

    @requires_auth
    def patch(self, platform_id):
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = 400
        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Updating %s (id=%s)'), self.human_name,
                      platform_id)
        if request.json:
            request_schema = partial_schema_factory(
                PlatformCreateRequestSchema)

            response_schema = PlatformItemResponseSchema()
            try:
                # Ignore missing fields to allow partial updates
                platform = request_schema.load(request.json, partial=True)
                platform.id = platform_id
                platform = db.session.merge(platform)
                db.session.commit()

                if platform is not None:
                    return_code = 200
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
                result = dict(status="ERROR", message=gettext('Invalid data'),
                              errors=e.messages)
                return_code = 400
            except Exception as e:
                result = {'status': 'ERROR',
                          'message': gettext("Internal error")}
                return_code = 500
                log.exception("Error in PATCH")
                db.session.rollback()

        return result, return_code
