"""add field to save model

Revision ID: a0d6c6699b69 
Revises: a85dce88d899
"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
import json
from tahiti.migration_utils import is_psql

# revision identifiers, used by Alembic.
revision = 'a0d6c6699b69'
down_revision = 'a85dce88d899'
branch_labels = None
depends_on = None

BASE_FORM_FIELD = 206
BASE_PORT = 16

def _insert_operation_form_field(conn):
    tb = table('operation_form_field',
                column('id', Integer), 
                column('name', String), 
                column('type', String), 
                column('required', Boolean), 
                column('order', Integer), 
                column('default', String), 
                column('suggested_widget', String), 
                column('values_url', String), 
                column('values', String), 
                column('scope', String), 
                column('enable_conditions', String), 
                column('editable', Boolean), 
                column('form_id', Integer))
    columns = [c.name for c in tb.columns]
    formats = json.dumps([
        {'key': 'DEFAULT', 'en': 'Default for the platform', 'pt': 'Formato padrão para a plataforma'},
        {'key': 'MLEAP', 'en': 'MLeap (can be deployed)', 'pt': 'MLeap (pode ser implantado)'},
    ])
    data = [
      [BASE_FORM_FIELD + 1, 'format', 'TEXT', 1, 4, 'DEFAULT', 'dropdown', None, formats, 'DESIGN', None, 1, 100]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 1)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM_FIELD + 1, 'pt', 'Formato', 'Formato para salvar o modelo. O formato MLeap permite implantar o modelo em produção pelo Lemonade.'],
      [BASE_FORM_FIELD + 1, 'en', 'Format', 'Format used to save the model. MLeap format allows to deploay a model into production using Lemonade.'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute(
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 1)

def _insert_operation_port(conn):
    tb = table('operation_port',
                column('id', Integer), 
                column('slug', String), 
                column('type', String), 
                column('tags', String), 
                column('order', Integer), 
                column('multiplicity', String), 
                column('operation_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_PORT + 1, 'input data', 'INPUT', None, 0, 'ONE', 39]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port(conn):
    conn.execute(
        'DELETE from operation_port WHERE id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 1)

def _insert_operation_port_translation(conn):
    tb = table('operation_port_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_PORT + 1, 'pt', 'dados de entrada', 'Dados de entrada'],
      [BASE_PORT + 1, 'en', 'input data', 'Input data'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_translation(conn):
    conn.execute(
        'DELETE from operation_port_translation WHERE id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 1)

def _insert_operation_port_interface_operation_port(conn):
    tb = table('operation_port_interface_operation_port',
                column('operation_port_interface_id', Integer), 
                column('operation_port_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [1, BASE_PORT + 1],
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_interface_operation_port(conn):
    conn.execute('DELETE FROM operation_port_interface_operation_port WHERE operation_port_id = %s',
            BASE_PORT + 1)

def _execute(conn, cmd):
    if isinstance(cmd, str):
        conn.execute(cmd)
    elif isinstance(cmd, list):
        for row in cmd:
            conn.execute(row)
    else: # it's a method
        cmd(conn)

# -------------------------------------------------------

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()
    commands = [
        _insert_operation_form_field,
        _insert_operation_form_field_translation,
        _insert_operation_port,
        _insert_operation_port_translation,
        _insert_operation_port_interface_operation_port,
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
        _delete_operation_form_field,
        _delete_operation_form_field_translation,
        _delete_operation_port,
        _delete_operation_port_translation,
        _delete_operation_port_interface_operation_port,
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
