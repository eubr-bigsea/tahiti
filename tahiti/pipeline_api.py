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
    @requires_auth
    def get():

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext(f'Listing {human_name}'))

        pipelines = Pipeline.query.all()

        result = PipelineItemResponseSchema(many=True).dump(pipelines)
        result_code = HTTPStatus.OK

        return {'data': result},result_code

    @staticmethod
    @requires_auth
    def post():
        result, result_code = {"status":"ERROR", "message":"Not found"}, HTTPStatus.NOT_FOUND

        request_schema = PipelineCreateRequestSchema()
        response_schema = PipelineItemResponseSchema()
        
        if request.json is not None:
            pipelinetemplate_id = request.json.pop('pipelinetemplate_id', None)

            fields_to_copy = [key for key in [field for field in request_schema.fields] \
                            if key not in request.json.keys() and key != "pipelinetemplate_id"]

            if pipelinetemplate_id is not None:
                pipeline_template = PipelineTemplate.query.get(pipelinetemplate_id)

                if pipeline_template is not None:
                    pipeline_template = PipelineTemplateItemResponseSchema().dump(pipeline_template)

                    for field in fields_to_copy:
                        request.json[field] = pipeline_template[field]

            pipeline = request_schema.load(request.json)
            
            if log.isEnabledFor(logging.DEBUG):
                log.debug(f'Adding {human_name}')

            db.session.add(pipeline)
            db.session.commit()
            
            result = {'data':response_schema.dump(pipeline)}
            result_code = HTTPStatus.CREATED
            
        return result, result_code

    @staticmethod
    @requires_auth
    def patch():
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND
    
        if request.json:

            request_schema = PipelineUpdateRequestSchema()
            response_schema = PipelineItemResponseSchema()

            pipeline = request_schema.load(request.json)

            if log.isEnabledFor(logging.DEBUG):
                log.debug(f'Updating %{human_name} (id={pipeline.id})')

            pipeline = db.session.merge(pipeline)
            db.session.commit()

            if pipeline is not None:

                result = {
                    'status': 'OK',
                    'message': f'{human_name} (id={pipeline.id}) was updated with success!',
                    'data': response_schema.dump(pipeline)
                }
                return_code = HTTPStatus.OK
                
        return result, return_code


class PipelineDetailApi(Resource):

    @staticmethod
    @requires_auth
    def get(pipeline_id):
        result, result_code = {"status":"ERROR",
                                "message":f"{human_name} not found (id={pipeline_id})"}, HTTPStatus.NOT_FOUND
        
        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Getting {human_name} (id={pipeline_id})')

        pipeline = Pipeline.query.get(pipeline_id)

        if pipeline is not None:
            result = PipelineItemResponseSchema().dump(pipeline)
            result_code = HTTPStatus.OK

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
            log.debug(f'Deleting {human_name} (id={pipeline_id})')
            
        pipeline = Pipeline.query.get(pipeline_id)

        if pipeline is not None:
            db.session.delete(pipeline)
            db.session.commit()
            result = {
                'status': 'OK',
                'message': f'{human_name} deleted with success!'
            }
            return_code = HTTPStatus.OK
            
        return {"data":result}, return_code