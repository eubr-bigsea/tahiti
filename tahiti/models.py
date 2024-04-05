import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, \
    DateTime, Text, Unicode, UnicodeText
from sqlalchemy.orm import relationship, backref
from sqlalchemy_i18n import make_translatable, translation_base, Translatable

make_translatable(options={'locales': ['pt', 'en'],
                           'auto_create_locales': False,
                           'fallback_locale': 'en'})

db = SQLAlchemy()


# noinspection PyClassHasNoInit
class OperationType:
    TRANSFORMATION = 'TRANSFORMATION'
    ACTION = 'ACTION'
    VISUALIZATION = 'VISUALIZATION'
    SHUFFLE = 'SHUFFLE'
    SYSTEM_META_OPERATION = 'SYSTEM_META_OPERATION'
    USER_META_OPERATION = 'USER_META_OPERATION'
    SHORTCUT = 'SHORTCUT'

    @staticmethod
    def values():
        return [n for n in list(OperationType.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class DiagramEnvironment:
    DESIGN = 'DESIGN'
    DEPLOYMENT = 'DEPLOYMENT'

    @staticmethod
    def values():
        return [n for n in list(DiagramEnvironment.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class ScriptType:
    JS_CLIENT = 'JS_CLIENT'
    PY_SERVER = 'PY_SERVER'

    @staticmethod
    def values():
        return [n for n in list(ScriptType.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class OperationPortType:
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    @staticmethod
    def values():
        return [n for n in list(OperationPortType.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class OperationPortMultiplicity:
    ONE = 'ONE'
    MANY = 'MANY'

    @staticmethod
    def values():
        return [n for n in list(OperationPortMultiplicity.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class ApplicationType:
    SPARK_APPLICATION = 'SPARK_APPLICATION'
    SPARK_CODE_FUNCTION = 'SPARK_CODE_FUNCTION'

    @staticmethod
    def values():
        return [n for n in list(ApplicationType.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class OperationFieldScope:
    DESIGN = 'DESIGN'
    EXECUTION = 'EXECUTION'
    BOTH = 'BOTH'

    @staticmethod
    def values():
        return [n for n in list(OperationFieldScope.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class DataType:
    BINARY = 'BINARY'
    CHARACTER = 'CHARACTER'
    DATE = 'DATE'
    DATETIME = 'DATETIME'
    DECIMAL = 'DECIMAL'
    DOUBLE = 'DOUBLE'
    ENUM = 'ENUM'
    FILE = 'FILE'
    FLOAT = 'FLOAT'
    INTEGER = 'INTEGER'
    LAT_LONG = 'LAT_LONG'
    LONG = 'LONG'
    TEXT = 'TEXT'
    TIME = 'TIME'
    TIMESTAMP = 'TIMESTAMP'
    VECTOR = 'VECTOR'

    @staticmethod
    def values():
        return [n for n in list(DataType.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class PermissionType:
    READ = 'READ'
    WRITE = 'WRITE'
    EXECUTE = 'EXECUTE'

    @staticmethod
    def values():
        return [n for n in list(PermissionType.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class WorkflowType:
    WORKFLOW = 'WORKFLOW'
    USER_TEMPLATE = 'USER_TEMPLATE'
    SYSTEM_TEMPLATE = 'SYSTEM_TEMPLATE'
    SUB_FLOW = 'SUB_FLOW'
    DATA_EXPLORER = 'DATA_EXPLORER'
    MODEL_BUILDER = 'MODEL_BUILDER'
    VIS_BUILDER = 'VIS_BUILDER'
    SQL = 'SQL'

    @staticmethod
    def values():
        return [n for n in list(WorkflowType.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class PublishingStatus:
    EDITING = 'EDITING'
    PUBLISHED = 'PUBLISHED'
    DISABLED = 'DISABLED'

    @staticmethod
    def values():
        return [n for n in list(PublishingStatus.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class TaskGroupType:
    PIPELINE = 'PIPELINE'
    SERVICE = 'SERVICE'
    TEMPLATE = 'TEMPLATE'

    @staticmethod
    def values():
        return [n for n in list(TaskGroupType.__dict__.keys())
                if n[0] != '_' and n != 'values']


# noinspection PyClassHasNoInit
class PluginStatus:
    PENDING = 'PENDING'
    INSTALLED = 'INSTALLED'
    OUTDATED = 'OUTDATED'
    ERROR = 'ERROR'
    DISABLED = 'DISABLED'

    @staticmethod
    def values():
        return [n for n in list(PluginStatus.__dict__.keys())
                if n[0] != '_' and n != 'values']


# Association tables definition
    # noinspection PyUnresolvedReferences
operation_category_operation = db.Table(
    'operation_category_operation',
    Column('operation_id', Integer,
           ForeignKey('operation.id'),
           nullable=False, index=True),
    Column('operation_category_id', Integer,
           ForeignKey('operation_category.id'),
           nullable=False, index=True))
# noinspection PyUnresolvedReferences
operation_platform = db.Table(
    'operation_platform',
    Column('operation_id', Integer,
           ForeignKey('operation.id'),
           nullable=False, index=True),
    Column('platform_id', Integer,
           ForeignKey('platform.id'),
           nullable=False, index=True))
# noinspection PyUnresolvedReferences
operation_operation_form = db.Table(
    'operation_operation_form',
    Column('operation_id', Integer,
           ForeignKey('operation.id'),
           nullable=False, index=True),
    Column('operation_form_id', Integer,
           ForeignKey('operation_form.id'),
           nullable=False, index=True))
# noinspection PyUnresolvedReferences
operation_port_interface_operation_port = db.Table(
    'operation_port_interface_operation_port',
    Column('operation_port_id', Integer,
           ForeignKey('operation_port.id'),
           nullable=False, index=True),
    Column('operation_port_interface_id', Integer,
           ForeignKey('operation_port_interface.id'),
           nullable=False, index=True))
# noinspection PyUnresolvedReferences
operation_subset_operation = db.Table(
    'operation_subset_operation',
    Column('operation_subset_id', Integer,
           ForeignKey('operation_subset.id'),
           nullable=False, index=True),
    Column('operation_id', Integer,
           ForeignKey('operation.id'),
           nullable=False, index=True))
# noinspection PyUnresolvedReferences
platform_form = db.Table(
    'platform_form',
    Column('platform_id', Integer,
           ForeignKey('platform.id'),
           nullable=False, index=True),
    Column('operation_form_id', Integer,
           ForeignKey('operation_form.id'),
           nullable=False, index=True))


class Application(db.Model):
    """ Any external application that can be ran by Juicer """
    __tablename__ = 'application'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)
    enabled = Column(Boolean,
                     default=True, nullable=False)
    type = Column(Enum(*list(ApplicationType.values()),
                       name='ApplicationTypeEnumType'), nullable=False)
    execution_parameters = Column(Text(4294000000))

    def __str__(self):
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
    environment = Column(Enum(*list(DiagramEnvironment.values()),
                              name='DiagramEnvironmentEnumType'),
                         default=DiagramEnvironment.DESIGN, nullable=False)

    # Associations
    source_id = Column(String(250),
                       ForeignKey("task.id",
                                  name="fk_flow_source_id"),
                       nullable=False,
                       index=True)
    source = relationship(
        "Task",
        overlaps='sources',
        foreign_keys=[source_id],
        backref=backref("sources",
                        cascade="all, delete-orphan"))
    target_id = Column(String(250),
                       ForeignKey("task.id",
                                  name="fk_flow_target_id"),
                       nullable=False,
                       index=True)
    target = relationship(
        "Task",
        overlaps='targets',
        foreign_keys=[target_id],
        backref=backref("targets",
                        cascade="all, delete-orphan"))
    workflow_id = Column(Integer,
                         ForeignKey("workflow.id",
                                    name="fk_flow_workflow_id"),
                         nullable=False,
                         index=True)
    workflow = relationship(
        "Workflow",
        overlaps='flows',
        foreign_keys=[workflow_id],
        backref=backref("flows",
                        cascade="all, delete-orphan"))

    def __str__(self):
        return self.source_port

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Operation(db.Model, Translatable):
    """ Operation executed in Lemonade """
    __tablename__ = 'operation'
    __translatable__ = {'locales': ['pt', 'en']}

    # Fields
    id = Column(Integer, primary_key=True)
    slug = Column(String(200), nullable=False)
    enabled = Column(Boolean, nullable=False)
    type = Column(Enum(*list(OperationType.values()),
                       name='OperationTypeEnumType'), nullable=False)
    icon = Column(String(200), nullable=False)
    css_class = Column(String(200))
    doc_link = Column(String(200))

    # Associations
    categories = relationship(
        "OperationCategory",
        overlaps="operations",
        secondary=operation_category_operation)
    platforms = relationship(
        "Platform",
        overlaps="operations",
        secondary=operation_platform,
        secondaryjoin=(
            "and_("
            "Platform.id==operation_platform.c.platform_id,"
            "Platform.enabled==1)"))
    forms = relationship(
        "OperationForm",
        overlaps="operations",
        secondary=operation_operation_form,
        secondaryjoin=(
            "and_("
            "OperationForm.id==operation_operation_form.c.operation_form_id,"
            "OperationForm.enabled==1)"))
    ports = relationship("OperationPort",
                         cascade="all, delete-orphan")
    scripts = relationship("OperationScript",
                           cascade="all, delete-orphan")

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationTranslation(translation_base(Operation)):
    """ Translation table for Operation """
    __tablename__ = 'operation_translation'

    # Fields
    name = Column(Unicode(200))
    description = Column(Unicode(800))
    label_format = Column(Unicode(800))


class OperationCategory(db.Model, Translatable):
    """ Allows categorize operations """
    __tablename__ = 'operation_category'
    __translatable__ = {'locales': ['pt', 'en']}

    # Fields
    id = Column(Integer, primary_key=True)
    type = Column(String(200), nullable=False)
    subtype = Column(String(200))
    order = Column(Integer,
                   default=1, nullable=False)
    default_order = Column(Integer,
                           default=1, nullable=False)

    def __str__(self):
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
    __translatable__ = {'locales': ['pt', 'en']}

    # Fields
    id = Column(Integer, primary_key=True)
    enabled = Column(Boolean,
                     default=True, nullable=False)
    order = Column(Integer, nullable=False)
    category = Column(String(200), nullable=False)

    # Associations
    fields = relationship("OperationFormField",
                          order_by="OperationFormField.order")

    def __str__(self):
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
    __translatable__ = {'locales': ['pt', 'en']}

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    type = Column(Enum(*list(DataType.values()),
                       name='DataTypeEnumType'), nullable=False)
    required = Column(Boolean, nullable=False)
    order = Column(Integer,
                   default=0, nullable=False)
    default = Column(Text(4294000000))
    suggested_widget = Column(String(200))
    values_url = Column(String(200))
    values = Column(Text(4294000000))
    scope = Column(Enum(*list(OperationFieldScope.values()),
                        name='OperationFieldScopeEnumType'),
                   default='BOTH', nullable=False)
    enable_conditions = Column(String(2000))
    editable = Column(Boolean,
                      default=True, nullable=False)

    # Associations
    form_id = Column(Integer,
                     ForeignKey("operation_form.id",
                                name="fk_operation_form_field_form_id"),
                     index=True)
    form = relationship(
        "OperationForm",
        overlaps='fields',
        foreign_keys=[form_id])

    def __str__(self):
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
    __translatable__ = {'locales': ['pt', 'en']}

    # Fields
    id = Column(Integer, primary_key=True)
    slug = Column(String(50), nullable=False)
    type = Column(Enum(*list(OperationPortType.values()),
                       name='OperationPortTypeEnumType'), nullable=False)
    tags = Column(Text(4294000000))
    order = Column(Integer)
    multiplicity = Column(Enum(*list(OperationPortMultiplicity.values()),
                               name='OperationPortMultiplicityEnumType'),
                          default=1, nullable=False)

    # Associations
    interfaces = relationship(
        "OperationPortInterface",
        overlaps="operation_ports",
        secondary=operation_port_interface_operation_port)
    operation_id = Column(Integer,
                          ForeignKey("operation.id",
                                     name="fk_operation_port_operation_id"),
                          nullable=False,
                          index=True)
    operation = relationship(
        "Operation",
        overlaps='ports',
        foreign_keys=[operation_id])

    def __str__(self):
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
    __translatable__ = {'locales': ['pt', 'en']}

    # Fields
    id = Column(Integer, primary_key=True)
    color = Column(String(50), nullable=False)

    def __str__(self):
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
    type = Column(Enum(*list(ScriptType.values()),
                       name='ScriptTypeEnumType'), nullable=False)
    enabled = Column(Boolean, nullable=False)
    body = Column(Text(4294000000), nullable=False)

    # Associations
    operation_id = Column(Integer,
                          ForeignKey("operation.id",
                                     name="fk_operation_script_operation_id"),
                          nullable=False,
                          index=True)
    operation = relationship(
        "Operation",
        overlaps='scripts',
        foreign_keys=[operation_id])

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class OperationSubset(db.Model):
    """ A subset of operations in a platform """
    __tablename__ = 'operation_subset'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # Associations
    platform_id = Column(Integer,
                         ForeignKey("platform.id",
                                    name="fk_operation_subset_platform_id"),
                         nullable=False,
                         index=True)
    platform = relationship(
        "Platform",
        overlaps='subsets',
        foreign_keys=[platform_id],
        back_populates="subsets"
    )
    operations = relationship(
        "Operation",
        overlaps="operation_subsets",
        secondary=operation_subset_operation,
        secondaryjoin=(
            "and_("
            "Operation.id==operation_subset_operation.c.operation_id,"
            "Operation.enabled==1)"))

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Pipeline(db.Model):
    """ Pipeline """
    __tablename__ = 'pipeline'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(200))
    enabled = Column(Boolean, nullable=False)
    user_id = Column(Integer, nullable=False)
    user_login = Column(String(50), nullable=False)
    user_name = Column(String(200), nullable=False)
    created = Column(DateTime,
                     default=datetime.datetime.utcnow, nullable=False)
    updated = Column(DateTime,
                     default=datetime.datetime.utcnow, nullable=False,
                     onupdate=datetime.datetime.utcnow)
    version = Column(Integer, nullable=False)
    execution_window = Column(Integer)
    variables = Column(String(1000))
    preferred_cluster_id = Column(Integer)

    # Associations
    steps = relationship("PipelineStep",
                         cascade="all, delete-orphan")

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class PipelineStep(db.Model):
    """ Pipeline step """
    __tablename__ = 'pipeline_step'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    order = Column(Integer, nullable=False)
    scheduling = Column(String(200))
    description = Column(String(200))
    enabled = Column(Boolean, nullable=False)
    workflow_type = Column(Enum(*list(WorkflowType.values()),
                                name='WorkflowTypeEnumType'))

    # Associations
    pipeline_id = Column(Integer,
                         ForeignKey("pipeline.id",
                                    name="fk_pipeline_step_pipeline_id"),
                         nullable=False,
                         index=True)
    pipeline = relationship(
        "Pipeline",
        overlaps='steps',
        foreign_keys=[pipeline_id])
    workflow_id = Column(Integer,
                         ForeignKey("workflow.id",
                                    name="fk_pipeline_step_workflow_id"),
                         index=True)
    workflow = relationship(
        "Workflow",
        overlaps='workflow',
        foreign_keys=[workflow_id])

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class PipelineTemplate(db.Model):
    """ Pipeline template """
    __tablename__ = 'pipeline_template'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(200))
    enabled = Column(Boolean, nullable=False)

    # Associations
    steps = relationship("PipelineTemplateStep",
                         cascade="all, delete-orphan")

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class PipelineTemplateStep(db.Model):
    """ Pipeline template step """
    __tablename__ = 'pipeline_template_step'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    order = Column(Integer, nullable=False)
    description = Column(String(200))
    enabled = Column(Boolean, nullable=False)

    # Associations
    template_id = Column(Integer,
                         ForeignKey("pipeline_template.id",
                                    name="fk_pipeline_template_step_template_id"),
                         nullable=False,
                         index=True)
    template = relationship(
        "PipelineTemplate",
        overlaps='steps',
        foreign_keys=[template_id])

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Platform(db.Model, Translatable):
    """ Execution platform """
    __tablename__ = 'platform'
    __translatable__ = {'locales': ['pt', 'en']}

    # Fields
    id = Column(Integer, primary_key=True)
    slug = Column(String(200), nullable=False)
    enabled = Column(Boolean, nullable=False)
    icon = Column(String(200), nullable=False)
    version = Column(String(200),
                     default=1.0)
    plugin = Column(Boolean,
                    default=False, nullable=False)

    # Associations
    forms = relationship(
        "OperationForm",
        overlaps="platforms",
        secondary=platform_form,
        secondaryjoin=(
            "and_("
            "OperationForm.id==platform_form.c.operation_form_id,"
            "OperationForm.enabled==1)"))
    subsets = relationship("OperationSubset",
                           cascade="all, delete-orphan",
                           order_by="OperationSubset.name")

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class PlatformTranslation(translation_base(Platform)):
    """ Translation table for Platform """
    __tablename__ = 'platform_translation'

    # Fields
    name = Column(Unicode(200))
    description = Column(Unicode(200))


class PlatformPlugin(db.Model):
    """ Plugin for a platform """
    __tablename__ = 'platform_plugin'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(200))
    version = Column(String(200))
    copyright = Column(String(200))
    status = Column(Enum(*list(PluginStatus.values()),
                         name='PluginStatusEnumType'))
    message = Column(Text(4294000000))
    manifest = Column(Text(4294000000))
    ids_offset = Column(Integer, nullable=False)
    uuid = Column(String(200), nullable=False)
    url = Column(String(200))
    use_compiler = Column(Boolean,
                          default=False, nullable=False)
    use_executor = Column(Boolean,
                          default=False, nullable=False)

    # Associations
    platform_id = Column(Integer,
                         ForeignKey("platform.id",
                                    name="fk_platform_plugin_platform_id"),
                         nullable=False,
                         index=True)
    platform = relationship(
        "Platform",
        overlaps='plugins',
        foreign_keys=[platform_id],
        backref=backref("plugins",
                        cascade="all, delete-orphan"))

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class RoleOperationSubset(db.Model):
    """ Role associated to a subset of operations in a platform """
    __tablename__ = 'role_operation_subset'

    # Fields
    id = Column(Integer, primary_key=True)
    role_name = Column(String(50), nullable=False)
    role_id = Column(Integer, nullable=False)

    # Associations
    subset_id = Column(Integer,
                       ForeignKey("operation_subset.id",
                                  name="fk_role_operation_subset_subset_id"),
                       nullable=False,
                       index=True)
    subset = relationship(
        "OperationSubset",
        overlaps='roles',
        foreign_keys=[subset_id],
        backref=backref("roles",
                        cascade="all, delete-orphan"))

    def __str__(self):
        return self.role_name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class SourceCode(db.Model):
    """ Trusted source code that can be used in Lemonade """
    __tablename__ = 'source_code'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    enabled = Column(Boolean, nullable=False)
    suspicious = Column(Boolean, nullable=False)
    requirements = Column(String(200))
    imports = Column(String(200))
    help = Column(String(400))
    code = Column(String(4000), nullable=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


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
    forms = Column(Text(4294000000), nullable=False)
    version = Column(Integer, nullable=False)
    environment = Column(Enum(*list(DiagramEnvironment.values()),
                              name='DiagramEnvironmentEnumType'),
                         default=DiagramEnvironment.DESIGN, nullable=False)
    enabled = Column(Boolean,
                     default=True, nullable=False)
    width = Column(Integer,
                   default=0)
    height = Column(Integer,
                    default=0)
    display_order = Column(Integer,
                           default=0)
    group_id = Column(String(200))
    __mapper_args__ = {
        'version_id_col': version,
    }

    # Associations
    workflow_id = Column(Integer,
                         ForeignKey("workflow.id",
                                    name="fk_task_workflow_id"),
                         nullable=False,
                         index=True)
    workflow = relationship(
        "Workflow",
        overlaps='tasks',
        foreign_keys=[workflow_id],
        backref=backref("tasks",
                        cascade="all, delete-orphan"))
    operation_id = Column(Integer,
                          ForeignKey("operation.id",
                                     name="fk_task_operation_id"),
                          nullable=False,
                          index=True)
    operation = relationship(
        "Operation",
        overlaps='operation',
        foreign_keys=[operation_id])

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class TaskGroup(db.Model):
    """ Group of tasks """
    __tablename__ = 'task_group'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    type = Column(Enum(*list(TaskGroupType.values()),
                       name='TaskGroupTypeEnumType'), nullable=False)
    color = Column(String(200))

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class Workflow(db.Model):
    """ Workflow in Lemonade. It's a set of tasks """
    __tablename__ = 'workflow'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(Text(4294000000))
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
    template_code = Column(Text(4294000000))
    forms = Column(Text(4294000000))
    deployment_enabled = Column(Boolean,
                                default=False, nullable=False)
    publishing_enabled = Column(Boolean,
                                default=False, nullable=False)
    publishing_status = Column(Enum(*list(PublishingStatus.values()),
                                    name='PublishingStatusEnumType'))
    type = Column(Enum(*list(WorkflowType.values()),
                       name='WorkflowTypeEnumType'),
                  default=WorkflowType.WORKFLOW, nullable=False)
    preferred_cluster_id = Column(Integer)
    __mapper_args__ = {
        'version_id_col': version,
    }

    # Associations
    platform_id = Column(Integer,
                         ForeignKey("platform.id",
                                    name="fk_workflow_platform_id"),
                         nullable=False,
                         index=True)
    platform = relationship(
        "Platform",
        overlaps='platform',
        foreign_keys=[platform_id])
    subset_id = Column(Integer,
                       ForeignKey("operation_subset.id",
                                  name="fk_workflow_subset_id"),
                       index=True)
    subset = relationship(
        "OperationSubset",
        overlaps='subset',
        foreign_keys=[subset_id])
    pipeline_id = Column(Integer,
                         ForeignKey("pipeline.id",
                                    name="fk_workflow_pipeline_id"),
                         index=True)
    pipeline = relationship(
        "Pipeline",
        overlaps='pipeline',
        foreign_keys=[pipeline_id])
    platform_id = Column(Integer,
                         ForeignKey("platform.id",
                                    name="fk_workflow_platform_id"),
                         nullable=False,
                         index=True)
    platform = relationship(
        "Platform",
        overlaps='platform',
        foreign_keys=[platform_id])

    def __str__(self):
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
    content = Column(Text(4294000000), nullable=False)

    # Associations
    workflow_id = Column(Integer,
                         ForeignKey("workflow.id",
                                    name="fk_workflow_history_workflow_id"),
                         nullable=False,
                         index=True)
    workflow = relationship(
        "Workflow",
        overlaps='versions',
        foreign_keys=[workflow_id],
        backref=backref("versions",
                        cascade="all, delete-orphan"))

    def __str__(self):
        return self.version

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class WorkflowPermission(db.Model):
    """ Associate users and permissions """
    __tablename__ = 'workflow_permission'

    # Fields
    id = Column(Integer, primary_key=True)
    permission = Column(Enum(*list(PermissionType.values()),
                             name='PermissionTypeEnumType'), nullable=False)
    user_id = Column(Integer, nullable=False)
    user_login = Column(String(50), nullable=False)
    user_name = Column(String(200), nullable=False)

    # Associations
    workflow_id = Column(Integer,
                         ForeignKey("workflow.id",
                                    name="fk_workflow_permission_workflow_id"),
                         nullable=False,
                         index=True)
    workflow = relationship(
        "Workflow",
        overlaps='permissions',
        foreign_keys=[workflow_id],
        backref=backref("permissions",
                        cascade="all, delete-orphan"))

    def __str__(self):
        return self.permission

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)


class WorkflowVariable(db.Model):
    """ Variables for workflow """
    __tablename__ = 'workflow_variable'

    # Fields
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    label = Column(String(200))
    description = Column(Text(4294000000))
    type = Column(Enum(*list(DataType.values()),
                       name='DataTypeEnumType'), nullable=False)
    multiplicity = Column(Integer,
                          default=1, nullable=False)
    suggested_widget = Column(String(200))
    default_value = Column(Text(4294000000))
    parameters = Column(Text(4294000000))

    # Associations
    workflow_id = Column(Integer,
                         ForeignKey("workflow.id",
                                    name="fk_workflow_variable_workflow_id"),
                         nullable=False,
                         index=True)
    workflow = relationship(
        "Workflow",
        overlaps='variables',
        foreign_keys=[workflow_id],
        backref=backref("variables",
                        cascade="all, delete-orphan"))

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)

