"""empty message

Revision ID: 6fc05b004619
Revises: a237518ec5e1
Create Date: 2023-06-07 14:29:05.153771

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6fc05b004619'
down_revision = 'a237518ec5e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('type', sa.Enum('SPARK_APPLICATION', 'SPARK_CODE_FUNCTION', name='ApplicationTypeEnumType'), nullable=False),
    sa.Column('execution_parameters', mysql.LONGTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=200), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('type', sa.Enum('TRANSFORMATION', 'ACTION', 'VISUALIZATION', 'SHUFFLE', 'SYSTEM_META_OPERATION', 'USER_META_OPERATION', 'SHORTCUT', name='OperationTypeEnumType'), nullable=False),
    sa.Column('icon', sa.String(length=200), nullable=False),
    sa.Column('css_class', sa.String(length=200), nullable=True),
    sa.Column('doc_link', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=200), nullable=False),
    sa.Column('subtype', sa.String(length=200), nullable=True),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('default_order', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation_form',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation_port_interface',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('platform',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=200), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('icon', sa.String(length=200), nullable=False),
    sa.Column('version', sa.String(length=200), nullable=True),
    sa.Column('plugin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('source_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', mysql.LONGTEXT(), nullable=True),
    sa.Column('code', mysql.LONGTEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('type', sa.Enum('PIPELINE', 'SERVICE', 'TEMPLATE', name='TaskGroupTypeEnumType'), nullable=False),
    sa.Column('color', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation_category_operation',
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.Column('operation_category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_category_id'], ['operation_category.id'], ),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], )
    )
    op.create_index(op.f('ix_operation_category_operation_operation_category_id'), 'operation_category_operation', ['operation_category_id'], unique=False)
    op.create_index(op.f('ix_operation_category_operation_operation_id'), 'operation_category_operation', ['operation_id'], unique=False)
    op.create_table('operation_category_translation',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation_category.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('operation_form_field',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('type', sa.Enum('BINARY', 'CHARACTER', 'DATE', 'DATETIME', 'DECIMAL', 'DOUBLE', 'ENUM', 'FILE', 'FLOAT', 'INTEGER', 'LAT_LONG', 'LONG', 'TEXT', 'TIME', 'TIMESTAMP', 'VECTOR', name='DataTypeEnumType'), nullable=False),
    sa.Column('required', sa.Boolean(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('default', mysql.LONGTEXT(), nullable=True),
    sa.Column('suggested_widget', sa.String(length=200), nullable=True),
    sa.Column('values_url', sa.String(length=200), nullable=True),
    sa.Column('values', mysql.LONGTEXT(), nullable=True),
    sa.Column('scope', sa.Enum('DESIGN', 'EXECUTION', 'BOTH', name='OperationFieldScopeEnumType'), nullable=False),
    sa.Column('enable_conditions', sa.String(length=2000), nullable=True),
    sa.Column('editable', sa.Boolean(), nullable=False),
    sa.Column('form_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['form_id'], ['operation_form.id'], name='fk_operation_form_field_form_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operation_form_field_form_id'), 'operation_form_field', ['form_id'], unique=False)
    op.create_table('operation_form_translation',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation_form.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('operation_operation_form',
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.Column('operation_form_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_form_id'], ['operation_form.id'], ),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], )
    )
    op.create_index(op.f('ix_operation_operation_form_operation_form_id'), 'operation_operation_form', ['operation_form_id'], unique=False)
    op.create_index(op.f('ix_operation_operation_form_operation_id'), 'operation_operation_form', ['operation_id'], unique=False)
    op.create_table('operation_platform',
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.Column('platform_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], ),
    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], )
    )
    op.create_index(op.f('ix_operation_platform_operation_id'), 'operation_platform', ['operation_id'], unique=False)
    op.create_index(op.f('ix_operation_platform_platform_id'), 'operation_platform', ['platform_id'], unique=False)
    op.create_table('operation_port',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.Column('type', sa.Enum('INPUT', 'OUTPUT', name='OperationPortTypeEnumType'), nullable=False),
    sa.Column('tags', mysql.LONGTEXT(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('multiplicity', sa.Enum('ONE', 'MANY', name='OperationPortMultiplicityEnumType'), nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], name='fk_operation_port_operation_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operation_port_operation_id'), 'operation_port', ['operation_id'], unique=False)
    op.create_table('operation_port_interface_translation',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation_port_interface.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('operation_script',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('JS_CLIENT', 'PY_SERVER', name='ScriptTypeEnumType'), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('body', mysql.LONGTEXT(), nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], name='fk_operation_script_operation_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operation_script_operation_id'), 'operation_script', ['operation_id'], unique=False)
    op.create_table('operation_subset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('platform_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], name='fk_operation_subset_platform_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operation_subset_platform_id'), 'operation_subset', ['platform_id'], unique=False)
    op.create_table('operation_translation',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.Column('description', sa.Unicode(length=800), nullable=True),
    sa.Column('label_format', sa.Unicode(length=800), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('platform_form',
    sa.Column('platform_id', sa.Integer(), nullable=False),
    sa.Column('operation_form_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_form_id'], ['operation_form.id'], ),
    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], )
    )
    op.create_index(op.f('ix_platform_form_operation_form_id'), 'platform_form', ['operation_form_id'], unique=False)
    op.create_index(op.f('ix_platform_form_platform_id'), 'platform_form', ['platform_id'], unique=False)
    op.create_table('platform_plugin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('version', sa.String(length=200), nullable=True),
    sa.Column('copyright', sa.String(length=200), nullable=True),
    sa.Column('status', sa.Enum('PENDING', 'INSTALLED', 'OUTDATED', 'ERROR', 'DISABLED', name='PluginStatusEnumType'), nullable=True),
    sa.Column('message', mysql.LONGTEXT(), nullable=True),
    sa.Column('manifest', mysql.LONGTEXT(), nullable=True),
    sa.Column('ids_offset', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=200), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('use_compiler', sa.Boolean(), nullable=False),
    sa.Column('use_executor', sa.Boolean(), nullable=False),
    sa.Column('platform_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], name='fk_platform_plugin_platform_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_platform_plugin_platform_id'), 'platform_plugin', ['platform_id'], unique=False)
    op.create_table('platform_translation',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.Column('description', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['platform.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('operation_form_field_translation',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('label', sa.Unicode(length=200), nullable=True),
    sa.Column('help', sa.UnicodeText(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation_form_field.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('operation_port_interface_operation_port',
    sa.Column('operation_port_id', sa.Integer(), nullable=False),
    sa.Column('operation_port_interface_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_port_id'], ['operation_port.id'], ),
    sa.ForeignKeyConstraint(['operation_port_interface_id'], ['operation_port_interface.id'], )
    )
    op.create_index(op.f('ix_operation_port_interface_operation_port_operation_port_interface_id'), 'operation_port_interface_operation_port', ['operation_port_interface_id'], unique=False)
    op.create_index(op.f('ix_operation_port_interface_operation_port_operation_port_id'), 'operation_port_interface_operation_port', ['operation_port_id'], unique=False)
    op.create_table('operation_port_translation',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.Column('description', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation_port.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('operation_subset_operation',
    sa.Column('operation_subset_id', sa.Integer(), nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], ),
    sa.ForeignKeyConstraint(['operation_subset_id'], ['operation_subset.id'], )
    )
    op.create_index(op.f('ix_operation_subset_operation_operation_id'), 'operation_subset_operation', ['operation_id'], unique=False)
    op.create_index(op.f('ix_operation_subset_operation_operation_subset_id'), 'operation_subset_operation', ['operation_subset_id'], unique=False)
    op.create_table('role_operation_subset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=50), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('subset_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subset_id'], ['operation_subset.id'], name='fk_role_operation_subset_subset_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_role_operation_subset_subset_id'), 'role_operation_subset', ['subset_id'], unique=False)
    op.create_table('workflow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', mysql.LONGTEXT(), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_login', sa.String(length=50), nullable=False),
    sa.Column('user_name', sa.String(length=200), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=1000), nullable=True),
    sa.Column('is_template', sa.Boolean(), nullable=False),
    sa.Column('is_system_template', sa.Boolean(), nullable=False),
    sa.Column('is_public', sa.Boolean(), nullable=False),
    sa.Column('template_code', mysql.LONGTEXT(), nullable=True),
    sa.Column('forms', mysql.LONGTEXT(), nullable=True),
    sa.Column('deployment_enabled', sa.Boolean(), nullable=False),
    sa.Column('publishing_enabled', sa.Boolean(), nullable=False),
    sa.Column('publishing_status', sa.Enum('EDITING', 'PUBLISHED', 'DISABLED', name='PublishingStatusEnumType'), nullable=True),
    sa.Column('type', sa.Enum('WORKFLOW', 'USER_TEMPLATE', 'SYSTEM_TEMPLATE', 'SUB_FLOW', 'DATA_EXPLORER', 'MODEL_BUILDER', 'VIS_BUILDER', name='WorkflowTypeEnumType'), nullable=False),
    sa.Column('preferred_cluster_id', sa.Integer(), nullable=True),
    sa.Column('subset_id', sa.Integer(), nullable=True),
    sa.Column('platform_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], name='fk_workflow_platform_id'),
    sa.ForeignKeyConstraint(['subset_id'], ['operation_subset.id'], name='fk_workflow_subset_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_workflow_platform_id'), 'workflow', ['platform_id'], unique=False)
    op.create_index(op.f('ix_workflow_subset_id'), 'workflow', ['subset_id'], unique=False)
    op.create_table('task',
    sa.Column('id', sa.String(length=250), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('left', sa.Integer(), nullable=False),
    sa.Column('top', sa.Integer(), nullable=False),
    sa.Column('z_index', sa.Integer(), nullable=False),
    sa.Column('forms', mysql.LONGTEXT(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('environment', sa.Enum('DESIGN', 'DEPLOYMENT', name='DiagramEnvironmentEnumType'), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('display_order', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.String(length=200), nullable=True),
    sa.Column('workflow_id', sa.Integer(), nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], name='fk_task_operation_id'),
    sa.ForeignKeyConstraint(['workflow_id'], ['workflow.id'], name='fk_task_workflow_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_operation_id'), 'task', ['operation_id'], unique=False)
    op.create_index(op.f('ix_task_workflow_id'), 'task', ['workflow_id'], unique=False)
    op.create_table('workflow_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_login', sa.String(length=50), nullable=False),
    sa.Column('user_name', sa.String(length=200), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('content', mysql.LONGTEXT(), nullable=False),
    sa.Column('workflow_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['workflow_id'], ['workflow.id'], name='fk_workflow_history_workflow_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_workflow_history_workflow_id'), 'workflow_history', ['workflow_id'], unique=False)
    op.create_table('workflow_permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('permission', sa.Enum('READ', 'WRITE', 'EXECUTE', name='PermissionTypeEnumType'), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_login', sa.String(length=50), nullable=False),
    sa.Column('user_name', sa.String(length=200), nullable=False),
    sa.Column('workflow_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['workflow_id'], ['workflow.id'], name='fk_workflow_permission_workflow_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_workflow_permission_workflow_id'), 'workflow_permission', ['workflow_id'], unique=False)
    op.create_table('workflow_variable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('label', sa.String(length=200), nullable=True),
    sa.Column('description', mysql.LONGTEXT(), nullable=True),
    sa.Column('type', sa.Enum('BINARY', 'CHARACTER', 'DATE', 'DATETIME', 'DECIMAL', 'DOUBLE', 'ENUM', 'FILE', 'FLOAT', 'INTEGER', 'LAT_LONG', 'LONG', 'TEXT', 'TIME', 'TIMESTAMP', 'VECTOR', name='DataTypeEnumType'), nullable=False),
    sa.Column('multiplicity', sa.Integer(), nullable=False),
    sa.Column('suggested_widget', sa.String(length=200), nullable=True),
    sa.Column('default_value', mysql.LONGTEXT(), nullable=True),
    sa.Column('parameters', mysql.LONGTEXT(), nullable=True),
    sa.Column('workflow_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['workflow_id'], ['workflow.id'], name='fk_workflow_variable_workflow_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_workflow_variable_workflow_id'), 'workflow_variable', ['workflow_id'], unique=False)
    op.create_table('flow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_port', sa.Integer(), nullable=False),
    sa.Column('target_port', sa.Integer(), nullable=False),
    sa.Column('source_port_name', sa.String(length=200), nullable=True),
    sa.Column('target_port_name', sa.String(length=200), nullable=True),
    sa.Column('environment', sa.Enum('DESIGN', 'DEPLOYMENT', name='DiagramEnvironmentEnumType'), nullable=False),
    sa.Column('source_id', sa.String(length=250), nullable=False),
    sa.Column('target_id', sa.String(length=250), nullable=False),
    sa.Column('workflow_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['source_id'], ['task.id'], name='fk_flow_source_id'),
    sa.ForeignKeyConstraint(['target_id'], ['task.id'], name='fk_flow_target_id'),
    sa.ForeignKeyConstraint(['workflow_id'], ['workflow.id'], name='fk_flow_workflow_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_flow_source_id'), 'flow', ['source_id'], unique=False)
    op.create_index(op.f('ix_flow_target_id'), 'flow', ['target_id'], unique=False)
    op.create_index(op.f('ix_flow_workflow_id'), 'flow', ['workflow_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_flow_workflow_id'), table_name='flow')
    op.drop_index(op.f('ix_flow_target_id'), table_name='flow')
    op.drop_index(op.f('ix_flow_source_id'), table_name='flow')
    op.drop_table('flow')
    op.drop_index(op.f('ix_workflow_variable_workflow_id'), table_name='workflow_variable')
    op.drop_table('workflow_variable')
    op.drop_index(op.f('ix_workflow_permission_workflow_id'), table_name='workflow_permission')
    op.drop_table('workflow_permission')
    op.drop_index(op.f('ix_workflow_history_workflow_id'), table_name='workflow_history')
    op.drop_table('workflow_history')
    op.drop_index(op.f('ix_task_workflow_id'), table_name='task')
    op.drop_index(op.f('ix_task_operation_id'), table_name='task')
    op.drop_table('task')
    op.drop_index(op.f('ix_workflow_subset_id'), table_name='workflow')
    op.drop_index(op.f('ix_workflow_platform_id'), table_name='workflow')
    op.drop_table('workflow')
    op.drop_index(op.f('ix_role_operation_subset_subset_id'), table_name='role_operation_subset')
    op.drop_table('role_operation_subset')
    op.drop_index(op.f('ix_operation_subset_operation_operation_subset_id'), table_name='operation_subset_operation')
    op.drop_index(op.f('ix_operation_subset_operation_operation_id'), table_name='operation_subset_operation')
    op.drop_table('operation_subset_operation')
    op.drop_table('operation_port_translation')
    op.drop_index(op.f('ix_operation_port_interface_operation_port_operation_port_id'), table_name='operation_port_interface_operation_port')
    op.drop_index(op.f('ix_operation_port_interface_operation_port_operation_port_interface_id'), table_name='operation_port_interface_operation_port')
    op.drop_table('operation_port_interface_operation_port')
    op.drop_table('operation_form_field_translation')
    op.drop_table('platform_translation')
    op.drop_index(op.f('ix_platform_plugin_platform_id'), table_name='platform_plugin')
    op.drop_table('platform_plugin')
    op.drop_index(op.f('ix_platform_form_platform_id'), table_name='platform_form')
    op.drop_index(op.f('ix_platform_form_operation_form_id'), table_name='platform_form')
    op.drop_table('platform_form')
    op.drop_table('operation_translation')
    op.drop_index(op.f('ix_operation_subset_platform_id'), table_name='operation_subset')
    op.drop_table('operation_subset')
    op.drop_index(op.f('ix_operation_script_operation_id'), table_name='operation_script')
    op.drop_table('operation_script')
    op.drop_table('operation_port_interface_translation')
    op.drop_index(op.f('ix_operation_port_operation_id'), table_name='operation_port')
    op.drop_table('operation_port')
    op.drop_index(op.f('ix_operation_platform_platform_id'), table_name='operation_platform')
    op.drop_index(op.f('ix_operation_platform_operation_id'), table_name='operation_platform')
    op.drop_table('operation_platform')
    op.drop_index(op.f('ix_operation_operation_form_operation_id'), table_name='operation_operation_form')
    op.drop_index(op.f('ix_operation_operation_form_operation_form_id'), table_name='operation_operation_form')
    op.drop_table('operation_operation_form')
    op.drop_table('operation_form_translation')
    op.drop_index(op.f('ix_operation_form_field_form_id'), table_name='operation_form_field')
    op.drop_table('operation_form_field')
    op.drop_table('operation_category_translation')
    op.drop_index(op.f('ix_operation_category_operation_operation_id'), table_name='operation_category_operation')
    op.drop_index(op.f('ix_operation_category_operation_operation_category_id'), table_name='operation_category_operation')
    op.drop_table('operation_category_operation')
    op.drop_table('task_group')
    op.drop_table('source_code')
    op.drop_table('platform')
    op.drop_table('operation_port_interface')
    op.drop_table('operation_form')
    op.drop_table('operation_category')
    op.drop_table('operation')
    op.drop_table('application')
    # ### end Alembic commands ###
