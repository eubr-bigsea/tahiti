# -*- coding: utf-8 -*-
import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, \
    Enum, DateTime, Numeric, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()


# noinspection PyClassHasNoInit
class OperationType:
    ACTION = 'ACTION'
    SHUFFLE = 'SHUFFLE'
    TRANSFORMATION = 'TRANSFORMATION'


# noinspection PyClassHasNoInit
class StatusExecution:
    COMPLETED = 'COMPLETED'
    WAITING = 'WAITING'
    INTERRUPTED = 'INTERRUPTED'
    CANCELED = 'CANCELED'
    RUNNING = 'RUNNING'
    ERROR = 'ERROR'
    PENDING = 'PENDING'


# noinspection PyClassHasNoInit
class OperationPortType:
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'


# noinspection PyClassHasNoInit
class OperationPortMultiplicity:
    MANY = 'MANY'
    ONE = 'ONE'


# noinspection PyClassHasNoInit
class DataSourceFormat:
    XML_FILE = 'XML_FILE'
    NETCDF4 = 'NETCDF4'
    HDF5 = 'HDF5'
    CSV_FILE = 'CSV_FILE'
    CUSTOM = 'CUSTOM'
    JSON = 'JSON'
    TEXT = 'TEXT'
    PICKLE = 'PICKLE'


# noinspection PyClassHasNoInit
class StorageType:
    HDFS = 'HDFS'
    OPHIDIA = 'OPHIDIA'
    ELASTIC_SEARCH = 'ELASTIC_SEARCH'
    MONGODB = 'MONGODB'
    POSTGIS = 'POSTGIS'
    HBASE = 'HBASE'
    CASSANDRA = 'CASSANDRA'


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


class Operation(db.Model):
    """ Operation executed in Lemonade """
    __tablename__ = 'operation'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    enabled = Column(Boolean, nullable=False)
    description = Column(String(200), nullable=False)
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
    forms = relationship("OperationForm", back_populates="operation")
    ports = relationship("OperationPort", back_populates="operation")

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


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


class OperationCategory(db.Model):
    """ Allows categorize operations """
    __tablename__ = 'operation_category'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    type = Column(String(200), nullable=False)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationForm(db.Model):
    """ A form used to fill parameters to the operations """
    __tablename__ = 'operation_form'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    # Associations
    fields = relationship("OperationFormField")

    operation_id = Column(Integer, 
                          ForeignKey("operation.id"), nullable=False)
    operation = relationship("Operation", foreign_keys=[operation_id])

    def __unicode__(self):
        return self.name

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
    suggested_widget = Column(String(200))
    values_url = Column(String(200))
    values = Column(String(200))
    # Associations

    form_id = Column(Integer, 
                     ForeignKey("operation_form.id"), nullable=False)
    form = relationship("OperationForm", foreign_keys=[form_id])

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
    user_id = Column(Integer)
    user_login = Column(String(50))
    user_name = Column(String(200))
    # Associations
    tasks = relationship("Task", back_populates="workflow")

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Task(db.Model):
    """ Task executed in Lemonade """
    __tablename__ = 'task'

    # Fields
    id = Column(Integer, primary_key=True)
    order = Column(Integer, nullable=False)
    log_level = Column(String(200), nullable=False)
    is_start = Column(Boolean, nullable=False, default=False)
    is_end = Column(Boolean, nullable=False, default=False)
    operation_id = Column(Integer, nullable=False)
    operation_name = Column(String(200), nullable=False)
    # Associations

    workflow_id = Column(Integer, 
                         ForeignKey("workflow.id"), nullable=False)
    workflow = relationship("Workflow", foreign_keys=[workflow_id], 
                            back_populates="tasks"
    )

    def __unicode__(self):
        return self.order

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Execution(db.Model):
    """ Records a workflow execution """
    __tablename__ = 'execution'

    # Fields
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    started = Column(DateTime)
    finished = Column(DateTime)
    status = Column(Enum(*StatusExecution.__dict__.keys(), 
                         name='StatusExecutionEnumType'), nullable=False)
    workflow_id = Column(Integer, nullable=False)
    workflow_name = Column(String(200), nullable=False)
    workflow_definition = Column(Text, nullable=False)
    user_id = Column(Integer, nullable=False)
    user_login = Column(String(50), nullable=False)
    user_name = Column(String(200), nullable=False)
    # Associations
    tasks_execution = relationship("TaskExecution", back_populates="execution")

    def __unicode__(self):
        return self.created

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class TaskExecution(db.Model):
    """ Records a task execution """
    __tablename__ = 'task_execution'

    # Fields
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    status = Column(Enum(*StatusExecution.__dict__.keys(), 
                         name='StatusExecutionEnumType'), nullable=False)
    task_id = Column(Integer, nullable=False)
    operation_id = Column(Integer, nullable=False)
    operation_name = Column(String(200), nullable=False)
    # Associations

    execution_id = Column(Integer, 
                          ForeignKey("execution.id"), nullable=False)
    execution = relationship("Execution", foreign_keys=[execution_id])

    def __unicode__(self):
        return self.date

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class DataSource(db.Model):
    """ Data source in Lemonade system (anything that stores data. """
    __tablename__ = 'data_source'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    enabled = Column(Boolean, nullable=False)
    read_only = Column(Boolean, nullable=False)
    url = Column(String(200), nullable=False)
    created = Column(DateTime, nullable=False, default=func.now())
    format = Column(Enum(*DataSourceFormat.__dict__.keys(), 
                         name='DataSourceFormatEnumType'), nullable=False)
    provenience = Column(Text)
    estimated_rows = Column(Integer)
    estimated_size_in_mega_bytes = Column(Numeric(10, 2))
    expiration = Column(String(200))
    user_id = Column(Integer)
    user_login = Column(String(50))
    user_name = Column(String(200))
    tags = Column(String(100))
    # Associations

    storage_id = Column(Integer, 
                        ForeignKey("storage.id"), nullable=False)
    storage = relationship("Storage", foreign_keys=[storage_id])

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Attribute(db.Model):
    """ Data source attribute. """
    __tablename__ = 'attribute'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    type = Column(Enum(*DataType.__dict__.keys(), 
                       name='DataTypeEnumType'), nullable=False)
    size = Column(Integer)
    precision = Column(Integer)
    nullable = Column(Boolean, nullable=False)
    enumeration = Column(Boolean, nullable=False)
    missing_representation = Column(String(200))
    feature = Column(Boolean, nullable=False, default=True)
    label = Column(Boolean, nullable=False, default=True)
    distinct_values = Column(Integer)
    mean_value = Column(Float)
    median_value = Column(String(200))
    max_value = Column(String(200))
    min_value = Column(String(200))
    std_deviation = Column(Float)
    missing_total = Column(String(200))
    deciles = Column(Text)
    # Associations

    data_source_id = Column(Integer, 
                            ForeignKey("data_source.id"), nullable=False)
    data_source = relationship("DataSource", foreign_keys=[data_source_id], 
                               backref=backref(
                                   "attributes",
                                   cascade="all, delete-orphan"))

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Storage(db.Model):
    """ Type of storage used by data sources """
    __tablename__ = 'storage'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(Enum(*StorageType.__dict__.keys(), 
                       name='StorageTypeEnumType'), nullable=False)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)
