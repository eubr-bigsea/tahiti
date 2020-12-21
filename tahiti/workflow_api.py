# -*- coding: utf-8 -*-}
import logging
import os
import uuid

import requests
from flask import request, current_app, g
from flask_babel import gettext
from flask_restful import Resource
from sqlalchemy import or_
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.elements import and_

from tahiti.app_auth import requires_auth
from tahiti.schema import *

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


def get_workflow(workflow_id):
    workflows = optimize_workflow_query(
        Workflow.query.filter_by(id=workflow_id).order_by(
            Workflow.name))

    workflows = _filter_by_permissions(workflows, list(PermissionType.values()))

    workflows = workflows.options(

        joinedload('tasks.operation.forms')).options(
        joinedload('tasks.operation.forms')).options(
        joinedload('tasks.operation.forms.fields'))

    workflow = workflows.first()
    if workflow is not None:
        # Set the json form for operations
        for task in workflow.tasks:
            current_form = json.loads(task.forms) if task.forms else {}
            for form in task.operation.forms:
                for field in form.fields:
                    if field.name not in current_form:
                        current_form[field.name] = {
                            'value': field.default}
            db.session.expunge(task) # in order to avoid unnecessary updates
            task.forms = json.dumps(current_form)
    return workflow


def _filter_by_permissions(workflows, permissions, consider_public=True):
    if g.user.id not in (0, 1):  # It is not a inter service call
        sub_query = WorkflowPermission.query.with_entities(
            WorkflowPermission.workflow_id).filter(
            WorkflowPermission.permission.in_(permissions),
            WorkflowPermission.user_id == g.user.id)
        conditions = [
            Workflow.user_id == g.user.id,
            Workflow.id.in_(sub_query)
        ]
        if consider_public:
            conditions.append(Workflow.is_public)
        workflows = workflows.filter(or_(*conditions))
    return workflows

def test_and_apply_filter(request, arg, workflow, condition):
    result = workflow
    value = request.args.get(arg)
    if value:
        result = workflow.filter(condition(value))
    return result    

