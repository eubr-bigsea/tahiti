# -*- coding: utf-8 -*-

import json
from copy import deepcopy
from marshmallow import Schema, fields, post_load
from marshmallow.validate import OneOf
from models import *


def PartialSchemaFactory(schema_cls):
    schema = schema_cls(partial=True)
    for field_name, field in schema.fields.items():
        if isinstance(field, fields.Nested):
            new_field = deepcopy(field)
            new_field.schema.partial = True
            schema.fields[field_name] = new_field
    return schema

def load_json(str):
    print ">>>>>>>>>>", str
    try:
        return json.loads(str)
    except:
        return "Error loading JSON"

# region Protected
class KeyValueSchema(Schema):
    name = fields.String(required=True)
    value = fields.String(required=True)


class KeyValuePairExecuteRequestSchema(KeyValueSchema):
    pass


# endregion


class FlowListResponseSchema(Schema):
    """ JSON schema for listing """
    source_port = fields.Integer(required=True)
    target_port = fields.Integer(required=True)
    source_id = fields.String(required=True)
    target_id = fields.String(required=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Flow"""
        return Flow(**data)

    class Meta:
        ordered = True


class FlowItemResponseSchema(Schema):
    """ JSON schema for listing """
    source_port = fields.Integer(required=True)
    target_port = fields.Integer(required=True)
    source_id = fields.String(required=True)
    target_id = fields.String(required=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Flow"""
        return Flow(**data)

    class Meta:
        ordered = True


class FlowCreateRequestSchema(Schema):
    """ JSON schema for new instance """
    source_port = fields.Integer(required=True)
    target_port = fields.Integer(required=True)
    source_id = fields.String(required=True)
    target_id = fields.String(required=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Flow"""
        return Flow(**data)

    class Meta:
        ordered = True


class OperationSimpleListResponseSchema(Schema):
    """ JSON simple """
    id = fields.Integer()
    name = fields.String(required=False)
    slug = fields.String(required=False)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
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
    categories = fields.Nested('schema.OperationCategoryListResponseSchema',
                               many=True)
    forms = fields.Nested('schema.OperationFormListResponseSchema',
                          many=True)
    ports = fields.Nested('schema.OperationPortListResponseSchema',
                          many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
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
    categories = fields.Nested('schema.OperationCategoryCreateRequestSchema',
                               many=True)
    forms = fields.Nested('schema.OperationFormCreateRequestSchema',
                          many=True)
    ports = fields.Nested('schema.OperationPortCreateRequestSchema',
                          many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
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
    categories = fields.Nested('schema.OperationCategoryItemResponseSchema',
                               many=True)
    forms = fields.Nested('schema.OperationFormItemResponseSchema',
                          many=True)
    ports = fields.Nested('schema.OperationPortItemResponseSchema',
                          many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True


class OperationUpdateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=False)
    slug = fields.String(required=False)
    enabled = fields.Boolean(required=False)
    description = fields.String(required=False)
    type = fields.String(required=False,
                         validate=[OneOf(OperationType.__dict__.keys())])
    icon = fields.String(required=False)
    categories = fields.Nested('schema.OperationCategoryUpdateRequestSchema',
                               required=True,
                               many=True)
    forms = fields.Nested('schema.OperationFormUpdateRequestSchema',
                          required=True,
                          many=True)
    ports = fields.Nested('schema.OperationPortUpdateRequestSchema',
                          required=True,
                          many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True


class OperationCategoryCreateRequestSchema(Schema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationCategory"""
        return OperationCategory(**data)

    class Meta:
        ordered = True


class OperationCategoryListResponseSchema(Schema):
    """ JSON schema for response """
    name = fields.String(required=True)
    type = fields.String(required=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationCategory"""
        return OperationCategory(**data)

    class Meta:
        ordered = True


class OperationCategoryItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    type = fields.String(required=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationCategory"""
        return OperationCategory(**data)

    class Meta:
        ordered = True


class OperationFormListResponseSchema(Schema):
    """ JSON serialization schema """
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldListResponseSchema',
                           many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationForm"""
        return OperationForm(**data)

    class Meta:
        ordered = True


class OperationFormCreateRequestSchema(Schema):
    """ JSON serialization schema """
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldCreateRequestSchema',
                           many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationForm"""
        return OperationForm(**data)

    class Meta:
        ordered = True


class OperationFormItemResponseSchema(Schema):
    """ JSON serialization schema """
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldItemResponseSchema',
                           many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationForm"""
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
    default = fields.String(required=True)
    suggested_widget = fields.String(required=False)
    values_url = fields.String(required=False)
    values = fields.String(required=False)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationFormField"""
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
    default = fields.String(required=True)
    suggested_widget = fields.String(required=False)
    values_url = fields.String(required=False)
    values = fields.String(required=False)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationFormField"""
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
    default = fields.String(required=True)
    suggested_widget = fields.String(required=False)
    values_url = fields.String(required=False)
    values = fields.String(required=False)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationFormField"""
        return OperationFormField(**data)

    class Meta:
        ordered = True


class OperationPortListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationPortType.__dict__.keys())])
    description = fields.String(required=True)
    tags = fields.String(required=False)
    order = fields.Integer(required=False)
    multiplicity = fields.String(required=True, missing=1,
                                  default=1,
                                 validate=[OneOf(OperationPortMultiplicity.__dict__.keys())])
    interfaces = fields.Nested('schema.OperationPortInterfaceListResponseSchema',
                               many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPort"""
        return OperationPort(**data)

    class Meta:
        ordered = True


class OperationPortCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationPortType.__dict__.keys())])
    description = fields.String(required=True)
    tags = fields.String(required=False)
    order = fields.Integer(required=False)
    multiplicity = fields.String(required=True, missing=1,
                                  default=1,
                                 validate=[OneOf(OperationPortMultiplicity.__dict__.keys())])
    interfaces = fields.Nested('schema.OperationPortInterfaceCreateRequestSchema',
                               many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPort"""
        return OperationPort(**data)

    class Meta:
        ordered = True


class OperationPortItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationPortType.__dict__.keys())])
    description = fields.String(required=True)
    tags = fields.String(required=False)
    order = fields.Integer(required=False)
    multiplicity = fields.String(required=True, missing=1,
                                  default=1,
                                 validate=[OneOf(OperationPortMultiplicity.__dict__.keys())])
    interfaces = fields.Nested('schema.OperationPortInterfaceItemResponseSchema',
                               many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPort"""
        return OperationPort(**data)

    class Meta:
        ordered = True


class OperationPortInterfaceCreateRequestSchema(Schema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)

    class Meta:
        ordered = True


class OperationPortInterfaceListResponseSchema(Schema):
    """ JSON schema for response """
    name = fields.String(required=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)

    class Meta:
        ordered = True


class OperationPortInterfaceItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)

    class Meta:
        ordered = True


class TaskListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.String(required=True)
    left = fields.Integer(required=True)
    top = fields.Integer(required=True)
    z_index = fields.Integer(required=True)
    forms = fields.Function(lambda x: load_json(x.forms))
    operation = fields.Nested('schema.OperationSimpleListResponseSchema')
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Task"""
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
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Task"""
        data['forms'] = json.dumps(data['forms'])
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
    operation = fields.Nested('schema.OperationSimpleListResponseSchema')
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Task"""
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
    next_task_id = fields.Integer()
    operation = fields.Nested('schema.OperationExecuteRequestSchema')
    parameters = fields.Nested('schema.KeyValuePairExecuteRequestSchema',
                               many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Task"""
        return Task(**data)

    class Meta:
        ordered = True


class WorkflowExecuteRequestSchema(Schema):
    """ JSON schema for executing workflow """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    created = fields.DateTime(required=True, missing=datetime.datetime.now(),
                             default=datetime.datetime.now())
    updated = fields.DateTime(required=True)
    version = fields.Integer(required=True)
    tasks = fields.Nested('schema.TaskExecuteRequestSchema',
                          many=True)
    flows = fields.Nested('schema.FlowExecuteRequestSchema',
                          many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True


class WorkflowListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    created = fields.DateTime(required=True, missing=datetime.datetime.now(),
                             default=datetime.datetime.now())
    updated = fields.DateTime(required=True)
    version = fields.Integer(required=True)
    tasks = fields.Nested('schema.TaskListResponseSchema',
                          many=True)
    flows = fields.Nested('schema.FlowListResponseSchema',
                          many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True


class WorkflowCreateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    tasks = fields.Nested('schema.TaskCreateRequestSchema',
                          many=True)
    flows = fields.Nested('schema.FlowCreateRequestSchema',
                          many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True


class WorkflowItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    created = fields.DateTime(required=True, missing=datetime.datetime.now(),
                             default=datetime.datetime.now())
    updated = fields.DateTime(required=True)
    version = fields.Integer(required=True)
    tasks = fields.Nested('schema.TaskItemResponseSchema',
                          many=True)
    flows = fields.Nested('schema.FlowItemResponseSchema',
                          many=True)
    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True

