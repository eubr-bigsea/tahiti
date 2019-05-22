# -*- coding: utf-8 -*-}
"""survival analysis

Revision ID: acb362512a62
Revises: 910243d8f820
Create Date: 2018-01-31 17:18:58.543384

"""

from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'acb362512a62'
down_revision = '910243d8f820'
branch_labels = None
depends_on = None
KAPLAN_MEIER_SURVIVAL = 97
KAPLAN_MEIER_SURVIVAL_FORM_ID = 123

COX_PROPORTIONAL_HAZARDS_ID = 98
COX_PROPORTIONAL_HAZARDS_FORM_ID = 124

APPEARANCE_FORM_ID = 41
RESULTS_FORM_ID = 110


def _insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (27, 'en', 'Experimental'),
        (27, 'pt', 'Experimental'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category():
    operation_category_table = table('operation_category',
                                     column("id", Integer),
                                     column('type', String),
                                     )
    columns = ['id', 'type']
    all_categories = [
        (27, 'subgroup'),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in all_categories]

    op.bulk_insert(operation_category_table, rows)


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (KAPLAN_MEIER_SURVIVAL, 'kaplan-meier-survival', 1, 'TRANSFORMATION',
         'fa-space-shuttle'),
        (COX_PROPORTIONAL_HAZARDS_ID, 'cox-proportional-hazards', 1,
         'TRANSFORMATION', 'fa-space-shuttle'),
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
        (KAPLAN_MEIER_SURVIVAL, 'en', 'Kaplan-Meier survival',
         'Kaplan-Meier survival'),
        (KAPLAN_MEIER_SURVIVAL, 'pt', 'Kaplan-Meier survival',
         'Kaplan-Meier survival'),
        (COX_PROPORTIONAL_HAZARDS_ID, 'en', 'Cox proportional hazards',
         'Cox proportional hazards'),
        (COX_PROPORTIONAL_HAZARDS_ID, 'pt', 'Cox proportional hazards',
         'Cox proportional hazards'),
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
        (KAPLAN_MEIER_SURVIVAL, 1),
        (COX_PROPORTIONAL_HAZARDS_ID, 1),
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
        (KAPLAN_MEIER_SURVIVAL_FORM_ID, 1, 1, 'execution'),
        (COX_PROPORTIONAL_HAZARDS_FORM_ID, 1, 1, 'execution'),
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
        (KAPLAN_MEIER_SURVIVAL, KAPLAN_MEIER_SURVIVAL_FORM_ID),
        (KAPLAN_MEIER_SURVIVAL, APPEARANCE_FORM_ID),
        (KAPLAN_MEIER_SURVIVAL, RESULTS_FORM_ID),
        (COX_PROPORTIONAL_HAZARDS_ID, COX_PROPORTIONAL_HAZARDS_FORM_ID),
        (COX_PROPORTIONAL_HAZARDS_ID, APPEARANCE_FORM_ID),
        (KAPLAN_MEIER_SURVIVAL, RESULTS_FORM_ID),
        (COX_PROPORTIONAL_HAZARDS_ID, RESULTS_FORM_ID),
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
        (KAPLAN_MEIER_SURVIVAL_FORM_ID, 'en', 'Execution'),
        (KAPLAN_MEIER_SURVIVAL_FORM_ID, 'pt', 'Execução'),

        (COX_PROPORTIONAL_HAZARDS_FORM_ID, 'en', 'Execution'),
        (COX_PROPORTIONAL_HAZARDS_FORM_ID, 'pt', 'Execução'),
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
        (435, 'pivot_attribute', 'TEXT', 0, 3, None, 'attribute-selector',
         None, None, 'EXECUTION', KAPLAN_MEIER_SURVIVAL_FORM_ID),
        (436, 'duration_attribute', 'TEXT', 1, 1, None, 'attribute-selector',
         None, None, 'EXECUTION', KAPLAN_MEIER_SURVIVAL_FORM_ID),
        (437, 'event_observed_attribute', 'TEXT', 1, 2, None,
         'attribute-selector',
         None, None, 'EXECUTION', KAPLAN_MEIER_SURVIVAL_FORM_ID),

        (441, 'title', 'TEXT', 0, 4, None,
         'text', None, None, 'EXECUTION', KAPLAN_MEIER_SURVIVAL_FORM_ID),
        (442, 'legend', 'TEXT', 0, 5, None,
         'tag', None, None, 'EXECUTION', KAPLAN_MEIER_SURVIVAL_FORM_ID),

        (438, 'y_attribute', 'TEXT', 1, 1, None, 'attribute-selector',
         None, None, 'EXECUTION', COX_PROPORTIONAL_HAZARDS_FORM_ID),
        (439, 'time_attribute', 'TEXT', 1, 1, None, 'attribute-selector',
         None, None, 'EXECUTION', COX_PROPORTIONAL_HAZARDS_FORM_ID),
        (440, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector',
         None, None, 'EXECUTION', COX_PROPORTIONAL_HAZARDS_FORM_ID),

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
        (435, 'en', 'Pivot attribute',
         'Pivot attribute is used to create groups. Each group will be '
         'fit by the model;'),
        (435, 'pt', 'Atributo pivô', 'Atributo pivô usado para criar grupos.'
                                     'Cada grupo será a entrada para o modelo.'),

        (436, 'en', 'Duration attribute', 'Duration subject was observed for.'),
        (436, 'pt', 'Atributo com a duração',
         'Duração observada para o assunto.'),

        (437, 'en', 'Observed event attribute',
         'True if the the death was observed, False if the event '
         'was lost (right-censored).'),
        (437, 'pt', 'Atributo para evento observado',
         'Se VERDADEIRO, a morte foi observada, FALSO se o evento '
         'foi perdido.'),

        (438, 'en', 'Y attribute', 'Attribute with Y-axis values.'),
        (438, 'pt', 'Atributo Y', 'Atributo com o valores para eixo Y.'),

        (439, 'en', 'Time attribute', 'Attribute with time values.'),
        (439, 'pt', 'Atributo Temporal', 'Atributo com o valores temporais.'),

        (440, 'en', 'Attributes', 'Attributes used for the analysis'),
        (440, 'pt', 'Atributos', 'Atributos usados para a análise.'),

        (441, 'en', 'Chart Title',
         'Title for the graph.'),
        (441, 'pt', 'Título do gráfico',
         'Título usado para o gráfico.'),
        (442, 'en', 'Legend',
         'Values for legend. If not informed, it will be autogenerated.'),
        (442, 'pt', 'Legenda',
         'Valores para a legenda. Se não informados, eles serão'
         'gerados automaticamente.'),

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
        (KAPLAN_MEIER_SURVIVAL, 1),
        (KAPLAN_MEIER_SURVIVAL, 8),
        (KAPLAN_MEIER_SURVIVAL, 27),

        (COX_PROPORTIONAL_HAZARDS_ID, 1),
        (COX_PROPORTIONAL_HAZARDS_ID, 8),
        (COX_PROPORTIONAL_HAZARDS_ID, 27),
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
        (223, 'OUTPUT', None, KAPLAN_MEIER_SURVIVAL, 1, 'MANY', 'output data'),
        (224, 'INPUT', None, KAPLAN_MEIER_SURVIVAL, 1, 'ONE', 'input data'),

        (225, 'OUTPUT', None, COX_PROPORTIONAL_HAZARDS_ID, 1, 'MANY',
         'output data'),
        (226, 'INPUT', None, COX_PROPORTIONAL_HAZARDS_ID, 1, 'ONE',
         'input data'),
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
        (223, 'en', 'output data', 'Output data'),
        (223, 'pt', 'dados de saída', 'Dados de saída'),
        (224, 'en', 'input data', 'Input data'),
        (224, 'pt', 'dados de entrada', 'Dados de entrada'),

        (225, 'en', 'output data', 'Output data'),
        (225, 'pt', 'dados de saída', 'Dados de saída'),
        (226, 'en', 'input data', 'Input data'),
        (226, 'pt', 'dados de entrada', 'Dados de entrada'),

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
        (223, 1),
        (224, 1),
        (225, 1),
        (226, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id = 27'),
    (_insert_operation_category_translation,
     'DELETE FROM operation_category_translation WHERE id = 27'),

    (_insert_operation,
     'DELETE FROM operation WHERE id IN ({}, {})'.format(
         KAPLAN_MEIER_SURVIVAL, COX_PROPORTIONAL_HAZARDS_ID)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN ({}, {})'.format(
         KAPLAN_MEIER_SURVIVAL, COX_PROPORTIONAL_HAZARDS_ID)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = 1 AND operation_id IN ({}, {})'.format(
         KAPLAN_MEIER_SURVIVAL, COX_PROPORTIONAL_HAZARDS_ID)),
    (_insert_operation_category_operation,
     'DELETE from operation_category_operation '
     'WHERE operation_id IN ({}, {})'.format(KAPLAN_MEIER_SURVIVAL,
                                             COX_PROPORTIONAL_HAZARDS_ID)),
    (_insert_operation_port,
     "DELETE FROM operation_port WHERE id in (223, 224, 225, 226)"),
    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id in "
     "(223, 224, 225, 226)"),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id in (223, 224, 225, 226)"),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN ({0}, {1})'.format(
         KAPLAN_MEIER_SURVIVAL_FORM_ID, COX_PROPORTIONAL_HAZARDS_FORM_ID)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({0}, {1})'.format(KAPLAN_MEIER_SURVIVAL,
                                               COX_PROPORTIONAL_HAZARDS_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation  WHERE id IN ({0}, {1})'.format(
         KAPLAN_MEIER_SURVIVAL_FORM_ID, COX_PROPORTIONAL_HAZARDS_FORM_ID)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id IN ({0}, {1})'.format(
         KAPLAN_MEIER_SURVIVAL_FORM_ID, COX_PROPORTIONAL_HAZARDS_FORM_ID)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id IN ({0}, {1}))'.format(
         KAPLAN_MEIER_SURVIVAL_FORM_ID, COX_PROPORTIONAL_HAZARDS_FORM_ID)),

    (
        '''INSERT INTO
        operation_script(id, `type`, enabled, body, operation_id)
        VALUES (46, 'JS_CLIENT', '1',
        'onlyField(task, "x_attribute", true);', {})'''.format(
            KAPLAN_MEIER_SURVIVAL),
        '''DELETE FROM operation_script WHERE id = 46'''
    ),
    (
        '''INSERT INTO
        operation_script(id, `type`, enabled, body, operation_id)
        VALUES (47, 'JS_CLIENT', '1',
        'onlyField(task, "x_attribute", true);', {})'''.format(
            COX_PROPORTIONAL_HAZARDS_ID),
        '''DELETE FROM operation_script WHERE id = 47'''
    ),

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
    session.commit()