class WorkflowListApi(Resource):
    """ REST API for listing class Workflow """

    @staticmethod
    @requires_auth
    def get():
        workflows = Workflow.query
        try:
            if request.args.get('fields'):
                only = [x.strip() for x in
                        request.args.get('fields').split(',')]
            else:
                only = ('id', 'name', 'platform.id', 'permissions')


            workflows = test_and_apply_filter(request, 'platform', workflows, 
                lambda v: Workflow.platform.has(slug=v))

            # platform = request.args.get('platform', None)
            # if platform:
            #    workflows = workflows.filter(
            #        Workflow.platform.has(slug=platform))
            workflows = test_and_apply_filter(request, 'track', workflows, 
                lambda v: Workflow.publishing_enabled == (v != 'false'))
            workflows = test_and_apply_filter(request, 'published', workflows, 
                lambda v: Workflow.publishing_status == PublishingStatus.PUBLISHED)
            # is_track_filter = request.args.get('track')
            # if is_track_filter:
            #     workflows = workflows.filter(
            #         Workflow.publishing_enabled == (is_track_filter != 'false'))
            #     is_published = request.args.get('published')
            #     if is_published:
            #         workflows = workflows.filter(
            #             Workflow.publishing_status == PublishingStatus.PUBLISHED)

            workflows = test_and_apply_filter(request, 'enabled', workflows, 
                lambda v: Workflow.enabled == (v != 'false'))
            # enabled_filter = request.args.get('enabled')
            # if enabled_filter:
            #    workflows = workflows.filter(
            #        Workflow.enabled == (enabled_filter != 'false'))

            workflows = test_and_apply_filter(request, 'template', workflows, 
                lambda v: or_(and_(Workflow.user_id == g.user.id,
                              Workflow.is_template),
                         Workflow.is_system_template))
            # template_only = request.args.get('template')
            # if template_only is not None:
            #     template_only = template_only in ['1', 'true', 'True']
            # else:
            #     template_only = False

            # if template_only:
            #     workflows = workflows.filter(
            #         or_(and_(Workflow.user_id == g.user.id,
            #                  Workflow.is_template),
            #             Workflow.is_system_template))


            workflows = test_and_apply_filter(request, 'name', workflows, 
                lambda v: Workflow.name.like('%%{}%%'.format(v)))
            # name_filter = request.args.get('name')
            # if name_filter:
            #     workflows = workflows.filter(
            #         Workflow.name.like(
            #             '%%{}%%'.format(name_filter)))

            workflows = _filter_by_permissions(
                workflows, list(PermissionType.values()))
            sort = request.args.get('sort', 'name')
            if sort not in ['name', 'id', 'user_name', 'updated', 'created']:
                sort = 'name'
            sort_option = getattr(Workflow, sort)
            if request.args.get('asc', 'true') == 'false':
                sort_option = sort_option.desc()
            workflows = optimize_workflow_query(
                workflows.order_by(sort_option))
            page = int(request.args.get('page', 1))

            page_size = int(request.args.get('size', 20))
            page = int(page)
            pagination = workflows.paginate(page, page_size, False)
            if pagination.total < (page - 1) * page_size and page != 1:
                # Nothing in that specified page, return to page 1
                pagination = workflows.paginate(1, page_size, False)
            result = {
                'data': WorkflowListResponseSchema(many=True,
                                                   exclude=('permissions',),
                                                   only=only).dump(
                    pagination.items).data,
                'pagination': {'page': page, 'size': page_size,
                               'total': pagination.total,
                               'pages': pagination.total / page_size + 1}}
            return result

        except Exception as e:
            log.exception(e)
            result = dict(status="ERROR", message="Internal error")
            if current_app.debug:
                result['debug_detail'] = str(e)
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
            platform = cloned.pop('platform')
            cloned['platform'] = Platform.query.get(platform['id'])
            cloned['user_id'] = g.user.id
            cloned['user_login'] = g.user.login
            cloned['user_name'] = g.user.name

            for task in cloned['tasks']:
                task['id'] = str(uuid.uuid4())
                task['operation_id'] = task['operation']['id']
            cloned['platform_id'] = cloned['platform']['id']

            request_schema = WorkflowCreateRequestSchema()
            form = request_schema.load(cloned)
        elif request.json:
            data = request.json
            if 'user' in data:
                data.pop('user')
            request_schema = WorkflowCreateRequestSchema()
            response_schema = WorkflowItemResponseSchema()
            for task in data.get('tasks', {}):
                task['operation_id'] = task['operation']['id']
                task['forms'] = {k: v for k, v in list(task['forms'].items())
                                 if v.get('value') is not None or 
                                 v.get('publishing_enabled') == True}
            params = {}
            params.update(data)
            params['user_id'] = g.user.id
            params['user_login'] = g.user.login
            params['user_name'] = g.user.name
            params['platform_id'] = params.get('platform', {}).get(
                'id') or params.get('platform_id')
            params['subset_id'] = params.get('subset_id')
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
                result, result_code = response_schema.dump(
                    workflow).data, 200
                if workflow.is_template:
                    workflow.template_code = result
                    db.session.add(workflow)
                db.session.commit()
            except Exception as e:
                log.exception('Error in POST')
                result, result_code = dict(status="ERROR",
                                           message="Internal error"), 500
                if current_app.debug or True:
                    result['debug_detail'] = str(e)
                db.session.rollback()

        return result, result_code


