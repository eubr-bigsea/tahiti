# coding=utf-8
"""box_plot

Revision ID: ea3e48aa084c
Revises: 437099b06855
Create Date: 2019-04-16 08:29:24.212398

"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'ea3e48aa084c'
down_revision = '437099b06855'
branch_labels = None
depends_on = None

BOX_PLOT_ID = 123
BOX_PLOT_FORM_ID = 134

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
        (BOX_PLOT_ID, 'box-plot', 1, 'TRANSFORMATION', 'fa-chart'),
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
        (BOX_PLOT_ID, 'en', 'Box plot',
         'A box plot or boxplot is a method for graphically depicting groups '
         'of numerical data through their quartiles'),
        (BOX_PLOT_ID, 'pt', 'Box plot',
         'Diagrama de caixa, diagrama de extremos e quartis, boxplot ou box '
         'plot é uma ferramenta gráfica para representar a variação de dados '
         'observados de uma variável numérica por meio de quartis.'),
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
        (BOX_PLOT_ID, 1),
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
        (BOX_PLOT_FORM_ID, 1, 1, 'execution'),
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
        (BOX_PLOT_ID, BOX_PLOT_FORM_ID),
        (BOX_PLOT_ID, APPEARANCE_FORM_ID),
        (BOX_PLOT_ID, RESULTS_FORM_ID),
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
        (BOX_PLOT_FORM_ID, 'en', 'Execution'),
        (BOX_PLOT_FORM_ID, 'pt', 'Execução'),
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
        (490, 'title', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION',
         BOX_PLOT_FORM_ID),
        (491, 'fact_attributes', 'TEXT', 1, 2, None, 'attribute-selector',
         None, None, 'EXECUTION', BOX_PLOT_FORM_ID),
        (492, 'group_attribute', 'TEXT', 0, 3, None, 'attribute-selector',
         None, None, 'EXECUTION', BOX_PLOT_FORM_ID),
        (493, 'show_outliers', 'INTEGER', 0, 4, None, 'checkbox',
         None, None, 'EXECUTION', BOX_PLOT_FORM_ID),
        (494, 'x_title', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION',
         BOX_PLOT_FORM_ID),
        (495, 'y_title', 'TEXT', 0, 6, None, 'text', None, None, 'EXECUTION',
         BOX_PLOT_FORM_ID),

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
        (490, 'en', 'Chart Title', 'Title for the chart'),
        (490, 'pt', 'Título', 'Título para o gráfico'),

        (491, 'en', 'Input attribute(s)',
         'Calculate and box plot quartiles for these attributes.'),
        (491, 'pt', 'Atributo(s) de entrada',
         'Atributos usados para calcular os quartis e gerar o box plot.'),

        (492, 'en', 'Grouping attribute (x-axis)',
         'Input data will be grouped by this attribute and quartiles will be '
         'calculated for each group. Each group will be a box in x-axis.'),
        (492, 'pt', 'Atributo usado para agrupar (x-axis)',
         'Os dados de entrada serão agrupados por este atributo e os quartis '
         'serão calculados para cada grupo. Cada grupo será uma caixa no '
         'eixo X.'),

        (493, 'en', 'Show outliers', 'Display outliers'),
        (493, 'pt', 'Exibir discrepantes', 'Exibir discrepantes (outliers).'),

        (494, 'en', 'X-axis title', 'X-axis title.'),
        (494, 'pt', 'Título para o eixo X', 'Título para o eixo X.'),

        (495, 'en', 'Y-axis title', 'Y-axis title.'),
        (495, 'pt', 'Título para o eixo Y', 'Título para o eixo Y.'),

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
        (BOX_PLOT_ID, 1),
        (BOX_PLOT_ID, 15),
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
        (295, 'OUTPUT', None, BOX_PLOT_ID, 1, 'MANY', 'visualization'),
        (296, 'INPUT', None, BOX_PLOT_ID, 1, 'ONE', 'input data'),
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
        (295, 'en', 'visualization', 'Visualization'),
        (295, 'pt', 'visualization', 'Visualização'),

        (296, 'en', 'input data', 'Input data'),
        (296, 'pt', 'dados de entrada', 'Dados de entrada'),

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
        (295, 19),
        (296, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation,
     'DELETE FROM operation WHERE id IN ({})'.format(BOX_PLOT_ID)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN ({})'.format(BOX_PLOT_ID)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = 1 AND operation_id IN ({})'.format(BOX_PLOT_ID)),
    (_insert_operation_category_operation,
     'DELETE from operation_category_operation '
     'WHERE operation_id IN ({})'.format(BOX_PLOT_ID)),
    (_insert_operation_port,
     "DELETE FROM operation_port WHERE id in (295, 296)"),
    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id in (295, 296)"),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id in (295, 296)"),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN ({0})'.format(BOX_PLOT_FORM_ID)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({0})'.format(BOX_PLOT_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation  WHERE id IN ({0})'.format(
         BOX_PLOT_FORM_ID)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id IN ({0})'.format(
         BOX_PLOT_FORM_ID)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id IN ({0}))'.format(BOX_PLOT_FORM_ID)),

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
