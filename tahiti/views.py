# -*- coding: utf-8 -*-
from flask import render_template, make_response
from flask.views import MethodView
from sqlalchemy.orm import joinedload, Load

from tahiti.models import Operation, OperationScript, db, ScriptType, \
    OperationCategory


class AttributeSuggestionView(MethodView):
    # noinspection PyUnresolvedReferences
    @staticmethod
    def get():
        operations = db.session.query(Operation, OperationScript) \
            .join(Operation.scripts) \
            .options(joinedload(Operation.scripts),
                     Load(Operation).load_only('id', 'slug'),
                     Load(OperationScript).load_only('body')) \
            .filter(Operation.enabled) \
            .filter(OperationScript.enabled) \
            .filter(OperationScript.type == ScriptType.JS_CLIENT)

        data_sources = Operation.query.join(Operation.categories)\
            .options(Load(Operation).load_only('id'))\
            .filter(OperationCategory.type == 'data source')

        context = {'operations': operations}
        response = make_response(render_template('/js/attribute-suggestion.js',
                                                 **context))
        response.headers.set('Content-Type', 'application/javascript')
        return response