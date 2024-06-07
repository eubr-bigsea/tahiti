"""add xai operation in sklearn

Revision ID: 2064706940a6
Revises: 138dd7d899e6
Create Date: 2023-03-16 17:44:15.606453

"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText

# revision identifiers, used by Alembic.
revision = '2064706940a6'
down_revision = '138dd7d899e6'
branch_labels = None
depends_on = None


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
        [4206, 'xai', True, 'ACTION', 'fa-cloud-download-alt', None, None]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation(conn):
    conn.execute('DELETE from operation WHERE id = %s', 4206)


def _insert_operation_translation(conn):
    tb = table('operation_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String),
               column('description', String),
               column('label_format', String))
    columns = [c.name for c in tb.columns]
    data = [
        [4206, 'pt', 'XAI', 'XAI'],
        [4206, 'en', 'XAI', 'XAI']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_translation(conn):
    conn.execute(
        'DELETE from operation_translation WHERE id = %s', 4206)


def _insert_operation_script(conn):
    tb = table('operation_script',
               column('id', Integer),
               column('type', String),
               column('enabled', Boolean),
               column('body', String),
               column('operation_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [None, 'JS_CLIENT', 1, 'copyInput(task)', 4206]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_script(conn):
    conn.execute('DELETE from operation_script WHERE id = %s', 4206)

def _insert_operation_category(conn):
    tb = table('operation_category',
               column('id', Integer),
               column('type', String),
               column('subtype', String),
               column('order', Integer),
               column('default_order', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [4203, 'group', None, 0, 0]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category(conn):
    conn.execute(
        'DELETE from operation_category WHERE id = 4203')

def _insert_operation_category_translation(conn):
    tb = table('operation_category_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
        [4203, 'pt', 'Explicabilidade'],
        [4203, 'en', 'Explainability']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_translation(conn):
    conn.execute(
        'DELETE from operation_category_translation WHERE id = 4203')

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
               column('operation_id', Integer),
               column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [4206, 4203]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_category_operation(conn):
    conn.execute('DELETE from operation_category_operation WHERE operation_id = %s', 4206)


# def _insert_operation_form(conn):
#     tb = table('operation_form',
#                column('id', Integer),
#                column('enabled', Boolean),
#                column('order', Integer),
#                column('category', String))
#     columns = [c.name for c in tb.columns]
#     data = [
#         [BASE_FORM + 1, 1, 1, 'execution']
#     ]
#     rows = [dict(zip(columns, row)) for row in data]
#     op.bulk_insert(tb, rows)
#
#
# def _delete_operation_form(conn):
#     conn.execute('DELETE from operation_form WHERE id = %s', BASE_FORM + 1)
#
#
# def _insert_operation_form_translation(conn):
#     tb = table('operation_form_translation',
#                column('id', Integer),
#                column('locale', String),
#                column('name', String))
#     columns = [c.name for c in tb.columns]
#     data = [
#         [BASE_FORM + 1, 'pt', 'Execução'],
#         [BASE_FORM + 1, 'en', 'Execution']
#     ]
#     rows = [dict(zip(columns, row)) for row in data]
#     op.bulk_insert(tb, rows)
#
#
# def _delete_operation_form_translation(conn):
#     conn.execute('DELETE from operation_form_translation WHERE id = %s', BASE_FORM + 1)
#
#
# def _insert_operation_form_field(conn):
#     tb = table('operation_form_field',
#                column('id', Integer),
#                column('name', String),
#                column('type', String),
#                column('required', Boolean),
#                column('order', Integer),
#                column('default', String),
#                column('suggested_widget', String),
#                column('values_url', String),
#                column('values', String),
#                column('scope', String),
#                column('enable_conditions', String),
#                column('editable', Boolean),
#                column('form_id', Integer))
#     columns = [c.name for c in tb.columns]
#
#     url_value = '`${LIMONERO_URL}/models?simple=true&list=true&enabled=1`'
#
#
#     data = [
#         [BASE_FORM_FIELD + 1, 'model', 'TEXT', True, 1, None, 'lookup', url_value, None, 'EXECUTION', None, 1, BASE_FORM + 1]
#     ]
#     rows = [dict(zip(columns, row)) for row in data]
#     op.bulk_insert(tb, rows)
#
#
# def _delete_operation_form_field(conn):
#     conn.execute('DELETE from operation_form_field WHERE id = %s', BASE_FORM_FIELD + 1)
#

# def _insert_operation_form_field_translation(conn):
#     tb = table('operation_form_field_translation',
#                column('id', Integer),
#                column('locale', String),
#                column('label', String),
#                column('help', UnicodeText))
#     columns = [c.name for c in tb.columns]
#     data = [
#         [BASE_FORM_FIELD + 1, 'pt', 'Carrega Modelo', 'Carrega modelos salvos.'],
#         [BASE_FORM_FIELD + 1, 'en', 'Load Model', 'Load Model']
#     ]
#     rows = [dict(zip(columns, row)) for row in data]
#     op.bulk_insert(tb, rows)
#
# def _delete_operation_form_field_translation(conn):
#     conn.execute('DELETE from operation_form_field_translation WHERE id = %s', BASE_FORM_FIELD + 1)
#

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
        [4200, 'xai_in', 'INPUT', None, 1, 'ONE', 4206],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port(conn):
    conn.execute('DELETE from operation_port WHERE id = %s', 4200)


def _insert_operation_port_translation(conn):
    tb = table('operation_port_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String),
               column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
        [4200, 'pt', 'modelo', 'Saída do Modelo.'],
        [4200, 'en', 'model', 'Output Model.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_port_translation(conn):
    conn.execute('DELETE from operation_port_translation WHERE id = %s', 4200)



# def _insert_operation_operation_form(conn):
#     tb = table('operation_operation_form',
#                column('operation_id', Integer),
#                column('operation_form_id', Integer))
#     columns = [c.name for c in tb.columns]
#     data = [
#         [BASE_OP + 1, BASE_FORM + 1],
#         [BASE_OP + 1, 110],
#         [BASE_OP + 1, 41]
#     ]
#
#     rows = [dict(list(zip(columns, row))) for row in data]
#     op.bulk_insert(tb, rows)
#
# def _delete_operation_operation_form(conn):
#     conn.execute(
#         'DELETE from operation_operation_form WHERE operation_id = %s', BASE_OP + 1)


def _insert_operation_platform(conn):
    tb = table('operation_platform',
               column('operation_id', Integer),
               column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [4206, 4]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_platform(conn):
    conn.execute(
        'DELETE from operation_platform WHERE operation_id = %s', 4206)


# def _insert_operation_port_interface_operation_port(conn):
#     tb = table('operation_port_interface_operation_port',
#                column('operation_port_interface_id', Integer),
#                column('operation_port_id', Integer))
#     columns = [c.name for c in tb.columns]
#     data = [
#         [BASE_PORT + 1, 1]
#     ]
#     rows = [dict(list(zip(columns, row))) for row in data]
#     op.bulk_insert(tb, rows)
#
# def _delete_operation_port_interface_operation_port(conn):
#     conn.execute(
#         'DELETE from operation_port_interface_operation_port WHERE operation_port_id = %s', BASE_PORT + 1)
#

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
        # _insert_operation_form,
        # _insert_operation_form_translation,
        # _insert_operation_form_field,
        # _insert_operation_form_field_translation,
        _insert_operation_port,
        _insert_operation_port_translation,
        _insert_operation_category,
        _insert_operation_category_operation,
        # _insert_operation_operation_form,
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
        _delete_operation,
        _delete_operation_translation,
        _delete_operation_script,
        # _delete_operation_form,
        # _delete_operation_form_translation,
        # _delete_operation_form_field,
        # _delete_operation_form_field_translation,
        _delete_operation_port,
        _delete_operation_port_translation,
        _delete_operation_category_operation,
        # _delete_operation_operation_form,
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
