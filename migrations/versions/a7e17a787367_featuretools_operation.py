"""Featuretools operation

Revision ID: a7e17a787367 
Revises: a95701f64029
"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'a7e17a787367'
down_revision = 'a95701f64029'
branch_labels = None
depends_on = None

# --------------------------------------------------------------
# ATENTION: You must revise this auto-generated code.
# Please, review offsets and commands before running a migration
# and optionally, perform a database backup. If everything is 
# OK, remove this comment.
# --------------------------------------------------------------

BASE_PLATFORM = 11000
BASE_OP = 11000
BASE_CATEGORY = 11000
BASE_FORM = 11000
BASE_FORM_FIELD = 11000
BASE_PORT = 11000

def _insert_platform(conn):
    tb = table('platform',
                column('id', Integer), 
                column('slug', String), 
                column('enabled', Boolean), 
                column('icon', String), 
                column('version', String), 
                column('plugin', Boolean))
    columns = [c.name for c in tb.columns]
    data = [  ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_platform(conn):
    return 'SQL' 

def _insert_platform_translation(conn):
    tb = table('platform_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_platform_translation(conn):
    return 'SQL'

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
      [BASE_OP + 1, 'derivate-new-attributes', 1, 'TRANSFORMATION', '', '', ''],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation(conn):
    conn.execute(
        'DELETE from operation WHERE id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 1)

def _insert_operation_translation(conn):
    tb = table('operation_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_OP + 1, 'pt', 'Derivar novos atributos', 'Cria novos atributos usando Featuretools. '],
      [BASE_OP + 1, 'en', 'Derivate new attributes', 'Create new attributes using Featuretools.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_translation(conn):
    conn.execute(
        'DELETE from operation_translation WHERE id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 1)

def _insert_operation_script(conn):
    tb = table('operation_script',
                column('id', Integer), 
                column('type', String), 
                column('enabled', Boolean), 
                column('body', String), 
                column('operation_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [None, 'JS_CLIENT', 1, 'copyInput(task)', BASE_OP + 1]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_script(conn):
    conn.execute(
        'DELETE from operation_script WHERE id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 1)

def _insert_operation_category(conn):
    tb = table('operation_category',
                column('id', Integer), 
                column('type', String), 
                column('order', Integer), 
                column('default_order', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_CATEGORY + 1, 'group', 0, 0] 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category(conn):
    conn.execute(
        'DELETE from operation_category WHERE id BETWEEN %s AND %s', 
        BASE_CATEGORY + 1, BASE_CATEGORY + 1)

def _insert_operation_category_translation(conn):
    tb = table('operation_category_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_CATEGORY + 1, 'en', 'Feature engineering'], 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_translation(conn):
    conn.execute(
        'DELETE from operation_category_translation WHERE id BETWEEN %s AND %s', 
        BASE_CATEGORY + 1, BASE_CATEGORY + 1)

def _insert_operation_form(conn):
    tb = table('operation_form',
                column('id', Integer), 
                column('enabled', Boolean), 
                column('order', Integer), 
                column('category', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM + 1, 1, 1, 'execution']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form(conn):
    conn.execute(
        'DELETE from operation_form WHERE id BETWEEN %s AND %s', 
        BASE_FORM + 1, BASE_FORM + 1)

def _insert_operation_form_translation(conn):
    tb = table('operation_form_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM + 1, 'pt', 'Execução'],
      [BASE_FORM + 1, 'en', 'Execution']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_translation(conn):
    conn.execute(
        'DELETE from operation_form_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM + 1, BASE_FORM + 1)

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
    
    #****Listar as primitivas manualmente
    aggr_primitives = """[ 
                          {"key": "sum", "pt": "Soma", "value": "sum", "en": "Sum"},
                          {"key": "mean", "pt": "Média", "value": "mean", "en": "Mean"}
                         ]"""

    trans_primitives = """[ 
                          {"key": "time_since_previous", "pt": "Tempo anterior", "value": "time_since_previous", "en": "Time Since Previus"},
                          {"key": "day", "pt": "Dia", "value": "day", "en": "Day"}
                         ]"""
    data = [  
      [BASE_FORM_FIELD + 1, 'transaction-index', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 2, 'transaction-time', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 3, 'relationship-dataframe-index', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'DESIGN', None, 1, BASE_FORM + 1], 

      [BASE_FORM_FIELD + 4, 'aggregation-primitives', 'TEXT', 1, 1, None, 'tag', None, aggr_primitives, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 5, 'transform-primitives', 'TEXT', 1, 1, None, 'tag', None, trans_primitives, 'DESIGN', None, 1, BASE_FORM + 1] 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 5)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM_FIELD + 1,  'pt', 'Identificador transação', ''],
      [BASE_FORM_FIELD + 2,  'pt', 'Tempo transação', ''],
      [BASE_FORM_FIELD + 3,  'pt', 'Identificador relacionamento', ''],
      [BASE_FORM_FIELD + 4,  'pt', 'Primitivas de agregação', ''],
      [BASE_FORM_FIELD + 5,  'pt', 'Primitivas de transformação', ''],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute(
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 5)

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
      [BASE_PORT + 1, 'input_port', 'INPUT', None, 0, 'ONE', BASE_OP + 1],
      [BASE_PORT + 2, 'output_port', 'OUTPUT', None, 0, 'MANY', BASE_OP + 1]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port(conn):
    conn.execute(
        'DELETE from operation_port WHERE id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 2)

def _insert_operation_port_translation(conn):
    tb = table('operation_port_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_PORT + 1, 'pt', 'Input', 'Dataframe de entrada.'], 
      [BASE_PORT + 1, 'en', 'Input', 'Input dataframe.'],

      [BASE_PORT + 2, 'pt', 'Output', 'Dataframe de saída.'], 
      [BASE_PORT + 2, 'en', 'Output', 'Output dataframe.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_translation(conn):
    conn.execute(
        'DELETE from operation_port_translation WHERE id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 2)

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
                column('operation_id', Integer), 
                column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
            [BASE_OP + 1, BASE_CATEGORY + 1] 
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_operation(conn):
    conn.execute(
        'DELETE from operation_category_operation WHERE operation_id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 1)

def _insert_operation_operation_form(conn):
    tb = table('operation_operation_form',
                column('operation_id', Integer), 
                column('operation_form_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
            [BASE_OP + 1, BASE_FORM + 1], 
            [BASE_OP + 1, 110], 
            [BASE_OP + 1, 41] 
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_operation_form(conn):
    conn.execute(
        'DELETE from operation_operation_form WHERE operation_id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 1)

#def _insert_operation_subset_operation(conn):
#    tb = table('operation_subset_operation',
#                column('operation_id', Integer), 
#                column('operation_subset_id', Integer))
#    columns = [c.name for c in tb.columns]
#    data = [
#    ]
#    rows = [dict(list(zip(columns, row))) for row in data]
#    op.bulk_insert(tb, rows)
#
#def _delete_operation_subset_operation(conn):
#    return 'SQL'

SPARK_PLATFORM = 1 
SCIKIT_LEARN_PLATFORM = 4
def _insert_operation_platform(conn):
    tb = table('operation_platform',
                column('operation_id', Integer), 
                column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
            [BASE_OP + 1, SPARK_PLATFORM], 
            [BASE_OP + 1, SCIKIT_LEARN_PLATFORM], 
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_platform(conn):
    conn.execute(
        'DELETE from operation_platform WHERE operation_id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 1)

def _insert_operation_port_interface_operation_port(conn):
    tb = table('operation_port_interface_operation_port',
                column('operation_port_id', Integer),
                column('operation_port_interface_id', Integer)) 
    columns = [c.name for c in tb.columns]
    data = [
            [BASE_PORT + 1, 1],
            [BASE_PORT + 2, 1]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_interface_operation_port(conn):
    conn.execute(
        'DELETE from operation_port_interface_operation_port WHERE operation_port_id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 2)

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
        _insert_operation_port_interface_operation_port, 
        #_insert_operation_subset_operation,
        _insert_operation_platform,
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
        _delete_operation_port_translation, 
        _delete_operation_port, 
        _delete_operation_category_operation,
        _delete_operation_operation_form,
        #_delete_operation_subset_operation,
        _delete_operation_port_interface_operation_port, 
        _delete_operation_platform,
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
