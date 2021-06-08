# -*- coding: utf-8 -*-
from flask import render_template, make_response, request
from flask.views import MethodView
from sqlalchemy.orm import joinedload, Load

from tahiti.cache import cache
from tahiti.models import Operation, OperationScript, db, ScriptType


class AttributeSuggestionView(MethodView):
    # noinspection PyUnresolvedReferences
    @staticmethod
    @cache.memoize(600, make_name=lambda f: request.url)
    def get():


        operations = db.session.query(Operation, OperationScript) \
            .join(Operation.scripts) \
            .options(joinedload(Operation.scripts),
                     Load(Operation).load_only('id', 'slug'),
                     Load(OperationScript).load_only('body')) \
            .filter(Operation.enabled) \
            .filter(OperationScript.enabled) \
            .filter(OperationScript.type == ScriptType.JS_CLIENT)
        
        platform_id=request.args.get('platform')
        if platform_id:
            operations = operations.filter(
                    Operation.platforms.any(enabled=True, id=int(platform_id)))

        # data_sources = Operation.query.join(Operation.categories)\
        #     .options(Load(Operation).load_only('id'))\
        #     .filter(OperationCategory.type == 'data source')

        context = {'operations': operations}
        response = make_response(render_template('/js/attribute-suggestion.js',
                                                 **context))
        response.headers.set('Content-Type', 'application/javascript')
        response.headers.set('Cache-Control',
                             'no-cache, no-store, must-revalidate')
        response.headers.set('Pragma', 'no-cache')
        response.headers.set('Expires', '0')
        return response
