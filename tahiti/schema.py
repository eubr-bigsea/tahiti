# -*- coding: utf-8 -*-

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

# region Protected
class KeyValueSchema(Schema):
    name = fields.String(required=True)
    value = fields.String(required=True)


class KeyValuePairExecuteRequestSchema(KeyValueSchema):
    pass


# endregion


class OperationListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationType.__dict__.keys())])
    input_form = fields.String(required=True)
    icon = fields.String(required=True)
    categories = fields.Nested('schema.OperationCategoryListResponseSchema',
                               required=True,
                               many=True)
    forms = fields.Nested('schema.OperationFormListResponseSchema',
                          required=True,
                          many=True)
    ports = fields.Nested('schema.OperationPortListResponseSchema',
                          required=True,
                          many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
        return Operation(**data)


class OperationCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationType.__dict__.keys())])
    input_form = fields.String(required=True)
    icon = fields.String(required=True)
    categories = fields.Nested('schema.OperationCategoryCreateRequestSchema',
                               required=True,
                               many=True)
    forms = fields.Nested('schema.OperationFormCreateRequestSchema',
                          required=True,
                          many=True)
    ports = fields.Nested('schema.OperationPortCreateRequestSchema',
                          required=True,
                          many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
        return Operation(**data)


class OperationItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationType.__dict__.keys())])
    input_form = fields.String(required=True)
    icon = fields.String(required=True)
    categories = fields.Nested('schema.OperationCategoryItemResponseSchema',
                               required=True,
                               many=True)
    forms = fields.Nested('schema.OperationFormItemResponseSchema',
                          required=True,
                          many=True)
    ports = fields.Nested('schema.OperationPortItemResponseSchema',
                          required=True,
                          many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
        return Operation(**data)


class OperationUpdateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=False)
    slug = fields.String(required=False)
    enabled = fields.Boolean(required=False)
    description = fields.String(required=False)
    command = fields.String(required=False)
    type = fields.String(required=False,
                         validate=[OneOf(OperationType.__dict__.keys())])
    input_form = fields.String(required=False)
    icon = fields.String(required=False)
    categories = fields.Nested('schema.OperationCategoryUpdateRequestSchema',
                               many=True)
    forms = fields.Nested('schema.OperationFormUpdateRequestSchema',
                          many=True)
    ports = fields.Nested('schema.OperationPortUpdateRequestSchema',
                          many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
        return Operation(**data)


class OperationCategoryCreateRequestSchema(Schema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationCategory"""
        return OperationCategory(**data)


class OperationCategoryListResponseSchema(Schema):
    """ JSON schema for response """
    name = fields.String(required=True)
    type = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationCategory"""
        return OperationCategory(**data)


class OperationCategoryItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    type = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationCategory"""
        return OperationCategory(**data)


class OperationFormListResponseSchema(Schema):
    """ JSON serialization schema """
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldListResponseSchema',
                           required=True,
                           many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationForm"""
        return OperationForm(**data)


class OperationFormCreateRequestSchema(Schema):
    """ JSON serialization schema """
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldCreateRequestSchema',
                           required=True,
                           many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationForm"""
        return OperationForm(**data)


class OperationFormItemResponseSchema(Schema):
    """ JSON serialization schema """
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldItemResponseSchema',
                           required=True,
                           many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationForm"""
        return OperationForm(**data)


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
                               required=True,
                               many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPort"""
        return OperationPort(**data)


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
                               required=True,
                               many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPort"""
        return OperationPort(**data)


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
                               required=True,
                               many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPort"""
        return OperationPort(**data)


class OperationPortInterfaceCreateRequestSchema(Schema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)


class OperationPortInterfaceListResponseSchema(Schema):
    """ JSON schema for response """
    name = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)


class OperationPortInterfaceItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)
