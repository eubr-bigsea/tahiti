# -*- coding: utf-8 -*-}
import logging
import uuid

from flask import request, g
from flask_babel import gettext
from flask_restful import Resource

from tahiti.app_auth import requires_auth
from tahiti.schema import *
from tahiti.workflow_api import get_workflow

log = logging.getLogger(__name__)


class WorkflowFromTemplateApi(Resource):
    @staticmethod
    @requires_auth
    def post():
        params = request.json

        if 'template_id' in params and params.get('template_id'):
            workflow_id = int(params.get('template_id'))
            workflow = get_workflow(workflow_id)

            if workflow.user_id == g.user.id or workflow.is_system_template:
                # clone workflow
                response_schema = WorkflowItemResponseSchema()
                cloned = json.loads(
                    json.dumps(response_schema.dump(workflow)))
                cloned['platform_id'] = cloned['platform']['id']
                cloned['user_id'] = g.user.id
                cloned['user_login'] = g.user.login
                cloned['user_name'] = g.user.name
                cloned['name'] = params.get('name', 'workflow')
                cloned['is_template'] = False
                cloned['is_system_template'] = False
                del cloned['user']

                old_task_ids = {}
                for i, task in enumerate(cloned['tasks']):
                    new_task_id = str(uuid.uuid4())
                    old_task_ids[task['id']] = new_task_id
                    task['id'] = new_task_id
                    task['operation_id'] = task['operation']['id']
                    if not task.get('name'):
                        task['name'] = '{} {}'.format(task['operation']['name'],
                                                      i)

                for flow in cloned['flows']:
                    flow['source_id'] = old_task_ids[flow['source_id']]
                    flow['target_id'] = old_task_ids[flow['target_id']]

                request_schema = WorkflowCreateRequestSchema()
                form = request_schema.load(cloned)
                if not form.errors:
                    new_workflow = form
                    db.session.add(new_workflow)
                    db.session.flush()
                    db.session.commit()
                    result, result_code = response_schema.dump(
                        new_workflow), 200
                else:
                    result, result_code = dict(status="ERROR",
                                               message="Not authorized"), 401
            else:
                result, result_code = dict(status="ERROR",
                                           message="Not authorized"), 401
        else:
            result, result_code = dict(
                status="ERROR", message="Not found"), 404
        return result, result_code
