import math
import logging

from tahiti.app_auth import requires_auth, requires_permission

from flask import request
from flask_restful import Resource
from http import HTTPStatus

from flask_babel import gettext

from tahiti.models import PipelineTemplate, db
from tahiti.schema import (
    PipelineTemplateCreateRequestSchema,
    PipelineTemplateItemResponseSchema,
    PipelineTemplateListResponseSchema,
    partial_schema_factory,
)

log = logging.getLogger(__name__)
# region Protected\s*
# endregion


class PipelineTemplateListApi(Resource):
    """REST API for listing class PipelineTemplate"""

    def __init__(self):
        self.human_name = gettext("PipelineTemplate")

    @requires_auth
    def get(self):
        """
        Retrieve a list of instances of class PipelineTemplate.

        :return: A JSON object containing the list of PipelineTemplate
            instances data.
        :rtype: dict
        """
        if request.args.get("fields"):
            only = [f.strip() for f in request.args.get("fields").split(",")]
        else:
            only = ["id"] if request.args.get(
                "simple", "false") == "true" else None
        enabled_filter = request.args.get("enabled")
        if enabled_filter:
            pipeline_templates = PipelineTemplate.query.filter(
                PipelineTemplate.enabled == (enabled_filter != "false")
            )
        else:
            pipeline_templates = PipelineTemplate.query

        # Filters
        name = request.args.get('name')
        if name:
            pipeline_templates = pipeline_templates.filter(
                PipelineTemplate.name.ilike(f'%{name}%'))

        # Sorting
        sort = request.args.get('sort', 'name')
        if sort not in ['name', 'id']:
            sort = 'name'
        sort_option = getattr(PipelineTemplate, sort)
        if request.args.get('asc', 'true') == 'false':
            sort_option = sort_option.desc()

        pipeline_templates = pipeline_templates.order_by(sort_option)

        page = request.args.get("page") or "1"
        if page is not None and page.isdigit():
            page_size = int(request.args.get("size", 20))
            page = int(page)
            pagination = pipeline_templates.paginate(page, page_size, True)
            result = {
                "data": PipelineTemplateListResponseSchema(
                    many=True, only=only).dump(pagination.items),
                "pagination": {
                    "page": page,
                    "size": page_size,
                    "total": pagination.total,
                    "pages": int(math.ceil(1.0 * pagination.total / page_size)),
                },
            }
        else:
            result = {
                "data": PipelineTemplateListResponseSchema(
                    many=True, only=only).dump(pipeline_templates)
            }

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext("Listing %(name)s", name=self.human_name))
        return result

    @requires_auth
    @requires_permission(
        "ADMINISTRATOR",
    )
    def post(self):
        """
        Add a single instance of class PipelineTemplate.

        :return: A JSON object containing a success message.
        :rtype: dict
        """
        result = {
            "status": "ERROR",
            "message": gettext("Missing json in the request body"),
        }
        return_code = HTTPStatus.BAD_REQUEST

        if request.json is not None:
            request_schema = PipelineTemplateCreateRequestSchema()
            response_schema = PipelineTemplateItemResponseSchema()
            data = request.json
            data["version"] = 1
            pipeline_template = request_schema.load(request.json)

            if log.isEnabledFor(logging.DEBUG):
                log.debug(gettext("Adding %s"), self.human_name)
            pipeline_template = pipeline_template
            db.session.add(pipeline_template)
            db.session.commit()
            result = response_schema.dump(pipeline_template)
            return_code = HTTPStatus.CREATED
        return result, return_code


class PipelineTemplateDetailApi(Resource):
    """REST API for a single instance of class PipelineTemplate"""

    def __init__(self):
        self.human_name = gettext("PipelineTemplate")

    @requires_auth
    def get(self, pipeline_template_id):
        """
        Retrieve a single instance of class PipelineTemplate.

        :param pipeline_template_id: The ID of the PipelineTemplate instance
            to retrieve.
        :type pipeline_template_id: int
        :return: A JSON object containing the PipelineTemplate instance data.
        :rtype: dict
        """

        if log.isEnabledFor(logging.DEBUG):
            log.debug(
                gettext("Retrieving %s (id=%s)"),
                    self.human_name, pipeline_template_id
            )

        pipeline_template = PipelineTemplate.query.get(pipeline_template_id)
        return_code = HTTPStatus.OK
        if pipeline_template is not None:
            result = {
                "status": "OK",
                "data": [PipelineTemplateItemResponseSchema().dump(
                    pipeline_template)],
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                "status": "ERROR",
                "message": gettext(
                    "%(name)s not found (id=%(id)s)",
                    name=self.human_name,
                    id=pipeline_template_id,
                ),
            }

        return result, return_code

    @requires_auth
    @requires_permission(
        "ADMINISTRATOR",
    )
    def delete(self, pipeline_template_id):
        """
        Delete a single instance of class PipelineTemplate.

        :param pipeline_template_id: The ID of the PipelineTemplate instance
            to delete.
        :type pipeline_template_id: int
        :return: A JSON object containing a success message.
        :rtype: dict
        """

        return_code = HTTPStatus.NO_CONTENT
        if log.isEnabledFor(logging.DEBUG):
            log.debug(
                gettext("Deleting %s (id=%s)"), self.human_name,
                  pipeline_template_id
            )
        pipeline_template = PipelineTemplate.query.get(pipeline_template_id)
        if pipeline_template is not None:
            db.session.delete(pipeline_template)
            db.session.commit()
            result = {
                "status": "OK",
                "message": gettext(
                    "%(name)s deleted with success!", name=self.human_name
                ),
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                "status": "ERROR",
                "message": gettext(
                    "%(name)s not found (id=%(id)s).",
                    name=self.human_name,
                    id=pipeline_template_id,
                ),
            }
        return result, return_code

    @requires_auth
    @requires_permission(
        "ADMINISTRATOR",
    )
    def patch(self, pipeline_template_id):
        """
        Update a single instance of class PipelineTemplate.

        :param pipeline_template_id: The ID of the PipelineTemplate instance
            to update.
        :type pipeline_template_id: int
        :return: A JSON object containing a success message.
        :rtype: dict
        """
        result = {"status": "ERROR", "message": gettext("Insufficient data.")}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(
                gettext("Updating %s (id=%s)"), self.human_name,
                    pipeline_template_id
            )
        if request.json:
            request_schema = partial_schema_factory(
                PipelineTemplateCreateRequestSchema)
            response_schema = PipelineTemplateItemResponseSchema()
            # Ignore missing fields to allow partial updates

            data = request.json

            pipeline_template = request_schema.load(data, partial=True)
            pipeline_template.id = pipeline_template_id
            pipeline_template = db.session.merge(pipeline_template)

            db.session.commit()

            if pipeline_template is not None:
                return_code = HTTPStatus.OK
                result = {
                    "status": "OK",
                    "message": gettext(
                        "%(n)s (id=%(id)s) was updated with success!",
                        n=self.human_name,
                        id=pipeline_template_id,
                    ),
                    "data": [response_schema.dump(pipeline_template)],
                }
        return result, return_code
