# -*- coding: utf-8 -*-
import datetime
import json
from copy import deepcopy
from marshmallow import Schema, fields, post_load
from marshmallow.validate import OneOf
from models import *


def partial_schema_factory(schema_cls):
    schema = schema_cls(partial=True)
    for field_name, field in schema.fields.items():
        if isinstance(field, fields.Nested):
            new_field = deepcopy(field)
            new_field.schema.partial = True
            schema.fields[field_name] = new_field
    return schema


def load_json(str_value):
    try:
        return json.loads(str_value)
    except:
        return "Error loading JSON"


# region Protected
class KeyValueSchema(Schema):
    name = fields.String(required=True)
    value = fields.String(required=True)


class UserCreateRequestSchema(Schema):
    id = fields.Integer(required=True)
    login = fields.String(required=True)
    name = fields.String(required=True)


class KeyValuePairExecuteRequestSchema(KeyValueSchema):
    pass

# endregion


class ApplicationListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    type = fields.String(required=True,
                         validate=[OneOf(ApplicationType.__dict__.keys())])
    execution_parameters = fields.Function(
        lambda x: load_json(x.execution_parameters))

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Application"""
        return Application(**data)

    class Meta:
        ordered = True


class ApplicationItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    type = fields.String(required=True,
                         validate=[OneOf(ApplicationType.__dict__.keys())])
    execution_parameters = fields.Function(
        lambda x: load_json(x.execution_parameters))

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Application"""
        return Application(**data)

    class Meta:
        ordered = True


class FlowListResponseSchema(Schema):
    """ JSON schema for listing """
    source_port = fields.Integer(required=True)
    target_port = fields.Integer(required=True)
    source_port_name = fields.String(required=False, allow_none=True)
    target_port_name = fields.String(required=False, allow_none=True)
    source_id = fields.String(required=True)
    target_id = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Flow"""
        return Flow(**data)

    class Meta:
        ordered = True


class FlowItemResponseSchema(Schema):
    """ JSON schema for listing """
    source_port = fields.Integer(required=True)
    target_port = fields.Integer(required=True)
    source_port_name = fields.String(required=False, allow_none=True)
    target_port_name = fields.String(required=False, allow_none=True)
    source_id = fields.String(required=True)
    target_id = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Flow"""
        return Flow(**data)

    class Meta:
        ordered = True


class FlowCreateRequestSchema(Schema):
    """ JSON schema for new instance """
    source_port = fields.Integer(required=True)
    target_port = fields.Integer(required=True)
    source_port_name = fields.String(required=False, allow_none=True)
    target_port_name = fields.String(required=False, allow_none=True)
    source_id = fields.String(required=True)
    target_id = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Flow"""
        return Flow(**data)

    class Meta:
        ordered = True


class OperationSimpleListResponseSchema(Schema):
    """ JSON simple """
    id = fields.Integer(allow_none=True)
    name = fields.String(required=False, allow_none=True)
    slug = fields.String(required=False, allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True


class OperationListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationType.__dict__.keys())])
    icon = fields.String(required=True)
    categories = fields.Nested(
        'tahiti.schema.OperationCategoryListResponseSchema',
        required=True,
        many=True)
    platforms = fields.Nested(
        'tahiti.schema.PlatformListResponseSchema',
        required=True,
        many=True)
    forms = fields.Nested(
        'tahiti.schema.OperationFormListResponseSchema',
        required=True,
        many=True)
    ports = fields.Nested(
        'tahiti.schema.OperationPortListResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True


class OperationCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationType.__dict__.keys())])
    icon = fields.String(required=True)
    categories = fields.Nested(
        'tahiti.schema.OperationCategoryCreateRequestSchema',
        required=True,
        many=True)
    platforms = fields.Nested(
        'tahiti.schema.PlatformCreateRequestSchema',
        required=True,
        many=True)
    forms = fields.Nested(
        'tahiti.schema.OperationFormCreateRequestSchema',
        required=True,
        many=True)
    ports = fields.Nested(
        'tahiti.schema.OperationPortCreateRequestSchema',
        required=True,
        many=True)
    scripts = fields.Nested(
        'tahiti.schema.OperationScriptCreateRequestSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True


class OperationItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationType.__dict__.keys())])
    icon = fields.String(required=True)
    categories = fields.Nested(
        'tahiti.schema.OperationCategoryItemResponseSchema',
        required=True,
        many=True)
    platforms = fields.Nested(
        'tahiti.schema.PlatformItemResponseSchema',
        required=True,
        many=True)
    forms = fields.Nested(
        'tahiti.schema.OperationFormItemResponseSchema',
        required=True,
        many=True)
    ports = fields.Nested(
        'tahiti.schema.OperationPortItemResponseSchema',
        required=True,
        many=True)
    scripts = fields.Nested(
        'tahiti.schema.OperationScriptItemResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True


class OperationUpdateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=False, allow_none=True)
    slug = fields.String(required=False, allow_none=True)
    enabled = fields.Boolean(required=False, allow_none=True)
    description = fields.String(required=False, allow_none=True)
    type = fields.String(required=False, allow_none=True,
                         validate=[OneOf(OperationType.__dict__.keys())])
    icon = fields.String(required=False, allow_none=True)
    categories = fields.Nested(
        'tahiti.schema.OperationCategoryUpdateRequestSchema',
        required=True,
        many=True)
    platforms = fields.Nested(
        'tahiti.schema.PlatformUpdateRequestSchema',
        required=True,
        many=True)
    forms = fields.Nested(
        'tahiti.schema.OperationFormUpdateRequestSchema',
        required=True,
        many=True)
    ports = fields.Nested(
        'tahiti.schema.OperationPortUpdateRequestSchema',
        required=True,
        many=True)
    scripts = fields.Nested(
        'tahiti.schema.OperationScriptUpdateRequestSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True


class OperationCategoryCreateRequestSchema(Schema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationCategory"""
        return OperationCategory(**data)

    class Meta:
        ordered = True


