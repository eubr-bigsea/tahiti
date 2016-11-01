# -*- coding: utf-8 -*-}
from flask import request, current_app
from flask_restful import Resource
from sqlalchemy.orm import joinedload

from app_auth import requires_auth
from cache import cache
from schema import *


def optimize_operation_query(operations):
    return operations \
        .options(joinedload(Operation.current_translation)) \
        .options(joinedload('forms.current_translation')) \
        .options(joinedload('ports.current_translation')) \
        .options(joinedload('ports.interfaces.current_translation')) \
        .options(joinedload('forms.fields.current_translation')) \
        .options(joinedload('categories.current_translation')) \
        .options(joinedload('forms')) \
        .options(joinedload('ports')) \
        .options(joinedload('ports.interfaces')) \
        .options(joinedload('forms.fields')) \
        .options(joinedload('categories'))


class OperationListApi(Resource):
    """ REST API for listing class Operation """

    @staticmethod
    @requires_auth
    def get():
        @cache.memoize(600, make_name=lambda f: request.url)
        def result():
            only = ('id', 'name') \
                if request.args.get('simple', 'false') == 'true' else None
            operations = optimize_operation_query(
                Operation.query.order_by('operation.name'))
            return OperationListResponseSchema(many=True, only=only).dump(
                operations).data

        return result()

    @staticmethod
    @requires_auth
    def post():
        result, result_code = dict(
            status="ERROR", message="Missing json in the request body"), 401
        if request.json is not None:
            request_schema = OperationCreateRequestSchema()
            response_schema = OperationItemResponseSchema()
            form = request_schema.load(request.json)
            if form.errors:
                result, result_code = dict(
                    status="ERROR", message="Validation error",
                    errors=form.errors, ), 401
            else:
                try:
                    operation = form.data
                    db.session.add(operation)
                    db.session.commit()
                    result, result_code = response_schema.dump(
                        operation).data, 200
                except Exception, e:
                    result, result_code = dict(status="ERROR",
                                               message="Internal error"), 500
                    if current_app.debug:
                        result['debug_detail'] = e.message
                    db.session.rollback()

        return result, result_code


class OperationDetailApi(Resource):
    """ REST API for a single instance of class Operation """

    @staticmethod
    @requires_auth
    def get(operation_id):
        @cache.memoize(600, make_name=lambda f: request.url)
        def result():
            operation = optimize_operation_query(
                Operation.query.filter_by(id=operation_id).order_by('1')).first()
            if operation is not None:
                return OperationItemResponseSchema().dump(operation).data
            else:
                return dict(status="ERROR", message="Not found"), 404

        return result()

    @staticmethod
    @requires_auth
    def delete(operation_id):
        result, result_code = dict(status="ERROR", message="Not found"), 404

        operation = Operation.query.get(operation_id)
        if operation is not None:
            try:
                db.session.delete(operation)
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
    def patch(operation_id):
        result = dict(status="ERROR", message="Insufficient data")
        result_code = 404

        if request.json:
            request_schema = PartialSchemaFactory(OperationCreateRequestSchema)
            form = request_schema.load(request.json)
            response_schema = OperationItemResponseSchema()
            if not form.errors:
                try:
                    form.data.id = operation_id
                    operation = db.session.merge(form.data)
                    db.session.commit()

                    if operation is not None:
                        result, result_code = dict(
                            status="OK", message="Updated",
                            data=response_schema.dump(operation).data), 200
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
        return result, result_code
