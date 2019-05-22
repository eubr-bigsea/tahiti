# coding=utf-8
"""histogram

Revision ID: f39f7e2623e3
Revises: ea3e48aa084c
Create Date: 2019-04-25 11:26:55.487830

"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'f39f7e2623e3'
down_revision = 'ea3e48aa084c'
branch_labels = None
depends_on = None

HISTOGRAM_ID = 124
HISTOGRAM_FORM_ID = 135

APPEARANCE_FORM_ID = 41
RESULTS_FORM_ID = 110


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (HISTOGRAM_ID, 'histogram', 1, 'TRANSFORMATION', 'fa-chart'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (HISTOGRAM_ID, 'en', 'Histogram',
         'A histogram is a plot that lets you discover, and show, the '
         'underlying frequency distribution (shape) of a set of continuous '
         'data. This allows the inspection of the data for its '
         'underlying distribution (e.g., normal distribution), '
         'outliers, skewness, etc.'),
        (HISTOGRAM_ID, 'pt', 'Histograma',
         'Um histograma é um gráfico que permite descobrir e mostrar '
         'a distribuição de frequência subjacente (forma) de um '
         'conjunto de dados contínuos. '
         'Isso permite a inspeção dos dados para sua distribuição subjacente '
         '(por exemplo, distribuição normal), outliers, assimetria, etc.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        (HISTOGRAM_ID, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form():
    tb = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (HISTOGRAM_FORM_ID, 1, 1, 'execution'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (HISTOGRAM_ID, HISTOGRAM_FORM_ID),
        (HISTOGRAM_ID, APPEARANCE_FORM_ID),
        (HISTOGRAM_ID, RESULTS_FORM_ID),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String)
    )

    columns = [c.name for c in tb.columns]
    data = [
        (HISTOGRAM_FORM_ID, 'en', 'Execution'),
        (HISTOGRAM_FORM_ID, 'pt', 'Execução'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form_field():
    tb = table(
        'operation_form_field',
        column('id', Integer),
        column('name', String),
        column('type', String),
        column('required', Integer),
        column('order', Integer),
        column('default', Text),
        column('suggested_widget', String),
        column('values_url', String),
        column('values', String),
        column('scope', String),
        column('form_id', Integer), )

    columns = [c.name for c in tb.columns]

    data = [
        (496, 'title', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION',
         HISTOGRAM_FORM_ID),
        (497, 'attributes', 'TEXT', 1, 2, None, 'attribute-selector',
         None, None, 'EXECUTION', HISTOGRAM_FORM_ID),
        (498, 'bins', 'INTEGER', 0, 3, '10', 'integer',
         None, None, 'EXECUTION', HISTOGRAM_FORM_ID),
        (499, 'x_title', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION',
         HISTOGRAM_FORM_ID),
        (500, 'y_title', 'TEXT', 0, 6, None, 'text', None, None, 'EXECUTION',
         HISTOGRAM_FORM_ID),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (496, 'en', 'Chart Title', 'Title for the chart'),
        (496, 'pt', 'Título', 'Título para o gráfico'),

        (497, 'en', 'Input attribute(s)',
         'Generate a histogram for each one of these attributes.'),
        (497, 'pt', 'Atributo(s) de entrada',
         'Gera um histograma para cada um destes atributos.'),

        (498, 'en', 'Number of bins',
         'How many intervals data is split.'),
        (498, 'pt', 'Quantidade de intervalos (bins)',
         'Em quantos intervalos os dados serão divididos.'),

        (499, 'en', 'X-axis title', 'X-axis title.'),
        (499, 'pt', 'Título para o eixo X', 'Título para o eixo X.'),

        (500, 'en', 'Y-axis title', 'Y-axis title.'),
        (500, 'pt', 'Título para o eixo Y', 'Título para o eixo Y.'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (HISTOGRAM_ID, 1),
        (HISTOGRAM_ID, 15),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


#
def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('operation_id', Integer),
        column('order', Integer),
        column('multiplicity', String),
        column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (297, 'OUTPUT', None, HISTOGRAM_ID, 1, 'MANY', 'visualization'),
        (298, 'INPUT', None, HISTOGRAM_ID, 1, 'ONE', 'input data'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (297, 'en', 'visualization', 'Visualization'),
        (297, 'pt', 'visualization', 'Visualização'),

        (298, 'en', 'input data', 'Input data'),
        (298, 'pt', 'dados de entrada', 'Dados de entrada'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = [c.name for c in tb.columns]
    data = [
        (297, 19),
        (298, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation,
     'DELETE FROM operation WHERE id IN ({})'.format(HISTOGRAM_ID)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN ({})'.format(HISTOGRAM_ID)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = 1 AND operation_id IN ({})'.format(HISTOGRAM_ID)),
    (_insert_operation_category_operation,
     'DELETE from operation_category_operation '
     'WHERE operation_id IN ({})'.format(HISTOGRAM_ID)),
    (_insert_operation_port,
     "DELETE FROM operation_port WHERE id in (297, 298)"),
    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id in (297, 298)"),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id in (297, 298)"),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN ({0})'.format(HISTOGRAM_FORM_ID)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({0})'.format(HISTOGRAM_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation  WHERE id IN ({0})'.format(
         HISTOGRAM_FORM_ID)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id IN ({0})'.format(
         HISTOGRAM_FORM_ID)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id IN ({0}))'.format(HISTOGRAM_FORM_ID)),

]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    connection.execute('SET FOREIGN_KEY_CHECKS=0;')
    try:
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    session.commit()
