# -*- coding: utf-8 -*-

"""Insert operation LSH.

Revision ID: 89965c2cd39b
Revises: 3e92a3f9fa38
Create Date: 2019-09-12 15:29:52.014172

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json


# revision identifiers, used by Alembic.
revision = '89965c2cd39b'
down_revision = '3e92a3f9fa38'
branch_labels = None
depends_on = None

SCIKIT_LEARN_PLATAFORM_ID = 4
ID_OPERATION = 4039


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')

    data = [
        (ID_OPERATION, SCIKIT_LEARN_PLATAFORM_ID)
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('type', String),
        column('icon', Integer),)

    columns = ('id', 'slug', 'enabled', 'type', 'icon')

    data = [
        (ID_OPERATION, "locality-sensitive-hashing", 1, 'ACTION', ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_category_id', 'operation_id')
    data = [
        #Core Layers
        (32, 4039),
        (36, 4039)
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (ID_OPERATION, "pt", 'Hash Sensível à Localidade (LSH)', ''),
        (ID_OPERATION, "en", 'Locality Sensitive Hashing (LSH)', 'Locality Sensitive Hashing is an alternative method '
                                                                 'for vanilla approximate nearest neighbor search '
                                                                 'methods')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        #Flatten - data_format
        (ID_OPERATION, 41),  #appearance
        (ID_OPERATION, 4026),  # own execution form
        (ID_OPERATION, 110)
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        #Flatten
        (4026, 1, 1, 'execution'), #data_format
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(operation_form_table, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        #Flatten - data_format
        (4026, 'en', 'Execution'),
        (4026, 'pt', 'Execução'),
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
        column('enable_conditions', String),
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')

    data = [
        #Flatten - data_format
        (4127, 'label', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4026, None),
        (4128, 'n_estimators', 'INTEGER', 1, 1, 10, 'integer', None, None, 'EXECUTION', 4026, None),
        (4129, 'min_hash_match', 'INTEGER', 1, 1, 4, 'integer', None, None, 'EXECUTION', 4026, None),
        (4130, 'n_candidates', 'INTEGER', 1, 1, 10, 'integer', None, None, 'EXECUTION', 4026, None),
        (4131, 'n_neighbors', 'INTEGER', 1, 1, 5, 'integer', None, None, 'EXECUTION', 4026, None),
        (4132, 'random_state', 'INTEGER', 0, 1, None, 'integer', None, None, 'EXECUTION', 4026, None),
        (4133, 'radius', 'FLOAT', 0, 1, 1.0, 'decimal', None, None, 'EXECUTION', 4026, None),
        (4134, 'radius_cutoff_ratio', 'FLOAT', 0, 1, 0.9, 'decimal', None, None, 'EXECUTION', 4026, None),
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

    columns = ('id', 'locale', 'label', 'help')
    data = [
        #Flatten - data_format
        (4127, 'en', 'Label', 'Label.'),
        (4127, 'pt', 'Atributo usado como rótulo (label)', 'Atributo usado como rótulo (label).'),

        (4128, 'en', 'Number of trees', 'Number of trees in the LSH Forest.'),
        (4128, 'pt', 'Número de árvores', 'Número de árvores na floresta LSH.'),

        (4129, 'en', 'Lowest hash length', 'Lowest hash length to be searched when candidate selection is performed '
                                           'for nearest neighbors.'),
        (4129, 'pt', 'Menor tamanho de hash', 'Menor tamanho do hash a ser pesquisado quando a seleção do candidato é '
                                              'realizada para os vizinhos mais próximos.'),

        (4130, 'en', 'Minimum number of candidates', 'Minimum number of candidates evaluated per estimator, assuming '
                                                     'enough items meet the min_hash_match constraint.'),
        (4130, 'pt', 'Número mínimo de candidatos', 'Número mínimo de candidatos avaliados por estimador, assumindo '
                                                    'que itens suficientes atendem à restrição min_hash_match.'),

        (4131, 'en', 'Number of neighbors', 'Number of neighbors to be returned from query function when it is not '
                                            'provided to the kneighbors method.'),
        (4131, 'pt', 'Número de vizinho', 'Número de vizinhos a serem retornados da função de consulta quando ela não '
                                          'é fornecida ao método kneighbors.'),

        (4132, 'en', 'Random state', 'If int, random_state is the seed used by the random number generator; If '
                                     'RandomState instance, random_state is the random number generator; If None, the '
                                     'random number generator is the RandomState instance used by np.random.'),
        (4132, 'pt', 'Estado aleatório', 'Se int, random_state é a semente usada pelo gerador de números aleatórios; '
                                         'Se a instância RandomState, random_state for o gerador de números aleatórios;'
                                         ' Se Nenhum, o gerador de números aleatórios é a instância RandomState usada '
                                         'pelo np.random.'),

        (4133, 'en', 'Radius', 'Radius from the data point to its neighbors.'),
        (4133, 'pt', 'Raio', 'Raio do ponto de dados para seus vizinhos.'),

        (4134, 'en', 'Radius cutoff ratio', 'Radius neighbors will be searched until the ratio between total neighbors '
                                            'within the radius and the total candidates becomes less than this value '
                                            'unless it is terminated by hash length reaching min_hash_match.'),
        (4134, 'pt', 'Proporção de corte do raio', 'Os vizinhos de raio serão pesquisados até que a proporção entre o '
                                                   'total de vizinhos dentro do raio e o total de candidatos se torne '
                                                   'menor que esse valor, a menos que seja finalizada pelo comprimento '
                                                   'do hash atingindo min_hash_match.'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('order', Integer),
        column('multiplicity', String),
        column('operation_id', Integer),
        column('slug', String),)

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        #Reshape
        (4083, 'INPUT', '', 1, 'ONE', ID_OPERATION, 'input data'),
        (4084, 'OUTPUT', '', 1, 'ONE', ID_OPERATION, 'output data'),
        (4085, 'OUTPUT', '', 2, 'MANY', ID_OPERATION, 'output model'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        #Reshape
        (4083, 1),
        (4084, 1),
        (4085, 2),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        #Reshape
        (4083, "en", 'input data', 'Input data'),
        (4083, "pt", 'dados de entrada', 'Dados de entrada'),
        (4084, "en", 'output data', 'Output data'),
        (4084, "pt", 'dados de saída', 'Dados de saída'),
        (4085, "en", 'model', 'Model'),
        (4085, "pt", 'Modelo', 'Modelo'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 4039'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = {}'.format(ID_OPERATION)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id IN (4039)'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 4039 AND platform_id = {}'.format(SCIKIT_LEARN_PLATAFORM_ID)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id=4026'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4127 AND 4134'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id=4026'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4127 AND 4134'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4039'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4083 AND 4085'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 4083 AND 4085'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4083 AND 4085'),
    ("UPDATE operation SET enabled = 0 WHERE id = 4039",
     ""),

]

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    except:
        session.rollback()
        raise
    session.commit()