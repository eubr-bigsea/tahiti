"""Log scale for histogram

"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'da33b611f281'
down_revision = 'a0d6c6699b69'
branch_labels = None
depends_on = None


HISTOGRAM_ID = 124
HIST_ORIG_EXECUTION_FORM = 135

BASE_FORM_FIELD = 644
BASE_FORM = 156


# Not necessary to really show an operation
def _insert_operation_form(conn):
    tb = table('operation_form',
                column('id', Integer), 
                column('enabled', Boolean), 
                column('order', Integer), 
                column('category', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM + 1, True, 0, 'execution'],
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
                column('default', Text),
                column('suggested_widget', String),
                column('values_url', String),
                column('values', Text),
                column('scope', String),
                column('form_id', Integer),
                column('enable_conditions', String),
                column('editable', Boolean),
	)
    columns = [c.name for c in tb.columns]
    data = [
         [BASE_FORM_FIELD + 1, 'title', 'TEXT', False, 1, None, 'text', None, None, 'EXECUTION', BASE_FORM + 1, None, True],
         [BASE_FORM_FIELD + 2, 'attributes', 'TEXT', True, 2, None, 'attribute-selector', None, None, 'EXECUTION', BASE_FORM + 1, None, True],
         [BASE_FORM_FIELD + 3, 'bins', 'INTEGER', False, 3, '10', 'integer', None, None, 'EXECUTION', BASE_FORM + 1, None, True],
         [BASE_FORM_FIELD + 4, 'x_title', 'TEXT', False, 5, None, 'text', None, None, 'EXECUTION', BASE_FORM + 1, None, True],
         [BASE_FORM_FIELD + 5, 'x_log_scale', 'TEXT', False, 5, None, 'checkbox', None, None, 'EXECUTION', BASE_FORM + 1, None, True],
         [BASE_FORM_FIELD + 6, 'y_title', 'TEXT', False, 6, None, 'text', None, None, 'EXECUTION', BASE_FORM + 1, None, True],
         [BASE_FORM_FIELD + 7, 'y_log_scale', 'TEXT', False, 6, None, 'checkbox', None, None, 'EXECUTION', BASE_FORM + 1, None, True],
 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 7)


def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM_FIELD + 1, 'en', 'Chart Title', 'Title for the chart'],
      [BASE_FORM_FIELD + 1, 'pt', 'Título', 'Título para o gráfico'],
      [BASE_FORM_FIELD + 2, 'en', 'Input attribute(s)', 'Generate a histogram for each one of these attributes.'],
      [BASE_FORM_FIELD + 2, 'pt', 'Atributo(s) de entrada', 'Gera um histograma para cada um destes atributos.'],
      [BASE_FORM_FIELD + 3, 'en', 'Number of bins', 'How many intervals data is split.'],
      [BASE_FORM_FIELD + 3, 'pt', 'Quantidade de intervalos (bins)', 'Em quantos intervalos os dados serão divididos.'],
      [BASE_FORM_FIELD + 4, 'en', 'X-axis title', 'X-axis title.'],
      [BASE_FORM_FIELD + 4, 'pt', 'Título para o eixo X', 'Título para o eixo X.'],
      [BASE_FORM_FIELD + 5, 'en', 'X log scale', 'X log scale.'],
      [BASE_FORM_FIELD + 5, 'pt', 'Escala log eixo X', 'Escala log eixo X.'],
      [BASE_FORM_FIELD + 6, 'en', 'Y-axis title', 'Y-axis title.'],
      [BASE_FORM_FIELD + 6, 'pt', 'Título para o eixo Y', 'Título para o eixo Y.'],
      [BASE_FORM_FIELD + 7, 'en', 'Y log scale', 'Y log scale.'],
      [BASE_FORM_FIELD + 7, 'pt', 'Escala log eixo Y', 'Escala log eixo Y.'],
 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_form_field_translation(conn):
    conn.execute(
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 5)


def _upgrade_operation_operation_form(conn):
    conn.execute(
	'UPDATE operation_operation_form SET operation_form_id = {op_form_id} WHERE (operation_id = {hist_id} AND operation_form_id = {hist_orig_form});'.format(hist_id=HISTOGRAM_ID, hist_orig_form=HIST_ORIG_EXECUTION_FORM, op_form_id=BASE_FORM + 1)
    )

def _downgrade_operation_operation_form(conn):
    conn.execute(
	'UPDATE operation_operation_form SET operation_form_id = {op_form_id} WHERE (operation_id = {hist_id} AND operation_form_id = {hist_orig_form});'.format(hist_id=HISTOGRAM_ID, op_form_id=HIST_ORIG_EXECUTION_FORM, hist_orig_form=BASE_FORM + 1)
    )

    
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
        _insert_operation_form,
        _insert_operation_form_translation,
        _insert_operation_form_field,
        _insert_operation_form_field_translation,
        _upgrade_operation_operation_form,
    ]
    try:
        for cmd in commands:
            #import pdb; pdb.set_trace()
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
        _delete_operation_form,
        _delete_operation_form_translation,
        _delete_operation_form_field,
        _delete_operation_form_field_translation,
        _downgrade_operation_operation_form,
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
