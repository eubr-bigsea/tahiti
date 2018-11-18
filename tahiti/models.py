# -*- coding: utf-8 -*-
import datetime
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, \
    Enum, DateTime, Numeric, Text, Unicode, UnicodeText
from sqlalchemy import event
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy_i18n import make_translatable, translation_base, Translatable

make_translatable(options={'locales': ['pt', 'en', 'es'],
                           'auto_create_locales': True,
                           'fallback_locale': 'en'})

db = SQLAlchemy()


# noinspection PyClassHasNoInit
class OperationType:
    ACTION = 'ACTION'
    VISUALIZATION = 'VISUALIZATION'
    SHUFFLE = 'SHUFFLE'
    TRANSFORMATION = 'TRANSFORMATION'

    @staticmethod
    def values():
        return [n for n in OperationType.__dict__.keys()
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class ScriptType:
    PY_SERVER = 'PY_SERVER'
    JS_CLIENT = 'JS_CLIENT'

    @staticmethod
    def values():
        return [n for n in ScriptType.__dict__.keys()
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class OperationPortType:
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    @staticmethod
    def values():
        return [n for n in OperationPortType.__dict__.keys()
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class OperationPortMultiplicity:
    MANY = 'MANY'
    ONE = 'ONE'

    @staticmethod
    def values():
        return [n for n in OperationPortMultiplicity.__dict__.keys()
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class ApplicationType:
    SPARK_APPLICATION = 'SPARK_APPLICATION'
    SPARK_CODE_FUNCTION = 'SPARK_CODE_FUNCTION'

    @staticmethod
    def values():
        return [n for n in ApplicationType.__dict__.keys()
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class OperationFieldScope:
    BOTH = 'BOTH'
    EXECUTION = 'EXECUTION'
    DESIGN = 'DESIGN'

    @staticmethod
    def values():
        return [n for n in OperationFieldScope.__dict__.keys()
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class DataType:
    BINARY = 'BINARY'
    FLOAT = 'FLOAT'
    LAT_LONG = 'LAT_LONG'
    TIME = 'TIME'
    DOUBLE = 'DOUBLE'
    DECIMAL = 'DECIMAL'
    ENUM = 'ENUM'
    CHARACTER = 'CHARACTER'
    LONG = 'LONG'
    DATETIME = 'DATETIME'
    VECTOR = 'VECTOR'
    TEXT = 'TEXT'
    DATE = 'DATE'
    INTEGER = 'INTEGER'
    TIMESTAMP = 'TIMESTAMP'

    @staticmethod
    def values():
        return [n for n in DataType.__dict__.keys()
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class PermissionType:
    READ = 'READ'
    WRITE = 'WRITE'
    EXECUTE = 'EXECUTE'

    @staticmethod
    def values():
        return [n for n in PermissionType.__dict__.keys()
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class TaskGroupType:
    PIPELINE = 'PIPELINE'
    TEMPLATE = 'TEMPLATE'
    SERVICE = 'SERVICE'

    @staticmethod
    def values():
        return [n for n in TaskGroupType.__dict__.keys()
                if n[0] != '_' and n != 'values']


class Application(db.Model):
    """ Any external application that can be ran by Juicer """
    __tablename__ = 'application'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)
    enabled = Column(Boolean,
                     default=True, nullable=False)
    type = Column(Enum(*ApplicationType.values(),
                       name='ApplicationTypeEnumType'), nullable=False)
    execution_parameters = Column(String(16000000))
    __mapper_args__ = {
        'order_by': 'name'
    }

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Flow(db.Model):
    """ Flow of data between two tasks in Lemonade """
    __tablename__ = 'flow'

    # Fields
    id = Column(Integer, primary_key=True)
    source_port = Column(Integer, nullable=False)
    target_port = Column(Integer, nullable=False)
    source_port_name = Column(String(200))
    target_port_name = Column(String(200))

    # Associations
    source_id = Column(String(250),
                       ForeignKey("task.id"), nullable=False)
    source = relationship(
        "Task",
        foreign_keys=[source_id],
        backref=backref("sources",
                        cascade="all, delete-orphan"))
    target_id = Column(String(250),
                       ForeignKey("task.id"), nullable=False)
    target = relationship(
        "Task",
        foreign_keys=[target_id],
        backref=backref("targets",
                        cascade="all, delete-orphan"))
    workflow_id = Column(Integer,
                         ForeignKey("workflow.id"), nullable=False)
    workflow = relationship(
        "Workflow",
        foreign_keys=[workflow_id],
        backref=backref("flows",
                        cascade="all, delete-orphan"))

    def __unicode__(self):
        return self.source_port

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Operation(db.Model, Translatable):
    """ Operation executed in Lemonade """
    __tablename__ = 'operation'
    __translatable__ = {'locales': ['pt', 'en', 'es']}

    # Fields
    id = Column(Integer, primary_key=True)
    slug = Column(String(200), nullable=False)
    enabled = Column(Boolean, nullable=False)
    type = Column(Enum(*OperationType.values(),
                       name='OperationTypeEnumType'), nullable=False)
    icon = Column(String(200), nullable=False)

    # Associations
    # noinspection PyUnresolvedReferences
    operation_category_operation = db.Table(
        'operation_category_operation',
        Column('operation_id', Integer,
               ForeignKey('operation.id'), nullable=False),
        Column('operation_category_id', Integer,
               ForeignKey('operation_category.id'), nullable=False))
    categories = relationship(
        "OperationCategory",
        secondary=operation_category_operation)
    # noinspection PyUnresolvedReferences
    operation_platform = db.Table(
        'operation_platform',
        Column('operation_id', Integer,
               ForeignKey('operation.id'), nullable=False),
        Column('platform_id', Integer,
               ForeignKey('platform.id'), nullable=False))
    platforms = relationship(
        "Platform",
        secondary=operation_platform,
        secondaryjoin=(
            "and_("
            "Platform.id==operation_platform.c.platform_id,"
            "Platform.enabled==1)"))
    # noinspection PyUnresolvedReferences
    operation_operation_form = db.Table(
        'operation_operation_form',
        Column('operation_id', Integer,
               ForeignKey('operation.id'), nullable=False),
        Column('operation_form_id', Integer,
               ForeignKey('operation_form.id'), nullable=False))
    forms = relationship(
        "OperationForm",
        secondary=operation_operation_form,
        secondaryjoin=(
            "and_("
            "OperationForm.id==operation_operation_form.c.operation_form_id,"
            "OperationForm.enabled==1)"))
    ports = relationship("OperationPort", back_populates="operation")
    scripts = relationship("OperationScript", back_populates="operation")

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


class OperationCategory(db.Model, Translatable):
    """ Allows categorize operations """
    __tablename__ = 'operation_category'
    __translatable__ = {'locales': ['pt', 'en', 'es']}

    # Fields
    id = Column(Integer, primary_key=True)
    type = Column(String(200), nullable=False)
    order = Column(Integer,
                   default=1, nullable=False)
    default_order = Column(Integer,
                           default=1, nullable=False)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationCategoryTranslation(translation_base(OperationCategory)):
    """ Translation table for OperationCategory """
    __tablename__ = 'operation_category_translation'

    # Fields
    name = Column(Unicode(200))


class OperationForm(db.Model, Translatable):
    """ A form used to fill parameters to the operations """
    __tablename__ = 'operation_form'
    __translatable__ = {'locales': ['pt', 'en', 'es']}

    # Fields
    id = Column(Integer, primary_key=True)
    enabled = Column(Boolean,
                     default=True, nullable=False)
    order = Column(Integer, nullable=False)
    category = Column(String(200), nullable=False)
    __mapper_args__ = {
        'order_by': 'order'
    }

    # Associations
    fields = relationship("OperationFormField",
                          order_by="OperationFormField.order")

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationFormTranslation(translation_base(OperationForm)):
    """ Translation table for OperationForm """
    __tablename__ = 'operation_form_translation'

    # Fields
    name = Column(Unicode(200))


class OperationFormField(db.Model, Translatable):
    """ A field used to fill one parameter of a form for an operations """
    __tablename__ = 'operation_form_field'
    __translatable__ = {'locales': ['pt', 'en', 'es']}

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    type = Column(Enum(*DataType.values(),
                       name='DataTypeEnumType'), nullable=False)
    required = Column(Boolean, nullable=False)
    order = Column(Integer,
                   default=0, nullable=False)
    default = Column(String(16000000))
    suggested_widget = Column(String(200))
    values_url = Column(String(200))
    values = Column(String(16000000))
    scope = Column(Enum(*OperationFieldScope.values(),
                        name='OperationFieldScopeEnumType'),
                   default='BOTH', nullable=False)
    enable_conditions = Column(String(2000))
    __mapper_args__ = {
        'order_by': 'order'
    }

    # Associations
    form_id = Column(Integer,
                     ForeignKey("operation_form.id"), nullable=False)
    form = relationship(
        "OperationForm",
        foreign_keys=[form_id])

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationFormFieldTranslation(translation_base(OperationFormField)):
    """ Translation table for OperationFormField """
    __tablename__ = 'operation_form_field_translation'

    # Fields
    label = Column(Unicode(200))
    help = Column(UnicodeText())


class OperationPort(db.Model, Translatable):
    """ An input or output port for operation """
    __tablename__ = 'operation_port'
    __translatable__ = {'locales': ['pt', 'en', 'es']}

    # Fields
    id = Column(Integer, primary_key=True)
    slug = Column(String(50), nullable=False)
    type = Column(Enum(*OperationPortType.values(),
                       name='OperationPortTypeEnumType'), nullable=False)
    tags = Column(String(16000000))
    order = Column(Integer)
    multiplicity = Column(Enum(*OperationPortMultiplicity.values(),
                               name='OperationPortMultiplicityEnumType'),
                          default=1, nullable=False)
    __mapper_args__ = {
        'order_by': 'order'
    }

    # Associations
    # noinspection PyUnresolvedReferences
    operation_port_interface_operation_port = db.Table(
        'operation_port_interface_operation_port',
        Column('operation_port_id', Integer,
               ForeignKey('operation_port.id'), nullable=False),
        Column('operation_port_interface_id', Integer,
               ForeignKey('operation_port_interface.id'), nullable=False))
    interfaces = relationship(
        "OperationPortInterface",
        secondary=operation_port_interface_operation_port)
    operation_id = Column(Integer,
                          ForeignKey("operation.id"), nullable=False)
    operation = relationship(
        "Operation",
        foreign_keys=[operation_id])

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationPortTranslation(translation_base(OperationPort)):
    """ Translation table for OperationPort """
    __tablename__ = 'operation_port_translation'

    # Fields
    name = Column(Unicode(200))
    description = Column(Unicode(200))


class OperationPortInterface(db.Model, Translatable):
    """ An interface that a operation port supports """
    __tablename__ = 'operation_port_interface'
    __translatable__ = {'locales': ['pt', 'en', 'es']}

    # Fields
    id = Column(Integer, primary_key=True)
    color = Column(String(50), nullable=False)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationPortInterfaceTranslation(
        translation_base(OperationPortInterface)):
    """ Translation table for OperationPortInterface """
    __tablename__ = 'operation_port_interface_translation'

    # Fields
    name = Column(Unicode(200))


class OperationScript(db.Model):
    """ A script used in the context of the operation """
    __tablename__ = 'operation_script'

    # Fields
    id = Column(Integer, primary_key=True)
    type = Column(Enum(*ScriptType.values(),
                       name='ScriptTypeEnumType'), nullable=False)
    enabled = Column(Boolean, nullable=False)
    body = Column(String(16000000), nullable=False)

    # Associations
    operation_id = Column(Integer,
                          ForeignKey("operation.id"), nullable=False)
    operation = relationship(
        "Operation",
        foreign_keys=[operation_id])

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Platform(db.Model, Translatable):
    """ Execution platform """
    __tablename__ = 'platform'
    __translatable__ = {'locales': ['pt', 'en', 'es']}

    # Fields
    id = Column(Integer, primary_key=True)
    slug = Column(String(200), nullable=False)
    enabled = Column(Boolean, nullable=False)
    icon = Column(String(200), nullable=False)

    # Associations
    # noinspection PyUnresolvedReferences
    platform_form = db.Table(
        'platform_form',
        Column('platform_id', Integer,
               ForeignKey('platform.id'), nullable=False),
        Column('operation_form_id', Integer,
               ForeignKey('operation_form.id'), nullable=False))
    forms = relationship(
        "OperationForm",
        secondary=platform_form,
        secondaryjoin=(
            "and_("
            "OperationForm.id==platform_form.c.operation_form_id,"
            "OperationForm.enabled==1)"))

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class PlatformTranslation(translation_base(Platform)):
    """ Translation table for Platform """
    __tablename__ = 'platform_translation'

    # Fields
    name = Column(Unicode(200))
    description = Column(Unicode(200))


class Task(db.Model):
    """ Task executed in Lemonade """
    __tablename__ = 'task'

    # Fields
    id = Column(String(250), primary_key=True,
                autoincrement=False)
    name = Column(String(200))
    left = Column(Integer, nullable=False)
    top = Column(Integer, nullable=False)
    z_index = Column(Integer, nullable=False)
    forms = Column(String(16000000), nullable=False)
    version = Column(Integer, nullable=False)
    enabled = Column(Boolean,
                     default=True, nullable=False)
    __mapper_args__ = {
        'version_id_col': version,
    }

    # Associations
    workflow_id = Column(Integer,
                         ForeignKey("workflow.id"), nullable=False)
    workflow = relationship(
        "Workflow",
        foreign_keys=[workflow_id],
        backref=backref("tasks",
                        cascade="all, delete-orphan"))
    operation_id = Column(Integer,
                          ForeignKey("operation.id"), nullable=False)
    operation = relationship(
        "Operation",
        foreign_keys=[operation_id])

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class TaskGroup(db.Model):
    """ Group of tasks """
    __tablename__ = 'task_group'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    type = Column(Enum(*TaskGroupType.values(),
                       name='TaskGroupTypeEnumType'), nullable=False)
    color = Column(String(200))

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Workflow(db.Model):
    """ Workflow in Lemonade. It's a set of tasks """
    __tablename__ = 'workflow'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(16000000))
    enabled = Column(Boolean,
                     default=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    user_login = Column(String(50), nullable=False)
    user_name = Column(String(200), nullable=False)
    created = Column(DateTime,
                     default=datetime.datetime.utcnow, nullable=False)
    updated = Column(DateTime,
                     default=datetime.datetime.utcnow, nullable=False,
                     onupdate=datetime.datetime.utcnow)
    version = Column(Integer, nullable=False)
    image = Column(String(1000))
    is_template = Column(Boolean,
                         default=False, nullable=False)
    is_system_template = Column(Boolean,
                                default=False, nullable=False)
    is_public = Column(Boolean,
                       default=False, nullable=False)
    template_code = Column(String(16000000))
    forms = Column(String(16000000), nullable=False)
    __mapper_args__ = {
        'version_id_col': version, 'order_by': 'name'
    }

    # Associations
    platform_id = Column(Integer,
                         ForeignKey("platform.id"), nullable=False)
    platform = relationship(
        "Platform",
        foreign_keys=[platform_id])

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class WorkflowHistory(db.Model):
    """ Stores previous versions of the workflow. """
    __tablename__ = 'workflow_history'

    # Fields
    id = Column(Integer, primary_key=True)
    version = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    user_login = Column(String(50), nullable=False)
    user_name = Column(String(200), nullable=False)
    date = Column(DateTime,
                  default=datetime.datetime.utcnow, nullable=False)
    content = Column(String(16000000), nullable=False)

    # Associations
    workflow_id = Column(Integer,
                         ForeignKey("workflow.id"), nullable=False)
    workflow = relationship(
        "Workflow",
        foreign_keys=[workflow_id],
        backref=backref("versions",
                        cascade="all, delete-orphan"))

    def __unicode__(self):
        return self.version

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class WorkflowPermission(db.Model):
    """ Associate users and permissions """
    __tablename__ = 'workflow_permission'

    # Fields
    id = Column(Integer, primary_key=True)
    permission = Column(Enum(*PermissionType.values(),
                             name='PermissionTypeEnumType'), nullable=False)
    user_id = Column(Integer, nullable=False)
    user_login = Column(String(50), nullable=False)
    user_name = Column(String(200), nullable=False)

    # Associations
    workflow_id = Column(Integer,
                         ForeignKey("workflow.id"), nullable=False)
    workflow = relationship(
        "Workflow",
        foreign_keys=[workflow_id],
        backref=backref("permissions",
                        cascade="all, delete-orphan"))

    def __unicode__(self):
        return self.permission

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)

