# -*- coding: utf-8 -*-}
import logging
import os
import urllib2
import uuid

import jsondiff
from flask import Response
from flask import request, current_app, g
from flask_restful import Resource
from sqlalchemy.orm import joinedload

from app_auth import requires_auth
from schema import *

log = logging.getLogger(__name__)


def optimize_workflow_query(workflows):
    return workflows \
        .options(joinedload('tasks')) \
        .options(joinedload('tasks.operation')) \
        .options(joinedload('tasks.operation.current_translation')) \
        .options(joinedload('platform')) \
        .options(joinedload('platform.current_translation')) \
        .options(joinedload('flows'))


def update_port_name_in_flows(session, workflow_id):
    sql = """
        UPDATE flow, operation_port s, operation_port t,
        operation_port_translation t1, operation_port_translation t2
        SET source_port_name = t1.name, target_port_name = t2.name
        WHERE flow.source_port = s.id AND flow.target_port = t.id
        AND s.id = t1.id AND t.id = t2.id
        AND workflow_id = :id"""
    session.execute(sql, {'id': workflow_id})


class WorkflowListApi(Resource):
    """ REST API for listing class Workflow """

    @staticmethod
    @requires_auth
    def get():
        try:
            if request.args.get('fields'):
                only = [x.strip() for x in
                        request.args.get('fields').split(',')]
            else:
                only = ('id', 'name') \
                    if request.args.get('simple', 'false') == 'true' else None

            workflows = Workflow.query

            platform = request.args.get('platform', None)
            if platform:
                workflows = workflows.filter(
                    Workflow.platform.has(slug=platform))

            enabled_filter = request.args.get('enabled')
            if enabled_filter:
                workflows = workflows.filter(
                    Workflow.enabled == (enabled_filter != 'false'))

            user_id_filter = request.args.get('user_id')
            if user_id_filter:
                workflows = workflows.filter(
                    Workflow.user_id == user_id_filter)

            name_filter = request.args.get('name')
            if name_filter:
                workflows = workflows.filter(
                    Workflow.name.like('%%{}%%'.format(name_filter)))
            sort = request.args.get('sort', 'name')
            if sort not in ['name', 'id', 'user_name', 'updated', 'created']:
                sort = 'name'
            sort_option = getattr(Workflow, sort)
            if request.args.get('asc', 'true') == 'false':
                sort_option = sort_option.desc()
            workflows = optimize_workflow_query(
                workflows.order_by(sort_option))
            page = request.args.get('page', '20')

            if page is not None and page.isdigit():
                page_size = int(request.args.get('size', 20))
                page = int(page)
                pagination = workflows.paginate(page, page_size, True)
                result = {
                    'data': WorkflowListResponseSchema(many=True,
                                                       only=only).dump(
                        pagination.items).data,
                    'pagination': {'page': page, 'size': page_size,
                                   'total': pagination.total,
                                   'pages': pagination.total / page_size + 1}}
                print result
            else:
                result = {'data': WorkflowListResponseSchema(many=True,
                                                             only=only).dump(
                    workflows).data}

            return result
        except Exception, e:
            log.exception("Error in GET")
            result = dict(status="ERROR", message="Internal error")
            if current_app.debug:
                result['debug_detail'] = e.message
            return result, 500

    @staticmethod
    @requires_auth
    def post():
        result, result_code = dict(
            status="ERROR", message="Missing json in the request body"), 400
        if request.args.get('source'):
            original = Workflow.query.get(int(request.args.get('source')))
            response_schema = WorkflowItemResponseSchema()
            cloned = response_schema.dump(original).data
            # User field is not present in constructor
            user = cloned.pop('user')
            platform = cloned.pop('platform')
            cloned['platform'] = Platform.query.get(platform['id'])
            cloned['user_id'] = user['id']
            cloned['user_login'] = user['login']
            cloned['user_name'] = user['name']
            for task in cloned['tasks']:
                task['id'] = str(uuid.uuid1())
                task['operation_id'] = task['operation']['id']
            cloned['platform_id'] = cloned['platform']['id']

            request_schema = WorkflowCreateRequestSchema()
            form = request_schema.load(cloned)
        elif request.data is not None:
            data = json.loads(request.data)
            request_schema = WorkflowCreateRequestSchema()
            response_schema = WorkflowItemResponseSchema()
            for task in data.get('tasks', {}):
                task['operation_id'] = task['operation']['id']
                task['forms'] = {k: v for k, v in task['forms'].iteritems()
                                 if v.get('value') is not None}
            params = {}
            params.update(data)
            user = params.pop('user')
            params['user_id'] = user['id']
            params['user_login'] = user['login']
            params['user_name'] = user['name']
            params['platform_id'] = params.get('platform', {}).get(
                'id') or params.get('platform_id')

            form = request_schema.load(params)
        else:
            return result, result_code

        if form.errors:
            result, result_code = dict(
                status="ERROR", message="Validation error",
                errors=form.errors), 400
        else:
            try:
                workflow = form.data
                db.session.add(workflow)
                db.session.flush()
                update_port_name_in_flows(db.session, workflow.id)
                db.session.commit()
                result, result_code = response_schema.dump(
                    workflow).data, 200
                if workflow.is_template:
                    workflow.template_code = result
                    db.session.add(workflow)
                    db.session.commit()
            except Exception, e:
                log.exception('Error in POST')
                result, result_code = dict(status="ERROR",
                                           message="Internal error"), 500
                if current_app.debug or True:
                    result['debug_detail'] = e.message
                db.session.rollback()

        return result, result_code


