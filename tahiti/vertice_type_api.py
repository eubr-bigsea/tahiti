import math
import logging

from tahiti.app_auth import requires_auth, requires_permission

from flask import request, g
from flask_restful import Resource
from http import HTTPStatus

from tahiti.schema import (
    VerticeTypeCreateRequestSchema,
    VerticeTypeItemResponseSchema,
    VerticeTypeListResponseSchema,
    partial_schema_factory,
)
from tahiti.models import VerticeType, db
from flask_babel import gettext

log = logging.getLogger(__name__)
# region Protected\s*
# endregion\w*


class VerticeTypeListApi(Resource):
    """REST API for listing class VerticeType"""

    def __init__(self):
        self.human_name = gettext("VerticeType")

    @requires_auth
    def get(self):
        """
        Retrieve a list of instances of class VerticeType.

        :return: A JSON object containing the list of VerticeType instances data.
        :rtype: dict
        """
        if request.args.get("fields"):
            only = [f.strip() for f in request.args.get("fields").split(",")]
        else:
            only = (
                ("id",)
                if request.args.get("simple", "false") == "true"
                else None
            )
        enabled_filter = request.args.get("enabled")
        if enabled_filter:
            vertice_types = VerticeType.query.filter(
                VerticeType.enabled == (enabled_filter != "false")
            )
        else:
            vertice_types = VerticeType.query
        name_filter = request.args.get('name')
        if name_filter:
            vertice_types = vertice_types.filter(
                     VerticeType.name.like(
                         '%%{}%%'.format(name_filter)))

        sort = request.args.get("sort", "name")
        if sort not in ["name", "id"]:
            sort = "name"
        sort_option = getattr(VerticeType, sort)
        if request.args.get("asc", "true") == "false":
            sort_option = sort_option.desc()
        vertice_types = vertice_types.order_by(sort_option)

        page = request.args.get("page") or "1"
        if page is not None and page.isdigit():
            page_size = int(request.args.get("size", 20))
            page = int(page)
            pagination = vertice_types.paginate(page, page_size, True)
            result = {
                "data": VerticeTypeListResponseSchema(many=True, only=only).dump(
                    pagination.items
                ),
                "pagination": {
                    "page": page,
                    "size": page_size,
                    "total": pagination.total,
                    "pages": int(math.ceil(1.0 * pagination.total / page_size)),
                },
            }
        else:
            result = {
                "data": VerticeTypeListResponseSchema(many=True, only=only).dump(
                    vertice_types
                )
            }

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext("Listing %(name)s", name=self.human_name))
        return result

    @requires_auth
    def post(self):
        """
        Add a single instance of class VerticeType.

        :return: A JSON object containing a success message.
        :rtype: dict
        """
        result = {
            "status": "ERROR",
            "message": gettext("Missing json in the request body"),
        }
        return_code = HTTPStatus.BAD_REQUEST

        if request.json is not None:
            request_schema = VerticeTypeCreateRequestSchema()
            response_schema = VerticeTypeItemResponseSchema()
            data = request.json

            # User information
            data["user_id"] = g.user.id
            data["user_login"] = g.user.login
            data["user_name"] = g.user.name

            vertice_type = request_schema.load(request.json)
            # Parent
            if "parent_id" in data:
                vertice_type.parent = VerticeType.query.get(data["parent_id"])

            if log.isEnabledFor(logging.DEBUG):
                log.debug(gettext("Adding %s"), self.human_name)
            vertice_type = vertice_type
            db.session.add(vertice_type)
            db.session.commit()
            result = response_schema.dump(vertice_type)
            return_code = HTTPStatus.CREATED
        return result, return_code


class VerticeTypeDetailApi(Resource):
    """REST API for a single instance of class VerticeType"""

    def __init__(self):
        self.human_name = gettext("VerticeType")

    @requires_auth
    def get(self, vertice_type_id):
        """
        Retrieve a single instance of class VerticeType.

        :param vertice_type_id: The ID of the VerticeType instance to retrieve.
        :type vertice_type_id: int
        :return: A JSON object containing the VerticeType instance data.
        :rtype: dict
        """

        if log.isEnabledFor(logging.DEBUG):
            log.debug(
                gettext("Retrieving %s (id=%s)"),
                self.human_name,
                vertice_type_id,
            )

        vertice_type = VerticeType.query.get(vertice_type_id)
        return_code = HTTPStatus.OK
        if vertice_type is not None:
            result = {
                "status": "OK",
                "data": [VerticeTypeItemResponseSchema().dump(vertice_type)],
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                "status": "ERROR",
                "message": gettext(
                    "%(name)s not found (id=%(id)s)",
                    name=self.human_name,
                    id=vertice_type_id,
                ),
            }

        return result, return_code

    @requires_auth
    @requires_permission(
        "ADMINISTRATOR",
    )
    def delete(self, vertice_type_id):
        """
        Delete a single instance of class VerticeType.

        :param vertice_type_id: The ID of the VerticeType instance to delete.
        :type vertice_type_id: int
        :return: A JSON object containing a success message.
        :rtype: dict
        """

        return_code = HTTPStatus.NO_CONTENT
        if log.isEnabledFor(logging.DEBUG):
            log.debug(
                gettext("Deleting %s (id=%s)"), self.human_name, vertice_type_id
            )
        vertice_type = VerticeType.query.get(vertice_type_id)
        if vertice_type is not None:
            db.session.delete(vertice_type)
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
                    id=vertice_type_id,
                ),
            }
        return result, return_code

    @requires_auth
    @requires_permission(
        "ADMINISTRATOR",
    )
    def patch(self, vertice_type_id):
        """
        Update a single instance of class VerticeType.

        :param vertice_type_id: The ID of the VerticeType instance to update.
        :type vertice_type_id: int
        :return: A JSON object containing a success message.
        :rtype: dict
        """
        result = {"status": "ERROR", "message": gettext("Insufficient data.")}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(
                gettext("Updating %s (id=%s)"), self.human_name, vertice_type_id
            )
        if request.json:
            request_schema = partial_schema_factory(
                VerticeTypeCreateRequestSchema
            )
            response_schema = VerticeTypeItemResponseSchema()
            # Ignore missing fields to allow partial updates

            data = request.json

            vertice_type = request_schema.load(data, partial=True)
            # Parent
            if "parent_id" in data:
                if data['parent_id'] is None:
                    vertice_type.parent = None
                else:
                    vertice_type.parent = VerticeType.query.get(
                        data["parent_id"])

            vertice_type.id = vertice_type_id
            vertice_type = db.session.merge(vertice_type)

            db.session.commit()

            if vertice_type is not None:
                return_code = HTTPStatus.OK
                result = {
                    "status": "OK",
                    "message": gettext(
                        "%(n)s (id=%(id)s) was updated with success!",
                        n=self.human_name,
                        id=vertice_type_id,
                    ),
                    "data": [response_schema.dump(vertice_type)],
                }
        return result, return_code
