"""Changes sept 2021

Revision ID: a6aa24bf8d35 
Revises: a6b3c5df78e8
"""
import json
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
from tahiti.migration_utils import (downgrade_actions, upgrade_actions,
        is_mysql, is_psql, is_sqlite, get_psql_enum_alter_commands)

# revision identifiers, used by Alembic.
revision = 'a6aa24bf8d35'
down_revision = 'a6b3c5df78e8'
branch_labels = None
depends_on = None

def _execute(conn, cmd):
    if isinstance(cmd, str):
        conn.execute(cmd)
    elif isinstance(cmd, list):
        for row in cmd:
            conn.execute(row)
    else: # it's a method
        cmd(conn)

def add_workflow_types(conn):
    values = ['WORKFLOW','SYSTEM_TEMPLATE','SUB_FLOW','USER_TEMPLATE']
    new_types = ['DATA_EXPLORER', 'MODEL_BUILDER', 'VIS_BUILDER']
    def get_psql_commands():

        return get_psql_enum_alter_commands(['workflow'], ['type'],
                       'WorkflowTypeEnumType', values+new_types, 'WORKFLOW')

    types = [f"'{x}'" for x in (values + new_types)]
    if is_mysql():
        conn.execute(text(f"""
            ALTER TABLE workflow CHANGE `type` `type`
             enum({', '.join(types)})
                 CHARSET utf8 COLLATE utf8_unicode_ci NOT NULL;"""
         ))
    elif is_psql():
        change_enum = get_psql_commands()
        upgrade_actions([[change_enum]])

def remove_workflow_types(conn):
    values = ['WORKFLOW','SYSTEM_TEMPLATE','SUB_FLOW','USER_TEMPLATE']
    def get_psql_commands():
        return get_psql_enum_alter_commands(['workflow'], ['type'],
                       'WorkflowTypeEnumType', values, 
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
        upgrade_actions([[get_psql_commands()]])

# -------------------------------------------------------

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()
    handle_invalid = json.dumps([
            {"en": "Throw error", "pt": "Falhar com erro", "key": "error"},
            {"en": "Skip invalid row", "pt": "Ignorar registro com problema", "key": "skip"},
            {"en": "Keep row", "pt": "Manter o registro", "key": "keep"},
        ])
    commands = [
	add_workflow_types,
        
        '''UPDATE operation_form_field
        SET `values`= NULL 
        WHERE id in (348, 352, 356)''' if is_mysql()
        else 
        '''UPDATE operation_form_field
        SET "values"= NULL 
        WHERE id in (348, 352, 356)'''

        ,
        
        '''UPDATE operation_form_field 
        SET suggested_widget = 'dropdown'
        WHERE id = 210''',

        f'''insert into operation_form_field values(
        609, 'handle_invalid', 'TEXT', false, 3, 
        'keep', 'dropdown', NULL, 
        '{handle_invalid}', 
        'EXECUTION', NULL, true, 51)''',

        '''INSERT into operation_form_field_translation
        VALUES(609, 'pt', 'Tratar dados inválidos (nulos)',
        'Como tratar os dados inválidos.') ''',

        '''INSERT INTO operation_form_field_translation
        VALUES(609, 'en', 'Invalid data handling(null)',
        'How to handle invalid data (nulls).') ''',
    ]
    try:
        for cmd in commands:
            _execute(conn, cmd)
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()

    # Remove it if your DB doesn't support disabling FK checks
    if is_psql():
        conn.execute('SET CONSTRAINTS ALL DEFERRED')
    else:
        conn.execute('SET FOREIGN_KEY_CHECKS=0;')

    commands = [
        # remove_workflow_types,
        '''UPDATE operation_form_field
        SET `values`= '{"multiple": false}' 
        WHERE id in (348, 356)''' if is_mysql() else

        '''UPDATE operation_form_field
        SET "values"= '{"multiple": false}' 
        WHERE id in (348, 356)''' 
        ,

        '''UPDATE operation_form_field 
        SET suggested_widget = 'dropdown'
        WHERE id = 210''',

        '''DELETE FROM operation_form_field WHERE id = 609''',
        '''DELETE FROM operation_form_field_translation 
           WHERE id = 609 AND locale = 'pt' ''',

        '''DELETE FROM operation_form_field_translation 
           WHERE id = 609 AND locale = 'en' ''',
    ]

    try:
        for cmd in reversed(commands):
            _execute(conn, cmd)
    except:
        session.rollback()
        raise
    # Remove it if your DB doesn't support disabling FK checks
    if is_psql():
        conn.execute('SET CONSTRAINTS ALL IMMEDIATE')
    else:
        conn.execute('SET FOREIGN_KEY_CHECKS=1;')
    session.commit()
