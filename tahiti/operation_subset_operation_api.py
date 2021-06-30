# -*- coding: utf-8 -*-}
from tahiti.app_auth import requires_auth, requires_permission
from flask import request, current_app, g as flask_globals
from flask_restful import Resource
from sqlalchemy import or_

import math
import logging
from tahiti.schema import *
from flask_babel import gettext
from tahiti.util import translate_validation

log = logging.getLogger(__name__)

# region Protected
# endregion


class OperationSubsetOperationApi(Resource):
    @requires_auth
    @requires_permission('ADMINISTRATOR')
    def delete(self, subset_id, operation_id):
        return_code = 200
        operation_subset = OperationSubset.query.get(subset_id)
        if operation_subset is not None:
            try:
                operation_subset.operations = [op for op in 
                        operation_subset.operations if op.id != operation_id]
                db.session.add(operation_subset)
                db.session.commit()
                result = { 'status': 'OK', }
            except Exception as e:
                result = {'status': 'ERROR',
                          'message': gettext("Internal error")}
                return_code = 500
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
        else:
            return_code = 404
            result = {
                'status': 'ERROR',
                'message': gettext('%(name)s not found (id=%(id)s).',
                                   name=self.human_name, id=subset_id)
            }
        return result, return_code

    @requires_auth
    @requires_permission('ADMINISTRATOR')
    def post(self, subset_id, operation_id):
        return_code = 200

        operation_subset = OperationSubset.query.get(subset_id)
        operation = Operation.query.get(operation_id)
        if operation_subset is not None or operation is not None:
            try:
                operation_subset.operations.append(operation)
                db.session.add(operation_subset)
                db.session.commit()
                result = { 'status': 'OK', }
            except Exception as e:
                result = {'status': 'ERROR',
                          'message': gettext("Internal error")}
                return_code = 500
                if current_app.debug:
                    result['debug_detail'] = str(e)
                db.session.rollback()
        else:
            return_code = 404
            result = {
                'status': 'ERROR',
                'message': gettext('%(name)s not found (id=%(id)s).',
                                   name=self.human_name, id=subset_id)
            }
        return result, return_code

