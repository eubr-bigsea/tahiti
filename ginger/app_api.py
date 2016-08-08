#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from flask import Flask
from flask_restful import Api

from workflow_api import WorkflowExecuteListApi
from data_source_api import DataSourceListApi, DataSourceDetailApi
from models import db
from operation_api import OperationDetailApi, OperationListApi
from storage_api import StorageListApi

app = Flask(__name__)
api = Api(app)

mappings = {
    '/operations': OperationListApi,
    '/operations/<int:operation_id>': OperationDetailApi,
    '/datasources': DataSourceListApi,
    '/datasources/<int:data_source_id>': DataSourceDetailApi,
    '/storages': StorageListApi,
    '/workflows/execute': WorkflowExecuteListApi,
}
for path, view in mappings.iteritems():
    api.add_resource(view, path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=u'Gerador de código.')
    parser.add_argument('-c', dest='config', metavar='CONFIG',
                        help=u'Configuration file')

    args = parser.parse_args()

    print sorted(app.config.keys())
    app.config["RESTFUL_JSON"] = {"cls": app.json_encoder}
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'mysql://lemon:ju1c3@mysql3.ctweb.inweb.org.br:33060/lemonade'  # 'sqlite:////tmp/test.db'

    db.init_app(app)
    with app.app_context():
        db.create_all()

        '''
        # Create the Flask-Restless API manager.
        manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

        # Create API endpoints, which will be available at /api/<tablename> by
        # default. Allowed HTTP methods can be specified as well.
        prefix = '/api/v1'
        manager.create_api(Operation, methods=['GET', 'POST', 'DELETE'],
                           url_prefix=prefix)
        manager.create_api(Execution, methods=['GET'], url_prefix=prefix)
        '''

    app.run(debug=True)
