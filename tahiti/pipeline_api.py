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

human_name = gettext('Pipeline')


class PipelineApi(Resource):

    @staticmethod
    def _create_pipeline_steps(data:dict, steps:dict) -> (dict,HTTPStatus):

        pipeline_id = data['id']
        pipeline_step_schema = PipelineStepPrivateCreateRequestSchema()

        if steps is not None:
            for index,step in enumerate(steps):
                step['order'] = index+1
                step['pipeline_id'] = pipeline_id

                pipeline_step = pipeline_step_schema.load(step)
                 
                try:
                    
                    if log.isEnabledFor(logging.DEBUG):
                        log.debug(f'Adding Step')
                    db.session.add(pipeline_step)
                    db.session.commit()

                    pipeline_steps = PipelineStep.query.filter(PipelineStep.pipeline_id==pipeline_id).all()
                    result = data
                    result['steps'] = PipelineStepItemResponseSchema(many=True).dump(pipeline_steps)
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
    def _create_pipeline_from_scratch(data:dict) -> (dict,HTTPStatus):
        request_schema = PipelineCreateRequestSchema()
        response_schema = PipelineItemResponseSchema()

        pipeline = request_schema.load(data)

        try:
            if log.isEnabledFor(logging.DEBUG):
                log.debug(f'Adding {human_name}')

            db.session.add(pipeline)
            db.session.commit()
            
            result = response_schema.dump(pipeline)
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
    def _create_pipeline_from_template(data:dict, create_steps:bool) -> (dict,HTTPStatus):

        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Creating Pipeline using Template Pipeline')

        # getting the template pipeline that will be used as model to create a new pipeline
        template_pipeline_id = data.pop('templatepipeline_id')
        template_pipeline = TemplatePipeline.query.filter(TemplatePipeline.id==template_pipeline_id).first()

        
        # if the template pipeline exists, create a new pipeline with the info passed and template
        if template_pipeline is not None:
            request_schema = PipelineCreateRequestSchema()
            response_schema = PipelineItemResponseSchema()

            template_schema = TemplatePipelineItemResponseSchema()
            template_pipeline = template_schema.dump(template_pipeline)

            pipeline_attributes = [field for field in request_schema.fields]

            # get the data missing in pipeline request body copying from template pipeline
            for key in [key for key in template_pipeline.keys() if key in pipeline_attributes and key not in data.keys()]:
                    data[key]=template_pipeline[key]

            result, result_code = PipelineApi._create_pipeline_from_scratch(data)

            # get the steps of the template and duplicate them as pipeline steps 
            if create_steps:
                try:
                    template_pipeline_steps = TemplatePipelineStep.query.filter(TemplatePipelineStep.templatepipeline_id==template_pipeline_id).all()
                    steps = TemplatePipelineStepItemResponseSchema(many=True).dump(template_pipeline_steps)

                    pipeline_step_schema = PipelineStepPrivateCreateRequestSchema()

                    pipeline_id = result['id']

                    for step in steps:
                        pipeline_step = {'name':step['name'],\
                                            'order':step['order'],\
                                                'description': step['description'],\
                                                    'scheduling':step['scheduling'],\
                                                        'status':step['status'],\
                                                            'pipeline_id':pipeline_id}

                        pipeline_step = pipeline_step_schema.load(pipeline_step)

                        if log.isEnabledFor(logging.DEBUG):
                            log.debug(f'Adding Step')
                        db.session.add(pipeline_step)
                        db.session.commit()
                    
                    # steps as PipelineStep objects, they need to be dumped with the PipelineStepItemResponseSchema before add to result
                    pipeline_steps = PipelineStep.query.filter(PipelineStep.pipeline_id==pipeline_id).all()
                    result['steps'] = PipelineStepItemResponseSchema(many=True).dump(pipeline_steps)
                
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
            
        else:
            result= {
            'status': 'ERROR', 
            'message': f'Template Pipeline (id={template_pipeline_id}) does not exist!'
            }
            result_code = HTTPStatus.NOT_FOUND

        return result, result_code
        

    @staticmethod
    @requires_auth
    def get():

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext(f'Listing {human_name}'))

        pipelines = Pipeline.query.all()
        result = PipelineItemResponseSchema(many=True).dump(pipelines)
        result_code = HTTPStatus.OK

        for index,pipeline in enumerate(result):
            steps = PipelineStep.query.filter(PipelineStep.pipeline_id==pipeline['id']).order_by(PipelineStep.order).all()
            result[index]['steps'] = PipelineStepItemResponseSchema(many=True).dump(steps)
        
        return {'data': result},result_code



    @staticmethod
    @requires_auth
    def post():
        result, result_code = {"status":"ERROR", "message":"Not found"}, HTTPStatus.NOT_FOUND

        if request.json is not None:

            # check if steps were passed in the request structure
            steps = request.json.pop('steps', None)
            create_steps_from_template = False if steps is not None else True

            # check if a template pipeline ID was passed and call the specific method for pipeline creation using template or from scratch
            if 'templatepipeline_id' in request.json.keys():
                result, result_code = PipelineApi._create_pipeline_from_template(data=request.json, create_steps=create_steps_from_template)
            else:
                result, result_code = PipelineApi._create_pipeline_from_scratch(data=request.json)

            # create steps if they were passed through the request body
            if not create_steps_from_template and result_code is HTTPStatus.CREATED:
                result, result_code = PipelineApi._create_pipeline_steps(data=result, steps=steps)

            if 'steps' not in result.keys():
                result['steps'] = []

            return {'data': result}, result_code 

