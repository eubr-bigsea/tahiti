# -*- coding: utf-8 -*-}
import datetime

import pytz
from flask import request, g
from flask_restful import Resource

from app_auth import requires_auth
from models import db, Workflow, Execution, StatusExecution, TaskExecution
from schema import *


# region Protected


class WorkflowExecuteListApi(Resource):
    """ REST API for listing class Workflow """

    @staticmethod
    @requires_auth
    def post():
        if request.json is not None:
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
                    created=datetime.datetime.now(pytz.utc),
                    status=StatusExecution.PENDING,
                    workflow_id=form.data.get("id"),
                    workflow_name=form.data.get("name"),
                    workflow_definition=task_schema.dumps(
                        tasks, many=True).data,
                    user_id=user.id,
                    user_login=user.login,
                    user_name=user.name)

                for task in tasks:
                    task_exec = TaskExecution(
                        date=datetime.datetime.now(pytz.utc),
                        status=StatusExecution.PENDING,
                        task_id=task.get('id'),
                        operation_id=task.get('operation_id'),
                        operation_name=task.get('operation_name'),
                        execution=execution)
                    db.session.add(task_exec)

                db.session.add(execution)
                db.session.commit()
                return dict(status="OK", message="",
                            data=response_schema.dump(execution).data)
        else:
            return dict(status="ERROR",
                        message="Missing json in the request body"), 401

# endregion
