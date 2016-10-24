# -*- coding: utf-8 -*-}
from flask import request, current_app
from flask_restful import Resource

from app_auth import requires_auth
from models import db, Workflow
from schema import *


class WorkflowListApi(Resource):
    """ REST API for listing class Workflow """

    @staticmethod
    @requires_auth
    def get():
        only = ('id', 'name') \
            if request.args.get('simple', 'false') == 'true' else None
        workflows = Workflow.query.all()
        return WorkflowListResponseSchema(many=True, only=only).dump(workflows).data

    @staticmethod
    @requires_auth
    def post():
        result, result_code = dict(
            status="ERROR", message="Missing json in the request body"), 401
        if request.json is not None:
            request_schema = WorkflowCreateRequestSchema()
            response_schema = WorkflowItemResponseSchema()
            form = request_schema.load(request.json)
            if form.errors:
                result, result_code = dict(
                    status="ERROR", message="Validation error",
                    errors=form.errors,), 401
            else:
                try:
                    workflow = form.data
                    db.session.add(workflow)
                    db.session.commit()
                    result, result_code = response_schema.dump(workflow).data, 200
                except Exception, e:
                    result, result_code = dict(status="ERROR",
                                               message="Internal error"), 500
                    if current_app.debug:
                        result['debug_detail'] = e.message
                    db.session.rollback()

        return result, result_code


class WorkflowDetailApi(Resource):
    """ REST API for a single instance of class Workflow """

    @staticmethod
    @requires_auth
    def get(workflow_id):
        workflow = Workflow.query.get(workflow_id)
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
                db.session.delete(workflow)
                db.session.commit()
                result, result_code = dict(status="OK", message="Deleted"), 200
            except Exception, e:
                result, result_code = dict(status="ERROR",
                                           message="Internal error"), 500
                if current_app.debug:
                    result['debug_detail'] = e.message
                db.session.rollback()
        else:
            return result, result_code

    @staticmethod
    @requires_auth
    def patch(workflow_id):
        result = dict(status="ERROR", message="Insufficient data")
        result_code = 404

        if request.json:
            request_schema = PartialSchemaFactory(WorkflowCreateRequestSchema)
            form = request_schema.load(request.json)
            response_schema = WorkflowItemResponseSchema()
            if not form.errors:
                try:
                    form.data.id = workflow_id
                    workflow = db.session.merge(form.data)
                    db.session.commit()

                    if workflow is not None:
                        result, result_code = dict(
                            status="OK", message="Updated",
                            data=response_schema.dump(workflow).data), 200
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
                            errors=form.errors)
        return result, result_code