class PipelineDetailApi(Resource):

    @staticmethod
    @requires_auth
    def get(pipeline_id):
        result, result_code = {"status":"ERROR",
                                "message":f"{human_name} not found (id={pipeline_id})"}, HTTPStatus.NOT_FOUND
        
        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Getting {human_name} (id={pipeline_id})')

        pipeline = Pipeline.query.filter(Pipeline.id==pipeline_id).first()
        if pipeline is not None:
            result = PipelineItemResponseSchema().dump(pipeline)
            result_code = HTTPStatus.OK

            steps = PipelineStep.query.filter(PipelineStep.pipeline_id==pipeline_id).order_by(PipelineStep.order).all()
            result['steps'] = PipelineStepItemResponseSchema(many=True).dump(steps)

        return {'data': result}, result_code
            

    @staticmethod
    @requires_auth
    def delete(pipeline_id):
        result = {
                'status': 'ERROR',
                'message': f'{human_name} not found (id={pipeline_id}).'
            }
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Deleting %s (id=%s)'), human_name,
                      pipeline_id)
            
        pipeline = Pipeline.query.get(pipeline_id)
        steps = PipelineStep.query.filter(PipelineStep.pipeline_id==pipeline_id).all()

        if pipeline is not None:
            try:
                db.session.delete(pipeline)
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
    def patch(pipeline_id):
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Updating %{human_name} (id={pipeline_id})')
            
        if request.json:
            request_schema = partial_schema_factory(
                PipelineUpdateRequestSchema)
            response_schema = PipelineItemResponseSchema()

            steps = request.json.pop('steps', None)

            try:
                pipeline = request_schema.load(request.json, partial=True)
                pipeline.id = pipeline_id
                pipeline = db.session.merge(pipeline)
                db.session.commit()

                if pipeline is not None:

                    result = response_schema.dump(pipeline)

                    if steps is not None:
                        steps = PipelineStepUpdateRequestSchema(many=True).load(steps)

                        pipeline_steps = PipelineStep.query.filter(PipelineStep.pipeline_id==pipeline_id).all()
                        pipeline_steps_ids = []

                        for step in pipeline_steps:
                            pipeline_steps_ids.append(step.id)
                            step.enabled = 'DISABLED'
                            db.session.merge(step)
                        db.session.commit()

                    for index,step in enumerate(steps):
                        step.order = index+1
                        if step.id is not None:
                            if step.id not in pipeline_steps_ids:
                                raise DataConsistencyError(message=f"The Pipeline Step (id={step.id}) is associated with Pipeline (id={step.pipeline_id}), not the Pipeline passed through the body (id={pipeline_id}).")
                            db.session.merge(step)
                        else:
                            step.pipeline_id = pipeline_id
                            db.session.add(step)
                        db.session.commit()

                    pipeline_steps = PipelineStep.query.filter(PipelineStep.pipeline_id==pipeline_id).order_by(PipelineStep.order).all()
                    result['steps'] = PipelineStepItemResponseSchema(many=True).dump(pipeline_steps)
                    result = {
                        'status': 'OK',
                        'message': f'{human_name} (id={pipeline_id}) was updated with success!',
                        'data': result
                    }
                    return_code = HTTPStatus.OK
            except ValidationError as e:
                result = {
                    'status': 'ERROR',
                    'message': f'Invalid data for {human_name} (id={pipeline_id})',
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
    
class PipelineStepApi(Resource):

    @staticmethod
    @requires_auth
    def delete(pipeline_id, step_id):
        result = {
                'status': 'ERROR',
                'message': f'Step not found (id={step_id}) for Pipeline (id={pipeline_id}).'
            }
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Deleting Step (id={step_id}) for Pipeline (id={pipeline_id})')
            
        step = PipelineStep.query.get(step_id)

        if step is not None and step.pipeline_id==pipeline_id:

            try:
                db.session.delete(step)
                db.session.commit()
                result = {
                    'status': 'OK',
                    'message': f'Pipeline Step (id={step_id}) from Pipeline (id={pipeline_id}) deleted with success!'
                }

            except Exception as e:
                result = {'status': 'ERROR',
                          'message': "Internal error"}
                return_code = HTTPStatus.INTERNAL_SERVER_ERROR
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
            
        return {"data":result}, return_code