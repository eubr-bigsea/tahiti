# -*- coding: utf-8 -*-}
from flask import request, current_app
from flask_restful import Resource

from app_auth import requires_auth
from models import db, Storage
from schema import *

# region Protected
# endregion


class StorageListApi(Resource):
    """ REST API for listing class Storage """

    @staticmethod
    @requires_auth
    def get():
        only = ('id', 'name') \
            if request.args.get('simple', 'false') == 'true' else None
        storages = Storage.query.all()
        return StorageListResponseSchema(many=True, only=only).dump(storages).data
