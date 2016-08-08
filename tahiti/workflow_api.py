# -*- coding: utf-8 -*-}
import datetime
from flask import request, g
from flask_restful import Resource

from app_auth import requires_auth
from models import db, Workflow, Execution, StatusExecution
from schema import *


# region Protected


class WorkflowExecuteListApi(Resource):
    """ REST API for listing class Workflow """

    @staticmethod
    @requires_auth
    def post():
        json = request.json
        if json is not None:
            request_schema = WorkflowExecuteRequestSchema()
            response_schema = ExecutionItemResponseSchema()
            task_schema = TaskExecuteRequestSchema()
            form = request_schema.load(request.json)
            if form.errors:
                return dict(status="ERROR", message="Validation error",
                            errors=form.errors, ), 401
            else:
                tasks = form.data.pop('tasks')
                user = getattr(g, 'user')
                execution = Execution(
                    created=datetime.datetime.now(),
                    status=StatusExecution.PENDING,
                    workflow_id=form.data.get("id"),
                    workflow_name=form.data.get("name"),
                    workflow_definition=task_schema.dumps(
                        tasks, many=True).data,
                    user_id=user.id,
                    user_login=user.login,
                    user_name=user.name)

                db.session.add(execution)
                db.session.commit()
                return dict(status="OK", message="",
                            data=response_schema.dump(execution).data)
        else:
            return dict(status="ERROR",
                        message="Missing json in the request body"), 401

# endregion
