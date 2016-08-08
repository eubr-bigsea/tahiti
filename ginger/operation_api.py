# -*- coding: utf-8 -*-}
from flask import request
from flask_restful import Resource

from app_auth import requires_auth
from models import db, Operation
from schema import *

# region Protected
# endregion


class OperationListApi(Resource):
    """ REST API for listing class Operation """

    @staticmethod
    @requires_auth
    def get():
        operations = Operation.query.order_by('name')
        return OperationListResponseSchema(many=True).dump(operations).data

    @staticmethod
    @requires_auth
    def post():
        json = request.json
        if json is not None:
            request_schema = OperationCreateRequestSchema()
            response_schema = OperationItemResponseSchema()
            form = request_schema.load(request.json)
            if form.errors:
                return dict(status="ERROR", message="Validation error",
                            errors=form.errors,), 401
            else:
                operation = Operation(**form.data)
                db.session.add(operation)
                db.session.commit()
                return response_schema.dump(
                    dict(status="OK", message="", data=operation)).data
        else:
            return dict(status="ERROR",
                        message="Missing json in the request body"), 401


class OperationDetailApi(Resource):
    """ REST API for a single instance of class Operation """

    @staticmethod
    @requires_auth
    def get(operation_id):
        operation = Operation.query.get(operation_id)
        if operation is not None:
            return OperationItemResponseSchema().dump(operation).data
        else:
            return dict(status="ERROR", message="Not found"), 404

    @staticmethod
    @requires_auth
    def delete(operation_id):
        operation = Operation.query.get(operation_id)
        if operation is not None:
            db.session.delete(operation)
            db.session.commit()
            return dict(status="OK", message="Deleted")
        else:
            return dict(status="ERROR", message="Not found"), 404
    
    @staticmethod
    @requires_auth
    def patch(operation_id):
        if request.json:
            request_schema = OperationCreateRequestSchema(partial=True)
            form = request_schema.load(request.json)
            if not form.errors:
                Operation.query.filter_by(id=operation_id).update(**form.data)
                db.session.commit()
                operation = Operation.query.get(operation_id)
                if operation is not None:
                    return dict(status="OK", message="Updated")
                else:
                    return dict(status="ERROR", message="Not found"), 404
            else:
                return dict(status="ERROR", message="Invalid data",
                            erros=form.errors), 404
        else:
            return dict(status="ERROR", message="Insufficient data"), 404
