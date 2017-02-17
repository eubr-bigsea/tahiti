"""empty message

Revision ID: f654bbef525d
Revises: 
Create Date: 2017-02-17 13:19:31.548047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f654bbef525d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('type', sa.Enum('__module__', '__doc__', 'SPARK_APPLICATION', 'SPARK_CODE_FUNCTION', name='ApplicationTypeEnumType'), nullable=False),
    sa.Column('execution_parameters', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=200), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('type', sa.Enum('ACTION', '__module__', 'SHUFFLE', 'TRANSFORMATION', '__doc__', name='OperationTypeEnumType'), nullable=False),
    sa.Column('icon', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=200), nullable=False),
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
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation_category_operation',
    sa.Column('operation_id', sa.Integer(), nullable=True),
    sa.Column('operation_category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['operation_category_id'], ['operation_category.id'], ),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], )
    )
    op.create_table('operation_category_translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation_category.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('operation_form_field',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('type', sa.Enum('__module__', 'ENUM', 'LAT_LONG', 'DOUBLE', 'DECIMAL', 'FLOAT', 'CHARACTER', 'LONG', 'DATETIME', 'VECTOR', 'TEXT', 'TIME', 'DATE', 'INTEGER', 'TIMESTAMP', '__doc__', name='DataTypeEnumType'), nullable=False),
    sa.Column('required', sa.Boolean(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('default', sa.Text(), nullable=False),
    sa.Column('suggested_widget', sa.String(length=200), nullable=True),
    sa.Column('values_url', sa.String(length=200), nullable=True),
    sa.Column('values', sa.Text(), nullable=True),
    sa.Column('scope', sa.Enum('BOTH', '__module__', 'EXECUTION', 'DESIGN', '__doc__', name='OperationFieldScopeEnumType'), nullable=False),
    sa.Column('form_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['form_id'], ['operation_form.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation_form_translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation_form.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('operation_operation_form',
    sa.Column('operation_id', sa.Integer(), nullable=True),
    sa.Column('operation_form_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['operation_form_id'], ['operation_form.id'], ),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], )
    )
    op.create_table('operation_platform',
    sa.Column('operation_id', sa.Integer(), nullable=True),
    sa.Column('platform_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], ),
    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], )
    )
    op.create_table('operation_port',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('INPUT', '__module__', '__doc__', 'OUTPUT', name='OperationPortTypeEnumType'), nullable=False),
    sa.Column('tags', sa.Text(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('multiplicity', sa.Enum('MANY', '__module__', '__doc__', 'ONE', name='OperationPortMultiplicityEnumType'), nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation_port_interface_translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation_port_interface.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('operation_translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.Column('description', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('platform_translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.Column('description', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['platform.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('workflow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_login', sa.String(length=50), nullable=False),
    sa.Column('user_name', sa.String(length=200), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=1000), nullable=True),
    sa.Column('platform_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation_form_field_translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('label', sa.Unicode(length=200), nullable=True),
    sa.Column('help', sa.UnicodeText(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation_form_field.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('operation_port_interface_operation_port',
    sa.Column('operation_port_id', sa.Integer(), nullable=True),
    sa.Column('operation_port_interface_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['operation_port_id'], ['operation_port.id'], ),
    sa.ForeignKeyConstraint(['operation_port_interface_id'], ['operation_port_interface.id'], )
    )
    op.create_table('operation_port_translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('locale', sa.String(length=10), nullable=False),
    sa.Column('name', sa.Unicode(length=200), nullable=True),
    sa.Column('description', sa.Unicode(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['operation_port.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'locale')
    )
    op.create_table('task',
    sa.Column('id', sa.String(length=250), autoincrement=False, nullable=False),
    sa.Column('left', sa.Integer(), nullable=False),
    sa.Column('top', sa.Integer(), nullable=False),
    sa.Column('z_index', sa.Integer(), nullable=False),
    sa.Column('forms', sa.Text(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('workflow_id', sa.Integer(), nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], ),
    sa.ForeignKeyConstraint(['workflow_id'], ['workflow.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_port', sa.Integer(), nullable=False),
    sa.Column('target_port', sa.Integer(), nullable=False),
    sa.Column('source_port_name', sa.String(length=200), nullable=False),
    sa.Column('target_port_name', sa.String(length=200), nullable=False),
    sa.Column('source_id', sa.String(length=250), nullable=False),
    sa.Column('target_id', sa.String(length=250), nullable=False),
    sa.Column('workflow_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['source_id'], ['task.id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['task.id'], ),
    sa.ForeignKeyConstraint(['workflow_id'], ['workflow.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flow')
    op.drop_table('task')
    op.drop_table('operation_port_translation')
    op.drop_table('operation_port_interface_operation_port')
    op.drop_table('operation_form_field_translation')
    op.drop_table('workflow')
    op.drop_table('platform_translation')
    op.drop_table('operation_translation')
    op.drop_table('operation_port_interface_translation')
    op.drop_table('operation_port')
    op.drop_table('operation_platform')
    op.drop_table('operation_operation_form')
    op.drop_table('operation_form_translation')
    op.drop_table('operation_form_field')
    op.drop_table('operation_category_translation')
    op.drop_table('operation_category_operation')
    op.drop_table('platform')
    op.drop_table('operation_port_interface')
    op.drop_table('operation_form')
    op.drop_table('operation_category')
    op.drop_table('operation')
    op.drop_table('application')
    # ### end Alembic commands ###
