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


class PipelineListApi(Resource):
    """ REST API for listing class Pipeline """

    def __init__(self):
        self.human_name = gettext('Pipeline')

    @requires_auth
    def get(self):
        """
        Retrieve a list of instances of class Pipeline.

        :return: A JSON object containing the list of Pipeline instances data.
        :rtype: dict
        """
        if request.args.get('fields'):
            only = [f.strip() for f in request.args.get('fields').split(',')]
        else:
            only = ('id', ) if request.args.get(
                'simple', 'false') == 'true' else None
        enabled_filter = request.args.get('enabled')
        if enabled_filter:
            pipelines = Pipeline.query.filter(
                Pipeline.enabled == (enabled_filter != 'false'))
        else:
            pipelines = Pipeline.query

        sort = request.args.get('sort', 'name')
        if sort not in ['name']:
            sort = 'name'
        sort_option = getattr(Pipeline, sort)
        if request.args.get('asc', 'true') == 'false':
            sort_option = sort_option.desc()
        pipelines = pipelines.order_by(sort_option)

        page = request.args.get('page') or '1'
        if page is not None and page.isdigit():
            page_size = int(request.args.get('size', 20))
            page = int(page)
            pagination = pipelines.paginate(page, page_size, True)
            result = {
                'data': PipelineListResponseSchema(
                    many=True, only=only).dump(pagination.items),
                'pagination': {
                    'page': page, 'size': page_size,
                    'total': pagination.total,
                    'pages': int(math.ceil(1.0 * pagination.total / page_size))}
            }
        else:
            result = {
                'data': PipelineListResponseSchema(
                    many=True, only=only).dump(
                    pipelines)}

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Listing %(name)s', name=self.human_name))
        return result

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def post(self):
        """
        Add a single instance of class Pipeline.

        :return: A JSON object containing a success message.
        :rtype: dict
        """
        result = {'status': 'ERROR',
                  'message': gettext("Missing json in the request body")}
        return_code = HTTPStatus.BAD_REQUEST

        if request.json is not None:
            request_schema = PipelineCreateRequestSchema()
            response_schema = PipelineItemResponseSchema()
            pipeline = request_schema.load(request.json)

            if log.isEnabledFor(logging.DEBUG):
                log.debug(gettext('Adding %s'), self.human_name)
            pipeline = pipeline
            db.session.add(pipeline)
            db.session.commit()
            result = response_schema.dump(pipeline)
            return_code = HTTPStatus.CREATED
        return result, return_code


class PipelineDetailApi(Resource):
    """ REST API for a single instance of class Pipeline """

    def __init__(self):
        self.human_name = gettext('Pipeline')

    @requires_auth
    def get(self, pipeline_id):
        """
        Retrieve a single instance of class Pipeline.

        :param pipeline_id: The ID of the Pipeline instance to retrieve.
        :type pipeline_id: int
        :return: A JSON object containing the Pipeline instance data.
        :rtype: dict
        """

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Retrieving %s (id=%s)'), self.human_name,
                      pipeline_id)

        pipeline = Pipeline.query.get(pipeline_id)
        return_code = HTTPStatus.OK
        if pipeline is not None:
            result = {
                'status': 'OK',
                'data': [PipelineItemResponseSchema().dump(
                    pipeline)]
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext(
                    '%(name)s not found (id=%(id)s)',
                    name=self.human_name, id=pipeline_id)
            }

        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def delete(self, pipeline_id):
        """
        Delete a single instance of class Pipeline.

        :param pipeline_id: The ID of the Pipeline instance to delete.
        :type pipeline_id: int
        :return: A JSON object containing a success message.
        :rtype: dict
        """

        return_code = HTTPStatus.NO_CONTENT
        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Deleting %s (id=%s)'), self.human_name,
                      pipeline_id)
        pipeline = Pipeline.query.get(pipeline_id)
        if pipeline is not None:
            db.session.delete(pipeline)
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
                                   name=self.human_name, id=pipeline_id)
            }
        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def patch(self, pipeline_id):
        """
        Update a single instance of class Pipeline.

        :param pipeline_id: The ID of the Pipeline instance to update.
        :type pipeline_id: int
        :return: A JSON object containing a success message.
        :rtype: dict
        """
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Updating %s (id=%s)'), self.human_name,
                      pipeline_id)
        if request.json:
            request_schema = partial_schema_factory(
                PipelineCreateRequestSchema)
            response_schema = PipelineItemResponseSchema()
            # Ignore missing fields to allow partial updates
            pipeline = request_schema.load(request.json, partial=True)
            pipeline.id = pipeline_id
            pipeline = db.session.merge(pipeline)
            db.session.commit()

            if pipeline is not None:
                return_code = HTTPStatus.OK
                result = {
                    'status': 'OK',
                    'message': gettext(
                        '%(n)s (id=%(id)s) was updated with success!',
                        n=self.human_name,
                        id=pipeline_id),
                    'data': [response_schema.dump(
                        pipeline)]
                }
        return result, return_code

