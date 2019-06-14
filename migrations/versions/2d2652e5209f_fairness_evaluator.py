# coding=utf-8
"""fairness_evaluator

Revision ID: 2d2652e5209f
Revises: 950bf9412aac
Create Date: 2018-06-05 18:04:24.959057

"""
import json

from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '2d2652e5209f'
down_revision = '950bf9412aac'
branch_labels = None
depends_on = None

FAIRNESS_EVALUATOR_ID = 103

OPERATIONS = ', '.join([str(FAIRNESS_EVALUATOR_ID)])

FAIRNESS_EVALUATOR_FORM_ID = 129

FORMS = ', '.join([
    str(FAIRNESS_EVALUATOR_FORM_ID)])

APPEARANCE_FORM_ID = 41
RESULTS_FORM_ID = 110
OPERATION_CATEGORIES = 28
PORT_RANGE = ', '.join([str(x) for x in [237, 238]])


def _insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (28, 'en', 'Trustworthiness'),
        (28, 'pt', 'Confiabilidade'),
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
        (28, 'group'),
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
        (FAIRNESS_EVALUATOR_ID, 'fairness-evaluator', 1, 'TRANSFORMATION',
         'fa-balance-scale'),
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
        (FAIRNESS_EVALUATOR_ID, 'en', 'Fairness evaluator',
         'Evaluates if the result of a classifier is fair according to '
         'different criteria.'),
        (FAIRNESS_EVALUATOR_ID, 'pt', 'Avaliador de justiça',
         'Avalia se o resultado de um classificador é justo segundo diferentes '
         'critérios.'),
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
        (FAIRNESS_EVALUATOR_ID, 1),
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
        (FAIRNESS_EVALUATOR_FORM_ID, 1, 1, 'execution'),
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
        (FAIRNESS_EVALUATOR_ID, FAIRNESS_EVALUATOR_FORM_ID),
        (FAIRNESS_EVALUATOR_ID, APPEARANCE_FORM_ID),
        (FAIRNESS_EVALUATOR_ID, RESULTS_FORM_ID),
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
        (FAIRNESS_EVALUATOR_FORM_ID, 'en', 'Execution'),
        (FAIRNESS_EVALUATOR_FORM_ID, 'pt', 'Execução'),
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

    types = [
        {"key": "aequitas", "value": "Aequitas", "en": "Aequitas",
         "pt": "Aequitas"}]
    data = [
        (470, 'attributes', 'TEXT', 1, 0, None, 'attribute-selector', None,
         None, 'EXECUTION', FAIRNESS_EVALUATOR_FORM_ID),
        (471, 'type', 'TEXT', 0, 1, 'aequitas', 'dropdown', None,
         json.dumps(types), 'EXECUTION',
         FAIRNESS_EVALUATOR_FORM_ID),
        (472, 'tau', 'FLOAT', 1, 2, '0.8', 'decimal', None, None,
         'EXECUTION', FAIRNESS_EVALUATOR_FORM_ID),
        (473, 'label', 'TEXT', 0, 3, 'label', 'attribute-selector', None,
         None, 'EXECUTION', FAIRNESS_EVALUATOR_FORM_ID),
        (474, 'score', 'TEXT', 0, 4, 'score', 'attribute-selector', None,
         None, 'EXECUTION', FAIRNESS_EVALUATOR_FORM_ID),
        (475, 'baseline', 'TEXT', 1, 5, None, 'textarea', None, None,
         'EXECUTION', FAIRNESS_EVALUATOR_FORM_ID),
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
        (470, 'en', 'Sensitive feature attribute(s)',
         'Sensitive attribute(s)'),
        (470, 'pt', 'Atributos sensíveis (sujeitos a injustiça/discriminação)',
         'Atributos sensíveis (sujeitos a injustiça/discriminação).'),
        (471, 'en', 'Type of fairness evaluation',
         'Type of fairness evaluation.'),
        (471, 'pt', 'Tipo de avaliação de justiça',
         'Tipo de avaliação de justiça.'),
        (472, 'en', 'Value for boundaries calculation',
         '''Value for boundaries calculation. The value v for the metric should
         be in the range v < metric < 1/v to the metric be fair.'''),
        (472, 'pt', 'Valor para cálculo dos limites de cálculo',
         '''Valor para cálculo dos limites de cálculo. O valor v da métrica
         deverá estar na faixa v < metrica < 1/v para a métrica ser justa.'''),
        (473, 'en', 'Label attribute with the real value',
         'Label attribute with the real value.'),
        (473, 'pt', 'Atributo para rótulo com o valor real',
         'Atributo para rótulo com o valor real.'),
        (474, 'en', 'Score attribute with assigned result (prediction)',
         'Score attribute with assigned result (prediction).'),
        (474, 'pt', 'Atributo com o score com o resultado atribuído (predição)',
         'Atributo com o score com o resultado atribuído (predição).'),
        (475, 'en', '''Baseline value(s) used to contrast other values against
            (same order as sensitive parameter, comma separated)''',
         'Baseline value used to contrast other values against.'),
        (475, 'pt',
         '''Valor de referência usado para contrastar com os outros valores
         (mesma ordem do parâmetro atributos sensíveis, separado por vírgula
         )''',
         'Valor de referência usado para contrastar com os outros valores.'),
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
        (FAIRNESS_EVALUATOR_ID, 28),
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
        (237, 'INPUT', None, FAIRNESS_EVALUATOR_ID, 1, 'ONE',
         'input data'),
        (238, 'OUTPUT', None, FAIRNESS_EVALUATOR_ID, 1, 'MANY',
         'output data'),
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
        (237, 'en', 'input data', 'Input data'),
        (237, 'pt', 'dados de entrada', 'Dados de entrada'),
        (238, 'en', 'output data', 'Output data'),
        (238, 'pt', 'dados de saída', 'Dados de saída'),

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
        (237, 1),
        (238, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id IN ({})'.format(
         OPERATION_CATEGORIES)),
    (_insert_operation_category_translation,
     'DELETE FROM operation_category_translation WHERE id IN ({})'.format(
         OPERATION_CATEGORIES)),
    (_insert_operation,
     'DELETE FROM operation WHERE id IN ({})'.format(
         OPERATIONS)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN ({})'.format(
         OPERATIONS)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = 1 AND operation_id IN ({})'.format(
         OPERATIONS)),
    (_insert_operation_category_operation,
     'DELETE from operation_category_operation '
     'WHERE operation_id IN ({})'.format(OPERATIONS)),
    (_insert_operation_port,
     "DELETE FROM operation_port WHERE id in ({})".format(PORT_RANGE)),
    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id in "
     "({})".format(PORT_RANGE)),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id in ({})".format(PORT_RANGE)),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN ({})'.format(
         FORMS)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({})'.format(OPERATIONS)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation  WHERE id IN ({})'.format(
         FORMS)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id IN ({})'.format(
         FORMS)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id IN ({}))'.format(
         FORMS)),
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
    connection.execute('SET foreign_key_checks = 0;')

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
    connection.execute('SET foreign_key_checks = 1;')
    session.commit()
