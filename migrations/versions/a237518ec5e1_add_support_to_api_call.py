"""add support to API Call

Revision ID: a237518ec5e1 
Revises: af8eeaf80cd6
"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText
import json
from tahiti.migration_utils import (is_psql, is_mysql, is_sqlite,
        handle_params, get_enable_disable_fk_command)

# revision identifiers, used by Alembic.
revision = 'a237518ec5e1'
down_revision = 'af8eeaf80cd6'
branch_labels = None
depends_on = None

# --------------------------------------------------------------
# ATENTION: You must revise this auto-generated code.
# Please, review offsets and commands before running a migration
# and optionally, perform a database backup. If everything is 
# OK, remove this comment.
# --------------------------------------------------------------

BASE_OP = 143
BASE_FORM = 157
BASE_FORM_FIELD = 651
BASE_PORT = 351

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
      [BASE_OP + 1, 'api-call', 1, 'TRANSFORMATION', '', '', '']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation(conn):
    conn.execute(
        handle_params('DELETE from operation WHERE id BETWEEN %s AND %s'), 
        BASE_OP + 1, BASE_OP + 1)

def _insert_operation_translation(conn):
    tb = table('operation_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String)) 
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_OP + 1, 'pt', 'Chamada à API', 'Permite realizar uma chamada a uma API do tipo REST.'],
      [BASE_OP + 1, 'en', 'API call', 'Allows call a REST compatible API.'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_translation(conn):
    conn.execute(
        handle_params('DELETE from operation_translation WHERE id BETWEEN %s AND %s'), 
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
      [81, 'JS_CLIENT', 1, '', BASE_OP + 1]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_script(conn):
    conn.execute(
        handle_params('DELETE from operation_script WHERE operation_id BETWEEN %s AND %s'), 
        BASE_OP + 1, BASE_OP + 1)

def _insert_operation_form(conn):
    tb = table('operation_form',
                column('id', Integer), 
                column('enabled', Boolean), 
                column('order', Integer), 
                column('category', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM + 1, 1, 0, 'execution']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form(conn):
    conn.execute(
        handle_params('DELETE from operation_form WHERE id BETWEEN %s AND %s'), 
        BASE_FORM + 1, BASE_FORM + 1)

def _insert_operation_form_translation(conn):
    tb = table('operation_form_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM + 1, 'pt', 'Execução.'],
      [BASE_FORM + 1, 'en', 'Execution.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_translation(conn):
    conn.execute(
        handle_params('DELETE from operation_form_translation WHERE id BETWEEN %s AND %s'), 
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

    methods = json.dumps([{'key': 'GET', 'pt': 'GET', 'en': 'GET'},
            {'key': 'POST', 'pt': 'POST', 'en': 'POST'},
            {'key': 'PUT', 'pt': 'PUT', 'en': 'PUT'},
            {'key': 'DELETE', 'pt': 'DELETE', 'en': 'DELETE'},
            {'key': 'HEAD', 'pt': 'HEAD', 'en': 'HEAD'},
            {'key': 'OPTIONS', 'pt': 'OPTIONS', 'en': 'OPTIONS'},
            {'key': 'CONNECT', 'pt': 'CONNECT', 'en': 'CONNECT'},
            {'key': 'TRACE', 'pt': 'TRACE', 'en': 'TRACE'},
            {'key': 'PATCH', 'pt': 'PATCH', 'en': 'PATCH'},])

    data = [
      [BASE_FORM_FIELD + 1, 'method', 'TEXT', 1, 1, 'GET', 'dropdown', None, methods, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 2, 'url', 'TEXT', 1, 2, None, 'text', None, None, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 3, 'parameters', 'TEXT', 0, 3, '{}', 'textare', None, None, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 4, 'headers', 'TEXT', 0, 4, '{}', 'textare', None, None, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 5, 'result_to_df', 'INTEGER', 1, 5, '0', 'checkbox', None, None, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 6, 'success', 'TEXT', 1, 6, '200', 'text', None, None, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 7, 'user', 'TEXT', 0, 7, None, 'text', None, None, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 8, 'password', 'TEXT', 0, 8, None, 'text', None, None, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 9, 'ignore_certificate', 'INTEGER', 1, 9, '0', 'checkbox', None, None, 'DESIGN', None, 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 10, 'attributes', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', None, 1, BASE_FORM + 1],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field(conn):
    conn.execute(
        handle_params('DELETE from operation_form_field WHERE id BETWEEN %s AND %s'), 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 10)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM_FIELD + 1, 'pt', 'Método', 'Método HTTP para a chamada à API.'], 
      [BASE_FORM_FIELD + 2, 'pt', 'URL', 'URL para a chamada à API.'], 
      [BASE_FORM_FIELD + 3, 'pt', 'Parâmetros', 'Parâmetros para a chamada à API.'], 
      [BASE_FORM_FIELD + 4, 'pt', 'Cabeçalhos', 'Cabeçalhos para a chamada à API.'], 
      [BASE_FORM_FIELD + 5, 'pt', 'Converter resultado em dados', 'Converter resultado em dados.'], 
      [BASE_FORM_FIELD + 6, 'pt', 'Status de sucesso', 'Status HTTP indicativo de sucesso.'], 
      [BASE_FORM_FIELD + 7, 'pt', 'Usuário', 'Usuário usado para autenticação básica (se aplicável).'], 
      [BASE_FORM_FIELD + 8, 'pt', 'Senha', 'Senha usada para autenticação básica (se aplicável).'], 
      [BASE_FORM_FIELD + 9, 'pt', 'Ignorar problemas com certificado', 'Ignorar problemas com certificado.'],
      [BASE_FORM_FIELD + 10, 'pt', 'Sugestão de nomes de atributos (separados por vírgula)', 'Sugestão de nomes de atributos para as próximas tarefas (separados por vírgula).'],
      [BASE_FORM_FIELD + 1, 'en', 'Method', 'HTTP method used in API call.'], 
      [BASE_FORM_FIELD + 2, 'en', 'URL', 'URL used in API call.'], 
      [BASE_FORM_FIELD + 3, 'en', 'Parameters', 'API call parameters.'], 
      [BASE_FORM_FIELD + 4, 'en', 'Headers', 'API call HTTP headers.'], 
      [BASE_FORM_FIELD + 5, 'en', 'Convert result to data', 'Convert result to data.'], 
      [BASE_FORM_FIELD + 6, 'en', 'Success status code', 'HTTP status code indicating success.'], 
      [BASE_FORM_FIELD + 7, 'en', 'User', 'Basic authentication username (if applicable).'], 
      [BASE_FORM_FIELD + 8, 'en', 'Password', 'Basic authentication password (if applicable).'], 
      [BASE_FORM_FIELD + 9, 'en', 'Ignore certificate problems', 'Ignore certificate problems.'],
      [BASE_FORM_FIELD + 10, 'en', 'Attributes names suggestion (comma-separated)', 'Attributes names suggestion (comma-separated).'],

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute(
        handle_params('DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s'), 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 10)

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
      [BASE_PORT + 1, 'input data', 'INPUT', None, 1, 'ONE', BASE_OP + 1], 
      [BASE_PORT + 2, 'output data', 'OUTPUT', None, 2, 'MANY', BASE_OP + 1]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port(conn):
    conn.execute(
        handle_params('DELETE from operation_port WHERE id BETWEEN %s AND %s'), 
        BASE_PORT + 1, BASE_PORT + 2)

def _insert_operation_port_translation(conn):
    tb = table('operation_port_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_PORT + 1, 'pt', 'dados de entrada', 'Dados de entrada'], 
      [BASE_PORT + 2, 'pt', 'dados de saída', 'Dados de saída']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_translation(conn):
    conn.execute(
        handle_params('DELETE from operation_port_translation WHERE id BETWEEN %s AND %s'), 
        BASE_PORT + 1, BASE_PORT + 2)

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
                column('operation_id', Integer), 
                column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
            [BASE_OP + 1, 41]
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
            [BASE_OP + 1, 41],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_operation_form(conn):
    conn.execute(
        'DELETE from operation_operation_form WHERE operation_id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 1)

def _insert_operation_subset_operation(conn):
    tb = table('operation_subset_operation',
                column('operation_id', Integer), 
                column('operation_subset_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
            [BASE_OP + 1, 1],
            [BASE_OP + 1, 2],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_subset_operation(conn):
    conn.execute(
        'DELETE from operation_subset_operation WHERE operation_id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 1)

def _insert_operation_platform(conn):
    tb = table('operation_platform',
                column('operation_id', Integer), 
                column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
            [BASE_OP + 1, 1],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_platform(conn):
    conn.execute(
        'DELETE from operation_platform WHERE operation_id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 1)

def _insert_operation_port_interface_operation_port(conn):
    tb = table('operation_port_interface_operation_port',
                column('operation_port_interface_id', Integer), 
                column('operation_port_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
            [1, BASE_PORT + 1],
            [1, BASE_PORT + 2],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_interface_operation_port(conn):
    conn.execute(
        'DELETE from operation_port_interface_operation_port WHERE operation_port_id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 2)


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
        #_insert_operation_subset_operation,
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
    conn.execute(get_enable_disable_fk_command(false))

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
        # _delete_operation_subset_operation,
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
    conn.execute(get_enable_disable_fk_command(true))
    session.commit()
