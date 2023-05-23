"""xai platform

Revision ID: 48352bbe32be
Revises: 2064706940a6
Create Date: 2023-04-21 14:45:14.222684

"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText


# revision identifiers, used by Alembic.
revision = '48352bbe32be'
down_revision = '2064706940a6'
branch_labels = None
depends_on = None

BASE_PLATFORM = 20000
BASE_OP = 20000
BASE_CATEGORY = 20000
BASE_FORM = 20000
BASE_FORM_FIELD = 20000
BASE_PORT = 20000


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
        [BASE_PLATFORM + 1, 'xai', 1, 'icon', 'version', 0]
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
        [BASE_PLATFORM + 1, 'pt', 'Explicabilidade', 'Explicabilidade'],
        [BASE_PLATFORM + 1, 'en', 'Explainability', 'Explainability']
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
        [BASE_OP + 1, 'load-model', True, 'ACTION', 'fa-cloud-download-alt', None, None],
        [BASE_OP + 2, 'tree', 1, 'TRANSFORMATION', '', '', ''],
        [BASE_OP + 3, 'tree_ensemble', 1, 'TRANSFORMATION', '', '', ''],
        [BASE_OP + 4, 'regression', 1, 'TRANSFORMATION', '', '', ''],
        [BASE_OP + 5, 'clustering', 1, 'TRANSFORMATION', '', '', '']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation(conn):
    conn.execute(
        'DELETE from operation WHERE id BETWEEN %s AND %s',
        BASE_OP + 1, BASE_OP + 5)


def _insert_operation_translation(conn):
    tb = table('operation_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String),
               column('description', String),
               column('label_format', String))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_OP + 1, 'pt', 'Carregar Modelo', 'Carregar Modelo. '],
        [BASE_OP + 1, 'en', 'Load Model', 'Load Model. '],
        [BASE_OP + 2, 'pt', 'Árvores', 'Árvores de Decisão. '],
        [BASE_OP + 2, 'en', 'Tree', 'Decision Tree. '],
        [BASE_OP + 3, 'pt', 'Árvore Aglomeradas', 'Árvore Aglomeradas. '],
        [BASE_OP + 3, 'en', 'Tree-Ensemble', 'Tree-Essemble. '],
        [BASE_OP + 4, 'pt', 'Regressão', 'Regressão'],
        [BASE_OP + 4, 'en', 'Regression', 'Regression'],
        [BASE_OP + 5, 'pt', 'Clusterização', 'Clusterização.'],
        [BASE_OP + 5, 'en', 'Clustering', 'Clustering.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_translation(conn):
    conn.execute(
        'DELETE from operation_translation WHERE id BETWEEN %s AND %s',
        BASE_OP + 1, BASE_OP + 5)


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
        [None, 'JS_CLIENT', 1, 'copyInput(task)', BASE_OP + 4],
        [None, 'JS_CLIENT', 1, 'copyInput(task)', BASE_OP + 5]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_script(conn):
    conn.execute(
        'DELETE from operation_script WHERE id BETWEEN %s AND %s',
        BASE_OP + 1, BASE_OP + 5)


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
        [BASE_CATEGORY + 2, 'group', None, 0, 0],
        [BASE_CATEGORY + 3, 'subgroup', None, 0, 0],
        [BASE_CATEGORY + 4, 'subgroup', None, 0, 0],
        [BASE_CATEGORY + 5, 'group', None, 0, 0],
        [BASE_CATEGORY + 6, 'subgroup', None, 0, 0],
        [BASE_CATEGORY + 7, 'subgroup', None, 0, 0]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category(conn):
    conn.execute(
        'DELETE from operation_category WHERE id BETWEEN %s AND %s',
        BASE_CATEGORY + 1, BASE_CATEGORY + 7)


def _insert_operation_category_translation(conn):
    tb = table('operation_category_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_CATEGORY + 1, 'pt', 'Modelo'],
        [BASE_CATEGORY + 1, 'en', 'Model'],
        [BASE_CATEGORY + 2, 'pt', 'Interpretação'],
        [BASE_CATEGORY + 2, 'en', 'Interpretation'],
        [BASE_CATEGORY + 3, 'pt', 'Global'],
        [BASE_CATEGORY + 3, 'en', 'Global'],
        [BASE_CATEGORY + 4, 'pt', 'Local'],
        [BASE_CATEGORY + 4, 'en', 'Local'],
        [BASE_CATEGORY + 5, 'pt', 'Explicação'],
        [BASE_CATEGORY + 5, 'en', 'Explanation'],
        [BASE_CATEGORY + 6, 'pt', 'Global'],
        [BASE_CATEGORY + 6, 'en', 'Global'],
        [BASE_CATEGORY + 7, 'pt', 'Local'],
        [BASE_CATEGORY + 7, 'en', 'Local'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_category_translation(conn):
    conn.execute(
        'DELETE from operation_category_translation WHERE id BETWEEN %s AND %s',
        BASE_CATEGORY + 1, BASE_CATEGORY + 7)


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
        [BASE_FORM + 4, 1, 1, 'execution'],
        [BASE_FORM + 5, 1, 1, 'execution'],
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
        [BASE_FORM + 4, 'en', 'Execution'],
        [BASE_FORM + 5, 'pt', 'Execução'],
        [BASE_FORM + 5, 'en', 'Execution'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_form_translation(conn):
    conn.execute(
        'DELETE from operation_form_translation WHERE id BETWEEN %s AND %s',
        BASE_FORM + 1, BASE_FORM + 5)

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

    url_value = '`${LIMONERO_URL}/models?simple=true&list=true&enabled=1`'

    data = [
        [BASE_FORM_FIELD + 1, 'model', 'TEXT', True, 1, None, 'lookup', url_value, None, 'EXECUTION', None, 1, BASE_FORM + 1],
        [BASE_FORM_FIELD + 2, 'feature importance', 'INTEGER', 1, 1, '1', 'checkbox', None, None, 'DESIGN', None, 1,  BASE_FORM + 2],
        [BASE_FORM_FIELD + 3, 'tree surface', 'INTEGER', 1, 1, '1', 'checkbox', None, None, 'DESIGN', None, 1,  BASE_FORM + 2],
        [BASE_FORM_FIELD + 4, 'feature importance', 'INTEGER', 1, 1, '1', 'checkbox', None, None, 'DESIGN', None, 1,  BASE_FORM + 3],
        [BASE_FORM_FIELD + 5, 'forest importance', 'INTEGER', 1, 1, '1', 'checkbox', None, None, 'DESIGN', None, 1,  BASE_FORM + 3],
        [BASE_FORM_FIELD + 6, 'feature importance', 'INTEGER', 1, 1, '1', 'checkbox', None, None, 'DESIGN', None, 1,  BASE_FORM + 4],
        [BASE_FORM_FIELD + 7, 'p-value', 'INTEGER', 1, 1, '1', 'checkbox', None, None, 'DESIGN', None, 1,  BASE_FORM + 4],
        [BASE_FORM_FIELD + 8, 'show surface', 'INTEGER', 1, 1, '1', 'checkbox', None, None, 'DESIGN', None, 1,  BASE_FORM + 5],
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE id BETWEEN %s AND %s',
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 8)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
               column('id', Integer),
               column('locale', String),
               column('label', String),
               column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_FORM_FIELD + 1, 'pt', 'Modelo', 'Modelo'],
        [BASE_FORM_FIELD + 1, 'en', 'Model', 'Model'],
        [BASE_FORM_FIELD + 2, 'pt', 'Importancia das Características', 'Importancia das Características.'],
        [BASE_FORM_FIELD + 2, 'en', 'Feature Importance', 'Feature Importance.'],
        [BASE_FORM_FIELD + 3, 'pt', 'Superfície da Árvore', 'Superfície da Árvore'],
        [BASE_FORM_FIELD + 3, 'en', 'Tree Surface', 'Tree Surface'],
        [BASE_FORM_FIELD + 4, 'pt', 'Importancia das Características', 'Importancia das Características.'],
        [BASE_FORM_FIELD + 4, 'en', 'Feature Importance', 'Feature Importance.'],
        [BASE_FORM_FIELD + 5, 'pt', 'Importancia da Floresta', 'Importancia da Floresta'],
        [BASE_FORM_FIELD + 5, 'en', 'Forest Importance', 'Forest Importance.'],
        [BASE_FORM_FIELD + 6, 'pt', 'Importancia das Características', 'Importancia das Características.'],
        [BASE_FORM_FIELD + 6, 'en', 'Feature Importance', 'Feature Importance.'],
        [BASE_FORM_FIELD + 7, 'pt', 'p-valor', 'p-valor.'],
        [BASE_FORM_FIELD + 7, 'en', 'p-value', 'p-value.'],
        [BASE_FORM_FIELD + 8, 'pt', 'Mostrar Superfície', 'Mostrar Superfície.'],
        [BASE_FORM_FIELD + 8, 'en', 'Show Surface', 'Show Surface.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute(
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s',
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 8)

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
        [BASE_PORT + 1, 'model_out_port', 'OUTPUT', None, 1, 'MANY', BASE_OP + 1],
        [BASE_PORT + 2, 'tree_in', 'INPUT', None, 1, 'ONE', BASE_OP + 2],
        [BASE_PORT + 3, 'ensemble_in', 'INPUT', None, 1, 'ONE', BASE_OP + 3],
        [BASE_PORT + 4, 'regression_in', 'INPUT', None, 1, 'ONE', BASE_OP + 4],
        [BASE_PORT + 5, 'cluster_in', 'INPUT', None, 1, 'ONE', BASE_OP + 5]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port(conn):
    conn.execute(
        'DELETE from operation_port WHERE id BETWEEN %s AND %s',
        BASE_PORT + 1, BASE_PORT + 5)

def _insert_operation_port_translation(conn):
    tb = table('operation_port_translation',
               column('id', Integer),
               column('locale', String),
               column('name', String),
               column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_PORT + 1, 'pt', 'Modelo', 'Modelo.'],
        [BASE_PORT + 1, 'en', 'Model', 'Model.'],
        [BASE_PORT + 2, 'pt', 'Modelo Árvore', 'Modelo Árvore.'],
        [BASE_PORT + 2, 'en', 'Tree model', 'Tree model.'],
        [BASE_PORT + 3, 'pt', 'Aglomerado', 'Aglomerado.'],
        [BASE_PORT + 3, 'en', 'Ensemble', 'Ensemble.'],
        [BASE_PORT + 4, 'pt', 'Regressão', 'Regressão.'],
        [BASE_PORT + 4, 'en', 'Regression', 'Regression.'],
        [BASE_PORT + 5, 'pt', 'Cluster', 'Cluster.'],
        [BASE_PORT + 5, 'en', 'Clustering', 'Clustering.']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_port_translation(conn):
    conn.execute(
        'DELETE from operation_port_translation WHERE id BETWEEN %s AND %s',
        BASE_PORT + 1, BASE_PORT + 5)


def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
               column('operation_id', Integer),
               column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_OP + 1, BASE_CATEGORY + 1],
        [BASE_OP + 2, BASE_CATEGORY + 2],
        [BASE_OP + 2, BASE_CATEGORY + 3],
        [BASE_OP + 3, BASE_CATEGORY + 2],
        [BASE_OP + 3, BASE_CATEGORY + 3],
        [BASE_OP + 4, BASE_CATEGORY + 2],
        [BASE_OP + 4, BASE_CATEGORY + 3],
        [BASE_OP + 5, BASE_CATEGORY + 2],
        [BASE_OP + 5, BASE_CATEGORY + 3]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_category_operation(conn):
    conn.execute(
        'DELETE from operation_category_operation WHERE operation_id BETWEEN %s AND % s', BASE_OP + 1, BASE_OP + 5)

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
        [BASE_OP + 4, 41],
        [BASE_OP + 5, BASE_FORM + 5],
        [BASE_OP + 5, 110],
        [BASE_OP + 5, 41]
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_operation_form(conn):
    conn.execute(
        'DELETE from operation_operation_form WHERE operation_id BETWEEN %s AND %s',
        BASE_OP + 1, BASE_OP + 5)

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
        [BASE_OP + 4, BASE_PLATFORM + 1],
        [BASE_OP + 5, BASE_PLATFORM + 1]

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_platform(conn):
    conn.execute(
        'DELETE from operation_platform WHERE operation_id BETWEEN %s AND %s',
        BASE_OP + 1, BASE_OP + 5)

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

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_interface_operation_port(conn):
    conn.execute(
        'DELETE from operation_port_interface_operation_port WHERE operation_port_id BETWEEN % s AND %s ',
        BASE_PORT + 1, BASE_PORT + 5)

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
