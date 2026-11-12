""" Builds the OpenAPI spec from the registered resources and schemas. """
import inspect
import logging
import re

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema

from tahiti import schema as schema_module

log = logging.getLogger(__name__)

_METHODS = ('get', 'post', 'patch', 'put', 'delete')
_RULE_PARAM = re.compile(r'<(?:(\w+):)?(\w+)>')
_TYPES = {'int': 'integer', 'float': 'number'}


def _parameters(path):
    return [{'name': name, 'in': 'path', 'required': True,
             'schema': {'type': _TYPES.get(conv, 'string')}}
            for conv, name in _RULE_PARAM.findall(path)]


def _schema_name(schema):
    # Class name as is: apispec's default resolver drops the 'Schema' suffix,
    # which makes different schemas collide.
    return (schema if isinstance(schema, type) else type(schema)).__name__


def build_spec(mappings):
    """ mappings: {flask rule: flask_restful Resource class} """
    spec = APISpec(title='Lemonade :: Tahiti', version='1.0',
                   openapi_version='3.0.2',
                   plugins=[MarshmallowPlugin(schema_name_resolver=_schema_name)])
    for name, cls in inspect.getmembers(schema_module, inspect.isclass):
        # Only schemas defined in tahiti.schema, not marshmallow's own
        if (issubclass(cls, Schema) and cls.__module__ == schema_module.__name__
                and not name.startswith('_')):
            if name in spec.components.schemas:  # already added as a Nested
                continue
            try:
                spec.components.schema(name, schema=cls)
            except Exception as e:  # e.g. Nested() pointing to a missing class
                log.warning('Schema %s skipped in OpenAPI spec: %s', name, e)

    for rule, view in mappings.items():
        operations = {}
        for method in _METHODS:
            handler = getattr(view, method, None)
            if handler is None:
                continue
            doc = inspect.getdoc(handler) or ''
            operations[method] = {
                'summary': doc.split('\n')[0],
                'description': doc,
                'responses': {'200': {'description': 'Success'}},
            }
        if operations:
            path = _RULE_PARAM.sub(r'{\2}', rule)
            spec.path(path=path, operations=operations,
                      parameters=_parameters(rule))
    return spec.to_dict()
