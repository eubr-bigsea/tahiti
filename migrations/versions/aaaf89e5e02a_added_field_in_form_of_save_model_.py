"""Added field in form of save model operation

Revision ID: aaaf89e5e02a
Revises: 4c1a9c14d928
Create Date: 2023-01-05 18:58:56.935830

"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText

# revision identifiers, used by Alembic.
revision = 'aaaf89e5e02a'
down_revision = '4c1a9c14d928'
branch_labels = None
depends_on = None


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

    data = [
        [10004, 'description', 'TEXT', True, 1, None, 'text', None, None, 'EXECUTION', None, 1, 100]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_form_field(conn):
    conn.execute('DELETE from operation_form_field WHERE id = %s', 10004)


def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
               column('id', Integer),
               column('locale', String),
               column('label', String),
               column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
        [10004, 'pt', 'Descrição', 'Descrição sobre a fonte de dados.'],
        [10004, 'en', 'Description', 'Description about datasource']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute('DELETE from operation_form_field_translation WHERE id = %s', 10004)


    # -------------------------------------------------------

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
    conn.execute('SET FOREIGN_KEY_CHECKS=0;')
    commands = [
        _delete_operation_form_field,
        _delete_operation_form_field_translation,
    ]

    try:
        for cmd in reversed(commands):
            _execute(conn, cmd)

    except:
        session.rollback()
        raise
    # Remove it if your DB doesn't support disabling FK checks
    conn.execute('SET FOREIGN_KEY_CHECKS=1;')
    session.commit()

