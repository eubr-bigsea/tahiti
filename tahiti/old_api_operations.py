# -*- coding: utf-8 -*-
import json

from flask import Flask, request
from flask_restful import Resource, Api
import jsonschema

ATTRIBUTE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "type": {"type": "string"},  # FIXME
        "precision": {"type": "number"},
        "enabled": {"type": "boolean"},
        "enumeration": {"type": "string"}
    },
    "required": ["id", "name"]
}
DATABASE_SCHEMA = {
    "id": "http://lemonade.speed.dcc.ufmg.br/database#",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Schema for Lemonade database type",
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "enabled": {"type": "boolean"},
        "read-only": {"type": "boolean"},
        "url": {"type": "string"},
        "created": {"type": "string", "format": "date-time"},
        "type": {"type": "string"},  # FIXME
        "provenience": {"type": "string"},
        "estimated-rows": {"type": "number"},
        "estimated-size-in-megabytes": {"type": "number"},
        "projection": {"type": "string"},
        "filter": {"type": "string"},
        "attributes": {
            "type": "array",
            "items": {
                "minItems": 1,
                "uniqueItems": True,
                "oneOf": [
                    {"$ref": "#/definitions/attribute"}
                ]
            }
        }
    },
    "required": ["id", "name", "attributes", "enabled", "read-only", "url",
                 "created", "type"],
    "definitions": {
        "attribute": ATTRIBUTE_SCHEMA,
    }
}

PARAMETER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "type": {"type": "string"},  # FIXME
        "precision": {"type": "number"},
        "required": {"type": "boolean"},
        "multiple": {"type": "boolean"},
    },
    "required": ["id", "name"]
}
OPERATION_SCHEMA = {
    "id": "http://lemonade.speed.dcc.ufmg.br/operation#",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Schema for Lemonade operation type",
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "enabled": {"type": "boolean"},
        "command": {"type": "string"},
        "type": {"type": "string"},  # FIXME
        "input-form": {"type": "string"},
        "allow-multiple-input": {"type": "boolean"},
        "allow-multiple-output": {"type": "boolean"},
        "parameters": {
            "type": "array",
            "items": {
                "minItems": 0,
                "uniqueItems": True,
                "oneOf": [
                    {"$ref": "#/definitions/parameter"}
                ]
            }
        }
    },
    "required": ["id", "name", "enabled", "command", "type",
                 ],
    "definitions": {
        "attribute": PARAMETER_SCHEMA,
    }
}



class OperationsApi(Resource):
    @staticmethod
    def get():
        return {"status": {"status": "OK"}}

    @staticmethod
    def post():
        try:
            return {"result": jsonschema.validate(
                request.json, DATABASE_SCHEMA,
                format_checker=jsonschema.FormatChecker())}
        except jsonschema.ValidationError, ve:
            return {"errors": {
                "/".join(str(x) for x in ve.path): ve.message}
                   }, 400


class OperationApi(Resource):
    @staticmethod
    def get(op_id):
        return {op_id: 1}

    @staticmethod
    def delete(op_id):
        return {"deleted": op_id}

    @staticmethod
    def patch(op_id):
        return {"patched": op_id}


class OperationExecutionApi(Resource):
    @staticmethod
    def get(op_id):
        return {op_id: 1}

    @staticmethod
    def post(op_id):
        return {"deleted": op_id}
