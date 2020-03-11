# -*- coding: utf-8 -*-

"""Update KNN classifier (scikit_learn).

Revision ID: f744c0dbb4a1
Revises: 77cb7c3ffbee
Create Date: 2019-12-03 08:59:45.338834

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
revision = 'f744c0dbb4a1'
down_revision = '77cb7c3ffbee'
branch_labels = None
depends_on = None


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        #Flatten - data_format
        (4036, 41),  #appearance
        (4036, 4029),  # own execution form
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
        (4029, 1, 1, 'execution'), #data_format
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
        (4029, 'en', 'Execution'),
        (4029, 'pt', 'Execução'),
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
        (4254, 'n_neighbors', 'INTEGER', 0, 1, 5, 'integer', None,  None, 'EXECUTION', 4029, None),
        (4255, 'weights', 'TEXT', 0, 2, 'uniform', 'dropdown', None,
         json.dumps([
             {'key': 'uniform', 'value': 'uniform'},
             {'key': 'distance', 'value': 'distance'},
         ]),
         'EXECUTION', 4029, None),
        (4256, 'algorithm', 'TEXT', 0, 3, 'auto', 'dropdown', None,
         json.dumps([
             {'key': 'auto', 'value': 'auto'},
             {'key': 'ball_tree', 'value': 'ball_tree'},
             {'key': 'kd_tree', 'value': 'kd_tree'},
             {'key': 'brute', 'value': 'brute'},
         ]),
         'EXECUTION', 4029, None),
        (4257, 'leaf_size', 'INTEGER', 0, 4, 30, 'integer', None,  None, 'EXECUTION', 4029, None),
        (4258, 'p', 'INTEGER', 0, 5, 2, 'integer', None,  None, 'EXECUTION', 4029, None),
        (4259, 'metric', 'INTEGER', 0, 6, 'minkowski',  'dropdown', None,
         json.dumps([
             {'key': 'minkowski', 'value': 'minkowski'},
             {'key': 'euclidean', 'value': 'euclidean'},
             {'key': 'manhattan', 'value': 'manhattan'},
             {'key': 'chebyshev', 'value': 'chebyshev'},
             {'key': 'wminkowski', 'value': 'wminkowski'},
             {'key': 'seuclidean', 'value': 'seuclidean'},
             {'key': 'mahalanobis', 'value': 'mahalanobis'},
         ]),
         'EXECUTION', 4029, None),
        (4260, 'metric_params', 'TEXT', 0, 7, None, 'text', None,  None, 'EXECUTION', 4029, None),
        (4261, 'n_jobs', 'INTEGER', 0, 8, None, 'integer', None,  None, 'EXECUTION', 4029, None),
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
        (4254, 'en', 'Number of neighbors', 'Number of neighbors to use by default for kneighbors queries.'),
        (4254, 'pt', 'Número de vizinhos', 'Número de vizinhos a serem usados por padrão para consultas kneighbors.'),

        (4255, 'en', 'Weights', 'Weight function used in prediction.'),
        (4255, 'pt', 'Pesos', 'Função de peso usada na previsão.'),

        (4256, 'en', 'Algorithm', 'Algorithm used to compute the nearest neighbors.'),
        (4256, 'pt', 'Algoritmo', 'Algoritmo usado para calcular os vizinhos mais próximos.'),

        (4257, 'en', 'Leaf size', 'Leaf size passed to BallTree or KDTree.'),
        (4257, 'pt', 'Tamanho da folha', 'Tamanho da folha passado para o BallTree ou KDTree.'),

        (4258, 'en', 'Power', 'Power parameter for the Minkowski metric.'),
        (4258, 'pt', 'Potência', 'Parâmetro de potência para a métrica de Minkowski.'),

        (4259, 'en', 'Metric', 'The distance metric to use for the tree.'),
        (4259, 'pt', 'Métrica', 'A métrica de distância a ser usada na árvore.'),

        (4260, 'en', 'Metric parameters', 'Additional keyword arguments for the metric function (dictionary).'),
        (4260, 'pt', 'Parâmetros da métrica', 'Argumentos de palavras-chave adicionais para a função métrica'
                                              ' (dicionário).'),

        (4261, 'en', 'Number of jobs', 'The number of parallel jobs to run for neighbors search.'),
        (4261, 'pt', 'Número de tarefas', 'O número de tarefas paralelas a serem executadas na pesquisa de vizinhos.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `default` = 5 WHERE id = 3014 OR id = 4024""",
     """UPDATE operation_form_field SET `default` = 1 WHERE id = 3014 OR id = 4024"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4253 AND 4261'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4253 AND 4261'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4036 AND operation_form_id = 41 OR operation_form_'
     'id = 4029'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id=4029'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id=4029'),
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