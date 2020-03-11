# -*- coding: utf-8 -*-

"""Add DBSCAN Clustering Operation (scikit_learn).

Revision ID: 6c6668dd3682
Revises: 6d765dcaf192
Create Date: 2020-01-28 09:03:16.033929

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
revision = '6c6668dd3682'
down_revision = '6d765dcaf192'
branch_labels = None
depends_on = None


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')

    data = [
        (4043, 4)
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
        (4043, "dbscan-clustering", 1, 'ACTION', ''),
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
        (8, 4043),
        (19, 4043)
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
        (4043, "pt", 'Agrupamento DBSCAN', 'Usa o algoritmo DBSCAN para agrupamento.'),
        (4043, "en", 'DBSCAN Clustering', 'Uses DBSCAN algorithm for clustering.')
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
        (4043, 41),  #appearance
        (4043, 4032),  # own execution form
        (4043, 110)
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
        (4032, 1, 1, 'execution'), #data_format
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
        (4032, 'en', 'Execution'),
        (4032, 'pt', 'Execução'),
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
    enable_condition = 'this.algorithm.internalValue === "ball_tree" or this.algorithm.internalValue === "kd_tree"'
    data = [
        #Flatten - data_format
        (4327, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4032, None),
        (4328, 'prediction', 'TEXT', 0, 2, 'prediction', 'text', None, None, 'EXECUTION', 4032, None),
        (4329, 'eps', 'DECIMAL', 0, 3, 0.5, 'decimal', None, None, 'EXECUTION', 4032, None),
        (4330, 'min_samples', 'INTEGER ', 0, 4, 5, 'integer', None, None, 'EXECUTION', 4032, None),
        (4331, 'metric', 'TEXT', 0, 5, 'euclidean', 'dropdown', None,
         json.dumps([
             {'key': 'euclidean', 'value': 'euclidean'},
             {'key': 'cityblock', 'value': 'cityblock'},
             {'key': 'cosine', 'value': 'cosine'},
             {'key': 'l1', 'value': 'l1'},
             {'key': 'l2', 'value': 'l2'},
             {'key': 'manhattan', 'value': 'manhattan'},
         ]),
         'EXECUTION', 4032, None),
        (4332, 'metric_params', 'TEXT', 0, 6, None, 'text', None, None, 'EXECUTION', 4032, None),
        (4333, 'algorithm', 'TEXT', 0, 7, 'auto', 'dropdown', None,
         json.dumps([
             {'key': 'auto', 'value': 'auto'},
             {'key': 'ball_tree', 'value': 'ball_tree'},
             {'key': 'kd_tree', 'value': 'kd_tree'},
             {'key': 'brute', 'value': 'brute'},
         ]),
         'EXECUTION', 4032, None),
        (4334, 'leaf_size', 'INTEGER', 0, 8, 30, 'integer', None, None, 'EXECUTION', 4032, enable_condition),
        (4335, 'p', 'DECIMAL', 0, 9, None, 'decimal', None, None, 'EXECUTION', 4032, None),
        (4336, 'n_jobs', 'INTEGER', 0, 10, None, 'integer', None, None, 'EXECUTION', 4032, None),
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
        (4327, 'en', 'Features', 'Features.'),
        (4327, 'pt', 'Atributo(s) previsor(es)', 'Atributo(s) previsor(es).'),

        (4328, 'en', 'Prediction (new attribute)', 'Prediction (new attribute).'),
        (4328, 'pt', 'Atributo com a predição (novo)', 'Atributo com a predição (novo).'),

        (4329, 'en', 'Max. distance', 'The maximum distance between two samples for one to be considered as in the '
                                      'neighborhood of the other.'),
        (4329, 'pt', 'Distância máxima', 'A distância máxima entre duas amostras para uma ser considerada como na '
                                         'vizinhança da outra.'),

        (4330, 'en', 'Number of samples', 'The number of samples (or total weight) in a neighborhood for a point to be'
                                          ' considered as a core point.'),
        (4330, 'pt', 'Número de amostras', 'O número de amostras (ou peso total) em uma vizinhança para um ponto a ser'
                                           ' considerado como um ponto central.'),

        (4331, 'en', 'Metric', 'The metric to use when calculating distance between instances in a feature array.'),
        (4331, 'pt', 'Métrica', 'A métrica a ser usada ao calcular a distância entre instâncias em uma matriz de '
                                'features.'),

        (4332, 'en', 'Metric params', 'Additional keyword arguments for the metric function.'),
        (4332, 'pt', 'Parâmetros da métrica', 'Argumentos adicionais para a função métrica.'),

        (4333, 'en', 'Algorithm', 'The algorithm to be used by the NearestNeighbors module to compute pointwise '
                                  'distances and find nearest neighbors.'),
        (4333, 'pt', 'Algoritmo', 'O algoritmo a ser usado pelo módulo NearestNeighbors para calcular distâncias em '
                                  'pontos e encontrar os vizinhos mais próximos.'),

        (4334, 'en', 'Leaf size', 'Leaf size passed to BallTree or KDTree.'),
        (4334, 'pt', 'Tamanho da folha', 'Tamanho da folha passado para o BallTree ou KDTree.'),

        (4335, 'en', 'Power', 'The power of the Minkowski metric to be used to calculate distance between points.'),
        (4335, 'pt', 'Potência', 'A potência da métrica de Minkowski a ser usada para calcular a distância entre '
                                 'pontos.'),

        (4336, 'en', 'Number of jobs', 'The number of parallel jobs to run.'),
        (4336, 'pt', 'Número de tarefas', 'O número de tarefas paralelas a serem executadas.'),
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
        (4093, 'INPUT', '', 1, 'ONE', 4043, 'train input data'),
        (4094, 'OUTPUT', '', 1, 'ONE', 4043, 'output data'),
        (4095, 'OUTPUT', '', 2, 'MANY', 4043, 'model'),
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
        (4093, 1),
        (4094, 1),
        (4095, 2),
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
        (4093, "en", 'input data', 'Input data'),
        (4093, "pt", 'dados de entrada', 'Dados de entrada'),
        (4094, "en", 'output data', 'Output data'),
        (4094, "pt", 'dados de saída', 'Dados de saída'),
        (4095, "en", 'model', 'Model'),
        (4095, "pt", 'modelo', 'Modelo'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 4043'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = 4043'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id = 4043'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 4043 AND platform_id = 4'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id = 4032'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4327 AND 4336'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id = 4032'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4327 AND 4336'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4043'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4093 AND 4095'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 4093 AND 4095'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4093 AND 4095'),

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
