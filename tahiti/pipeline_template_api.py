# -*- coding: utf-8 -*-}
from http import HTTPStatus
import logging

from flask import request
from flask_babel import gettext
from flask_restful import Resource

from tahiti.app_auth import requires_auth
from tahiti.schema import *
from tahiti.models import PipelineTemplate

log = logging.getLogger(__name__)

human_name = gettext('PipelineTemplate')


class PipelineTemplateApi(Resource):

    @staticmethod
    @requires_auth
    def get():

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext(f'Listing {human_name}'))

        pipeline_templates = PipelineTemplate.query.all() 

        result = PipelineTemplateItemResponseSchema(many=True).dump(pipeline_templates)
        result_code = HTTPStatus.OK

        return {'data': result},result_code

    @staticmethod
    @requires_auth
    def post():
        result, result_code = {"status":"ERROR", "message":"Not found"}, HTTPStatus.NOT_FOUND

        request_schema = PipelineTemplateCreateRequestSchema()
        response_schema = PipelineTemplateItemResponseSchema()
        
        if request.json is not None:

            pipeline_template = request_schema.load(request.json)

            if log.isEnabledFor(logging.DEBUG):
                log.debug(f'Adding {human_name}')

            db.session.add(pipeline_template)
            db.session.commit()
            
            result = {'data':response_schema.dump(pipeline_template)}
            result_code = HTTPStatus.CREATED
            
        return result, result_code

    @staticmethod
    @requires_auth
    def patch():
        
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND

            
        if request.json:

            request_schema = PipelineTemplateUpdateRequestSchema()
            response_schema = PipelineTemplateItemResponseSchema()

            pipeline_template = request_schema.load(request.json)

            if log.isEnabledFor(logging.DEBUG):
                log.debug(f'Updating %{human_name} (id={pipeline_template.id})')

            original = PipelineTemplate.query.get(pipeline_template.id)

            if original is not None:

                pipeline_template = db.session.merge(pipeline_template)
                db.session.commit()
                
                if pipeline_template is not None:

                    result = {
                        'status': 'OK',
                        'message': f'{human_name} (id={pipeline_template.id}) was updated with success!',
                        'data': response_schema.dump(pipeline_template)
                    }
                    return_code = HTTPStatus.OK
            else:
                result = {'status': 'ERROR', 'message': f'Pipeline Template with id={pipeline_template.id} does not exist'}
                return_code = HTTPStatus.NOT_FOUND

        return result, return_code


class PipelineTemplateDetailApi(Resource):

    @staticmethod
    @requires_auth
    def get(pipeline_template_id):

        result, result_code = {"status":"ERROR",
                                "message":f"{human_name} not found (id={pipeline_template_id})"}, HTTPStatus.NOT_FOUND
        
        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Getting {human_name} (id={pipeline_template_id})')

        pipeline_template = PipelineTemplate.query.get(pipeline_template_id)
        
        if pipeline_template is not None:
            result = PipelineTemplateItemResponseSchema().dump(pipeline_template)
            result_code = HTTPStatus.OK

        return {'data': result}, result_code
            
    @staticmethod
    @requires_auth
    def delete(pipeline_template_id):
        result = {
                'status': 'ERROR',
                'message': f'{human_name} not found (id={pipeline_template_id}).'
            }
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(f'Deleting {human_name} (id={pipeline_template_id})')
            
        pipeline_template = PipelineTemplate.query.get(pipeline_template_id)

        if pipeline_template is not None:
            db.session.delete(pipeline_template)
            db.session.commit()
            result = {
                'status': 'OK',
                'message': f'{human_name} deleted with success!'
            }
            return_code = HTTPStatus.OK
            
        return {"data":result}, return_code