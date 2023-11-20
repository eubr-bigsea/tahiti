# -*- coding: utf-8 -*-}
from http import HTTPStatus
import logging

from flask import current_app, request
from flask_babel import gettext
from flask_restful import Resource

from marshmallow.exceptions import ValidationError
from tahiti.app_auth import requires_auth
from tahiti.schema import *
from tahiti.util import DataConsistencyError

log = logging.getLogger(__name__)

human_name = gettext('TemplatePipeline')

class TemplatePipelineApi(Resource):

    @staticmethod
    def _create_template_pipeline_steps(data:dict, steps:dict) -> (dict,HTTPStatus):

        template_pipeline_id = data['id']
        template_pipeline_step_schema = TemplatePipelineStepPrivateCreateRequestSchema()

        if steps is not None:
            for index,step in enumerate(steps):
                step['order'] = index+1
                step['templatepipeline_id'] = template_pipeline_id

                template_pipeline_step = template_pipeline_step_schema.load(step)
                 
                try:
                    
                    if log.isEnabledFor(logging.DEBUG):
                        log.debug(f'Adding Step')
                    db.session.add(template_pipeline_step)
                    db.session.commit()

                    template_pipeline_steps = TemplatePipelineStep.query.filter(TemplatePipelineStep.templatepipeline_id==template_pipeline_id).all()
                    result = data
                    result['steps'] = TemplatePipelineStepItemResponseSchema(many=True).dump(template_pipeline_steps)
                    result_code = HTTPStatus.CREATED

                except ValidationError as e:
                    result= {
                        'status': 'ERROR', 
                        'message': f'Invalid data for {human_name}',
                        'errors': translate_validation(e.messages)
                    }

                except Exception as e:
                    result = {'status': 'ERROR',
                                'message': "Internal error"}
                    result_code = 500
                    if current_app.debug:
                        result['debug_detail'] = str(e)

                    log.exception(e)
                    db.session.rollback()

        return result, result_code

    @staticmethod
    def _create_template_pipeline_from_scratch(data:dict) -> (dict,HTTPStatus):
        request_schema = TemplatePipelineCreateRequestSchema()
        response_schema = TemplatePipelineItemResponseSchema()

        template_pipeline = request_schema.load(data)

        try:
            if log.isEnabledFor(logging.DEBUG):
                log.debug(f'Adding {human_name}')

            db.session.add(template_pipeline)
            db.session.commit()
            
            result = response_schema.dump(template_pipeline)
            result_code = HTTPStatus.CREATED

        except ValidationError as e:
                result= {
                'status': 'ERROR', 
                'message': f'Invalid data for {human_name}',
                'errors': translate_validation(e.messages)
                }

        except Exception as e:
            result = {'status': 'ERROR',
                    'message': "Internal error"}
            result_code = 500
            if current_app.debug:
                result['debug_detail'] = str(e)

            log.exception(e)
            db.session.rollback()
        
        return result, result_code

    @staticmethod
    @requires_auth
    def get():

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext(f'Listing {human_name}'))

        template_pipelines = TemplatePipeline.query.all()
        result = PipelineItemResponseSchema(many=True).dump(template_pipelines)
        result_code = HTTPStatus.OK

        for index,template_pipeline in enumerate(result):
            steps = TemplatePipelineStep.query.filter(TemplatePipelineStep.templatepipeline_id==template_pipeline['id']).order_by(TemplatePipelineStep.order).all()
            result[index]['steps'] = TemplatePipelineStepItemResponseSchema(many=True).dump(steps)
        
        return {'data': result},result_code



    @staticmethod
    @requires_auth
    def post():
        result, result_code = {"status":"ERROR", "message":"Not found"}, HTTPStatus.NOT_FOUND

        if request.json is not None:

            # check if steps were passed in the request structure
            steps = request.json.pop('steps', None)

            result, result_code = TemplatePipelineApi._create_template_pipeline_from_scratch(data=request.json)

            # create steps if they were passed through the request body
            if steps is not None and result_code is HTTPStatus.CREATED:
                result, result_code = TemplatePipelineApi._create_template_pipeline_steps(data=result, steps=steps)

            if 'steps' not in result.keys():
                result['steps'] = []

            return {'data': result}, result_code 

