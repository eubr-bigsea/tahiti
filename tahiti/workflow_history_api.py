# -*- coding: utf-8 -*-}
import logging

from flask import request, g
from flask_babel import gettext
from flask_restful import Resource

from marshmallow.exceptions import ValidationError
from tahiti.app_auth import requires_auth
from tahiti.schema import *
from tahiti.workflow_api import get_workflow

log = logging.getLogger(__name__)


class WorkflowHistoryApi(Resource):
    @staticmethod
    @requires_auth
    def post(workflow_id):
        result, result_code = dict(status="ERROR", message="Not found"), 404
        params = request.json

        if 'version' in params:
            workflow = get_workflow(workflow_id)
            if workflow.user_id == g.user.id:
                version = int(params['version'])
                history = WorkflowHistory.query.filter(
                    WorkflowHistory.workflow_id == workflow_id,
                    WorkflowHistory.version == version).one()
                # return json.load(history.content), 200
                old = json.loads(history.content)
                old['platform_id'] = old['platform']['id']
                old['user_id'] = g.user.id
                old['user_login'] = g.user.login
                old['user_name'] = g.user.name
                del old['user']

                for i, task in enumerate(old['tasks']):
                    task['operation_id'] = task['operation']['id']
                    if not task.get('name'):
                        task['name'] = f"{task['operation']['name']} {i}"
                try:
                    result_code = 200

                    current_workflow = Workflow.query.get(workflow_id)
                    current_workflow.version += 1

                    response_schema = WorkflowItemResponseSchema()
                    historical_data = json.dumps(
                        response_schema.dump(current_workflow))
                    db.session.expunge(current_workflow)
                    #db.session.delete(history)
                    db.session.flush()

                    new_history = WorkflowHistory(
                            user_id=g.user.id, user_name=g.user.name,
                            user_login=g.user.login,
                            version=workflow.version,
                            workflow=workflow, content=historical_data)
                    
                    workflow = WorkflowCreateRequestSchema().load(old)
                    workflow.id = workflow_id
                    db.session.add(new_history)
                    db.session.flush()
                    db.session.merge(workflow)

                    db.session.commit()
                    result = {'status': 'OK', 
                    'message': gettext(
                        'Workflow restored to version {}. '
                        'A new version was created').format(version)}
                except ValidationError:
                    msg = gettext(
                        "Version %(version)s is not compatible anymore.",
                        version=params['version'])
                    result_code = 400
                    result = dict(status="ERROR", message=msg)
            else:
                result, result_code = dict(
                    status="ERROR", message=gettext("Not authorized")), 401

        return result, result_code

    @staticmethod
    @requires_auth
    def get(workflow_id):
        history = WorkflowHistory.query.filter(
            WorkflowHistory.workflow_id == workflow_id).order_by(
            WorkflowHistory.date.desc()).limit(20)
        only = ('id', 'date', 'version', 'user_name')
        return {'data': WorkflowHistoryListResponseSchema(
            many=True, only=only).dump(history)}