class OperationCategoryListResponseSchema(Schema):
    """ JSON schema for response """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationCategory"""
        return OperationCategory(**data)

    class Meta:
        ordered = True


class OperationCategoryItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    type = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationCategory"""
        return OperationCategory(**data)

    class Meta:
        ordered = True


class OperationFormListResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    order = fields.Integer(required=True)
    category = fields.String(required=True)
    fields = fields.Nested(
        'tahiti.schema.OperationFormFieldListResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationForm"""
        return OperationForm(**data)

    class Meta:
        ordered = True


class OperationFormCreateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    order = fields.Integer(required=True)
    category = fields.String(required=True)
    fields = fields.Nested(
        'tahiti.schema.OperationFormFieldCreateRequestSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationForm"""
        return OperationForm(**data)

    class Meta:
        ordered = True


class OperationFormItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    order = fields.Integer(required=True)
    category = fields.String(required=True)
    fields = fields.Nested(
        'tahiti.schema.OperationFormFieldItemResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationForm"""
        return OperationForm(**data)

    class Meta:
        ordered = True


class OperationFormFieldListResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(DataType.__dict__.keys())])
    required = fields.Boolean(required=True)
    order = fields.Integer(required=True)
    default = fields.String(required=False, allow_none=True)
    suggested_widget = fields.String(required=False, allow_none=True)
    values_url = fields.String(required=False, allow_none=True)
    values = fields.String(required=False, allow_none=True)
    scope = fields.String(required=True,
                          validate=[OneOf(OperationFieldScope.__dict__.keys())])

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationFormField"""
        return OperationFormField(**data)

    class Meta:
        ordered = True


class OperationFormFieldCreateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(DataType.__dict__.keys())])
    required = fields.Boolean(required=True)
    order = fields.Integer(required=True)
    default = fields.String(required=False, allow_none=True)
    suggested_widget = fields.String(required=False, allow_none=True)
    values_url = fields.String(required=False, allow_none=True)
    values = fields.String(required=False, allow_none=True)
    scope = fields.String(required=True,
                          validate=[OneOf(OperationFieldScope.__dict__.keys())])

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationFormField"""
        return OperationFormField(**data)

    class Meta:
        ordered = True


class OperationFormFieldItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(DataType.__dict__.keys())])
    required = fields.Boolean(required=True)
    order = fields.Integer(required=True)
    default = fields.String(required=False, allow_none=True)
    suggested_widget = fields.String(required=False, allow_none=True)
    values_url = fields.String(required=False, allow_none=True)
    values = fields.String(required=False, allow_none=True)
    scope = fields.String(required=True,
                          validate=[OneOf(OperationFieldScope.__dict__.keys())])

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationFormField"""
        return OperationFormField(**data)

    class Meta:
        ordered = True


class OperationPortListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationPortType.__dict__.keys())])
    description = fields.String(required=True)
    tags = fields.String(required=False, allow_none=True)
    order = fields.Integer(required=False, allow_none=True)
    multiplicity = fields.String(required=True, missing=1,
                                 default=1,
                                 validate=[OneOf(OperationPortMultiplicity.__dict__.keys())])
    interfaces = fields.Nested(
        'tahiti.schema.OperationPortInterfaceListResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationPort"""
        return OperationPort(**data)

    class Meta:
        ordered = True


class OperationPortCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationPortType.__dict__.keys())])
    description = fields.String(required=True)
    tags = fields.String(required=False, allow_none=True)
    order = fields.Integer(required=False, allow_none=True)
    multiplicity = fields.String(required=True, missing=1,
                                 default=1,
                                 validate=[OneOf(OperationPortMultiplicity.__dict__.keys())])
    interfaces = fields.Nested(
        'tahiti.schema.OperationPortInterfaceCreateRequestSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationPort"""
        return OperationPort(**data)

    class Meta:
        ordered = True


class OperationPortItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationPortType.__dict__.keys())])
    description = fields.String(required=True)
    tags = fields.String(required=False, allow_none=True)
    order = fields.Integer(required=False, allow_none=True)
    multiplicity = fields.String(required=True, missing=1,
                                 default=1,
                                 validate=[OneOf(OperationPortMultiplicity.__dict__.keys())])
    interfaces = fields.Nested(
        'tahiti.schema.OperationPortInterfaceItemResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationPort"""
        return OperationPort(**data)

    class Meta:
        ordered = True


class OperationPortInterfaceCreateRequestSchema(Schema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    color = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)

    class Meta:
        ordered = True


class OperationPortInterfaceListResponseSchema(Schema):
    """ JSON schema for response """
    name = fields.String(required=True)
    color = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)

    class Meta:
        ordered = True


class OperationPortInterfaceItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    color = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)

    class Meta:
        ordered = True


class OperationScriptListResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(ScriptType.__dict__.keys())])
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    body = fields.String(required=True)
    operation = fields.Nested(
        'tahiti.schema.OperationListResponseSchema',
        required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationScript"""
        return OperationScript(**data)

    class Meta:
        ordered = True


class OperationScriptCreateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(ScriptType.__dict__.keys())])
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    body = fields.String(required=True)
    operation = fields.Nested(
        'tahiti.schema.OperationCreateRequestSchema',
        required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationScript"""
        return OperationScript(**data)

    class Meta:
        ordered = True


class OperationScriptItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(ScriptType.__dict__.keys())])
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    body = fields.String(required=True)
    operation = fields.Nested(
        'tahiti.schema.OperationItemResponseSchema',
        required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of OperationScript"""
        return OperationScript(**data)

    class Meta:
        ordered = True


class PlatformListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    icon = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Platform"""
        return Platform(**data)

    class Meta:
        ordered = True


class PlatformCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Platform"""
        return Platform(**data)

    class Meta:
        ordered = True


class PlatformItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    description = fields.String(required=True)
    icon = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Platform"""
        return Platform(**data)

    class Meta:
        ordered = True


class TaskListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.String(required=True)
    left = fields.Integer(required=True)
    top = fields.Integer(required=True)
    z_index = fields.Integer(required=True)
    forms = fields.Function(lambda x: load_json(x.forms))
    version = fields.Integer(required=True)
    operation = fields.Nested(
        'tahiti.schema.OperationSimpleListResponseSchema',
        allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Task"""
        return Task(**data)

    class Meta:
        ordered = True


class TaskCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.String(required=True)
    left = fields.Integer(required=True)
    top = fields.Integer(required=True)
    z_index = fields.Integer(required=True)
    forms = fields.Dict(required=True)
    operation_id = fields.Integer(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Task"""
        data['forms'] = json.dumps(data.get('forms', []))
        return Task(**data)

    class Meta:
        ordered = True


class TaskItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.String(required=True)
    left = fields.Integer(required=True)
    top = fields.Integer(required=True)
    z_index = fields.Integer(required=True)
    forms = fields.Function(lambda x: load_json(x.forms))
    version = fields.Integer(required=True)
    operation = fields.Nested(
        'tahiti.schema.OperationSimpleListResponseSchema',
        allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Task"""
        return Task(**data)

    class Meta:
        ordered = True


class TaskExecuteRequestSchema(Schema):
    """ JSON schema for executing tasks """
    id = fields.String(required=True)
    left = fields.Integer(required=True)
    top = fields.Integer(required=True)
    z_index = fields.Integer(required=True)
    forms = fields.String(required=True)
    version = fields.Integer(required=True)
    next_task_id = fields.String(allow_none=True)
    operation = fields.Nested(
        'tahiti.schema.OperationExecuteRequestSchema',
        required=True)
    parameters = fields.Nested(
        'tahiti.schema.KeyValuePairExecuteRequestSchema',
        allow_none=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Task"""
        return Task(**data)

    class Meta:
        ordered = True


class WorkflowExecuteRequestSchema(Schema):
    """ JSON schema for executing workflow """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    created = fields.DateTime(required=True, missing=datetime.datetime.utcnow,
                              default=datetime.datetime.utcnow)
    updated = fields.DateTime(required=True, missing=datetime.datetime.utcnow,
                              default=datetime.datetime.utcnow)
    version = fields.Integer(required=True)
    image = fields.String(required=False, allow_none=True)
    tasks = fields.Nested(
        'tahiti.schema.TaskExecuteRequestSchema',
        allow_none=True,
        many=True)
    flows = fields.Nested(
        'tahiti.schema.FlowExecuteRequestSchema',
        allow_none=True,
        many=True)
    platform = fields.Nested(
        'tahiti.schema.PlatformExecuteRequestSchema',
        required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True


class WorkflowListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    created = fields.DateTime(required=True, missing=datetime.datetime.utcnow,
                              default=datetime.datetime.utcnow)
    updated = fields.DateTime(required=True, missing=datetime.datetime.utcnow,
                              default=datetime.datetime.utcnow)
    version = fields.Integer(required=True)
    image = fields.String(required=False, allow_none=True)
    tasks = fields.Nested(
        'tahiti.schema.TaskListResponseSchema',
        allow_none=True,
        many=True)
    flows = fields.Nested(
        'tahiti.schema.FlowListResponseSchema',
        allow_none=True,
        many=True)
    platform = fields.Nested(
        'tahiti.schema.PlatformListResponseSchema',
        required=True)
    user = fields.Function(
        lambda x: {
            "id": x.user_id,
            "name": x.user_name,
            "login": x.user_login})

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True


class WorkflowCreateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    image = fields.String(required=False, allow_none=True)
    tasks = fields.Nested(
        'tahiti.schema.TaskCreateRequestSchema',
        allow_none=True,
        many=True)
    flows = fields.Nested(
        'tahiti.schema.FlowCreateRequestSchema',
        allow_none=True,
        many=True)
    platform_id = fields.Integer(required=True)
    user = fields.Nested(
        'tahiti.schema.UserCreateRequestSchema',
        allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True


class WorkflowItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    created = fields.DateTime(required=True, missing=datetime.datetime.utcnow,
                              default=datetime.datetime.utcnow)
    updated = fields.DateTime(required=True, missing=datetime.datetime.utcnow,
                              default=datetime.datetime.utcnow)
    version = fields.Integer(required=True)
    image = fields.String(required=False, allow_none=True)
    tasks = fields.Nested(
        'tahiti.schema.TaskItemResponseSchema',
        allow_none=True,
        many=True)
    flows = fields.Nested(
        'tahiti.schema.FlowItemResponseSchema',
        allow_none=True,
        many=True)
    platform = fields.Nested(
        'tahiti.schema.PlatformItemResponseSchema',
        required=True)
    user = fields.Function(
        lambda x: {
            "id": x.user_id,
            "name": x.user_name,
            "login": x.user_login})

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data):
        """ Deserialize data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True

