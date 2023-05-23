"""protoboard plataform test

Revision ID: a245d1ca5643 
Revises: a237518ec5e1
"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText

# revision identifiers, used by Alembic.
revision = 'a245d1ca5643'
down_revision = 'a237518ec5e1'
branch_labels = None
depends_on = None

# --------------------------------------------------------------
# ATENTION: You must revise this auto-generated code.
# Please, review offsets and commands before running a migration
# and optionally, perform a database backup. If everything is 
# OK, remove this comment.
# --------------------------------------------------------------

BASE_PLATFORM = 10000
BASE_OP = 10000
BASE_CATEGORY = 10000
BASE_FORM = 10000
BASE_FORM_FIELD = 10000
BASE_PORT = 10000

def _insert_platform(conn):
    tb = table('platform',
               column('id', Integer),
               column('slug', String),
               column('enabled', Boolean),
               column('icon', String),
               column('version', String),
               column('plugin', Boolean))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_PLATFORM + 1, 'protoboard', 1, 'icon', 'version', 0]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_platform(conn):
    conn.execute(
        'DELETE from platform WHERE id BETWEEN %s AND %s',
        BASE_PLATFORM + 1, BASE_PLATFORM + 1)

def _insert_platform_translation(conn):
    tb = table('platform_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String),
               column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_PLATFORM + 1, 'pt', 'Placa de ensaio', 'Placa de ensaio'],
        [BASE_PLATFORM + 1, 'en', 'Protoboard', 'Protoboard']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_platform_translation(conn):
    conn.execute(
        'DELETE from platform_translation WHERE id BETWEEN %s AND %s',
        BASE_PLATFORM + 1, BASE_PLATFORM + 1)

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
        [BASE_OP + 1, 'fonte-5v', 1, 'TRANSFORMATION', '', '', ''],
        [BASE_OP + 2, 'terra', 1, 'TRANSFORMATION', '', '', ''],
        [BASE_OP + 3, 'and-7408', 1, 'TRANSFORMATION', '', '', ''],
        [BASE_OP + 4, 'led', 1, 'TRANSFORMATION', '', '', '']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation(conn):
    conn.execute(
        'DELETE from operation WHERE id BETWEEN %s AND %s',
        BASE_OP + 1, BASE_OP + 4)

def _insert_operation_translation(conn):
    tb = table('operation_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String),
               column('description', String),
               column('label_format', String))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_OP + 1, 'pt', 'Fonte 5v', 'Conectar fonte 5v no protoboard. '],
        [BASE_OP + 1, 'en', 'Source 5v', 'Connect source 5v on protoboard. '],
        [BASE_OP + 2, 'pt', 'Terra', 'Conectar terra no protoboard. '],
        [BASE_OP + 2, 'en', 'Ground', 'Connect ground on protoboard. '],
        [BASE_OP + 3, 'pt', '7408 AND', 'Operação AND.'],
        [BASE_OP + 3, 'en', '7408 AND', 'AND Operation.'],
        [BASE_OP + 4, 'pt', 'Led', 'Conectar led no protoboard.'],
        [BASE_OP + 4, 'en', 'Led', 'Connect led on protoboard.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_translation(conn):
    conn.execute(
        'DELETE from operation_translation WHERE id BETWEEN %s AND %s',
        BASE_OP + 1, BASE_OP + 4)

def _insert_operation_script(conn):
    tb = table('operation_script',
               column('id', Integer),
               column('type', String),
               column('enabled', Boolean),
               column('body', String),
               column('operation_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [None, 'JS_CLIENT', 1, 'copyInput(task)', BASE_OP + 1],
        [None, 'JS_CLIENT', 1, 'copyInput(task)', BASE_OP + 2],
        [None, 'JS_CLIENT', 1, 'copyInput(task)', BASE_OP + 3],
        [None, 'JS_CLIENT', 1, 'copyInput(task)', BASE_OP + 4]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_script(conn):
    conn.execute(
        'DELETE from operation_script WHERE id BETWEEN %s AND %s',
        BASE_OP + 1, BASE_OP + 4)

def _insert_operation_category(conn):
    tb = table('operation_category',
               column('id', Integer),
               column('type', String),
               column('subtype', String),
               column('order', Integer),
               column('default_order', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_CATEGORY + 1, 'group', None, 0, 0],
        [BASE_CATEGORY + 2, 'subgroup', None, 0, 0]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category(conn):
    conn.execute(
        'DELETE from operation_category WHERE id BETWEEN %s AND %s',
        BASE_CATEGORY + 1, BASE_CATEGORY + 2)

def _insert_operation_category_translation(conn):
    tb = table('operation_category_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_CATEGORY + 1, 'pt', 'Eletronicos'],
        [BASE_CATEGORY + 2, 'pt', 'Circuitos Integrados'],
        [BASE_CATEGORY + 1, 'en', 'Eletronics'],
        [BASE_CATEGORY + 2, 'en', 'Chips']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_translation(conn):
    conn.execute(
        'DELETE from operation_category_translation WHERE id BETWEEN %s AND %s',
        BASE_CATEGORY + 1, BASE_CATEGORY + 2)

def _insert_operation_form(conn):
    tb = table('operation_form',
               column('id', Integer),
               column('enabled', Boolean),
               column('order', Integer),
               column('category', String))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_FORM + 1, 1, 1, 'execution'],
        [BASE_FORM + 2, 1, 1, 'execution'],
        [BASE_FORM + 3, 1, 1, 'execution'],
        [BASE_FORM + 4, 1, 1, 'execution']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form(conn):
    conn.execute(
        'DELETE from operation_form WHERE id BETWEEN %s AND %s',
        BASE_FORM + 1, BASE_FORM + 4)

def _insert_operation_form_translation(conn):
    tb = table('operation_form_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_FORM + 1, 'pt', 'Execução'],
        [BASE_FORM + 1, 'en', 'Execution'],
        [BASE_FORM + 2, 'pt', 'Execução'],
        [BASE_FORM + 2, 'en', 'Execution'],
        [BASE_FORM + 3, 'pt', 'Execução'],
        [BASE_FORM + 3, 'en', 'Execution'],
        [BASE_FORM + 4, 'pt', 'Execução'],
        [BASE_FORM + 4, 'en', 'Execution']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_translation(conn):
    conn.execute(
        'DELETE from operation_form_translation WHERE id BETWEEN %s AND %s',
        BASE_FORM + 1, BASE_FORM + 4)

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

    colors = """[
    {"key": "#FFFF00", "pt": "Amarelo", "value": "Amarelo", "en": "Yellow"},
    {"key": "#0000FF", "pt": "Azul", "value": "Azul", "en": "Blue"},
    {"key": "#008000", "pt": "Verde", "value": "Verde", "en": "Green"},
    {"key": "#FF0000", "pt": "Vermelho", "value": "Vermelho", "en": "Red"}
    ]"""

    data = [
        [BASE_FORM_FIELD + 1, 'voltage', 'INTEGER', 1, 1, '1', 'checkbox', None, None, 'DESIGN', None, 1, BASE_FORM + 1],
        [BASE_FORM_FIELD + 2, 'color', 'TEXT', 1, 1, 'red', 'dropdown', None, colors, 'DESIGN', None, 1, BASE_FORM + 4]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE id BETWEEN %s AND %s',
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 2)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
               column('id', Integer),
               column('locale', String),
               column('label', String),
               column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_FORM_FIELD + 1, 'pt', 'Ligado ou desligado', 'Fonte ligada ou desligada.'],
        [BASE_FORM_FIELD + 1, 'en', 'on off', 'on off'],
        [BASE_FORM_FIELD + 2, 'pt', 'Cor', 'Cor do LED.'],
        [BASE_FORM_FIELD + 2, 'en', 'color', 'LED color.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute(
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s',
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 2)

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
        [BASE_PORT + 1, 'output_port', 'OUTPUT', None, 1, 'MANY', BASE_OP + 1],
        [BASE_PORT + 2, 'output_port', 'OUTPUT', None, 1, 'MANY', BASE_OP + 2],
        [BASE_PORT + 3, 'vcc_port', 'INPUT', None, 1, 'ONE', BASE_OP + 3],
        [BASE_PORT + 4, 'gnd_port', 'INPUT', None, 2, 'ONE', BASE_OP + 3],
        [BASE_PORT + 5, 'port_1a', 'INPUT', None, 3, 'ONE', BASE_OP + 3],
        [BASE_PORT + 6, 'port_1b', 'INPUT', None, 4, 'ONE', BASE_OP + 3],
        [BASE_PORT + 7, 'port_1y', 'OUTPUT', None, 5, 'MANY', BASE_OP + 3],
        [BASE_PORT + 8, 'led_port', 'INPUT', None, 1, 'ONE', BASE_OP + 4]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port(conn):
    conn.execute(
        'DELETE from operation_port WHERE id BETWEEN %s AND %s',
        BASE_PORT + 1, BASE_PORT + 8)

def _insert_operation_port_translation(conn):
    tb = table('operation_port_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String),
               column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_PORT + 1, 'pt', 'Vcc', 'Saída tensão.'],
        [BASE_PORT + 1, 'en', 'Vcc', 'Voltage output.'],
        [BASE_PORT + 2, 'pt', 'Gnd', 'Saída terra.'],
        [BASE_PORT + 2, 'en', 'Gnd', 'Ground output.'],
        [BASE_PORT + 3, 'pt', 'Vcc', 'Entrada tensão.'],
        [BASE_PORT + 3, 'en', 'Vcc', 'Voltage input.'],
        [BASE_PORT + 4, 'pt', 'Gnd', 'Entrada terra.'],
        [BASE_PORT + 4, 'en', 'Gnd', 'Ground input.'],
        [BASE_PORT + 5, 'pt', '1A', 'Entrada 1A.'],
        [BASE_PORT + 5, 'en', '1A', 'Input 1A.'],
        [BASE_PORT + 6, 'pt', '1B', 'Entrada 1B.'],
        [BASE_PORT + 6, 'en', '1B', 'Input 1B.'],
        [BASE_PORT + 7, 'pt', '1Y', 'Saída 1Y.'],
        [BASE_PORT + 7, 'en', '1Y', 'Output 1Y.'],
        [BASE_PORT + 8, 'pt', 'Entrada', 'Entrada.'],
        [BASE_PORT + 8, 'en', 'Input', 'Input.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_translation(conn):
    conn.execute(
        'DELETE from operation_port_translation WHERE id BETWEEN %s AND %s',
        BASE_PORT + 1, BASE_PORT + 8)

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
               column('operation_id', Integer),
               column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_OP + 1, BASE_CATEGORY + 1],
        [BASE_OP + 1, BASE_CATEGORY + 2],
        [BASE_OP + 2, BASE_CATEGORY + 1],
        [BASE_OP + 2, BASE_CATEGORY + 2],
        [BASE_OP + 3, BASE_CATEGORY + 1],
        [BASE_OP + 3, BASE_CATEGORY + 2],
        [BASE_OP + 4, BASE_CATEGORY + 1],
        [BASE_OP + 4, BASE_CATEGORY + 2]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_operation(conn):
    conn.execute(
        'DELETE from operation_category_operation WHERE operation_id BETWEEN %s AND % s', BASE_OP + 1, BASE_OP + 4)

def _insert_operation_operation_form(conn):
    tb = table('operation_operation_form',
               column('operation_id', Integer),
               column('operation_form_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_OP + 1, BASE_FORM + 1],
        [BASE_OP + 1, 110],
        [BASE_OP + 1, 41],
        [BASE_OP + 2, BASE_FORM + 2],
        [BASE_OP + 2, 110],
        [BASE_OP + 2, 41],
        [BASE_OP + 3, BASE_FORM + 3],
        [BASE_OP + 3, 110],
        [BASE_OP + 3, 41],
        [BASE_OP + 4, BASE_FORM + 4],
        [BASE_OP + 4, 110],
        [BASE_OP + 4, 41]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_operation_form(conn):
    conn.execute(
        'DELETE from operation_operation_form WHERE operation_id BETWEEN %s AND %s',
        BASE_OP + 1, BASE_OP + 4)

def _insert_operation_subset_operation(conn):
    tb = table('operation_subset_operation',
               column('operation_id', Integer),
               column('operation_subset_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_subset_operation(conn):
    return 'SQL'

def _insert_operation_platform(conn):
    tb = table('operation_platform',
               column('operation_id', Integer),
               column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_OP + 1, BASE_PLATFORM + 1],
        [BASE_OP + 2, BASE_PLATFORM + 1],
        [BASE_OP + 3, BASE_PLATFORM + 1],
        [BASE_OP + 4, BASE_PLATFORM + 1]

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_platform(conn):
    conn.execute(
        'DELETE from operation_platform WHERE operation_id BETWEEN %s AND %s',
        BASE_OP + 1, BASE_OP + 4)

def _insert_operation_port_interface_operation_port(conn):
    tb = table('operation_port_interface_operation_port',
               column('operation_port_interface_id', Integer),
               column('operation_port_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_PORT + 1, 1],
        [BASE_PORT + 2, 1],
        [BASE_PORT + 3, 1],
        [BASE_PORT + 4, 1],
        [BASE_PORT + 5, 1],
        [BASE_PORT + 6, 1],
        [BASE_PORT + 7, 1],
        [BASE_PORT + 8, 1]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_interface_operation_port(conn):
    conn.execute(
        'DELETE from operation_port_interface_operation_port WHERE operation_port_id BETWEEN % s AND %s ',
        BASE_PORT + 1, BASE_PORT + 8)


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
        _insert_platform,
        _insert_platform_translation,
        _insert_operation,
        _insert_operation_translation,
        _insert_operation_script,
        _insert_operation_category,
        _insert_operation_category_translation,
        _insert_operation_form,
        _insert_operation_form_translation,
        _insert_operation_form_field,
        _insert_operation_form_field_translation,
        _insert_operation_port,
        _insert_operation_port_translation,
        _insert_operation_category_operation,
        _insert_operation_operation_form,
        _insert_operation_subset_operation,
        _insert_operation_platform,
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
        _delete_platform,
        _delete_platform_translation,
        _delete_operation,
        _delete_operation_translation,
        _delete_operation_script,
        _delete_operation_category,
        _delete_operation_category_translation,
        _delete_operation_form,
        _delete_operation_form_translation,
        _delete_operation_form_field,
        _delete_operation_form_field_translation,
        _delete_operation_port,
        _delete_operation_port_translation,
        _delete_operation_category_operation,
        _delete_operation_operation_form,
        _delete_operation_subset_operation,
        _delete_operation_platform,
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
