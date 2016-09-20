# -*- coding: utf-8 -*-}
from flask import request
from flask_restful import Resource

from app_auth import requires_auth
from models import db, Execution
from schema import *

# region Protected
# endregion


class ExecutionListApi(Resource):
    """ REST API for listing class Execution """

    @staticmethod
    @requires_auth
    def get():
        only = ('id', 'name') \
            if request.args.get('simple', 'false') == 'true' else None
        executions = Execution.query.all()
        return ExecutionListResponseSchema(many=True, only=only).dump(executions).data


class ExecutionDetailApi(Resource):
    """ REST API for a single instance of class Execution """

    @staticmethod
    @requires_auth
    def get(execution_id):
        execution = Execution.query.get(execution_id)
        if execution is not None:
            return ExecutionItemResponseSchema().dump(execution).data
        else:
            return dict(status="ERROR", message="Not found"), 404

    @staticmethod
    @requires_auth
    def patch(execution_id):
        if request.json:
            request_schema = ExecutionCreateRequestSchema(partial=True)
            form = request_schema.load(request.json)
            if not form.errors:
                Execution.query.filter_by(id=execution_id).update(**form.data)
                db.session.commit()
                execution = Execution.query.get(execution_id)
                if execution is not None:
                    return dict(status="OK", message="Updated")
                else:
                    return dict(status="ERROR", message="Not found"), 404
            else:
                return dict(status="ERROR", message="Invalid data",
                            erros=form.errors), 404
        else:
            return dict(status="ERROR", message="Insufficient data"), 404
