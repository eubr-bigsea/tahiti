import math
import logging

from tahiti.app_auth import requires_auth, requires_permission

from flask import request
from flask_restful import Resource
from http import HTTPStatus

from tahiti.schema import *
from tahiti.models import *
from flask_babel import gettext

log = logging.getLogger(__name__)
# region Protected\s*
# endregion\w*


class PipelineStepListApi(Resource):
    """ REST API for listing class PipelineStep """

    def __init__(self):
        self.human_name = gettext('PipelineStep')

    @requires_auth
    def get(self):
        """
        Retrieve a list of instances of class PipelineStep.

        :return: A JSON object containing the list of PipelineStep instances data.
        :rtype: dict
        """
        if request.args.get('fields'):
            only = [f.strip() for f in request.args.get('fields').split(',')]
        else:
            only = ('id', ) if request.args.get(
                'simple', 'false') == 'true' else None
        enabled_filter = request.args.get('enabled')
        if enabled_filter:
            pipeline_steps = PipelineStep.query.filter(
                PipelineStep.enabled == (enabled_filter != 'false'))
        else:
            pipeline_steps = PipelineStep.query

        sort = request.args.get('sort', 'name')
        if sort not in ['name']:
            sort = 'name'
        sort_option = getattr(PipelineStep, sort)
        if request.args.get('asc', 'true') == 'false':
            sort_option = sort_option.desc()
        pipeline_steps = pipeline_steps.order_by(sort_option)

        page = request.args.get('page') or '1'
        if page is not None and page.isdigit():
            page_size = int(request.args.get('size', 20))
            page = int(page)
            pagination = pipeline_steps.paginate(page, page_size, True)
            result = {
                'data': PipelineStepListResponseSchema(
                    many=True, only=only).dump(pagination.items),
                'pagination': {
                    'page': page, 'size': page_size,
                    'total': pagination.total,
                    'pages': int(math.ceil(1.0 * pagination.total / page_size))}
            }
        else:
            result = {
                'data': PipelineStepListResponseSchema(
                    many=True, only=only).dump(
                    pipeline_steps)}

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Listing %(name)s', name=self.human_name))
        return result

    @requires_auth
    def post(self):
        """
        Add a single instance of class PipelineStep.

        :return: A JSON object containing a success message.
        :rtype: dict
        """
        result = {'status': 'ERROR',
                  'message': gettext("Missing json in the request body")}
        return_code = HTTPStatus.BAD_REQUEST

        if request.json is not None:
            request_schema = PipelineStepCreateRequestSchema()
            response_schema = PipelineStepItemResponseSchema()
            data = request.json
            pipeline_step = request_schema.load(request.json)

            if log.isEnabledFor(logging.DEBUG):
                log.debug(gettext('Adding %s'), self.human_name)
            pipeline_step = pipeline_step
            db.session.add(pipeline_step)
            db.session.commit()
            result = response_schema.dump(pipeline_step)
            return_code = HTTPStatus.CREATED
        return result, return_code


class PipelineStepDetailApi(Resource):
    """ REST API for a single instance of class PipelineStep """

    def __init__(self):
        self.human_name = gettext('PipelineStep')

    @requires_auth
    def get(self, pipeline_step_id):
        """
        Retrieve a single instance of class PipelineStep.

        :param pipeline_step_id: The ID of the PipelineStep instance to retrieve.
        :type pipeline_step_id: int
        :return: A JSON object containing the PipelineStep instance data.
        :rtype: dict
        """

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Retrieving %s (id=%s)'), self.human_name,
                      pipeline_step_id)

        pipeline_step = PipelineStep.query.get(pipeline_step_id)
        return_code = HTTPStatus.OK
        if pipeline_step is not None:
            result = {
                'status': 'OK',
                'data': [PipelineStepItemResponseSchema().dump(
                    pipeline_step)]
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext(
                    '%(name)s not found (id=%(id)s)',
                    name=self.human_name, id=pipeline_step_id)
            }

        return result, return_code

    @requires_auth
    def delete(self, pipeline_step_id):
        """
        Delete a single instance of class PipelineStep.

        :param pipeline_step_id: The ID of the PipelineStep instance to delete.
        :type pipeline_step_id: int
        :return: A JSON object containing a success message.
        :rtype: dict
        """

        return_code = HTTPStatus.NO_CONTENT
        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Deleting %s (id=%s)'), self.human_name,
                      pipeline_step_id)
        pipeline_step = PipelineStep.query.get(pipeline_step_id)
        if pipeline_step is not None:
            db.session.delete(pipeline_step)
            db.session.commit()
            result = {
                'status': 'OK',
                'message': gettext('%(name)s deleted with success!',
                                   name=self.human_name)
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext('%(name)s not found (id=%(id)s).',
                                   name=self.human_name, id=pipeline_step_id)
            }
        return result, return_code

    @requires_auth
    def patch(self, pipeline_step_id):
        """
        Update a single instance of class PipelineStep.

        :param pipeline_step_id: The ID of the PipelineStep instance to update.
        :type pipeline_step_id: int
        :return: A JSON object containing a success message.
        :rtype: dict
        """
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Updating %s (id=%s)'), self.human_name,
                      pipeline_step_id)
        if request.json:
            request_schema = partial_schema_factory(
                PipelineStepCreateRequestSchema)
            response_schema = PipelineStepItemResponseSchema()
            # Ignore missing fields to allow partial updates

            data = request.json

            pipeline_step = request_schema.load(data, partial=True)
            pipeline_step.id = pipeline_step_id
            pipeline_step = db.session.merge(pipeline_step)

            db.session.commit()

            if pipeline_step is not None:
                return_code = HTTPStatus.OK
                result = {
                    'status': 'OK',
                    'message': gettext(
                        '%(n)s (id=%(id)s) was updated with success!',
                        n=self.human_name,
                        id=pipeline_step_id),
                    'data': [response_schema.dump(
                        pipeline_step)]
                }
        return result, return_code

