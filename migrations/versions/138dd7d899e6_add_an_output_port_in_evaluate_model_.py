"""add an output port in evaluate model operation

Revision ID: 138dd7d899e6
Revises: 5a2676b63d2d
Create Date: 2023-02-07 20:04:26.046267

"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText

# revision identifiers, used by Alembic.
revision = '138dd7d899e6'
down_revision = '5a2676b63d2d'
branch_labels = None
depends_on = None


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
        [4210, 'model_out_port', 'OUTPUT', None, 4, 'MANY', 4017]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_port(conn):
    conn.execute('DELETE from operation_port WHERE id = %s', 4210)


def _insert_operation_port_translation(conn):
    tb = table('operation_port_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String),
               column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
        [4210, 'pt', 'modelo', 'Saída do Modelo.'],
        [4210, 'en', 'model', 'Model Output.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_port_translation(conn):
    conn.execute('DELETE from operation_port_translation WHERE id = %s', 4210)


def _insert_operation_port_interface_operation_port(conn):
    tb = table('operation_port_interface_operation_port',
               column('operation_port_interface_id', Integer),
               column('operation_port_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [4210, 1]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_interface_operation_port(conn):
    conn.execute(
        'DELETE from operation_port_interface_operation_port WHERE operation_port_id = %s', 4210)


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
        _insert_operation_port,
        _insert_operation_port_translation,
        # _insert_operation_port_interface_operation_port,
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
        _delete_operation_port,
        _delete_operation_port_translation,
        # _delete_operation_port_interface_operation_port,
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
