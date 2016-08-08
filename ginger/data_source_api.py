# -*- coding: utf-8 -*-}
from flask import request
from flask_restful import Resource

from app_auth import requires_auth
from models import db, DataSource
from schema import *

# region Protected
# endregion


class DataSourceListApi(Resource):
    """ REST API for listing class DataSource """

    @staticmethod
    @requires_auth
    def get():
        data_sources = DataSource.query.all()
        return DataSourceListResponseSchema(many=True).dump(data_sources).data

    @staticmethod
    @requires_auth
    def post():
        json = request.json
        if json is not None:
            request_schema = DataSourceCreateRequestSchema()
            response_schema = DataSourceItemResponseSchema()
            form = request_schema.load(request.json)
            if form.errors:
                return dict(status="ERROR", message="Validation error",
                            errors=form.errors,), 401
            else:
                data_source = DataSource(**form.data)
                db.session.add(data_source)
                db.session.commit()
                return response_schema.dump(
                    dict(status="OK", message="", data=data_source)).data
        else:
            return dict(status="ERROR",
                        message="Missing json in the request body"), 401


class DataSourceDetailApi(Resource):
    """ REST API for a single instance of class DataSource """

    @staticmethod
    @requires_auth
    def get(data_source_id):
        data_source = DataSource.query.get(data_source_id)
        if data_source is not None:
            return DataSourceItemResponseSchema().dump(data_source).data
        else:
            return dict(status="ERROR", message="Not found"), 404

    @staticmethod
    @requires_auth
    def delete(data_source_id):
        data_source = DataSource.query.get(data_source_id)
        if data_source is not None:
            db.session.delete(data_source)
            db.session.commit()
            return dict(status="OK", message="Deleted")
        else:
            return dict(status="ERROR", message="Not found"), 404
    
    @staticmethod
    @requires_auth
    def patch(data_source_id):
        if request.json:
            request_schema = DataSourceCreateRequestSchema(partial=True)
            form = request_schema.load(request.json)
            if not form.errors:
                DataSource.query.filter_by(id=data_source_id).update(**form.data)
                db.session.commit()
                data_source = DataSource.query.get(data_source_id)
                if data_source is not None:
                    return dict(status="OK", message="Updated")
                else:
                    return dict(status="ERROR", message="Not found"), 404
            else:
                return dict(status="ERROR", message="Invalid data",
                            erros=form.errors), 404
        else:
            return dict(status="ERROR", message="Insufficient data"), 404
