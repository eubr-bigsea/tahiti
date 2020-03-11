# -*- coding: utf-8 -*-

"""Insert operation local outlier factor

Revision ID: b819b756d9f9
Revises: 5b7ffd45dbea
Create Date: 2019-08-29 15:11:41.524975

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
revision = 'b819b756d9f9'
down_revision = '5b7ffd45dbea'
branch_labels = None
depends_on = None

SCIKIT_LEARN_PLATAFORM_ID = 4
ID_OPERATION = 4037

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
        (ID_OPERATION, "local-outlier-factor", 1, 'ACTION', ''),
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

    columns = ('id', 'type', 'order', 'default_order')
    data = [
        (4002, "subgroup", 1, 1),
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
        (8, 4037),
        (4002, 4037)
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (4002, "pt", 'Detecção de Anomalia'),
        (4002, "en", 'Outlier Detection'),
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
        (ID_OPERATION, "pt", 'Local Outlier Factor (LOF)', ''),
        (ID_OPERATION, "en", 'Local Outlier Factor (LOF)', 'The Local Outlier Factor (LOF) algorithm is '
                                                           'an unsupervised anomaly detection method which computes '
                                                           'the local density deviation of a given data point with '
                                                           'respect to its neighbors. It considers as outliers the '
                                                           'samples that have a substantially lower density than '
                                                           'their neighbors. ')
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
        (ID_OPERATION, 4024),  # own execution form
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
        (4024, 1, 1, 'execution'), #data_format
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
        (4024, 'en', 'Execution'),
        (4024, 'pt', 'Execução'),
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
    enable_condition = 'this.metric.internalValue === "minkowski"'
    data = [
        #Flatten - data_format
        (4119, 'n_neighbors', 'INTEGER', 0, 1, 20, 'integer', None, None, 'EXECUTION', 4024, None),
        (4115, 'algorithm', 'TEXT', 0, 1, "auto", 'dropdown', None,
         json.dumps([
             {"key": "ball_tree", "value": "ball_tree"},
             {"key": "kd_tree", "value": "kd_tree"},
             {"key": "brute", "value": "brute"},
             {"key": "auto", "value": "auto"}
         ]),
         'EXECUTION', 4024, None),
        (4117, 'leaf_size', 'INTEGER', 0, 1, 30, 'integer', None, None, 'EXECUTION', 4024, None),
        (4113, 'metric', 'TEXT', 1, 1, "minkowski", 'dropdown', None,
         json.dumps([
             {"key": "cityblock", "value": "cityblock"},
             {"key": "cosine", "value": "cosine"},
             {"key": "euclidean", "value": "euclidean"},
             {"key": "manhattan", "value": "manhattan"},
             {"key": "braycurtis", "value": "braycurtis"},
             {"key": "canberra", "value": "canberra"},
             {"key": "chebyshev", "value": "chebyshev"},
             {"key": "correlation", "value": "correlation"},
             {"key": "dice", "value": "dice"},
             {"key": "hamming", "value": "hamming"},
             {"key": "jaccard", "value": "jaccard"},
             {"key": "kulsinski", "value": "kulsinski"},
             {"key": "mahalanobis", "value": "mahalanobis"},
             {"key": "minkowski", "value": "minkowski"},
             {"key": "rogerstanimoto", "value": "rogerstanimoto"},
             {"key": "russellrao", "value": "russellrao"},
             {"key": "seuclidean", "value": "seuclidean"},
             {"key": "sokalmichener", "value": "sokalmichener"},
             {"key": "sokalsneath", "value": "sokalsneath"},
             {"key": "sqeuclidean", "value": "sqeuclidean"},
             {"key": "yule", "value": "yule"},
         ]),
         'EXECUTION', 4024, None),
        (4116, 'contamination', 'FLOAT', 0, 1, 0.22, 'decimal', None, None, 'EXECUTION', 4024, None), #Changed in
        # version 0.20: The default value of contamination will change from 0.1 in 0.20 to 'auto' in 0.22.
        (4118, 'p', 'INTEGER', 0, 1, 2, 'integer', None, None, 'EXECUTION', 4024, enable_condition),
        (4121, 'metric_params', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 4024, None),
        (4114, 'novelty', 'INTEGER', 1, 1, None, 'checkbox', None, None, 'EXECUTION', 4024, None),
        (4120, 'n_jobs', 'INTEGER', 0, 1, None, 'integer', None, None, 'EXECUTION', 4024, None),
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
        (4119, 'en', 'Number of neighbors', 'Number of neighbors.'),
        (4119, 'pt', 'Número de vizinhos', 'Número de vizinhos'),

        (4115, 'en', 'Algorithm', 'Algorithm used to compute the nearest neighbors.'),
        (4115, 'pt', 'Algoritmo', 'Algoritmo usado para computar os vizinhos mais próximos.'),

        (4117, 'en', 'Leaf size', 'Leaf size.'),
        (4117, 'pt', 'Tamanho da folha', 'Tamanho da folha.'),

        (4113, 'en', 'Metric', 'Metric used for the distance computation.'),
        (4113, 'pt', 'Métrica', 'Métrica usada para computar a distância.'),

        (4116, 'en', 'Contamination', 'The amount of contamination of the data set, i.e. the proportion of outliers '
                                      'in the data set.'),
        (4116, 'pt', 'Contaminação', 'A quantidade de contaminação do conjunto de dados, ou seja, a '
                                     'proporção de outliers.'),

        (4118, 'en', 'Minkowski parameter', 'Parameter for the Minkowski metric.'),
        (4118, 'pt', 'Parâmetro para Minkowski', 'Parâmetro para a métrica de Minkowski.'),

        (4121, 'en', 'Metric parameters', 'Additional keyword arguments for the metric function.'),
        (4121, 'pt', 'Parâmetros da métrica', 'Palvras-chave adicoinais para a função de métrica.'),

        (4114, 'en', 'Novelty', 'Use or not LocalOutlierFactor for novelty detection.'),
        (4114, 'pt', 'Novidade', 'Usar ou não LocalOutlierFactor para detecção de novidade.'),

        (4120, 'en', 'Parallel jobs', 'The number of parallel jobs to run for neighbors search.'),
        (4120, 'pt', 'Jobs paralelos', 'Número de tarefas paralelas a serem executadas na pesquisa de vizinhos.'),

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
        (4078, 'INPUT', '', 1, 'ONE', ID_OPERATION, 'input data'),
        (4079, 'OUTPUT', '', 1, 'ONE', ID_OPERATION, 'output data'),
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
        (4078, 1),
        (4079, 1),
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
        (4078, "en", 'input data', 'Input data'),
        (4078, "pt", 'dados de entrada', 'Dados de entrada'),
        (4079, "en", 'output data', 'Output data'),
        (4079, "pt", 'dados de saída', 'Dados de saída'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 4037'),
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id = 4002'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = {}'.format(ID_OPERATION)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id IN (4037)'),
    (_insert_operation_category_translation,
     'DELETE FROM operation_category_translation WHERE id = 4002'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 4037 AND platform_id = {}'.format(SCIKIT_LEARN_PLATAFORM_ID)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id=4024'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4113 AND 4121'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id=4024'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4113 AND 4121'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4037'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id IN (4078, 4079)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id IN (4078, 4079)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN (4078, 4079)'),

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
