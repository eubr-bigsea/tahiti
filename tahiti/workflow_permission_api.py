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

from marshmallow.exceptions import ValidationError
from tahiti.app_auth import requires_auth
from tahiti.schema import *
from tahiti.workflow_api import filter_by_permissions

log = logging.getLogger(__name__)


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
                    filtered = filter_by_permissions(
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

        filtered = filter_by_permissions(Workflow.query,
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
