# -*- coding: utf-8 -*-}
from flask import request
from flask_restful import Resource

from app_auth import requires_auth
from models import db, Storage
from schema import *


class StorageListApi(Resource):
    """ REST API for listing class Storage """

    @staticmethod
    @requires_auth
    def get():
        storages = Storage.query.all()
        return StorageListResponseSchema(many=True).dump(storages).data

    @staticmethod
    @requires_auth
    def post():
        json = request.json
        request_schema = StorageCreateRequestSchema()
        response_schema = StorageItemResponseSchema()
        validation_errors = request_schema.validate(json)
        if validation_errors:
            return dict(status="ERROR", message="Validation error",
                        errors=validation_errors)
        else:
            storage = Storage(**json)
            db.session.add(storage)
            db.session.commit()
            return response_schema.dump(
                dict(status="OK", message="", data=storage)).data