class WorkflowDetailApi(Resource):
    """ REST API for a single instance of class Workflow """

    @staticmethod
    @requires_auth
    def get(workflow_id):
        hack_path = '/var/tmp/{}.json'.format(workflow_id)
        if os.path.exists(hack_path):
            with open(hack_path) as f:
                return json.loads(f.read())
        else:
            workflow = optimize_workflow_query(
                Workflow.query.filter_by(id=workflow_id).order_by(
                    Workflow.name)).first()
            if workflow is not None:
                return WorkflowItemResponseSchema().dump(workflow).data
            else:
                return dict(status="ERROR", message="Not found"), 404

    @staticmethod
    @requires_auth
    def delete(workflow_id):
        result, result_code = dict(status="ERROR", message="Not found"), 404

        workflow = Workflow.query.get(workflow_id)
        if workflow is not None:
            try:
                # db.session.delete(workflow)
                # soft delete
                workflow.enabled = False
                db.session.commit()
                result, result_code = dict(status="OK", message="Deleted"), 200
            except Exception, e:
                log.exception('Error in DELETE')
                result, result_code = dict(status="ERROR",
                                           message="Internal error"), 500
                if current_app.debug:
                    result['debug_detail'] = e.message
                db.session.rollback()
        return result, result_code

    @staticmethod
    @requires_auth
    def patch(workflow_id):
        result = dict(status="ERROR", message="Insufficient data")
        result_code = 404
        try:
            if request.data:
                data = json.loads(request.data)
                request_schema = partial_schema_factory(
                    WorkflowCreateRequestSchema)
                for task in data.get('tasks', {}):
                    task['forms'] = {k: v for k, v in task['forms'].iteritems() \
                                     if v.get('value') is not None}
                # Ignore missing fields to allow partial updates
                params = {}
                params.update(data)
                if 'platform_id' in params and params['platform_id'] is None:
                    params.pop('platform_id')

                user = params.pop('user')
                params['user_id'] = user['id']
                params['user_login'] = user['login']
                params['user_name'] = user['name']

                form = request_schema.load(params, partial=True)
                response_schema = WorkflowItemResponseSchema()
                if not form.errors:
                    try:
                        form.data.id = workflow_id
                        form.data.updated = datetime.datetime.utcnow()

                        # Retrieves current version of workflow in order
                        # to save it in history.
                        workflow = Workflow.query.get(workflow_id)

                        historical_data = json.dumps(
                            response_schema.dump(workflow).data)
                        # if workflow.is_template:
                        #     workflow.template_code = historical_data

                        history = WorkflowHistory(
                            user_id=user['id'], user_name=user['name'],
                            user_login=user['login'],
                            version=workflow.version,
                            workflow=workflow, content=historical_data)
                        db.session.add(history)

                        workflow = db.session.merge(form.data)
                        db.session.flush()
                        update_port_name_in_flows(db.session, workflow.id)
                        db.session.commit()

                        db.session.commit()

                        if workflow is not None:
                            result, result_code = dict(
                                status="OK", message="Updated",
                                data=response_schema.dump(workflow).data), 200
                        else:
                            result = dict(status="ERROR", message="Not found")
                    except Exception, e:
                        log.exception('Error in PATCH')
                        result, result_code = dict(
                            status="ERROR", message="Internal error"), 500
                        if current_app.debug:
                            result['debug_detail'] = e.message
                        db.session.rollback()
                else:
                    result = dict(status="ERROR", message="Invalid data",
                                  errors=form.errors)
        except Exception as e:
            log.exception('Error in PATCH')
            result_code = 500
            import sys
            result = {'status': "ERROR", 'message': sys.exc_info()[1]}
        return result, result_code


