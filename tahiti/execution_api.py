# -*- coding: utf-8 -*-}
from flask import request, current_app
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
        result = dict(status="ERROR", message="Insufficient data")
        result_code = 404

        if request.json:
            request_schema = PartialSchemaFactory(ExecutionCreateRequestSchema)
            form = request_schema.load(request.json)
            response_schema = ExecutionItemResponseSchema()
            if not form.errors:
                try:
                    form.data.id = execution_id
                    execution = db.session.merge(form.data)
                    db.session.commit()

                    if execution is not None:
                        result, result_code = dict(
                            status="OK", message="Updated",
                            data=response_schema.dump(execution).data), 200
                    else:
                        result = dict(status="ERROR", message="Not found")
                except Exception, e:
                    result, result_code = dict(status="ERROR",
                                               message="Internal error"), 500
                    if current_app.debug:
                        result['debug_detail'] = e.message
                    db.session.rollback()
            else:
                result = dict(status="ERROR", message="Invalid data",
                            erros=form.errors)
        return result, result_code
