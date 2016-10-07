# -*- coding: utf-8 -*-
import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, \
    Enum, DateTime, Numeric, Text, Unicode
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from sqlalchemy_i18n import make_translatable, translation_base, Translatable

make_translatable(options={'locales': ['pt', 'en', 'es'],
                           'auto_create_locales': True,
                           'fallback_locale': 'en'})

db = SQLAlchemy()


# noinspection PyClassHasNoInit
class OperationType:
    ACTION = 'ACTION'
    SHUFFLE = 'SHUFFLE'
    TRANSFORMATION = 'TRANSFORMATION'


# noinspection PyClassHasNoInit
class OperationPortType:
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'


# noinspection PyClassHasNoInit
class OperationPortMultiplicity:
    MANY = 'MANY'
    ONE = 'ONE'


# noinspection PyClassHasNoInit
class DataType:
    FLOAT = 'FLOAT'
    LAT_LONG = 'LAT_LONG'
    TIME = 'TIME'
    DOUBLE = 'DOUBLE'
    DECIMAL = 'DECIMAL'
    ENUM = 'ENUM'
    CHARACTER = 'CHARACTER'
    LONG = 'LONG'
    DATETIME = 'DATETIME'
    TEXT = 'TEXT'
    DATE = 'DATE'
    INTEGER = 'INTEGER'


class Operation(db.Model, Translatable):
    """ Operation executed in Lemonade """
    __tablename__ = 'operation'
    __translatable__ = {'locales': ['pt', 'en', 'es']}

    # Fields
    id = Column(Integer, primary_key=True)
    slug = Column(String(200), nullable=False)
    enabled = Column(Boolean, nullable=False)
    command = Column(String(200), nullable=False)
    type = Column(Enum(*OperationType.__dict__.keys(), 
                       name='OperationTypeEnumType'), nullable=False)
    input_form = Column(Text, nullable=False)
    icon = Column(String(200), nullable=False)
    # Associations
    # noinspection PyUnresolvedReferences
    operation_category_operation = db.Table(
        'operation_category_operation',
        Column('operation_id', Integer, ForeignKey('operation.id')),
        Column('operation_category_id', Integer, ForeignKey('operation_category.id')))
    categories = relationship("OperationCategory",
                              secondary=operation_category_operation)
    # noinspection PyUnresolvedReferences
    operation_operation_form = db.Table(
        'operation_operation_form',
        Column('operation_id', Integer, ForeignKey('operation.id')),
        Column('operation_form_id', Integer, ForeignKey('operation_form.id')))
    forms = relationship("OperationForm",
                          secondary=operation_operation_form)
    ports = relationship("OperationPort", back_populates="operation")

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationTranslation(translation_base(Operation)):
    """ Translation table for Operation """
    __tablename__ = 'operation_translation'

    # Fields
    name = Column(Unicode(200))
    description = Column(Unicode(200))


class OperationPortInterface(db.Model):
    """ An interface that a operation port supports """
    __tablename__ = 'operation_port_interface'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationPort(db.Model):
    """ An input or output port for operation """
    __tablename__ = 'operation_port'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    type = Column(Enum(*OperationPortType.__dict__.keys(), 
                       name='OperationPortTypeEnumType'), nullable=False)
    description = Column(String(200), nullable=False)
    tags = Column(Text)
    order = Column(Integer)
    multiplicity = Column(Enum(*OperationPortMultiplicity.__dict__.keys(), 
                               name='OperationPortMultiplicityEnumType'), nullable=False, default=1)
    # Associations
    # noinspection PyUnresolvedReferences
    operation_port_interface_operation_port = db.Table(
        'operation_port_interface_operation_port',
        Column('operation_port_id', Integer, ForeignKey('operation_port.id')),
        Column('operation_port_interface_id', Integer, ForeignKey('operation_port_interface.id')))
    interfaces = relationship("OperationPortInterface",
                                    secondary=operation_port_interface_operation_port)

    operation_id = Column(Integer, 
                          ForeignKey("operation.id"), nullable=False)
    operation = relationship("Operation", foreign_keys=[operation_id])

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationCategory(db.Model, Translatable):
    """ Allows categorize operations """
    __tablename__ = 'operation_category'
    __translatable__ = {'locales': ['pt', 'en', 'es']}

    # Fields
    id = Column(Integer, primary_key=True)
    type = Column(String(200), nullable=False)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationCategoryTranslation(translation_base(OperationCategory)):
    """ Translation table for OperationCategory """
    __tablename__ = 'operation_category_translation'

    # Fields
    name = Column(Unicode(200))


class OperationForm(db.Model):
    """ A form used to fill parameters to the operations """
    __tablename__ = 'operation_form'

    # Fields
    id = Column(Integer, primary_key=True)
    enabled = Column(Boolean, nullable=False, default=True)
    name = Column(String(200), nullable=False)
    # Associations
    fields = relationship("OperationFormField", 
                          order_by="OperationFormField.order")

    def __unicode__(self):
        return self.enabled

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationFormField(db.Model):
    """ A field used to fill one parameter of a form for an operations """
    __tablename__ = 'operation_form_field'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    label = Column(String(200), nullable=False)
    help = Column(Text, nullable=False)
    type = Column(Enum(*DataType.__dict__.keys(), 
                       name='DataTypeEnumType'), nullable=False)
    required = Column(Boolean, nullable=False)
    order = Column(Integer, nullable=False)
    default = Column(Text, nullable=False)
    suggested_widget = Column(String(200))
    values_url = Column(String(200))
    values = Column(Text)
    # Associations

    form_id = Column(Integer, 
                     ForeignKey("operation_form.id"), nullable=False)
    form = relationship("OperationForm", foreign_keys=[form_id])

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)
