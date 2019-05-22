# coding=utf-8
"""new operations bucketizer lof

Revision ID: 950bf9412aac
Revises: b993656aa211
Create Date: 2018-05-18 14:44:51.369414

"""
import json

from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '950bf9412aac'
down_revision = 'b993656aa211'
branch_labels = None
depends_on = None

BUCKETIZER_ID = 100
QUANTILE_DISCRETIZER_ID = 101
OUTLIER_DETECTION_ID = 102

OPERATIONS = ', '.join([str(BUCKETIZER_ID), str(QUANTILE_DISCRETIZER_ID),
                        str(OUTLIER_DETECTION_ID)])

BUCKETIZER_FORM_ID = 126
QUANTILE_DISCRETIZER_FORM_ID = 127
OUTLIER_DETECTION_FORM_ID = 128

FORMS = ', '.join([str(BUCKETIZER_FORM_ID), str(QUANTILE_DISCRETIZER_FORM_ID),
                   str(OUTLIER_DETECTION_FORM_ID)])

APPEARANCE_FORM_ID = 41
RESULTS_FORM_ID = 110

PORT_RANGE = ', '.join(
    [str(x) for x in [229, 230, 231, 232, 233, 234, 235, 236]])


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (BUCKETIZER_ID, 'bucketizer', 1, 'TRANSFORMATION', 'fa-box-open'),
        (QUANTILE_DISCRETIZER_ID, 'quantile-discretizer', 1, 'TRANSFORMATION',
         'fa-ruler-horizontal'),
        (OUTLIER_DETECTION_ID, 'outlier-detection', 1, 'TRANSFORMATION',
         'fa-user-secret'),
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
        (BUCKETIZER_ID, 'en', 'Bucketizer',
         'Bucketizer maps an attribute of continuous features to an attribute '
         'of feature buckets.'),
        (BUCKETIZER_ID, 'pt', 'Divisão em buckets',
         'Mapeia um atributo em buckets.'),

        (QUANTILE_DISCRETIZER_ID, 'en', 'Quantile discretizer',
         'Quantile discretizer takes an attribute with continuous features and '
         'outputs an attribute with binned categorical features.'),
        (QUANTILE_DISCRETIZER_ID, 'pt', 'Discretizador em quantis',
         'Discretizador em quantis recebe um atributo e associa-o a quantis '
         'especificados em faixas de valores.'),

        (OUTLIER_DETECTION_ID, 'en', 'Outlier detection',
         'Outlier detection.'),
        (OUTLIER_DETECTION_ID, 'pt', 'Detecção de anomalias',
         'Determina se uma observação deve ser considerada anômala ou não.'),
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
        (BUCKETIZER_ID, 1),
        (QUANTILE_DISCRETIZER_ID, 1),
        (OUTLIER_DETECTION_ID, 1),

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
        (BUCKETIZER_FORM_ID, 1, 1, 'execution'),
        (QUANTILE_DISCRETIZER_FORM_ID, 1, 1, 'execution'),
        (OUTLIER_DETECTION_FORM_ID, 1, 1, 'execution'),
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
        (BUCKETIZER_ID, BUCKETIZER_FORM_ID),
        (BUCKETIZER_ID, APPEARANCE_FORM_ID),
        (BUCKETIZER_ID, RESULTS_FORM_ID),

        (QUANTILE_DISCRETIZER_ID, QUANTILE_DISCRETIZER_FORM_ID),
        (QUANTILE_DISCRETIZER_ID, APPEARANCE_FORM_ID),
        (QUANTILE_DISCRETIZER_ID, RESULTS_FORM_ID),

        (OUTLIER_DETECTION_ID, OUTLIER_DETECTION_FORM_ID),
        (OUTLIER_DETECTION_ID, APPEARANCE_FORM_ID),
        (OUTLIER_DETECTION_ID, RESULTS_FORM_ID),
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
        (BUCKETIZER_FORM_ID, 'en', 'Execution'),
        (BUCKETIZER_FORM_ID, 'pt', 'Execução'),

        (QUANTILE_DISCRETIZER_FORM_ID, 'en', 'Execution'),
        (QUANTILE_DISCRETIZER_FORM_ID, 'pt', 'Execução'),

        (OUTLIER_DETECTION_FORM_ID, 'en', 'Execution'),
        (OUTLIER_DETECTION_FORM_ID, 'pt', 'Execução'),
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

    handle_invalid = [
        {"key": "skip", "value": "Skip", "en": "Skip", "pt": "Ignorar"},
        {"key": "keep", "value": "Keep", "en": "Keep", "pt": "Manter"},
        {"key": "error", "value": "Raise error", "en": "Raise error",
         "pt": "Gerar erro"}]
    data = [
        (459, 'attributes', 'TEXT', 1, 0, None, 'attribute-selector',
         None, None, 'EXECUTION', BUCKETIZER_FORM_ID),
        (460, 'aliases', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION',
         BUCKETIZER_FORM_ID),
        (461, 'splits', 'TEXT', 1, 2, None, 'text', None, None, 'EXECUTION',
         BUCKETIZER_FORM_ID),
        (462, 'handle_invalid', 'TEXT', 1, 3, 'skip', 'dropdown', None,
         json.dumps(handle_invalid), 'EXECUTION', BUCKETIZER_FORM_ID),

        (463, 'attributes', 'TEXT', 1, 0, None, 'attribute-selector',
         None, None, 'EXECUTION', QUANTILE_DISCRETIZER_FORM_ID),
        (464, 'aliases', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION',
         QUANTILE_DISCRETIZER_FORM_ID),
        (465, 'buckets', 'INTEGER', 1, 2, None, 'integer', None, None,
         'EXECUTION', QUANTILE_DISCRETIZER_FORM_ID),
        (466, 'relative_error', 'FLOAT', 1, 3, '0.001', 'decimal', None,
         None, 'EXECUTION', QUANTILE_DISCRETIZER_FORM_ID),

        (467, 'features', 'TEXT', 1, 0, None, 'attribute-selector', None, None,
         'EXECUTION', OUTLIER_DETECTION_FORM_ID),
        (468, 'alias', 'TEXT', 0, 1, 'outlier', 'text', None, None, 'EXECUTION',
         OUTLIER_DETECTION_FORM_ID),
        (469, 'min_points', 'INTEGER', 1, 2, None, 'integer', None, None,
         'EXECUTION', OUTLIER_DETECTION_FORM_ID),
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
        (459, 'en', 'Attribute(s)',
         'List of attributes used in the transformation.'),
        (459, 'pt', 'Atributos',
         'Lista de atributos usados na transformação.'),
        (460, 'en', 'Name(s) for new attribute(s)',
         'Name(s) for new attribute(s). If omitted, the name of original '
         'attribute with a suffix will be used.'),
        (460, 'pt', 'Nome do(s) novo(s) attributo(s)',
         'Nome do(s) novo(s) atributo(s). Se omitido, o nome do atributo '
         'original com um sufixo será usado.'),
        (461, 'en', 'Splits (list of values with the minimum of 3 elements, '
                    'used to define the ranges, '
                    'separated by comma)',
         'Splits (list of values with the minimum of 3 elements, '
         'used to define the ranges, '
         'separated by comma, -INF and INF are valid values).'),
        (461, 'pt', 'Divisores (lista de valores com no mínimo de 3 elementos, '
                    'usado para definir as faixas, separados por vírgula, '
                    '-INF e INF são valores válidos).',
         'Divisores (lista de valores com no mínimo de 3 elementos, usado para '
         'definir as faixas, separados por vírgula).'),
        (462, 'en', 'How to handle invalid data?',
         'How to handle invalid data?'),
        (462, 'pt', 'Como tratar dados inválidos?',
         'Como tratar dados inválidos?'),
        (463, 'en', 'Attribute(s)',
         'List of attributes used in the transformation.'),
        (463, 'pt', 'Atributos',
         'Lista de atributos usados na transformação.'),
        (464, 'en', 'Name(s) for new attribute(s)',
         'Name(s) for new attribute(s). If omitted, the name of original '
         'attribute with a suffix will be used.'),
        (464, 'pt', 'Nome do(s) novo(s) attributo(s)',
         'Nome do(s) novo(s) atributo(s). Se omitido, o nome do atributo '
         'original com um sufixo será usado.'),
        (465, 'en', 'Number of buckets',
         'How many buckets are going to be created.'),
        (465, 'pt', 'Número de categorias (buckets)',
         'Quantas categorias (buckets) serão criadas.'),
        (466, 'en', 'Relative error (between [0.0, 1.0])',
         'The relative target precision for the approximate '
         'quantile algorithm used to generate buckets.'),
        (466, 'pt', 'Erro relativo (entre [0.0, 1.0])',
         'A precisão do alvo relativo para o algoritmo quantil aproximado '
         'usado para gerar categorias (buckets).'),

        (467, 'en', 'Feature attribute(s)',
         'Feature attribute(s)'),
        (467, 'pt', 'Atributo(s) usado(s) como feature(s)',
         'Atributo(s) usado(s) como feature(s)'),
        (468, 'en', 'Name for the new attribute',
         'Name for the new attribute.'),
        (468, 'pt', 'Nome para o novo atributo',
         'Nome para o novo atributo.'),
        (469, 'en', 'Minimum number of points',
         'Minimum number of points.'),
        (469, 'pt', 'Número mínimo de pontos',
         'Número mínimo de pontos.'),
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
        (BUCKETIZER_ID, 1),
        (BUCKETIZER_ID, 8),
        (BUCKETIZER_ID, 23),

        (BUCKETIZER_ID, 1),
        (QUANTILE_DISCRETIZER_ID, 8),
        (QUANTILE_DISCRETIZER_ID, 23),

        (OUTLIER_DETECTION_ID, 8),
        (OUTLIER_DETECTION_ID, 27),
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
        (229, 'INPUT', None, BUCKETIZER_ID, 1, 'ONE',
         'input data'),
        (230, 'OUTPUT', None, BUCKETIZER_ID, 1, 'MANY',
         'output data'),
        (231, 'OUTPUT', None, BUCKETIZER_ID, 2, 'MANY',
         'model'),

        (232, 'INPUT', None, QUANTILE_DISCRETIZER_ID, 1, 'ONE',
         'input data'),
        (233, 'OUTPUT', None, QUANTILE_DISCRETIZER_ID, 1, 'MANY',
         'output data'),
        (234, 'OUTPUT', None, QUANTILE_DISCRETIZER_ID, 2, 'MANY',
         'model'),

        (235, 'INPUT', None, OUTLIER_DETECTION_ID, 1, 'ONE',
         'input data'),
        (236, 'OUTPUT', None, OUTLIER_DETECTION_ID, 1, 'MANY',
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
        (229, 'en', 'input data', 'Input data'),
        (229, 'pt', 'dados de entrada', 'Dados de entrada'),
        (230, 'en', 'output data', 'Output data'),
        (230, 'pt', 'dados de saída', 'Dados de saída'),
        (231, 'en', 'model', 'Model'),
        (231, 'pt', 'modelo', 'Modelo'),

        (232, 'en', 'input data', 'Input data'),
        (232, 'pt', 'dados de entrada', 'Dados de entrada'),
        (233, 'en', 'output data', 'Output data'),
        (233, 'pt', 'dados de saída', 'Dados de saída'),
        (234, 'en', 'model', 'Model'),
        (234, 'pt', 'modelo', 'Modelo'),

        (235, 'en', 'input data', 'Input data'),
        (235, 'pt', 'dados de entrada', 'Dados de entrada'),
        (236, 'en', 'output data', 'Output data'),
        (236, 'pt', 'dados de saída', 'Dados de saída'),

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
        (229, 1),
        (230, 1),
        (231, 20),

        (232, 1),
        (233, 1),
        (234, 20),

        (235, 1),
        (236, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [

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
     'WHERE operation_id IN ({})'.format(BUCKETIZER_ID)),
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

    ("""
     UPDATE operation_form_field SET
        suggested_widget = 'lookup',
        values_url = '`${LIMONERO_URL}/storages`' WHERE id IN (87, 233);
    """,
     """
     SELECT 1
     """),
    ("""
        UPDATE operation_script SET
        body = 'copyAddExpressionAlias(task, "expressions", "alias");'
        WHERE `id` IN (48);
    """,
     """SELECT 1"""),
    ("""
        UPDATE operation_script SET
        body = 'copyAddExpressionAlias(task, "expression", "alias");'
        WHERE `id` IN (2);
    """,
     """SELECT 1"""),
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
