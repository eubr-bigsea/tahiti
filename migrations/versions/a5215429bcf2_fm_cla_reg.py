"""fm_cla_reg

Revision ID: a5215429bcf2 
Revises: c1bbd1bb8f85
"""
import json
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText
from tahiti.migration_utils import is_sqlite


# revision identifiers, used by Alembic.
revision = 'a5215429bcf2'
down_revision = 'c1bbd1bb8f85'
branch_labels = None
depends_on = None

# --------------------------------------------------------------
# ATENTION: You must revise this auto-generated code.
# Please, review offsets and commands before running a migration
# and optionally, perform a database backup. If everything is 
# OK, remove this comment.
# --------------------------------------------------------------

META_PLATFORM = 1000

APPEARANCE_FORM_ID=41

BASE_PLATFORM = 2236
BASE_OP = 2236
BASE_FORM = 2236
BASE_FORM_FIELD = 2236

# Model builder
# Uses READ_DATA, SAMPLE

FM_CLASSIFIER = BASE_OP + 9

FM_REGRESSION = BASE_OP + 10

CAT_CLASSIFICATION = 4
CAT_REGRESSION = 47
CAT_CLUSTERING = 46
CAT_MODEL_BUILDER = 2113

ORIGINAL_SAVE_FORM = 28

ALL_OPS = [
    # New ML algorithms
    FM_CLASSIFIER, FM_REGRESSION,
]

ATTRIBUTES_FORM = BASE_FORM + 2
ALIASES_FORM = BASE_FORM + 3
KEEP_ATTRIBUTE_FORM = BASE_FORM + 4
ATTRIBUTE_FORM = BASE_FORM + 5
ALIAS_FORM = BASE_FORM + 6

MAX_OP = max(ALL_OPS)

def execute(conn, cmd, *params):
    if is_sqlite():
        cmd2 = cmd.replace('%s', '?')
    else:
        cmd2 = cmd
    conn.execute(cmd2, *params)

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
      [FM_CLASSIFIER, 'fm-classifier', 1, 'TRANSFORMATION', '', '', ''],
      [FM_REGRESSION, 'fm-regression', 1, 'TRANSFORMATION', '', '', ''],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation(conn):
    execute(conn, 
        'DELETE from operation WHERE id BETWEEN %s AND %s',
        BASE_OP, max(ALL_OPS))

def _insert_operation_translation(conn):
    tb = table('operation_translation',
                column('id', Integer),
                column('locale', String),
                column('name', String),
                column('description', String),
                column('label_format', String),
                )
    columns = [c.name for c in tb.columns]
    data = [
      [FM_CLASSIFIER, 'pt', 'Classificador Factorization Machines', 'Classificador Factorization machines.', ''],
      [FM_REGRESSION, 'pt', 'Regressão Factorization Machines', 'Regressão Factorization machines.', ''],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_translation(conn):
    execute(conn, 
        'DELETE from operation_translation WHERE id BETWEEN %s AND %s',
        BASE_OP, max(ALL_OPS))

def _insert_operation_form(conn):
    tb = table('operation_form',
                column('id', Integer),
                column('enabled', Boolean),
                column('order', Integer),
                column('category', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM + 0, 1, 1, 'execution'], # Comment
      [BASE_FORM + 1, 1, 1, 'execution'], # ReadData
    ]
    exclusions = set([FM_CLASSIFIER,FM_REGRESSION])

    for op_id in set(ALL_OPS) - exclusions: # Operations' form
        data.append([op_id + 50, 1, 1, 'execution'])

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form(conn):
    execute(conn, 
        'DELETE from operation_form WHERE id BETWEEN %s AND %s',
        BASE_FORM, BASE_FORM+1)

def _insert_operation_form_translation(conn):
    tb = table('operation_form_translation',
                column('id', Integer),
                column('locale', String),
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM, 'pt', 'Execução'], # Common form to all ops
      [BASE_FORM + 1, 'pt', 'Execução'],

      [BASE_FORM, 'en', 'Execution'],
      [BASE_FORM + 1, 'en', 'Execution'],
    ]
    exclusions = set([FM_REGRESSION, FM_CLASSIFIER])

    for op_id in set(ALL_OPS) - exclusions: # Operations' form
        data.append([op_id + 50, 'pt', 'Execução'])
        data.append([op_id + 50, 'en', 'Execution'])

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_translation(conn):
    execute(conn, 
        'DELETE from operation_form_translation WHERE id BETWEEN %s AND %s',
        BASE_FORM, BASE_FORM + 1)
    
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
    data = []
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE form_id BETWEEN %s AND %s', 
        BASE_FORM + 1, BASE_FORM + 2)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = []
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute(
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 2)

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
                column('operation_id', Integer),
                column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [FM_CLASSIFIER, CAT_MODEL_BUILDER],
      [FM_CLASSIFIER, CAT_CLASSIFICATION],
      [FM_REGRESSION, CAT_MODEL_BUILDER],
      [FM_REGRESSION, CAT_REGRESSION],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_operation(conn):
    execute(conn, 
        '''DELETE FROM operation_category_operation
            WHERE operation_id BETWEEN %s and %s ''',
        BASE_OP, MAX_OP)
#corrigir
def _insert_operation_operation_form(conn):
    tb = table('operation_operation_form',
                column('operation_id', Integer),
                column('operation_form_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [FM_CLASSIFIER, BASE_FORM],
        [FM_REGRESSION, BASE_FORM + 1]
    ]
    
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _delete_operation_operation_form(conn):
    execute(conn, 
        '''DELETE FROM operation_operation_form
            WHERE operation_id BETWEEN %s and %s''',
        BASE_OP, BASE_FORM + 1)

def _insert_operation_platform(conn):
    tb = table('operation_platform',
                column('operation_id', Integer),
                column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [op_id, META_PLATFORM] for op_id in ALL_OPS
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_platform(conn):
    execute(conn, 
        '''DELETE FROM operation_platform
            WHERE operation_id BETWEEN %s and %s''',
        BASE_OP, MAX_OP)

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
        _insert_operation_form,
        _insert_operation_form_translation,
        _insert_operation_form_field,
        _insert_operation_form_field_translation,
        _insert_operation_category_operation,
        _insert_operation_operation_form,
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
        _delete_operation,
        _delete_operation_translation,
        _delete_operation_form,
        _delete_operation_form_translation,
        _delete_operation_form_field,
        _delete_operation_form_field_translation,
        _delete_operation_category_operation,
        _delete_operation_operation_form,
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
