# -*- coding: utf-8 -*-}
from flask import request
from flask_restful import Resource

from tahiti.app_auth import requires_auth
from tahiti.schema import *


class PlatformListApi(Resource):
    """ REST API for listing class Platform """

    @staticmethod
    @requires_auth
    def get():
        only = ('id', 'name') \
            if request.args.get('simple', 'false') == 'true' else None
        enabled_filter = request.args.get('enabled') in ["true", 1, "1"]
        platforms = Platform.query.filter(
            Platform.enabled == (enabled_filter == enabled_filter))

        platforms = platforms.order_by(Platform.slug)

        return PlatformListResponseSchema(
            many=True, only=only).dump(platforms).data


class PlatformDetailApi(Resource):
    """ REST API for a single instance of class Platform """

    @staticmethod
    @requires_auth
    def get(platform_id):
        platform = Platform.query.get(platform_id)
        if platform is not None:
            return PlatformItemResponseSchema().dump(platform).data
        else:
            return dict(status="ERROR", message="Not found"), 404
