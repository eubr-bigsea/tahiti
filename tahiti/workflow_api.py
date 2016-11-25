# -*- coding: utf-8 -*-}
from flask import request, current_app
from flask_restful import Resource

from sqlalchemy.orm import joinedload
from app_auth import requires_auth
from schema import *

def optimize_workflow_query(workflows):
    return workflows \
        .options(joinedload('tasks')) \
        .options(joinedload('tasks.operation')) \
        .options(joinedload('tasks.operation.current_translation')) \
        .options(joinedload('platform')) \
        .options(joinedload('platform.current_translation')) \
        .options(joinedload('flows'))

class WorkflowListApi(Resource):
    """ REST API for listing class Workflow """

    @staticmethod
    @requires_auth
    def get():
        try:
            if request.args.get('fields'):
                only = [x.strip() for x in request.args.get('fields').split(',')]
            else:
                only = ('id', 'name') \
                    if request.args.get('simple', 'false') == 'true' else None
    
            workflows = Workflow.query
            
            platform = request.args.get('platform', None)
            if platform:
                workflows = workflows.filter(Workflow.platform.has(slug=platform))
    
            enabled_filter = request.args.get('enabled')
            if enabled_filter:
                workflows = workflows.filter(
                    Workflow.enabled == (enabled_filter != 'false'))
    
            name_filter = request.args.get('name')
            if name_filter:
                workflows = workflows.filter(
                    Workflow.name.like('%%{}%%'.format(name_filter)))
            workflows = optimize_workflow_query(workflows.order_by(Workflow.name))
            page = request.args.get('page')

            if page is not None and page.isdigit():
                page_size = int(request.args.get('size', 20))
                page = int(page)
                pagination = workflows.paginate(page, page_size, True)
                result = {
                    'data': WorkflowListResponseSchema(many=True, only=only).dump(pagination.items).data, 
                    'pagination': {'page': page, 'size': page_size, 'total': pagination.total, 
                                   'pages': pagination.total / page_size + 1}}
                print result
            else:
                result = {'data': WorkflowListResponseSchema(many=True, only=only).dump(workflows).data}
        
            return result
        except Exception, e:
            result = dict(status="ERROR", message="Internal error")
            if current_app.debug:
                result['debug_detail'] = e.message
            return result, 500
    
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
                    errors=form.errors), 401
            else:
                try:
                    workflow = form.data
                    db.session.add(workflow)
                    db.session.commit()
                    result, result_code = response_schema.dump(
                        workflow).data, 200
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
        #workflow = optimize_workflow_query(Workflow.query.filter_by(id=workflow_id))
        workflow = optimize_workflow_query(Workflow.query.filter_by(id=workflow_id)\
            .order_by(Workflow.name)).first()
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
        return result, result_code

    @staticmethod
    @requires_auth
    def patch(workflow_id):
        result = dict(status="ERROR", message="Insufficient data")
        result_code = 404
        try:
            if request.json:
                request_schema = partial_schema_factory(WorkflowCreateRequestSchema)
                # Ignore missing fields to allow partial updates
                form = request_schema.load(request.json, partial=True)
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
        except:
            result_code = 500
            import sys
            result = {status:"ERROR", message:sys.exc_info()[1]}
        return result, result_code