class WorkflowImportApi(Resource):
    @staticmethod
    @requires_auth
    def post():
        url = request.form.get('url')
        token = request.form.get('token')
        contents = request.form.get('source')

        if not contents:
            if not all([url, token]):
                return {'error': 'Missing url or token parameter',
                        'status': 'ERROR'}, 400

            r = urllib2.Request(url, headers={"X-Auth-Token": token})
            contents = urllib2.urlopen(r).read()
        # noinspection PyBroadException
        try:
            original = json.loads(contents)
            platform = original.pop('platform')

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
                new_id = str(uuid.uuid1())
                original_task_ids[task['id']] = new_id
                task['id'] = new_id

            # updates flows
            for flow in original['flows']:
                flow['source_id'] = original_task_ids[flow['source_id']]
                flow['target_id'] = original_task_ids[flow['target_id']]

            response_schema = WorkflowItemResponseSchema()
            request_schema = WorkflowCreateRequestSchema()

            form = request_schema.load(original)

            if form.errors:
                result, result_code = dict(
                    status="ERROR", message="Validation error",
                    errors=form.errors), 400
            else:
                try:
                    workflow = form.data
                    db.session.add(workflow)
                    db.session.flush()
                    update_port_name_in_flows(db.session, workflow.id)
                    db.session.commit()
                    result, result_code = response_schema.dump(
                        workflow).data, 200
                except Exception, e:
                    log.exception('Error in POST')
                    result, result_code = dict(status="ERROR",
                                               message="Internal error"), 500
                    if current_app.debug or True:
                        result['debug_detail'] = e.message
                    db.session.rollback()

            return {'status': 'OK', 'message': '',
                    'workflow': result}, result_code

        except Exception as e:
            log.exception(e)
            return 'Invalid workflow', 400


class WorkflowHistoryApi(Resource):
    @staticmethod
    @requires_auth
    def get(workflow_id):
        history = WorkflowHistory.query.filter(
            WorkflowHistory.workflow_id == workflow_id).order_by(
            WorkflowHistory.version.desc()).limit(50)
        return WorkflowHistoryListResponseSchema(
            only=('id', 'date', 'user_id', 'user_name', 'version'),
            many=True).dump(history).data


class RevertToWorkflowHistoryApi(Resource):
    @staticmethod
    @requires_auth
    def post(workflow_id, version):
        result, result_code = dict(status="ERROR", message="Not found"), 404

        history = WorkflowHistory.query.filter(
            WorkflowHistory.version == version,
            WorkflowHistory.workflow_id == workflow_id).first()
        if history is not None:
            try:
                w = json.loads(history.content)
                user = w.pop('user')
                w['user_id'] = user['id']
                w['user_login'] = user['login']
                w['user_name'] = user['name']

                # Remove version, it causes problems when updating
                del w['version']
                w['platform_id'] = w['platform']['id']
                for t in w['tasks']:
                    t['operation_id'] = t['operation']['id']
                    del t['version']

                schema = WorkflowItemResponseSchema()
                create_schema = WorkflowCreateRequestSchema()
                loaded = create_schema.load(w)
                if loaded.errors:
                    result = 'Incompatible history for workflow.'
                    result_code = 201
                else:
                    new_workflow = loaded.data
                    new_workflow.updated = datetime.datetime.utcnow()
                    new_workflow.id = workflow_id

                    historical_data = json.dumps(
                        schema.dump(history.workflow).data)

                    history = WorkflowHistory(
                        user_id=user['id'], user_name=user['name'],
                        user_login=user['login'],
                        version=history.workflow.version,
                        workflow=history.workflow, content=historical_data)

                    db.session.merge(new_workflow)
                    update_port_name_in_flows(db.session, new_workflow.id)
                    db.session.add(history)
                    db.session.commit()

                    result = {'status': 'OK', 'message': '',
                              'workflow': schema.dump(new_workflow).data}
                    result_code = 200
            except Exception as e:
                log.exception(e)
                return 'Invalid workflow', 400
        return result, result_code


class WorkflowHistoryDiffApi(Resource):
    @staticmethod
    @requires_auth
    def get(workflow_id, version):
        history = WorkflowHistory.query.filter(
            WorkflowHistory.workflow_id == workflow_id,
            WorkflowHistory.version == version).first()
        if history:
            schema = WorkflowItemResponseSchema()
            version_json = json.loads(history.content)

            def fix_diff_dict(d):
                new_dict = {}
                for k, v in d.iteritems():
                    key = str(k)
                    if isinstance(v, dict):
                        new_dict[key] = fix_diff_dict(v)
                    else:
                        new_dict[key] = v
                return new_dict

            # noinspection PyProtectedMember
            current_json = json.loads(schema.dumps(history.workflow).data)
            diff = jsondiff.diff(version_json, current_json)

            result = fix_diff_dict(diff)
            result_code = 200
        else:
            result, result_code = dict(status="ERROR", message="Not found"), 404
        return result, result_code