class WorkflowDetailApi(Resource):
    """ REST API for a single instance of class Workflow """

    @staticmethod
    @requires_auth
    def get(workflow_id):
        workflow = get_workflow(workflow_id)
        if workflow is not None:
            return WorkflowItemResponseSchema().dump(workflow).data
        else:
            return dict(status="ERROR", message="Not found"), 404

    @staticmethod
    @requires_auth
    def delete(workflow_id):
        result, result_code = dict(status="ERROR", message="Not found"), 404

        filtered = _filter_by_permissions(
            Workflow.query, [PermissionType.WRITE])

        workflow = filtered.filter(Workflow.id == workflow_id).first()
        if workflow is not None:
            try:
                # db.session.delete(workflow)
                # soft delete
                workflow.enabled = False
                db.session.commit()
                result, result_code = dict(status="OK", message="Deleted"), 200
            except Exception as e:
                log.exception('Error in DELETE')
                result, result_code = dict(status="ERROR",
                                           message="Internal error"), 500
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
        return result, result_code

    @staticmethod
    @requires_auth
    def patch(workflow_id):
        result = dict(status="ERROR", message="Insufficient data")
        result_code = 404
        try:
            if request.json:
                data = request.json
                request_schema = partial_schema_factory(
                    WorkflowCreateRequestSchema)
                for task in data.get('tasks', {}):
                    task['forms'] = {k: v for k, v in
                                     list(task['forms'].items())
                                     if v.get('value') is not None or 
                                     v.get('publishing_enabled') == True}
                    task['operation_id'] = task['operation']['id']

                # Ignore missing fields to allow partial updates
                params = {}
                params.update(data)
                if 'platform_id' in params and params['platform_id'] is None:
                    params.pop('platform_id')

                if 'user' in params:
                    del params['user']

                # Only with permission
                if not ('ADMINISTRATOR' in g.user.permissions) and \
                        'is_system_template' in params:
                    del params['is_system_template']

                # Keeps the same owner
                # params['user_id'] = g.user.id
                # params['user_login'] = g.user.login
                # params['user_name'] = g.user.name

                if params.get('forms') is not None:
                    params['forms'] = json.dumps(params['forms'])
                else:
                    params['forms'] = '{}'
                form = request_schema.load(params, partial=True)
                response_schema = WorkflowItemResponseSchema()
                if not form.errors:
                    try:
                        filtered = _filter_by_permissions(
                            Workflow.query, [PermissionType.WRITE])
                        temp_workflow = filtered.filter(
                            Workflow.id == workflow_id).first()

                        if temp_workflow is not None:
                            form.data.id = workflow_id
                            form.data.updated = datetime.datetime.utcnow()

                            workflow = db.session.merge(form.data)
                            if (workflow.publishing_enabled and 
                                    workflow.publishing_status is None):
                                workflow.publishing_status = PublishingStatus.EDITING
                            db.session.flush()
                            update_port_name_in_flows(db.session, workflow.id)
                            db.session.commit()

                            historical_data = json.dumps(
                                response_schema.dump(workflow).data)
                            # if workflow.is_template:
                            #     workflow.template_code = historical_data

                            history = WorkflowHistory(
                                user_id=g.user.id, user_name=g.user.name,
                                user_login=g.user.login,
                                version=workflow.version,
                                workflow=workflow, content=historical_data)
                            db.session.add(history)
                            db.session.commit()

                            if workflow is not None:
                                result, result_code = dict(
                                    status="OK", message="Updated",
                                    data=response_schema.dump(
                                        workflow).data), 200
                            else:
                                result = dict(status="ERROR",
                                              message="Not found")
                    except Exception as e:
                        log.exception('Error in PATCH')
                        result, result_code = dict(
                            status="ERROR", message="Internal error"), 500
                        if current_app.debug:
                            result['debug_detail'] = str(e)
                        db.session.rollback()
                else:
                    result = dict(status="ERROR", message="Invalid data",
                                  errors=form.errors)
                    result_code = 400
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
        contents = request.json if request.json else None

        # Imports from URL
        if not contents:
            if not all([url, token]):
                return {'error': 'Missing url or token parameter',
                        'status': 'ERROR'}, 400
            r = requests.get(url, headers={"X-Auth-Token": token})
            if r.status_code == 200:
                contents = r.text
                original = json.loads(contents)
            else:
                return 'Error reading source workflow: ' + \
                       r.status_code + '\n' + r.text, 400
        else:
            original = json.loads(contents.get('content'))
        # noinspection PyBroadException
        try:
            platform = original.pop('platform')

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
                    result, result_code = workflow.id, 200
                except Exception as e:
                    log.exception('Error in POST')
                    result, result_code = dict(status="ERROR",
                                               message="Internal error"), 500
                    if current_app.debug or True:
                        result['debug_detail'] = str(e)
                    db.session.rollback()

            return {'status': 'OK', 'message': '',
                    'workflow': result}, result_code

        except Exception as e:
            log.exception(e)
            return 'Invalid workflow', 400


class WorkflowHistoryApi(Resource):
    @staticmethod
    @requires_auth
    def post(workflow_id):
        result, result_code = dict(status="ERROR", message="Not found"), 404
        params = request.json

        if 'version' in params:
            workflow = get_workflow(workflow_id)
            if workflow.user_id == g.user.id:
                history = WorkflowHistory.query.filter(
                    WorkflowHistory.workflow_id == workflow_id,
                    WorkflowHistory.version == int(params['version'])).one()
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
                        task['name'] = '{} {}'.format(task['operation']['name'],
                                                      i)

                rw = WorkflowCreateRequestSchema().load(old)
                if rw.errors:
                    result_code = 400
                    result = dict(
                        status="ERROR",
                        message="Version {} is not compatible anymore.".format(
                            params['version']))
                else:
                    result = old
                    result_code = 200
            else:
                result, result_code = dict(status="ERROR",
                                           message="Not authorized"), 401

        return result, result_code

    @staticmethod
    @requires_auth
    def get(workflow_id):
        history = WorkflowHistory.query.filter(
            WorkflowHistory.workflow_id == workflow_id).order_by(
            WorkflowHistory.date.desc()).limit(20)
        only = ('id', 'date', 'version', 'user_name')
        return {'data': WorkflowHistoryListResponseSchema(
            many=True, only=only).dump(history).data}


