"""add new fields to pipeline

Revision ID: 843451bc6ee4
Revises: a5215429bcf2
Create Date: 2023-12-11 09:21:15.637102

"""
from alembic import op, context
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import sqlalchemy as sa

from tahiti.migration_utils import (downgrade_actions, upgrade_actions,
        is_mysql, is_psql, is_sqlite, get_psql_enum_alter_commands)

# revision identifiers, used by Alembic.
revision = '843451bc6ee4'
down_revision = 'a5215429bcf2'
branch_labels = None
depends_on = None

def add_workflow_types(conn):
    values = ['WORKFLOW','SYSTEM_TEMPLATE','SUB_FLOW','USER_TEMPLATE',
                'DATA_EXPLORER', 'MODEL_BUILDER', 'VIS_BUILDER']
    new_types = ['SQL']
    def get_psql_commands():

        return get_psql_enum_alter_commands(['workflow'], ['type'],
                       'StorageTypeEnumType', values, *new_types)

    types = [f"'{x}'" for x in (values + new_types)]
    if is_mysql():
        conn.execute(text(f"""
            ALTER TABLE workflow CHANGE `type` `type`
             enum({', '.join(types)})
                 CHARSET utf8 COLLATE utf8_unicode_ci NOT NULL;"""
         ))
    elif is_psql():
        upgrade_actions(get_commands())

def remove_workflow_types(conn):
    values = ['WORKFLOW','SYSTEM_TEMPLATE','SUB_FLOW','USER_TEMPLATE',
                'DATA_EXPLORER', 'MODEL_BUILDER', 'VIS_BUILDER']
    def get_psql_commands():
        return get_psql_enum_alter_commands(['workflow'], ['type'],
                       'StorageTypeEnumType', values, 
			'DATA_EXPLORER', 'MODEL_EXPLORER', 
			'VIS_EXPLORER'),
    types = [f"'{x}'" for x in values]
    if is_mysql():
        conn.execute(text(f"""
            ALTER TABLE workflow CHANGE `type` `type`
             enum({', '.join(types)})
                 CHARSET utf8 COLLATE utf8_unicode_ci NOT NULL;"""
         ))
    elif is_psql():
        upgrade_actions(get_commands())


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pipeline', sa.Column('execution_window', sa.Integer(), nullable=True))
    op.add_column('pipeline', sa.Column('variables', sa.String(length=1000), nullable=True))
    op.add_column('pipeline', sa.Column('preferred_cluster_id', sa.Integer(), nullable=True))
    op.add_column('workflow', sa.Column('pipeline_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_workflow_pipeline_id'), 'workflow', ['pipeline_id'], unique=False)

    with op.batch_alter_table("workflow") as batch_op:
        batch_op.create_foreign_key('fk_workflow_pipeline_id', 'pipeline', ['pipeline_id'], ['id'])
    # ### end Alembic commands ###

    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()
    add_workflow_types(conn)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_workflow_pipeline_id', 'workflow', type_='foreignkey')
    op.drop_index(op.f('ix_workflow_pipeline_id'), table_name='workflow')
    op.drop_column('workflow', 'pipeline_id')
    op.drop_column('pipeline', 'preferred_cluster_id')
    op.drop_column('pipeline', 'variables')
    op.drop_column('pipeline', 'execution_window')
    # ### end Alembic commands ###

    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()
    remove_workflow_types(conn)
