# -*- coding: utf-8 -*-}
import logging

from flask import request, current_app
from flask_restful import Resource

from tahiti.app_auth import requires_auth
from tahiti.schema import *

log = logging.getLogger(__name__)


class ApplicationListApi(Resource):
    """ REST API for listing class Application """

    @staticmethod
    @requires_auth
    def get():
        only = ('id', 'name') \
            if request.args.get('simple', 'false') == 'true' else None
        applications = Application.query.order_by('name')
        return ApplicationListResponseSchema(many=True, only=only).dump(
            applications).data

    @staticmethod
    @requires_auth
    def post():
        result, result_code = dict(
            status="ERROR", message="Missing json in the request body"), 401
        if request.json is not None:
            request_schema = ApplicationCreateRequestSchema()
            response_schema = ApplicationItemResponseSchema()
            form = request_schema.load(request.json)
            if form.errors:
                result, result_code = dict(
                    status="ERROR", message="Validation error",
                    errors=form.errors, ), 401
            else:
                try:
                    application = form.data
                    db.session.add(application)
                    db.session.commit()
                    result, result_code = response_schema.dump(
                        application).data, 200
                except Exception as e:
                    log.exception('Error in POST')
                    result, result_code = dict(status="ERROR",
                                               message="Internal error"), 500
                    if current_app.debug:
                        result['debug_detail'] = e.message
                    db.session.rollback()

        return result, result_code


class ApplicationDetailApi(Resource):
    """ REST API for a single instance of class Application """

    @staticmethod
    @requires_auth
    def get(application_id):
        application = Application.query.get(application_id)
        if application is not None:
            return ApplicationItemResponseSchema().dump(application).data
        else:
            return dict(status="ERROR", message="Not found"), 404

    @staticmethod
    @requires_auth
    def delete(application_id):
        result, result_code = dict(status="ERROR", message="Not found"), 404

        application = Application.query.get(application_id)
        if application is not None:
            try:
                db.session.delete(application)
                db.session.commit()
                result, result_code = dict(status="OK", message="Deleted"), 200
            except Exception as e:
                log.exception('Error in DELETE')
                result, result_code = dict(status="ERROR",
                                           message="Internal error"), 500
                if current_app.debug:
                    result['debug_detail'] = e.message
                db.session.rollback()
        return result, result_code

    @staticmethod
    @requires_auth
    def patch(application_id):
        result = dict(status="ERROR", message="Insufficient data")
        result_code = 404

        if request.json:
            request_schema = partial_schema_factory(
                ApplicationCreateRequestSchema)
            # Ignore missing fields to allow partial updates
            form = request_schema.load(request.json, partial=True)
            response_schema = ApplicationItemResponseSchema()
            if not form.errors:
                try:
                    form.data.id = application_id
                    application = db.session.merge(form.data)
                    db.session.commit()

                    if application is not None:
                        result, result_code = dict(
                            status="OK", message="Updated",
                            data=response_schema.dump(application).data), 200
                    else:
                        result = dict(status="ERROR", message="Not found")
                except Exception as e:
                    log.exception('Error in PATCH')
                    result, result_code = dict(status="ERROR",
                                               message="Internal error"), 500
                    if current_app.debug:
                        result['debug_detail'] = e.message
                    db.session.rollback()
            else:
                result = dict(status="ERROR", message="Invalid data",
                              errors=form.errors)
        return result, result_code
