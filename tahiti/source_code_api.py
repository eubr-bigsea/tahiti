# -*- coding: utf-8 -*-}
import logging

from flask import request, current_app, g
from flask_restful import Resource

from tahiti.app_auth import requires_auth
from tahiti.models import *

log = logging.getLogger(__name__)

class SourceCodeApi(Resource):
    """ REST API for Source Codes """

    @staticmethod
    @requires_auth
    def get_source_code(source_code_id):
        code = SourceCode.query.select().where(id == source_code_id)
        return code
    
    @staticmethod
    @requires_auth
    def add_source_code(new_source_code):
        code = SourceCode.query.insert().values(new_source_code)
        return code

    @staticmethod
    @requires_auth
    def update_source_code(source_code_id, new_source_code):
        code = SourceCode.query.update().where(id == source_code_id).values(new_source_code)
        return code

    @staticmethod
    @requires_auth
    def delete_source_code(source_code_id):
        code = SourceCode.query.delete().where(id == source_code_id)
        return code