# -*- coding: utf-8 -*-
"""feature_extraction_ops

Revision ID: bd294c13637b
Revises: 1214d3ffa0ce
Create Date: 2017-09-04 13:41:11.171364

"""
import json

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'bd294c13637b'
down_revision = '1214d3ffa0ce'
branch_labels = None
depends_on = None


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String),
               )
    all_ops = (
        (90, 'standard-scaler', 1, 'TRANSFORMATION', 'fa-balance-scale'),
        (91, 'min-max-scaler', 1, 'TRANSFORMATION', 'fa-arrows-v'),
        (92, 'max-abs-scaler', 1, 'TRANSFORMATION', 'fa-lemon-o'),

    )
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    all_ops = [
        (90, 'en', 'Standard scaler',
         ('Transforms the input (vector rows), normalizing each feature to '
          'have unit standard deviation and/or zero mean.')),
        (90, 'pt', 'Escalador padrão',
         ('Transforma a entrada (linhas com vetores), normalizando-os '
          'de forma que cada caracteristica (feature) tenha desvio-padrão '
          'unitário e/ou média zero.')),

        (91, 'en', 'Min-max scaler',
         ('Transforms the input (vector rows), rescaling each feature to a '
          'specific range (often [0, 1]). ')),
        (91, 'pt', 'Escalador min-máx',
         ('Transforma a entrada (linhas com vetores), reescalando cada '
          'caracteristica (feature) para uma faixa específica '
          '(geralmente [0, 1])')),

        (92, 'en', 'Max-abs scaler',
         ('Transforms the input (vector rows), rescaling each value (feature) '
          'to range [-1, 1] by dividing through the maximum absolute value '
          'in each value (feature(.')),
        (92, 'pt', 'Escalador máx-abs',
         ('Transforma a entrada (linhas com vetores), reescalando cada '
          'caracteristica(feature) para a faixa [-1, 1], '
          'através da divisão pelo valor absoluto máximo de cada '
          'caracteristica (feature)')),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    all_ops = [
        (90, 1),
        (91, 1),
        (92, 1),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

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
        column('slug', String))

    all_ops = [
        (203, 'INPUT', None, 90, 1, 'ONE', 'input data'),
        (204, 'OUTPUT', None, 90, 1, 'MANY', 'output data'),
        (205, 'OUTPUT', None, 90, 2, 'MANY', 'transformation model'),

        (206, 'INPUT', None, 91, 1, 'ONE', 'input data'),
        (207, 'OUTPUT', None, 91, 1, 'MANY', 'output data'),
        (208, 'OUTPUT', None, 91, 2, 'MANY', 'transformation model'),

        (209, 'INPUT', None, 92, 1, 'ONE', 'input data'),
        (210, 'OUTPUT', None, 92, 1, 'MANY', 'output data'),
        (211, 'OUTPUT', None, 92, 2, 'MANY', 'transformation model'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    all_ops = [
        (203, 'en', 'input data', 'Input data'),
        (203, 'pt', 'dados de entrada', 'Dados de entrada'),

        (204, 'en', 'output data', 'Output data'),
        (204, 'pt', 'dados de saída', 'Dados de saída'),

        (205, 'en', 'transformation model', 'Transformation model'),
        (205, 'pt', 'modelo de transformação', 'Modelo de transformação'),

        (206, 'en', 'input data', 'Input data'),
        (206, 'pt', 'dados de entrada', 'Dados de entrada'),

        (207, 'en', 'output data', 'Output data'),
        (207, 'pt', 'dados de saída', 'Dados de saída'),

        (208, 'en', 'transformation model', 'Transformation model'),
        (208, 'pt', 'modelo de transformação', 'Modelo de transformação'),

        (209, 'en', 'input data', 'Input data'),
        (209, 'pt', 'dados de entrada', 'Dados de entrada'),

        (210, 'en', 'output data', 'Output data'),
        (210, 'pt', 'dados de saída', 'Dados de saída'),

        (211, 'en', 'transformation model', 'Transformation model'),
        (211, 'pt', 'modelo de transformação', 'Modelo de transformação'),

    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface():
    tb = table(
        'operation_port_interface',
        column('id', Integer),
        column('color', String))
    columns = [c.name for c in tb.columns]
    data = [
        (20, '#ED254E'),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)

    tb = table(
        'operation_port_interface_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = [c.name for c in tb.columns]
    data = [
        (20, 'en', 'TransformationModel'),
        (20, 'pt', 'TransformationModel'),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)


def _insert_operation_script():
    tb = table(
        'operation_script',
        column('id', Integer),
        column('type', String),
        column('enabled', Integer),
        column('body', String),
        column('operation_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        # Clustering model
        (29, 'JS_CLIENT', 1,
         "copyInputAddField(task, 'prediction', false, null);", 90),

        (30, 'JS_CLIENT', 1, "copyInputAddField(task, 'alias', false, null);",
         90),
        (31, 'JS_CLIENT', 1, "copyInputAddField(task, 'alias', false, null);",
         91),
        (32, 'JS_CLIENT', 1, "copyInputAddField(task, 'alias', false, null);",
         92),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (203, 1),
        (204, 1),
        (206, 1),
        (207, 1),
        (209, 1),
        (210, 1),

        (205, 20),
        (208, 20),
        (211, 20),
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
        (90, 8),
        (91, 8),
        (92, 8),

        (90, 23),
        (91, 23),
        (92, 23),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

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
        (114, 1, 1, 'execution'),
        (115, 1, 1, 'execution'),
        (116, 1, 1, 'execution'),

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
        (90, 114),
        (90, 110),
        (90, 41),

        (91, 115),
        (91, 110),
        (91, 41),

        (92, 116),
        (92, 110),
        (92, 41),
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
        (114, 'en', 'Execution'),
        (114, 'pt', 'Execução'),

        (115, 'en', 'Execution'),
        (115, 'pt', 'Execução'),

        (116, 'en', 'Execution'),
        (116, 'pt', 'Execução'),
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

    modes = [
        {"key": "PERMISSIVE", "value": "Convert invalid data to NULL"},
        {"key": "DROPMALFORMED", "value": "Ignore whole corrupted record"},
        {"key": "FAILFAST", "value": "Stop processing and raise error"},
    ]
    data = [
        # Standard
        [348, 'attribute', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 114],
        [349, 'alias', 'TEXT', 0, 2, None, 'text', None, None,
         'EXECUTION', 114],
        [350, 'with_mean', 'INTEGER', 1, 3, '0', 'checkbox', None, None,
         'EXECUTION', 114],
        [351, 'with_std', 'INTEGER', 1, 4, '1', 'checkbox', None, None,
         'EXECUTION', 114],

        # Min-max
        [352, 'attribute', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 115],
        [353, 'alias', 'TEXT', 0, 2, None, 'text', None, None,
         'EXECUTION', 115],
        [354, 'min', 'FLOAT', 0, 3, '0.0', 'decimal', None, None,
         'EXECUTION', 115],
        [355, 'max', 'FLOAT', 0, 4, '1.0', 'decimal', None, None,
         'EXECUTION', 115],

        # Max-abs
        [356, 'attribute', 'TEXT', 0, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 116],
        [357, 'alias', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION',
         116],

        # Data reader
        [358, 'mode', 'TEXT', 0, 5, 'PERMISSIVE', 'dropdown', None,
         json.dumps(modes), 'EXECUTION', 18],

        # Aggregation
        [359, 'pivot', 'TEXT', 0, 3, None, 'attribute-selector', None, None,
         'EXECUTION', 15],

        [360, 'pivot_values', 'TEXT', 0, 4, None, 'textarea', None, None,
         'EXECUTION', 15],
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
        [348, 'en', 'Attribute with features',
         'Attribute with features to be transformed.'],
        [348, 'pt', 'Atributo com as características (features)',
         'Atributo com as características (features) a ser transformado.'],
        [349, 'en', 'New attribute name',
         'Name of the new attribute with transformed features.'],
        [349, 'pt', 'Nome do novo atributo',
         ('Nome do novo atributo com as '
          'características (features) transformadas.')],

        [350, 'en', 'Center data with mean',
         'Center data with mean (default: false).'],
        [350, 'pt', 'Centralizar os dados com a média',
         'Centralizar os dados com a média (falso por padrão)'],

        [351, 'en', 'Scale to unit standard deviation',
         'Scale to unit standard deviation (default: true).'],
        [351, 'pt', 'Escalar os dados para desvio-padrão unitário',
         ('Escalar os dados para desvio-padrão unitário '
          '(verdadeiro por padrão)')],

        [352, 'en', 'Attribute with features',
         'Attribute with features to be transformed.'],
        [352, 'pt', 'Atributo com as características (features)',
         'Atributo com as características (features) a ser transformado.'],
        [353, 'en', 'New attribute name',
         'Name of the new attribute with transformed features.'],
        [353, 'pt', 'Nome do novo atributo',
         ('Nome do novo atributo com as '
          'características (features) transformadas.')],

        [354, 'en', 'Lower bound of the output feature range',
         'Lower bound of the output feature range (default: 0.0).'],
        [354, 'pt', 'Limite inferior para a faixa',
         'Limite inferior para a faixa (valor padrão: 0.0).'],
        [355, 'en', 'Upper bound of the output feature range',
         'Upper bound of the output feature range (default: 1.0).'],
        [355, 'pt', 'Limite superior para a faixa',
         'Limite superior para a faixa (valor padrão: 1.0).'],

        [356, 'en', 'Attribute with features',
         'Attribute with features to be transformed.'],
        [356, 'pt', 'Atributo com as características (features)',
         'Atributo com as características (features) a ser transformado.'],
        [357, 'en', 'New attribute name',
         'Name of the new attribute with transformed features.'],
        [357, 'pt', 'Nome do novo atributo',
         ('Nome do novo atributo com as '
          'características (features) transformadas.')],

        [358, 'en', 'What to do in case of invalid data',
         'What to do in case of invalid data'],
        [358, 'pt', 'O que fazer em caso de dados inválidos',
         'Opção sobre o que fazer em caso de dados inválidos.'],

        # Aggregation
        [359, 'en', 'Attribute used as pivot',
         'Attribute used as pivot. Each attribute '
         'value will generate a new attribute'],
        [359, 'pt', 'Atributo usado como pivô',
         'Atributo usado como pivô. Cada valor para o atributo irá gerar '
         'um novo atributo.'],

        [360, 'en', 'Pivot values (recommended if pivot is used)',
         'Pivot values. Recommended if pivot is used (better performance).'],
        [360, 'pt', 'Valores do pivô (recomendado, se pivô for usado)',
         'Valores do pivô. Recomendado, se pivô for usado '
         '(melhora desempenho).'],


    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN 90 AND 92'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 90 AND 92'),
    (_insert_operation_port,
     'DELETE FROM operation_port '
     'WHERE (operation_id BETWEEN 90 AND 92)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE (operation_id BETWEEN 90 AND 92))'),
    (_insert_operation_port_interface,
     [
         'DELETE FROM operation_port_interface_translation WHERE id = 20',
         'DELETE FROM operation_port_interface WHERE id = 20'
     ]
     ),
    (_insert_operation_script,
     [
         '''DELETE FROM operation_script WHERE operation_id BETWEEN 90 AND 92
            OR id = 29
         ''',
     ]
     ),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE (operation_id BETWEEN 90 AND 92))'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN 90 AND 92;'),
    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN 90 AND 92'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 114 AND 116'),
    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN 90 AND 92'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 114 AND 116'),
    (_insert_operation_form_field,
     """DELETE FROM operation_form_field
        WHERE (form_id BETWEEN 114 AND 116) OR id = 358"""),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE (form_id BETWEEN 114 AND 116)) OR id = 358'),

    # Fix in apply model
    [
        [
            '''UPDATE operation_form_field SET required = 0, `order` = 3
            WHERE id = 238''',
            """
            UPDATE operation_form_field_translation
                SET label = 'Nome do novo atributo (herdado do modelo)',
                help = 'Nome do novo atributo (transformado, herda do modelo).'
                WHERE id = 238 AND locale = 'pt' """,
            """
            UPDATE operation_form_field_translation
                SET label = 'New attribute name (inherited from model)',
                help = 'New attribute name (transformed, inherited from model).'
                WHERE id = 238 AND locale = 'en' """,
        ],
        [
            '''UPDATE operation_form_field SET required = 1,
            `order`= 1 WHERE id = 238''',
            """
            UPDATE operation_form_field_translation
                SET label = 'Atributo com a predição (novo, herda do modelo)',
                    help = 'Atributo com a predição (novo, herda do modelo).'
                WHERE id = 238 AND locale = 'pt' """,
            """
            UPDATE operation_form_field_translation SET
                label = 'Prediction attribute name (new, inherited from model)',
                help = 'Prediction attribute name (new, inherited from model)'
                WHERE id = 238 AND locale = 'en' """,
        ]
    ],
    # Associate TransformationModel interface to ApplyModel
    [
        '''INSERT INTO operation_port_interface_operation_port
            (operation_port_id, operation_port_interface_id)
            VALUES(93, 20)'''
        ,
        '''DELETE FROM operation_port_interface_operation_port
            WHERE operation_port_id = 93 AND
            operation_port_interface_id = 20'''
    ],
    # Scatter plot
    [
        '''UPDATE operation SET slug = 'scatter-plot' WHERE id = 87''',
        '''UPDATE operation SET slug = 'plot-chart' WHERE id = 87''',
    ]
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
