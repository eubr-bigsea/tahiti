"""New operations definition

"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'f1ff40611872'
down_revision = 'a85dce88d899'
branch_labels = None
depends_on = None


BASE_CATEGORY = 45
BASE_OP = 4049
BASE_FORM = 4050
BASE_FORM_FIELD = 4392
BASE_PORT = 4111


def _insert_operation_category(conn):
    tb = table('operation_category',
                column('id', Integer), 
                column('type', String), 
                column('order', Integer), 
                column('default_order', Integer), 
	 )
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_CATEGORY + 1, 'group', 0, 2],
      [BASE_CATEGORY + 2, 'subgroup', 0, 0],
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
                column('name', String), 
	 )
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_CATEGORY + 1, 'en', 'Statistics'],
      [BASE_CATEGORY + 1, 'pt', 'Estatística'],
      [BASE_CATEGORY + 2, 'en', 'Probability distributions'],
      [BASE_CATEGORY + 2, 'pt', 'Distribuições de probabilidade'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_category_translation(conn):
    conn.execute(
        'DELETE from operation_category_translation WHERE id BETWEEN %s AND %s', 
        BASE_CATEGORY + 1, BASE_CATEGORY + 2)


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
      [BASE_OP + 1, 'pdf', True, 'TRANSFORMATION', '', '', ''],
      [BASE_OP + 2, 'cdf', True, 'TRANSFORMATION', '', '', ''],
      [BASE_OP + 3, 'rename-attr', True, 'TRANSFORMATION', '', '', ''],
      [BASE_OP + 4, 'ccdf', True, 'TRANSFORMATION', '', '', ''],
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
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_OP + 1, 'pt', 'Função de densidade de probabilidade', 'A função de densidade de probabilidade (PDF) é a probabilidade de que uma variável aleatória, digamos X, tenha um valor exatamente igual a x'],
      [BASE_OP + 1, 'en', 'Probability density function', 'The probability density function (PDF) is the probability that a random variable, say X, will take a value exactly equal to x'],
      [BASE_OP + 2, 'pt', 'Função cumulativa de distribuição', 'A função de distribuição cumulativa (CDF) calcula a probabilidade cumulativa para um determinado valor x. Use o CDF para determinar a probabilidade de que uma observação aleatória tirada da população seja menor ou igual a um certo valor. Você também pode usar essas informações para determinar a probabilidade de uma observação ser maior do que um determinado valor ou entre dois valores.'],
      [BASE_OP + 2, 'en', 'Cumulative distribution function', 'The cumulative distribution function (CDF) calculates the cumulative probability for a given x-value. Use the CDF to determine the probability that a random observation that is taken from the population will be less than or equal to a certain value. You can also use this information to determine the probability that an observation will be greater than a certain value, or between two values.'],
      [BASE_OP + 3, 'pt', 'Renomeia os atributos', 'Renomeia os atributos'],
      [BASE_OP + 3, 'en', 'Renames attributes', 'Renames attributes'],
      [BASE_OP + 4, 'pt', 'Função cumulativa inversa de distribuição', 'A função de distribuição cumulativa inversa (CCDF) calcula a probabilidade cumulativa para um determinado valor de x a 0. Use o CCDF para determinar a probabilidade de que uma observação aleatória tirada da população seja menor ou igual a um certo valor. Você também pode usar essas informações para determinar a probabilidade de uma observação ser maior do que um determinado valor ou entre dois valores.'],
      [BASE_OP + 4, 'en', 'Inverse cumulative distribution function', 'The inverse cumulative distribution function (CCDF) calculates the cumulative probability for a given range from x-value to 0. Use the CDF to determine the probability that a random observation that is taken from the population will be less than or equal to a certain value. You can also use this information to determine the probability that an observation will be greater than a certain value, or between two values.'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_translation(conn):
    conn.execute(
        'DELETE from operation_translation WHERE id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 4)


def _insert_operation_platform(conn):
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer),
    )
    columns = [c.name for c in tb.columns]
    data = [
	[BASE_OP + 1, 1],
	[BASE_OP + 1, 4],
	[BASE_OP + 2, 1],
	[BASE_OP + 2, 4],
	[BASE_OP + 3, 4],
	[BASE_OP + 4, 1],
	[BASE_OP + 4, 4],
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_platform(conn):
    conn.execute(
	'DELETE from operation_platform WHERE operation_id BETWEEN %s AND %s', 
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
      [BASE_OP + 1, 'JS_CLIENT', 1, "copyInputAddAttributesSplitAlias(task, 'attributes', 'alias', '_pdf');", BASE_OP + 1],
      [BASE_OP + 2, 'JS_CLIENT', 1, "copyInputAddAttributesSplitAlias(task, 'attributes', 'alias', '_cdf');", BASE_OP + 2],
      [BASE_OP + 3, 'JS_CLIENT', 1, "copyInputAddAttributesSplitAlias(task, 'attributes', 'alias', '_renamed');", BASE_OP + 3],
      [BASE_OP + 4, 'JS_CLIENT', 1, "copyInputAddAttributesSplitAlias(task, 'attributes', 'alias', '_ccdf');", BASE_OP + 4],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_script(conn):
    conn.execute(
        'DELETE from operation_script WHERE id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 4)


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
      [BASE_FORM_FIELD + 1, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'DESIGN', None, 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 2, 'alias', 'TEXT', 0, 2, None, 'text', None, None, 'DESIGN', None, 1, BASE_FORM + 1]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE form_id BETWEEN %s AND %s', 
        BASE_FORM + 1, BASE_FORM + 1)


def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM_FIELD + 1, 'pt', 'Atributo(s)', 'Atributos para a função'],
      [BASE_FORM_FIELD + 1, 'en', 'Attribute(s)', 'Attributes for the function'],
      [BASE_FORM_FIELD + 2, 'pt', 'Nome do(s) novo(s) atributo(s)', 'Nome do(s) novo(s) atributo(s)'],
      [BASE_FORM_FIELD + 2, 'en', 'Name of the new attributes', 'Name of the new attributes'],
    ]
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
        [BASE_OP + 1, BASE_CATEGORY + 1],
        [BASE_OP + 1, BASE_CATEGORY + 2],
        [BASE_OP + 1, 4001],
        [BASE_OP + 2, BASE_CATEGORY + 1],
        [BASE_OP + 2, BASE_CATEGORY + 2],
        [BASE_OP + 2, 4001],
        [BASE_OP + 3, 7],
        [BASE_OP + 3, 4001],
        [BASE_OP + 4, BASE_CATEGORY + 1],
        [BASE_OP + 4, BASE_CATEGORY + 2],
        [BASE_OP + 4, 4001],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_category_operation(conn):
    sql = "DELETE from operation_category_operation WHERE operation_id BETWEEN %s AND %s"
    conn.execute(sql, BASE_OP + 1, BASE_OP + 4)


def _insert_operation_operation_form(conn):
    tb = table('operation_operation_form',
                column('operation_id', Integer), 
                column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
	[BASE_OP + 1, BASE_FORM + 1],
	[BASE_OP + 1, 110],
	[BASE_OP + 1, 41],
	[BASE_OP + 2, BASE_FORM + 1],
	[BASE_OP + 2, 110],
	[BASE_OP + 2, 41],
	[BASE_OP + 3, BASE_FORM + 1],
	[BASE_OP + 3, 110],
	[BASE_OP + 3, 41],
	[BASE_OP + 4, BASE_FORM + 1],
	[BASE_OP + 4, 110],
	[BASE_OP + 4, 41],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_operation_form(conn):
    conn.execute(
        'DELETE from operation_operation_form WHERE operation_form_id BETWEEN %s AND %s', 
        BASE_FORM + 1, BASE_FORM + 4)


def _insert_operation_port(conn):
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('operation_id', Integer),
        column('order', Integer),
        column('multiplicity', String),
        column('slug', String))
    rows = [
        (BASE_PORT + 1, 'INPUT', None, BASE_OP + 1, 1, 'ONE', 'input data'),
        (BASE_PORT + 2, 'OUTPUT', None, BASE_OP + 1, 1, 'MANY', 'output data'),
        (BASE_PORT + 3, 'INPUT', None, BASE_OP + 2, 1, 'ONE', 'input data'),
        (BASE_PORT + 4, 'OUTPUT', None, BASE_OP + 2, 1, 'MANY', 'output data'),
        (BASE_PORT + 5, 'INPUT', None, BASE_OP + 3, 1, 'ONE', 'input data'),
        (BASE_PORT + 6, 'OUTPUT', None, BASE_OP + 3, 1, 'MANY', 'output data'),
        (BASE_PORT + 7, 'INPUT', None, BASE_OP + 4, 1, 'ONE', 'input data'),
        (BASE_PORT + 8, 'OUTPUT', None, BASE_OP + 4, 1, 'MANY', 'output data'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]
    op.bulk_insert(tb, rows)


def _delete_operation_port(conn):
    conn.execute(
        'DELETE from operation_port WHERE id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 8)


def _insert_operation_port_translation(conn):
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (BASE_PORT + 1, 'en', 'input data', 'Input data'),
        (BASE_PORT + 1, 'pt', 'dados de entrada', 'Dados de entrada'),

        (BASE_PORT + 2, 'en', 'output data', 'Output data'),
        (BASE_PORT + 2, 'pt', 'dados de saída', 'Dados de saída'),

        (BASE_PORT + 3, 'en', 'input data', 'Input data'),
        (BASE_PORT + 3, 'pt', 'dados de entrada', 'Dados de entrada'),

        (BASE_PORT + 4, 'en', 'output data', 'Output data'),
        (BASE_PORT + 4, 'pt', 'dados de saída', 'Dados de saída'),

        (BASE_PORT + 5, 'en', 'input data', 'Input data'),
        (BASE_PORT + 5, 'pt', 'dados de entrada', 'Dados de entrada'),

        (BASE_PORT + 6, 'en', 'output data', 'Output data'),
        (BASE_PORT + 6, 'pt', 'dados de saída', 'Dados de saída'),

        (BASE_PORT + 7, 'en', 'output data', 'Output data'),
        (BASE_PORT + 7, 'pt', 'dados de saída', 'Dados de saída'),

        (BASE_PORT + 8, 'en', 'output data', 'Output data'),
        (BASE_PORT + 8, 'pt', 'dados de saída', 'Dados de saída'),

    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]
    op.bulk_insert(tb, rows)


def _delete_operation_port_translation(conn):
    conn.execute(
        'DELETE from operation_port_translation WHERE id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 8)


def _insert_operation_port_interface_operation_port(conn):
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (BASE_PORT + 1, 1),
        (BASE_PORT + 2, 1),
        (BASE_PORT + 3, 1),
        (BASE_PORT + 4, 1),
        (BASE_PORT + 5, 1),
        (BASE_PORT + 6, 1),
        (BASE_PORT + 7, 1),
        (BASE_PORT + 8, 1),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)


def _delete_operation_port_interface_operation_port (conn):
    conn.execute(
        'DELETE from operation_port_interface_operation_port WHERE operation_port_id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 8)

    
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
        _insert_operation_category,
        _insert_operation_category_translation,
        _insert_operation,
        _insert_operation_translation,
        _insert_operation_platform,
        _insert_operation_script,
        _insert_operation_form,
        _insert_operation_form_translation,
        _insert_operation_form_field,
        _insert_operation_form_field_translation,
        _insert_operation_category_operation,
        _insert_operation_operation_form,
	_insert_operation_port,
	_insert_operation_port_translation,
	_insert_operation_port_interface_operation_port,
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
        _delete_operation_category,
        _delete_operation_category_translation,
        _delete_operation,
        _delete_operation_translation,
        _delete_operation_platform,
        _delete_operation_script,
        _delete_operation_form,
        _delete_operation_form_translation,
        _delete_operation_form_field,
        _delete_operation_form_field_translation,
        _delete_operation_category_operation,
        _delete_operation_operation_form,
	_delete_operation_port,
	_delete_operation_port_translation,
	_delete_operation_port_interface_operation_port,
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
