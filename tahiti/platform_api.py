# -*- coding: utf-8 -*-}
import logging
from flask import request
from flask_restful import Resource

from flask_babel import gettext
from tahiti.app_auth import requires_auth
from tahiti.schema import *

log = logging.getLogger(__name__)

class PlatformListApi(Resource):
    """ REST API for listing class Platform """

    @staticmethod
    @requires_auth
    def get():
        only = ('id', 'name') \
            if request.args.get('simple', 'false') == 'true' else None
        all_platforms = request.args.get('all') in ["true", 1, "1"]
        if all_platforms:
            platforms = Platform.query
        else:
            platforms = Platform.query.filter(Platform.enabled)

        platforms = platforms.order_by(Platform.slug)

        return PlatformListResponseSchema(
            many=True, only=only).dump(platforms).data


class PlatformDetailApi(Resource):
    """ REST API for a single instance of class Platform """
    human_name = 'Platform'
    @staticmethod
    @requires_auth
    def get(platform_id):
        platform = Platform.query.get(platform_id)
        if platform is not None:
            return PlatformItemResponseSchema().dump(platform).data
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
            # Ignore missing fields to allow partial updates
            form = request_schema.load(request.json, partial=True)
            response_schema = PlatformItemResponseSchema()
            if not form.errors:
                try:
                    form.data.id = platform_id
                    platform = db.session.merge(form.data)
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
                                platform).data]
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
                                       id=platform_id),
                    'errors': form.errors
                }
        return result, return_code
 