class TemplatePipelineDetailApi(Resource):

    @staticmethod
    @requires_auth
    def get(template_pipeline_id):
        result, result_code = {"status":"ERROR",
                                "message":f"{human_name} not found (id={template_pipeline_id})"}, HTTPStatus.NOT_FOUND
        
        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Getting {human_name} (id={template_pipeline_id})')

        template_pipeline = TemplatePipeline.query.filter(TemplatePipeline.id==template_pipeline_id).first()
        if template_pipeline is not None:
            result = TemplatePipelineItemResponseSchema().dump(template_pipeline)
            result_code = HTTPStatus.OK

            steps = TemplatePipelineStep.query.filter(TemplatePipelineStep.templatepipeline_id==template_pipeline_id).order_by(TemplatePipelineStep.order).all()
            result['steps'] = TemplatePipelineStepItemResponseSchema(many=True).dump(steps)

        return {'data': result}, result_code
            

    @staticmethod
    @requires_auth
    def delete(template_pipeline_id):
        result = {
                'status': 'ERROR',
                'message': f'{human_name} not found (id={template_pipeline_id}).'
            }
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Deleting {human_name} (id={template_pipeline_id})')
            
        template_pipeline = TemplatePipeline.query.get(template_pipeline_id)
        steps = TemplatePipelineStep.query.filter(TemplatePipelineStep.templatepipeline_id==template_pipeline_id).all()

        if template_pipeline is not None:
            try:
                db.session.delete(template_pipeline)
                if steps != []:
                    map(db.session.delete,steps)
                db.session.commit()
                result = {
                    'status': 'OK',
                    'message': f'{human_name} deleted with success!'
                }

            except Exception as e:
                result = {'status': 'ERROR',
                          'message': "Internal error"}
                return_code = HTTPStatus.INTERNAL_SERVER_ERROR
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
            
        return {"data":result}, return_code

    @staticmethod
    @requires_auth
    def patch(template_pipeline_id):
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Updating %{human_name} (id={template_pipeline_id})')
            
        if request.json:
            request_schema = partial_schema_factory(
                TemplatePipelineUpdateRequestSchema)
            response_schema = TemplatePipelineItemResponseSchema()

            steps = request.json.pop('steps', None)

            try:
                template_pipeline = request_schema.load(request.json, partial=True)
                template_pipeline.id = template_pipeline_id
                template_pipeline = db.session.merge(template_pipeline)
                db.session.commit()

                if template_pipeline is not None:

                    result = response_schema.dump(template_pipeline)

                    if steps is not None:
                        steps = TemplatePipelineStepUpdateRequestSchema(many=True).load(steps)

                        template_pipeline_steps = TemplatePipelineStep.query.filter(TemplatePipelineStep.templatepipeline_id==template_pipeline_id).all()
                        template_pipeline_steps_ids = []

                        for step in template_pipeline_steps:
                            template_pipeline_steps_ids.append(step.id)
                            step.enabled = 'DISABLED'
                            db.session.merge(step)
                        db.session.commit()

                    for index,step in enumerate(steps):
                        step.order = index+1
                        if step.id is not None:
                            if step.id not in template_pipeline_steps_ids:
                                raise DataConsistencyError(message=f"The Template Pipeline Step (id={step.id}) is associated with Template Pipeline (id={step.templatepipeline_id}), not the Template Pipeline passed through the body (id={template_pipeline_id}).")
                            db.session.merge(step)
                        else:
                            step.templatepipeline_id = template_pipeline_id
                            db.session.add(step)
                        db.session.commit()

                    template_pipeline_steps = TemplatePipelineStep.query.filter(TemplatePipelineStep.templatepipeline_id==template_pipeline_id).order_by(TemplatePipelineStep.order).all()
                    result['steps'] = TemplatePipelineStepItemResponseSchema(many=True).dump(template_pipeline_steps)
                    result = {
                        'status': 'OK',
                        'message': f'{human_name} (id={template_pipeline_id}) was updated with success!',
                        'data': result
                    }
                    return_code = HTTPStatus.OK
            except ValidationError as e:
                result = {
                    'status': 'ERROR',
                    'message': f'Invalid data for {human_name} (id={template_pipeline_id})',
                    'errors': translate_validation(e.messages)
                }

                return_code = 400

            except DataConsistencyError as e:

                result = {'status': 'VALIDATION ERROR',
                          'message': e.message}
                return_code = 400

                log.exception("Error in PATCH")
                db.session.rollback()

            except Exception as e:
                result = {'status': 'ERROR',
                          'message': "Internal error"}
                return_code = 500

                log.exception("Error in PATCH")
                db.session.rollback()

        return result, return_code
    
class TemplatePipelineStepApi(Resource):

    @staticmethod
    @requires_auth
    def delete(template_pipeline_id, step_id):
        result = {
                'status': 'ERROR',
                'message': f'Step not found (id={step_id}) for Template Pipeline (id={template_pipeline_id}).'
            }
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Deleting Step (id={step_id}) for Template Pipeline (id={template_pipeline_id})')
            
        step = TemplatePipelineStep.query.get(step_id)

        if step is not None and step.templatepipeline_id==template_pipeline_id:

            try:
                db.session.delete(step)
                db.session.commit()
                result = {
                    'status': 'OK',
                    'message': f'Template Pipeline Step (id={step_id}) from Template Pipeline (id={template_pipeline_id}) deleted with success!'
                }

            except Exception as e:
                result = {'status': 'ERROR',
                          'message': "Internal error"}
                return_code = HTTPStatus.INTERNAL_SERVER_ERROR
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
            
        return {"data":result}, return_code