class WorkflowAddFromTemplateApi(Resource):
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
                    json.dumps(response_schema.dump(workflow).data))
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
                    new_workflow = form.data
                    db.session.add(new_workflow)
                    db.session.flush()
                    db.session.commit()
                    result, result_code = response_schema.dump(
                        new_workflow).data, 200
                else:
                    result, result_code = dict(status="ERROR",
                                               message="Not authorized"), 401
            else:
                result, result_code = dict(status="ERROR",
                                           message="Not authorized"), 401
        else:
            result, result_code = dict(status="ERROR", message="Not found"), 404
        return result, result_code

    @staticmethod
    @requires_auth
    def get(workflow_id):
        history = WorkflowHistory.query.filter(
            WorkflowHistory.workflow_id == workflow_id).order_by(
            WorkflowHistory.date.desc()).limit(20)
        only = ('id', 'date', 'version', 'user_name')
        return {'data': WorkflowHistoryListResponseSchema(
            many=True, only=only).dump(history).data}


class WorkflowPermissionApi(Resource):
    """ REST API for sharing a Workflow """

    @staticmethod
    @requires_auth
    def post(workflow_id, user_id):
        result, result_code = dict(
            status="ERROR",
            message=gettext('Missing json in the request body')), 400

        if request.json is not None:
            form = request.json
            to_validate = ['permission', 'user_name', 'user_login']
            error = False
            for check in to_validate:
                if check not in form or form.get(check, '').strip() == '':
                    result, result_code = dict(
                        status="ERROR", message=gettext('Validation error'),
                        errors={'Missing': check}), 400
                    error = True
                    break
                if check == 'permission' and form.get(
                        'permission') not in list(PermissionType.values()):
                    result, result_code = dict(
                        status="ERROR", message=gettext('Validation error'),
                        errors={'Invalid': check}), 400
                    error = True
                    break
            if not error:
                try:
                    filtered = _filter_by_permissions(
                        Workflow.query, [PermissionType.WRITE])
                    workflow = filtered.filter(
                        Workflow.id == workflow_id).first()

                    if workflow is not None:
                        conditions = [WorkflowPermission.workflow_id ==
                                      workflow_id,
                                      WorkflowPermission.user_id == user_id]
                        permission = WorkflowPermission.query.filter(
                            *conditions).first()

                        action_performed = 'Added'
                        if permission is not None:
                            action_performed = 'Updated'
                            permission.permission = form['permission']
                        else:
                            permission = WorkflowPermission(
                                workflow=workflow, user_id=user_id,
                                user_name=form['user_name'],
                                user_login=form['user_login'],
                                permission=form['permission'])

                        db.session.add(permission)
                        db.session.commit()
                        result, result_code = {'message': action_performed,
                                               'status': 'OK'}, 200
                    else:
                        result, result_code = dict(
                            status="ERROR",
                            message=gettext("%(type)s not found.",
                                            type=gettext('Data source'))), 404
                except Exception as e:
                    log.exception('Error in POST')
                    result, result_code = dict(status="ERROR",
                                               message=gettext(
                                                   "Internal error")), 500
                    if current_app.debug:
                        result['debug_detail'] = str(e)
                    db.session.rollback()

        return result, result_code

    @staticmethod
    @requires_auth
    def delete(workflow_id, user_id):
        result, result_code = dict(status="ERROR",
                                   message=gettext("%(type)s not found.",
                                                   type=gettext(
                                                       'Data source'))), 404

        filtered = _filter_by_permissions(Workflow.query,
                                          [PermissionType.WRITE])
        workflow = filtered.filter(Workflow.id == workflow_id).first()
        if workflow is not None:
            permission = WorkflowPermission.query.filter(
                WorkflowPermission.workflow_id == workflow_id,
                WorkflowPermission.user_id == user_id).first()
            if permission is not None:
                try:
                    db.session.delete(permission)
                    db.session.commit()
                    result, result_code = dict(
                        status="OK",
                        message=gettext("%(what)s was successively deleted",
                                        what=gettext('Workflow'))), 200
                except Exception as e:
                    log.exception('Error in DELETE')
                    result, result_code = dict(status="ERROR",
                                               message=gettext(
                                                   "Internal error")), 500
                    if current_app.debug:
                        result['debug_detail'] = str(e)
                    db.session.rollback()
        return result, result_code
