# -*- coding: utf-8 -*-}
import math
import logging

from tahiti.app_auth import requires_auth, requires_permission
from flask import request, current_app, g as flask_globals
from flask_restful import Resource
from sqlalchemy import or_
from http import HTTPStatus
from marshmallow.exceptions import ValidationError

from tahiti.schema import *
from tahiti.util import translate_validation
from flask_babel import gettext

log = logging.getLogger(__name__)


class ApplicationListApi(Resource):
    """ REST API for listing class Application """

    def __init__(self):
        self.human_name = gettext('Application')

    @requires_auth
    def get(self):
        if request.args.get('fields'):
            only = [f.strip() for f in request.args.get('fields').split(',')]
        else:
            only = ('id', ) if request.args.get(
                'simple', 'false') == 'true' else None
        enabled_filter = request.args.get('enabled')
        if enabled_filter:
            applications = Application.query.filter(
                Application.enabled == (enabled_filter != 'false'))
        else:
            applications = Application.query

        page = request.args.get('page') or '1'
        if page is not None and page.isdigit():
            page_size = int(request.args.get('size', 20))
            page = int(page)
            pagination = applications.paginate(page, page_size, True)
            result = {
                'data': ApplicationListResponseSchema(
                    many=True, only=only).dump(pagination.items),
                'pagination': {
                    'page': page, 'size': page_size,
                    'total': pagination.total,
                    'pages': int(math.ceil(1.0 * pagination.total / page_size))}
            }
        else:
            result = {
                'data': ApplicationListResponseSchema(
                    many=True, only=only).dump(
                    applications)}

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Listing %(name)s', name=self.human_name))
        return result

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def post(self):
        result = {'status': 'ERROR',
                  'message': gettext("Missing json in the request body")}
        return_code = HTTPStatus.BAD_REQUEST

        if request.json is not None:
            request_schema = ApplicationCreateRequestSchema()
            response_schema = ApplicationItemResponseSchema()
            application = request_schema.load(request.json)
            try:
                if log.isEnabledFor(logging.DEBUG):
                    log.debug(gettext('Adding %s'), self.human_name)
                application = application
                db.session.add(application)
                db.session.commit()
                result = response_schema.dump(application)
                return_code = HTTPStatus.CREATED
            except ValidationError as e:
                result = {
                    'status': 'ERROR',
                    'message': gettext('Invalid data for %(name)s.)',
                                       name=self.human_name),
                    'errors': translate_validation(e.messages)
                }
            except Exception as e:
                result = {'status': 'ERROR',
                          'message': gettext("Internal error")}
                return_code = 500
                if current_app.debug:
                    result['debug_detail'] = str(e)

                log.exception(e)
                db.session.rollback()

        return result, return_code


class ApplicationDetailApi(Resource):
    """ REST API for a single instance of class Application """

    def __init__(self):
        self.human_name = gettext('Application')

    @requires_auth
    def get(self, application_id):

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Retrieving %s (id=%s)'), self.human_name,
                      application_id)

        application = Application.query.get(application_id)
        return_code = HTTPStatus.OK
        if application is not None:
            result = {
                'status': 'OK',
                'data': [ApplicationItemResponseSchema().dump(
                    application)]
            }
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext(
                    '%(name)s not found (id=%(id)s)',
                    name=self.human_name, id=application_id)
            }

        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def delete(self, application_id):
        return_code = HTTPStatus.NO_CONTENT
        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Deleting %s (id=%s)'), self.human_name,
                      application_id)
        application = Application.query.get(application_id)
        if application is not None:
            try:
                db.session.delete(application)
                db.session.commit()
                result = {
                    'status': 'OK',
                    'message': gettext('%(name)s deleted with success!',
                                       name=self.human_name)
                }
            except Exception as e:
                result = {'status': 'ERROR',
                          'message': gettext("Internal error")}
                return_code = HTTPStatus.INTERNAL_SERVER_ERROR
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
        else:
            return_code = HTTPStatus.NOT_FOUND
            result = {
                'status': 'ERROR',
                'message': gettext('%(name)s not found (id=%(id)s).',
                                   name=self.human_name, id=application_id)
            }
        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR',)
    def patch(self, application_id):
        result = {'status': 'ERROR', 'message': gettext('Insufficient data.')}
        return_code = HTTPStatus.NOT_FOUND

        if log.isEnabledFor(logging.DEBUG):
            log.debug(gettext('Updating %s (id=%s)'), self.human_name,
                      application_id)
        if request.json:
            request_schema = partial_schema_factory(
                ApplicationCreateRequestSchema)
            # Ignore missing fields to allow partial updates
            application = request_schema.load(request.json, partial=True)
            response_schema = ApplicationItemResponseSchema()
            try:
                application.id = application_id
                application = db.session.merge(application)
                db.session.commit()

                if application is not None:
                    return_code = HTTPStatus.OK
                    result = {
                        'status': 'OK',
                        'message': gettext(
                            '%(n)s (id=%(id)s) was updated with success!',
                            n=self.human_name,
                            id=application_id),
                        'data': [response_schema.dump(
                            application)]
                    }
            except ValidationError as e:
                result = {
                    'status': 'ERROR',
                    'message': gettext('Invalid data for %(name)s (id=%(id)s)',
                                       name=self.human_name,
                                       id=application_id),
                    'errors': translate_validation(e.messages)
                }
            except Exception as e:
                result = {'status': 'ERROR',
                          'message': gettext("Internal error")}
                return_code = 500
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
        return result, return_code
