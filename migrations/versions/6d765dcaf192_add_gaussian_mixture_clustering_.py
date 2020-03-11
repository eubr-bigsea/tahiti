# -*- coding: utf-8 -*-

"""Add Gaussian Mixture Clustering Operation (scikit_learn).

Revision ID: 6d765dcaf192
Revises: 2b87a7f6e8fb
Create Date: 2020-01-23 16:48:08.244366

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
revision = '6d765dcaf192'
down_revision = '2b87a7f6e8fb'
branch_labels = None
depends_on = None


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')

    data = [
        (4042, 4)
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
        (4042, "gaussian-mixture", 1, 'ACTION', ''),
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
        (8, 4042),
        (19, 4042)
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
        (4042, "pt", 'Mistura de Gaussianas', 'Agrupamento Mistura de Gaussianas.'),
        (4042, "en", 'Gaussian Mixture', 'Gaussian Mixture Clustering.')
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
        (4042, 41),  #appearance
        (4042, 4031),  # own execution form
        (4042, 110)
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
        (4031, 1, 1, 'execution'), #data_format
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
        (4031, 'en', 'Execution'),
        (4031, 'pt', 'Execução'),
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
        (4314, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4031, None),
        (4315, 'prediction', 'TEXT', 0, 2, 'prediction', 'text', None, None, 'EXECUTION', 4031, None),
        (4316, 'n_components', 'INTEGER', 1, 3, 1, 'integer', None, None, 'EXECUTION', 4031, None),
        (4317, 'covariance_type', 'TEXT', 0, 7, 'full', 'dropdown', None,
         json.dumps([
             {'key': 'tied', 'value': 'tied'},
             {'key': 'full', 'value': 'full'},
             {'key': 'diag', 'value': 'diag'},
             {'key': 'spherical', 'value': 'spherical'},
         ]),
         'EXECUTION', 4031, None),
        (4318, 'tol', 'DECIMAL', 0, 5, 1e-3, 'decimal', None, None, 'EXECUTION', 4031, None),
        (4319, 'reg_covar', 'DECIMAL', 0, 6, 1e-6, 'text', None, None, 'EXECUTION', 4031, None),
        (4320, 'max_iter', 'INTEGER', 1, 4, 100, 'integer', None, None, 'EXECUTION', 4031, None),
        (4321, 'n_init', 'INTEGER', 0, 8, 1, 'integer', None, None, 'EXECUTION', 4031, None),
        (4322, 'init_params', 'TEXT', 0, 9, 'kmeans', 'dropdown', None,
         json.dumps([
             {'key': 'kmeans', 'value': 'kmeans'},
             {'key': 'random', 'value': 'random'},
         ]),
         'EXECUTION', 4031, None),
        (4323, 'weights_init', 'TEXT', 0, 10, None, 'text', None, None, 'EXECUTION', 4031, None),
        (4324, 'means_init', 'TEXT', 0, 11, None, 'text', None, None, 'EXECUTION', 4031, None),
        (4325, 'precisions_init', 'TEXT', 0, 12, None, 'text', None, None, 'EXECUTION', 4031, None),
        (4326, 'random_state', 'INTEGER', 0, 13, None, 'integer', None, None, 'EXECUTION', 4031, None),
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
        (4314, 'en', 'Features', 'Features.'),
        (4314, 'pt', 'Atributo(s) previsor(es)', 'Atributo(s) previsor(es).'),

        (4315, 'en', 'Prediction (new attribute)', 'Prediction (new attribute).'),
        (4315, 'pt', 'Atributo com a predição (novo)', 'Atributo com a predição (novo).'),

        (4316, 'en', 'Number of components', 'The number of mixture components.'),
        (4316, 'pt', 'Número de agrupamentos (K)', 'Número de agrupamentos (K).'),

        (4317, 'en', 'Covariance type', 'String describing the type of covariance parameters to use.'),
        (4317, 'pt', 'Tipo de covariância', 'String descrevendo o tipo de parâmetros de covariância a serem usados.'),

        (4318, 'en', 'Tolerance', 'The convergence threshold.'),
        (4318, 'pt', 'Tolerância', ' Tolerância de convergência para as somas das distâncias intra-cluster do ponto ao'
                                   ' centroide.'),

        (4319, 'en', 'Regularization of covariance', 'Non-negative regularization added to the diagonal of '
                                                     'covariance.'),
        (4319, 'pt', 'Regularização da covariância', 'Regularização não negativa adicionada à diagonal da '
                                                     'covariância.'),

        (4320, 'en', 'Max. number of iterations', 'The number of EM iterations to perform.'),
        (4320, 'pt', 'Número máx. de iterações', 'Número máx. de iterações'),

        (4321, 'en', 'Number of initializations', 'The number of initializations to perform.'),
        (4321, 'pt', 'Número de inicializações', 'O número de inicializações a serem executadas.'),

        (4322, 'en', 'Method', 'The method used to initialize the weights, the means and the precisions.'),
        (4322, 'pt', 'Método', 'O método usado para inicializar os pesos, os meios e as precisões.'),

        (4323, 'en', 'Initial weights', 'The user-provided initial weights.'),
        (4323, 'pt', 'Pesos iniciais', 'Os pesos iniciais fornecidos pelo usuário.'),

        (4324, 'en', 'Initial means', 'The user-provided initial means.'),
        (4324, 'pt', 'Meios iniciais', 'Os meios iniciais fornecidos pelo usuário.'),

        (4325, 'en', 'Initial precisions', 'The user-provided initial precisions (inverse of the covariance '
                                           'matrices).'),
        (4325, 'pt', 'Precisões iniciais', 'As precisões iniciais fornecidas pelo usuário (inversa das matrizes de '
                                           'covariância).'),

        (4326, 'en', 'Seed', 'The seed used by the random number generator.'),
        (4326, 'pt', 'Semente', 'A semente usada pelo gerador de números aleatórios.'),
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
        (4090, 'INPUT', '', 1, 'ONE', 4042, 'train input data'),
        (4091, 'OUTPUT', '', 1, 'ONE', 4042, 'output data'),
        (4092, 'OUTPUT', '', 2, 'MANY', 4042, 'model'),
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
        (4090, 1),
        (4091, 1),
        (4092, 2),
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
        (4090, "en", 'input data', 'Input data'),
        (4090, "pt", 'dados de entrada', 'Dados de entrada'),
        (4091, "en", 'output data', 'Output data'),
        (4091, "pt", 'dados de saída', 'Dados de saída'),
        (4092, "en", 'model', 'Model'),
        (4092, "pt", 'modelo', 'Modelo'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 4042'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = 4042'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id = 4042'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 4042 AND platform_id = 4'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id = 4031'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4314 AND 4326'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id = 4031'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4314 AND 4326'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4042'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4090 AND 4092'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 4090 AND 4092'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4090 AND 4092'),

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