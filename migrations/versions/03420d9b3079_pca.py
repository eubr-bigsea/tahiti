# coding=utf-8
"""pca

Revision ID: 03420d9b3079
Revises: 71866c551e33
Create Date: 2017-12-05 09:49:48.883138

"""
import json

from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '03420d9b3079'
down_revision = '71866c551e33'
branch_labels = None
depends_on = None

PCA_ID = 95
PCA_FORM_ID = 120

LSH_ID = 96
LSH_FORM_ID = 121

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
        (PCA_ID, 'pca', 1, 'TRANSFORMATION',
         'fa-sort-amount-desc'),
        (LSH_ID, 'lsh', 1, 'TRANSFORMATION',
         'hashtag'),
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
        (PCA_ID, 'en', ' Principal component analysis',
         'Principal component analysis (PCA) is a statistical procedure '
         'that uses an orthogonal transformation to convert a set of '
         'observations of possibly correlated variables into a set of '
         'values of linearly uncorrelated variables called principal '
         'components. A PCA operation trains a model to project vectors to '
         'a low-dimensional space using PCA.'),
        (PCA_ID, 'pt', 'Análise de componentes principais',
         'Análise de componentes principais ou ACP/PCA (Principal component '
         'analysis) é um procedimento estatístico que usa uma transformação '
         'ortogonal para converter um conjunto de observações de variáveis '
         'possivelmente correlacionadas em um conjunto de valores de '
         'variáveis linearmente não-correlacionadas, chamadas de componentes '
         'principais. Uma operação ACP treina um modelo para projetar vetores '
         'para um espaço de menor dimensionalidade usando ACP.'),
        (LSH_ID, 'en', 'Locality-sensitive hashing',
         'Locality-sensitive hashing (LSH) reduces the dimensionality of '
         'high-dimensional data. LSH hashes input items so that similar items '
         'map to the same “buckets” with high probability (the number of '
         'buckets being much smaller than the universe of possible input '
         'items). LSH differs from conventional and cryptographic hash '
         'functions because it aims to maximize the probability of a '
         '"collision" for similar items.'),
        (LSH_ID, 'pt', 'Locality-sensitive hashing',
         'Locality-sensitive hashing (LSH) reduz a quantidade de dimensões de '
         'dados com alta dimensionalidade. LSH hashes analisa os itess de '
         'forma que itens similares sejam mapeados para os mesmos "buckets" '
         'com alta probabilidade (sendo o número de de buckets muito menor '
         'que o universo de possíveis itens). LSH difere das funções '
         'tradicionais de hash convencionais e daquelas usadas para '
         'criptografiahash porque busca maximizar a probabilidade de uma '
         '"colisão" para itens similares.'),
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
        (PCA_ID, 1),
        (LSH_ID, 1),
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
        (PCA_FORM_ID, 1, 1, 'execution'),
        (LSH_FORM_ID, 1, 1, 'execution'),
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
        (PCA_ID, PCA_FORM_ID),
        (PCA_ID, APPEARANCE_FORM_ID),
        (PCA_ID, RESULTS_FORM_ID),
        (LSH_ID, LSH_FORM_ID),
        (LSH_ID, APPEARANCE_FORM_ID),
        (PCA_ID, RESULTS_FORM_ID),
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
        (PCA_FORM_ID, 'en', 'Execution'),
        (PCA_FORM_ID, 'pt', 'Execução'),

        (LSH_FORM_ID, 'en', 'Execution'),
        (LSH_FORM_ID, 'pt', 'Execução'),
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

    options = [
        {"key": "min-hash-lsh", "value": "Min hash LSH for Jackard distance"},
        {"key": "bucketed-random",
         "value": "Bucketed random projection for Euclidean distance"},
    ]

    data = [
        (420, 'k', 'INTEGER', 1, 1, None, 'integer',
         None, None, 'EXECUTION', PCA_FORM_ID),
        (421, 'attribute', 'TEXT', 1, 2, None, 'attribute-selector',
         None, None, 'EXECUTION', PCA_FORM_ID),

        (422, 'output_attribute', 'TEXT', 1, 3, 'pca_features', 'text',
         None, None, 'EXECUTION', PCA_FORM_ID),

        (423, 'num_hash_tables', 'INTEGER', 1, 1, '1', 'integer',
         None, None, 'EXECUTION', LSH_FORM_ID),
        (424, 'attribute', 'TEXT', 0, 2, None, 'attribute-selector', None, None,
         'EXECUTION', LSH_FORM_ID),
        (425, 'output_attribute', 'TEXT', 1, 3, 'hashes', 'text', None, None,
         'EXECUTION', LSH_FORM_ID),

        (426, 'type', 'TEXT', 1, 4, 'min-hash-lsh', 'dropdown', None,
         json.dumps(options), 'EXECUTION', LSH_FORM_ID),

        (427, 'bucket_length', 'INTEGER', 1, 5, None, 'integer', None, None,
         'EXECUTION', LSH_FORM_ID),
        (428, 'seed', 'INTEGER', 1, 6, None, 'integer', None, None, 'EXECUTION',
         LSH_FORM_ID),

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
        (420, 'en', 'Number of principal components',
         'Number of principal components.'),
        (420, 'pt', 'Número de componentes principais',
         'Número de componentes principais'),

        (421, 'en', 'Attribute with features vector',
         'Attribute with features vector.'),
        (421, 'pt', 'Atributo com o vetor de features',
         'Atributo com o vetor de features.'),

        (422, 'en', 'PCA output attribute', 'PCA output attribute.'),
        (422, 'pt', 'Atributo para saída do ACP',
         'Atributo para saída do ACP.'),

        (423, 'en', 'Number of hash tables',
         'Number of hash tables. Increasing number of hash tables lowers the '
         'false negative rate, and decreasing it improves the running '
         'performance.'),
        (423, 'pt', 'Número de tabelas hash',
         'Número de tabelas hash. Aumentar o número de tabelas hash diminui a '
         'taxa de falsos positivos e decrementá-lo melhora o tempo de execução'
         ),

        (424, 'en', 'Attribute with features vector',
         'Attribute with features vector.'),
        (424, 'pt', 'Atributo com o vetor de features',
         'Atributo com o vetor de features.'),

        (425, 'en', 'Output attribute', 'Output attribute.'),
        (425, 'pt', 'Atributo para saída',
         'Atributo para saída.'),

        (426, 'en', 'LSH type', 'LSH type.'),
        (426, 'pt', 'Tipo do LSH', 'Tipo do LSH.'),

        (427, 'en',
         'Bucket length (only for type Bucketed Random Projection LSH',
         'Bucket length (only for type Bucketed Random Projection LSH. '
         'A larger bucket lowers the false negative rate.'),
        (427, 'pt',
         'Tamanho do bucket (apenas para Bucketd Random Projection LSH)',
         'Tamanho do bucket (apenas para Bucketd Random Projection LSH). '
         'Um tamanho de bucket maior diminui a taxa de falsos negativos.'),

        (428, 'en', 'Seed for random numbers', 'Seed for random numbers.'),
        (428, 'pt', 'Semente para números aleatórios',
         'Semente para números aleatórios.'),
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
        (PCA_ID, 1),
        (PCA_ID, 8),
        (PCA_ID, 23),

        (LSH_ID, 1),
        (LSH_ID, 8),
        (LSH_ID, 23),
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
        (217, 'OUTPUT', None, PCA_ID, 1, 'MANY', 'output data'),
        (218, 'INPUT', None, PCA_ID, 1, 'ONE', 'input data'),

        (219, 'OUTPUT', None, LSH_ID, 1, 'MANY', 'output data'),
        (220, 'INPUT', None, LSH_ID, 1, 'ONE', 'input data'),
        (221, 'OUTPUT', None, LSH_ID, 2, 'MANY', 'model')
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
        (217, 'en', 'output data', 'Output data'),
        (217, 'pt', 'dados de saída', 'Dados de saída'),
        (218, 'en', 'input data', 'Input data'),
        (218, 'pt', 'dados de entrada', 'Dados de entrada'),

        (219, 'en', 'output data', 'Output data'),
        (219, 'pt', 'dados de saída', 'Dados de saída'),
        (220, 'en', 'input data', 'Input data'),
        (220, 'pt', 'dados de entrada', 'Dados de entrada'),

        (221, 'en', 'model', 'Model'),
        (221, 'pt', 'model', 'Modelo'),
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
        (217, 1),
        (218, 1),
        (219, 1),
        (220, 1),
        (221, 21),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    ("INSERT INTO operation_port_interface VALUES(21, '#307351')",
     "DELETE FROM operation_port_interface WHERE id = 21"),

    ("""
        INSERT INTO operation_port_interface_translation VALUES(21, 'en',
        'LSHModel');""",
     "DELETE FROM operation_port_interface_translation WHERE id = 21 "
     "  AND locale = 'en'"),
    ("""
        INSERT INTO operation_port_interface_translation VALUES(21, 'pt',
        'LSHModel');""",
     "DELETE FROM operation_port_interface_translation WHERE id = 21 "
     "  AND locale = 'pt'"
     ),

    (
        'ALTER TABLE operation_translation MODIFY description VARCHAR(4000);',
        'ALTER TABLE operation_translation MODIFY description VARCHAR(200);',
    ),
    (_insert_operation,
     'DELETE FROM operation WHERE id IN ({}, {})'.format(
         PCA_ID, LSH_ID)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN ({}, {})'.format(
         PCA_ID, LSH_ID)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = 1 AND operation_id IN ({}, {})'.format(
         PCA_ID, LSH_ID)),
    (_insert_operation_category_operation,
     'DELETE from operation_category_operation '
     'WHERE operation_id IN ({}, {})'.format(PCA_ID,
                                             LSH_ID)),
    (_insert_operation_port,
     "DELETE FROM operation_port WHERE id in (217, 218, 219, 220, 221)"),
    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id in "
     "(217, 218, 219, 220, 221)"),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id in (217, 218, 219, 220, 221)"),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN ({0}, {1})'.format(
         PCA_FORM_ID, LSH_FORM_ID)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({0}, {1})'.format(PCA_ID,
                                               LSH_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation  WHERE id IN ({0}, {1})'.format(
         PCA_FORM_ID, LSH_FORM_ID)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id IN ({0}, {1})'.format(
         PCA_FORM_ID, LSH_FORM_ID)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id IN ({0}, {1}))'.format(PCA_FORM_ID,
                                              LSH_FORM_ID)),
    (
        '''INSERT INTO
        operation_script(id, `type`, enabled, body, operation_id)
        VALUES (43, 'JS_CLIENT', '1',
        'copyInputAddField(task, "output_attribute", false, "pca_features");',
            95)''',
        '''DELETE FROM operation_script WHERE id = 43'''
    ),
    (
        '''INSERT INTO
        operation_script(id, `type`, enabled, body, operation_id)
        VALUES (44, 'JS_CLIENT', '1',
        'copyInputAddField(task, "output_attribute", false, "hashes");', 96)''',
        '''DELETE FROM operation_script WHERE id = 44'''
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
