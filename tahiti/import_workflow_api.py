# -*- coding: utf-8 -*-}
import logging
import uuid

import requests
from flask import request, current_app, g
from flask_babel import gettext
from flask_restful import Resource

from marshmallow.exceptions import ValidationError
from tahiti.app_auth import requires_auth
from tahiti.schema import *

log = logging.getLogger(__name__)


def update_port_name_in_flows(session, workflow_id):
    sql = """
        UPDATE flow f, task ts, task tt,
        	operation_port os, operation_port ot
        SET source_port_name = os.slug, target_port_name = ot.slug,
            source_port = os.id, target_port = ot.id
        WHERE 
        	f.source_id  = ts.id 
        	AND f.target_id  = tt.id
        	AND os.operation_id = ts.operation_id 
        	AND ot.operation_id = tt.operation_id 
        	AND (os.slug = f.source_port_name OR os.id = f.source_port)
        	AND (ot.slug = f.target_port_name OR ot.id = f.target_port)
        	AND f.workflow_id = :id"""
    session.execute(sql, {'id': workflow_id})


class ImportWorkflowApi(Resource):
    @staticmethod
    @requires_auth
    def post():
        url = request.form.get('url')
        token = request.form.get('token')
        contents = request.json if request.json else None

        # Imports from URL
        if not contents:
            if not all([url, token]):
                return {'error': gettext('Missing url or token parameter'),
                        'status': 'ERROR'}, 400
            r = requests.get(url, headers={"X-Auth-Token": token})
            if r.status_code == 200:
                contents = r.text
                original = json.loads(contents)
            else:
                return gettext('Error reading source workflow:') + \
                    r.status_code + '\n' + r.text, 400
        else:
            original = json.loads(contents.get('content'))
        # noinspection PyBroadException
        try:
            platform = original.pop('platform')

            if 'forms' in original:
                original['form'] = json.dumps(original.pop('forms'))
            user = g.user
            original.pop('user')
            original['platform'] = Platform.query.get(platform['id'])
            original['user_id'] = user.id
            original['user_login'] = user.login
            original['user_name'] = user.name
            original['platform_id'] = platform['id']

            original_task_ids = {}
            for task in original['tasks']:
                task['operation_id'] = task['operation']['id']
                new_id = str(uuid.uuid4())
                original_task_ids[task['id']] = new_id
                task['id'] = new_id

            # updates flows
            for flow in original['flows']:
                flow['source_id'] = original_task_ids[flow['source_id']]
                flow['target_id'] = original_task_ids[flow['target_id']]

            request_schema = WorkflowCreateRequestSchema()

            # Handle variables parameters serialization
            for variable in original.get('variables', []):
                if 'parameters' in variable:
                    variable['parameters'] = json.dumps(variable['parameters'])
            workflow = request_schema.load(original)
            try:
                db.session.add(workflow)
                db.session.flush()
                update_port_name_in_flows(db.session, workflow.id)
                db.session.commit()
                result, result_code = workflow.id, 200
            except ValidationError as e:
                result = {
                    'status': 'ERROR',
                    'message': gettext('Invalid data for %(name)s.)',
                                       name='workflow'),
                    'errors': e.messages
                }
            except Exception as e:
                log.exception('Error in POST')
                result = {
                    'status': 'ERROR', 'message': gettext("Internal error")}
                result_code = 500
                if current_app.debug or True:
                    result['debug_detail'] = str(e)
                db.session.rollback()

            return {'status': 'OK', 'message': '',
                    'workflow': result}, result_code

        except Exception as e:
            log.exception(e)
            return {'status': 'ERROR', 
                'message': gettext('Invalid workflow')}, 400
