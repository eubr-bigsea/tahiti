"""add decision tree regressor

Revision ID: a8642d0d1aa3 
Revises: a0d6c6699b69
"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText
from tahiti.migration_utils import is_psql

# revision identifiers, used by Alembic.
revision = 'a8642d0d1aa3'
down_revision = 'a0d6c6699b69'
branch_labels = None
depends_on = None

# --------------------------------------------------------------
# ATENTION: You must revise this auto-generated code.
# Please, review offsets and commands before running a migration
# and optionally, perform a database backup. If everything is 
# OK, remove this comment.
# --------------------------------------------------------------

BASE_FORM_FIELD = 138
BASE_PORT = 348
DECISION_TREE_REG = 61

def _insert_operation(conn):
    tb = table('operation',
                column('id', Integer), 
                column('slug', String), 
                column('enabled', Boolean), 
                column('type', String), 
                column('icon', String), 
                column('css_class', String), 
                column('doc_link', String))
    columns = [c.name for c in tb.columns]
    data = [
      [DECISION_TREE_REG, 'decision-tree-regression-model', 1, 'TRANSFORMATION', '', '', '']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation(conn):
    conn.execute(
        'DELETE from operation WHERE id BETWEEN %s AND %s', DECISION_TREE_REG, DECISION_TREE_REG)

def _insert_operation_translation(conn):
    tb = table('operation_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String), )
    columns = [c.name for c in tb.columns]
    data = [
      [DECISION_TREE_REG, 'pt', 'Regressor árvore de decisão', 'Regressor árvore de decisão'], 
      [DECISION_TREE_REG, 'en', 'Decision tree regressor', 'Decision tree regressor'], 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_translation(conn):
    conn.execute(
        'DELETE from operation_translation WHERE id = %s', DECISION_TREE_REG) 

def _insert_operation_script(conn):
    tb = table('operation_script',
                column('id', Integer), 
                column('type', String), 
                column('enabled', Boolean), 
                column('body', String), 
                column('operation_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [78, 'JS_CLIENT', 1, 'copyInputAddField(task, "prediction", false, null);', DECISION_TREE_REG], 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_script(conn):
    conn.execute(
        'DELETE from operation_script WHERE operation_id BETWEEN %s AND %s', 
        DECISION_TREE_REG, DECISION_TREE_REG)

def _insert_operation_form(conn):
    tb = table('operation_form',
                column('id', Integer), 
                column('enabled', Boolean), 
                column('order', Integer), 
                column('category', String))
    columns = [c.name for c in tb.columns]
    data = [
      [29, 1, 1, 'execution']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form(conn):
    conn.execute(
        'DELETE from operation_form WHERE id = %s', 29), 

def _insert_operation_form_translation(conn):
    tb = table('operation_form_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [29, 'pt', 'Execução'], 
      [29, 'en', 'Execution'], 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_translation(conn):
    conn.execute(
        'DELETE from operation_form_translation WHERE id = %s', 29)

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
      [BASE_FORM_FIELD + 1, 'max_depth', 'INTEGER', 0, 7, None, 'integer', None, None, 'DESIGN', None, 1, 29], 
      [BASE_FORM_FIELD + 2, 'min_instance', 'INTEGER', 0, 8, None, 'integer', None, None, 'DESIGN', None, 1, 29], 
      [BASE_FORM_FIELD + 3, 'min_info_gain', 'FLOAT', 0, 9, None, 'decimal', None, None, 'DESIGN', None, 1, 29], 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 10)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM_FIELD + 1, 'pt', 'Profundidade máxima', 'Profundidade máxima.'], 
      [BASE_FORM_FIELD + 2, 'pt', 'Mínimo de instâncias por nó', 'Mínimo de instâncias por nó.'], 
      [BASE_FORM_FIELD + 3, 'pt', 'Ganho de informação (info gain) mínimo', 'Ganho de informação (info gain) mínimo.'], 
      [BASE_FORM_FIELD + 1, 'en', 'Max. depth', 'Max. depth.'], 
      [BASE_FORM_FIELD + 2, 'en', 'Min instances per node', 'Min instances per node.'], 
      [BASE_FORM_FIELD + 3, 'en', 'Min. info gain', 'Min. info gain.'], 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute(
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 3)

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
      [BASE_PORT + 1, 'train input data', 'INPUT', None, 1, 'ONE', DECISION_TREE_REG], 
      [BASE_PORT + 2, 'output data', 'OUTPUT', None, 1, 'MANY', DECISION_TREE_REG], 
      [BASE_PORT + 3, 'model', 'OUTPUT', None, 2, 'MANY', DECISION_TREE_REG], 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port(conn):
    conn.execute(
        'DELETE from operation_port WHERE id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 3)

def _insert_operation_port_translation(conn):
    tb = table('operation_port_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_PORT + 1, 'pt', 'dados de entrada', 'Dados de entrada'], 
      [BASE_PORT + 2, 'pt', 'dados de saída', 'Dados de saída'], 
      [BASE_PORT + 3, 'pt', 'modelo', 'Modelo.'], 
      [BASE_PORT + 1, 'en', 'input data', 'Input data.'], 
      [BASE_PORT + 2, 'en', 'output data', 'Output data.'], 
      [BASE_PORT + 3, 'en', 'model', 'Model.'], 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_translation(conn):
    conn.execute(
        'DELETE from operation_port_translation WHERE id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 3)

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
                column('operation_id', Integer), 
                column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [DECISION_TREE_REG, 8],
        [21, 8]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_operation(conn):
    conn.execute('delete from operation_category_operation WHERE operation_id = %s',
            DECISION_TREE_REG)

def _insert_operation_operation_form(conn):
    tb = table('operation_operation_form',
                column('operation_id', Integer), 
                column('operation_form_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [DECISION_TREE_REG, 29],
        [DECISION_TREE_REG, 41],
        [DECISION_TREE_REG, 110],
        [DECISION_TREE_REG, 110],
        [DECISION_TREE_REG, 102],
        [DECISION_TREE_REG, 132],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_operation_form(conn):
    conn.execute('DELETE FROM operation_operation_form WHERE operation_id = %s', DECISION_TREE_REG)

def _insert_operation_platform(conn):
    tb = table('operation_platform',
                column('operation_id', Integer), 
                column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [DECISION_TREE_REG, 1]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_platform(conn):
    conn.execute('DELETE from operation_platform where operation_id = %s', DECISION_TREE_REG)

def _insert_operation_port_interface_operation_port(conn):
    tb = table('operation_port_interface_operation_port',
                column('operation_port_interface_id', Integer), 
                column('operation_port_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [1, BASE_PORT + 1],
        [1, BASE_PORT + 2],
        [2, BASE_PORT + 3],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_interface_operation_port(conn):
    conn.execute(
        '''delete from operation_port_interface_operation_port 
            where operation_port_id between %s and %s''',
            BASE_PORT + 1, BASE_PORT + 3)


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
        _insert_operation,
        _insert_operation_translation,
        _insert_operation_script,
        _insert_operation_form,
        _insert_operation_form_translation,
        _insert_operation_form_field,
        _insert_operation_form_field_translation,
        _insert_operation_port,
        _insert_operation_port_translation,
        _insert_operation_category_operation,
        _insert_operation_operation_form,
        _insert_operation_platform,
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
        _delete_operation,
        _delete_operation_translation,
        _delete_operation_script,
        _delete_operation_form,
        _delete_operation_form_translation,
        _delete_operation_form_field,
        _delete_operation_form_field_translation,
        _delete_operation_port,
        _delete_operation_port_translation,
        _delete_operation_category_operation,
        _delete_operation_operation_form,
        _delete_operation_platform,
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
