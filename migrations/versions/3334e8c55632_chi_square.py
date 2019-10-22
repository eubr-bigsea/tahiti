"""Chi-square

Revision ID: 3334e8c55632
Revises: f98150821301
Create Date: 2019-10-21 14:51:35.574727

"""
import json

from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '3334e8c55632'
down_revision = 'f98150821301'
branch_labels = None
depends_on = None

CHI_ID = 126
CHI_FORM_ID = 137
RESULTS_FORM_ID = 110
APPEARANCE_FORM_ID = 41
NEXT_ATTRIBUTE_ID = 504
NEXT_PORT_ID = 299
CATEGORY_FEATURE_SELECTION = 44
CATEGORY_DATA_PROCESSING = 32


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (CHI_ID, 'chi-sq-selector', 1, 'TRANSFORMATION', 'fa-chart'),
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
        (CHI_ID, 'en', 'Chi-square selector',
         'Selects categorical features to use for predicting a '
         'categorical label. But features must be converted to a numerical '
         'representation before using this operation.'),
        (CHI_ID, 'pt', 'Seletor chi-square',
         'Seleciona features categórias para serem usadas para predizer um '
         'rótulo categórico. Mas as features devem ser convertidas para uma '
         'representação numérica antes de usar esta operação.'),
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
        (CHI_ID, 1),
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
        (CHI_FORM_ID, 1, 1, 'execution'),
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
        (CHI_ID, CHI_FORM_ID),
        (CHI_ID, RESULTS_FORM_ID),
        (CHI_ID, APPEARANCE_FORM_ID),
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
        (CHI_FORM_ID, 'en', 'Execution'),
        (CHI_FORM_ID, 'pt', 'Execução'),
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
        column('form_id', Integer),
        column('enable_conditions', Integer),
    )

    columns = [c.name for c in tb.columns]

    options = [
        {"key": "numTopFeatures", "value": "Number of top features",
         "en": "Number of top features",
         "pt": "Número de top features"},
        {"key": "percentile", "value": "Percentile", "en": "Percentile",
         "pt": "Percentil"},
        {"key": "fpr", "value": "Highest p-value for features to be kept (FPR)",
         "en": "Highest p-value for features to be kept (FPR)",
         "pt": "Valor de p-value para que a feature seja mantida (FPR)"},
        {"key": "fdr", "value": "False-discovery rate (FDR)",
         "en": "False-discovery rate (FDR)",
         "pt": "Taxa de falsas descobertas (FDR)"},
        {"key": "fwe", "value": "Family-wise error (FWE)",
         "en": "Family-wise error (FWE)",
         "pt": "Taxa do erro conjunto (FWE)"},
    ]
    data = [
        (NEXT_ATTRIBUTE_ID + 0, 'attributes', 'TEXT', 1, 1, None,
         'attribute-selector', None, None, 'EXECUTION', CHI_FORM_ID, None),
        (NEXT_ATTRIBUTE_ID + 1, 'label', 'TEXT', 1, 2, None,
         'attribute-selector', None, None, 'EXECUTION', CHI_FORM_ID, None),
        (NEXT_ATTRIBUTE_ID + 2, 'alias', 'TEXT', 0, 3, 'chi_output',
         'text', None, None, 'EXECUTION', CHI_FORM_ID, None),
        (NEXT_ATTRIBUTE_ID + 3, 'selector_type', 'TEXT', 1, 4, 'numTopFeatures',
         'dropdown', None, json.dumps(options), 'EXECUTION', CHI_FORM_ID, None),
        (NEXT_ATTRIBUTE_ID + 4, 'num_top_features', 'INTEGER', 0, 5, 50,
         'text', None, None, 'EXECUTION', CHI_FORM_ID,
            'this.selector_type.internalValue === "numTopFeatures"'),
        (NEXT_ATTRIBUTE_ID + 5, 'percentile', 'FLOAT', 0, 6, '0.1',
         'decimal', None, None, 'EXECUTION', CHI_FORM_ID,
            'this.selector_type.internalValue === "percentile"'),
        (NEXT_ATTRIBUTE_ID + 6, 'fpr', 'FLOAT', 0, 7, '0.05',
         'decimal', None, None, 'EXECUTION', CHI_FORM_ID,
            'this.selector_type.internalValue === "fpr"'),
        (NEXT_ATTRIBUTE_ID + 7, 'fdr', 'FLOAT', 0, 8, '0.05',
         'decimal', None, None, 'EXECUTION', CHI_FORM_ID,
            'this.selector_type.internalValue === "fdr"'),
        (NEXT_ATTRIBUTE_ID + 8, 'fwe', 'FLOAT', 0, 9, '0.05',
         'decimal', None, None, 'EXECUTION', CHI_FORM_ID,
            'this.selector_type.internalValue === "fwe"'),

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
        (NEXT_ATTRIBUTE_ID + 0, 'en', 'Features',
         'Features (must have been converted to numeric).'),
        (NEXT_ATTRIBUTE_ID + 0, 'pt', 'Features',
         'Features (Devem ter sido convertidas para numérico).'),

        (NEXT_ATTRIBUTE_ID + 1, 'en', 'Label attribute',
         'Label attribute.'),
        (NEXT_ATTRIBUTE_ID + 1, 'pt', 'Atributo com o rótulo',
         'Atributo com o rótulo.'),

        (NEXT_ATTRIBUTE_ID + 2, 'en', 'Output attribute',
         'Output attribute.'),
        (NEXT_ATTRIBUTE_ID + 2, 'pt', 'Atributo de saída',
         'Atributo de saída.'),

        (NEXT_ATTRIBUTE_ID + 3, 'en', 'Selection type',
         'Selection type.'),
        (NEXT_ATTRIBUTE_ID + 3, 'pt', 'Tipo de seleção',
         'Tipo de seleção.'),

        (NEXT_ATTRIBUTE_ID + 4, 'en', 'Number of top features',
         'Number of features that will be selected, '
         'ordered by ascendin4 p-value.'),
        (NEXT_ATTRIBUTE_ID + 4, 'pt', 'Quantidade de top features',
         'Quantidade de features que serão selecionadas, ordenadas de forma '
         'ascendente pelo p-value.'),

        (NEXT_ATTRIBUTE_ID + 5, 'en',
         'Percentile in range (0,1] (value >0 and <=1)',
         'Percentile of features that will be selected, ordered by '
         'ascending p-value.'),
        (NEXT_ATTRIBUTE_ID + 5, 'pt',
         'Percentil na faixa (0,1] (valor >0 e <=1)',
         'Percentil das features que serão selecionadas, ordenadas pelo '
         'p-value de forma ascendente.'),

        (NEXT_ATTRIBUTE_ID + 6, 'en',
         'Highest p-value for features to be kept (FPR)',
         'Highest p-value for features to be kept (FPR).'),
        (NEXT_ATTRIBUTE_ID + 6, 'pt',
         'Maior valor de p-value para feature ser mantida (FPR).',
         'Maior valor de p-value para feature ser mantida (FPR).'),

        (NEXT_ATTRIBUTE_ID + 7, 'en',
         'Upper bound of the expected false discovery rate',
         'The upper bound of the expected false discovery rate.'),
        (NEXT_ATTRIBUTE_ID + 7, 'pt',
         'Limite superior da taxa de falsa descoberta (FDR)',
         'Limite superior da taxa de falsa descoberta (FDR).'),

        (NEXT_ATTRIBUTE_ID + 8, 'en',
         'Upper bound of the expected family-wise error rate (FWE)',
         'The upper bound of the expected family-wise error rate (FWE).'),
        (NEXT_ATTRIBUTE_ID + 8, 'pt',
         'Limite superior da taxa de erro conjunto (FWE)',
         'Limite superior da taxa de erro conjunto (FWE).'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category():
    tb = table(
        'operation_category',
        column('id', Integer),
        column('type', String),
        column('order', Integer),
        column('default_order', Integer),
    )

    columns = [c.name for c in tb.columns]
    data = [
        (CATEGORY_FEATURE_SELECTION, 'subgroup', 0, 1),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
    )

    columns = [c.name for c in tb.columns]
    data = [
        (CATEGORY_FEATURE_SELECTION, 'en', 'Feature selection'),
        (CATEGORY_FEATURE_SELECTION, 'pt', 'Seleção de features'),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]

    data = [
        (CHI_ID, 1),
        (CHI_ID, CATEGORY_FEATURE_SELECTION),
        (CHI_ID, CATEGORY_DATA_PROCESSING),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


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
        (NEXT_PORT_ID + 0, 'OUTPUT', None, CHI_ID, 1, 'MANY', 'model'),
        (NEXT_PORT_ID + 1, 'OUTPUT', None, CHI_ID, 2, 'MANY', 'output data'),
        (NEXT_PORT_ID + 2, 'INPUT', None, CHI_ID, 1, 'ONE', 'input data'),
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
        (NEXT_PORT_ID + 0, 'en', 'model', 'Model'),
        (NEXT_PORT_ID + 0, 'pt', 'modelo', 'Modelo'),

        (NEXT_PORT_ID + 1, 'en', 'output data', 'Output data'),
        (NEXT_PORT_ID + 1, 'pt', 'dados de saída', 'Dados de saída'),

        (NEXT_PORT_ID + 2, 'en', 'input data', 'Input data'),
        (NEXT_PORT_ID + 2, 'pt', 'dados de entrada', 'Dados de entrada'),

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
        (NEXT_PORT_ID + 0, 20),
        (NEXT_PORT_ID + 1, 1),
        (NEXT_PORT_ID + 2, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation,
     'DELETE FROM operation WHERE id IN ({})'.format(CHI_ID)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN ({})'.format(CHI_ID)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = 1 AND operation_id IN ({})'.format(CHI_ID)),

    (_insert_operation_category,
     'DELETE from operation_category '
     'WHERE id IN ({})'.format(CATEGORY_FEATURE_SELECTION)),

    (_insert_operation_category_translation,
     'DELETE from operation_category_translation '
     'WHERE id IN ({})'.format(CATEGORY_FEATURE_SELECTION)),

    (_insert_operation_category_operation,
     'DELETE from operation_category_operation '
     'WHERE operation_id IN ({})'.format(CHI_ID)),

    (_insert_operation_port,
     "DELETE FROM operation_port WHERE id BETWEEN {} AND {}".format(
         NEXT_PORT_ID, NEXT_PORT_ID + 2)),
    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id BETWEEN {} AND {}".format(
         NEXT_PORT_ID, NEXT_PORT_ID + 2)),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id BETWEEN {} AND {}".format(
         NEXT_PORT_ID, NEXT_PORT_ID + 2)),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN ({0})'.format(CHI_FORM_ID)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({0})'.format(CHI_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation  WHERE id IN ({0})'.format(
         CHI_FORM_ID)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id IN ({0})'.format(
         CHI_FORM_ID)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id IN ({0}))'.format(CHI_FORM_ID)),

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
