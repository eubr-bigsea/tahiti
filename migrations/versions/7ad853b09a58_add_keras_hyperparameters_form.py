# -*- coding: utf-8 -*-
"""Add keras hyperparameters form.

Revision ID: 7ad853b09a58
Revises: 1d36e073f89d
Create Date: 2018-11-19 11:29:50.593296

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
revision = '7ad853b09a58'
down_revision = '1d36e073f89d'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5


def _insert_platform_form():
    operation_form_table = table(
        'platform_form',
        column('platform_id', Integer),
        column('operation_form_id', Integer))

    columns = ('platform_id', 'operation_form_id')
    data = [
        #Hyperparameters
        (KERAS_PLATAFORM_ID, 5161),
        #Data
        (KERAS_PLATAFORM_ID, 5162),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(operation_form_table, rows)


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

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [
        # Number of epochs
        (5163, 'number_of_epochs', 'INTEGER', 1, 1, 10, 'integer', None, None, 'EXECUTION', 5161),
        # Batch size
        (5164, 'batch_size', 'INTEGER', 1, 2, 32, 'integer', None, None, 'EXECUTION', 5161),

        # Metrics
        (5165, 'metrics', 'TEXT', 1, 5, "Categorical Accuracy", 'select2', None,
         json.dumps([
             {"value": "Binary Accuracy", "key": "acc"},
             {"value": "Categorical Accuracy", "key": "acc"},
             {"value": "Sparse Categorical Accuracy", "key": "sparse_categorical_accuracy"},
             {"value": "Top k Categorical Accuracy", "key": "top_k_categorical_accuracy"},
             {"value": "Sparse Top k Categorical Accuracy", "key": "sparse_top_k_categorical_accuracy"},
             {"value": "Mean Squared Error", "key": "mse"},
             {"value": "Mean Absolute Error", "key": "mae"},
             {"value": "Mean Absolute Percentage Error", "key": "mape"},
             {"value": "Cosine Proximity", "key": "cosine"},
         ]),
         'EXECUTION', 5161),

        # Batch size
        (5166, 'k', 'INTEGER', 0, 6, 5, 'integer', None, None, 'EXECUTION', 5161),
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
        # Number of epoch
        (5163, 'en', 'Number of epochs', 'Integer. Number of epochs to train the model. '
                                         'An epoch is an iteration over the entire x and y '
                                         'data provided. Note that in conjunction with '
                                         'initial_epoch,  epochs is to be understood as "final epoch". '
                                         'The model is not trained for a number of iterations '
                                         'given by epochs, but merely until the epoch of '
                                         'index epochs is reached.'),

        # Batch size
        (5164, 'en', 'Batch size', 'Integer or None. Number of samples per gradient update. '
                                   'If unspecified, batch_size will default to 32.'),

        (5165, 'en', 'Metrics', 'A metric is a function that is used to judge the performance of your model.'),

        (5166, 'en', 'K', 'K is a parameter required for the metrics '
                          'related to the Top K Categorical Accuracy functions.'),
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
        (5060, "group", 6, 6),
        (5061, "subgroup", 1, 1),
        (5062, "subgroup", 2, 2),
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
        #Loss Functions
        (5060, 5061),
        (5060, 5062),
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
        (5060, "en", 'Functions'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')
    data = [
        (5061, KERAS_PLATAFORM_ID),#loss functions
        (5062, KERAS_PLATAFORM_ID),#optimizer functions
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ('UPDATE operation_form_field '
     'SET `order` = 3 '
     'WHERE id = 5161',
     'UPDATE operation_form_field '
     'SET `order` = 1 '
     'WHERE id = 5161'),

    ('UPDATE operation_form_field '
     'SET form_id = 5161, `order` = 4 '
     'WHERE id = 5162',
     'UPDATE operation_form_field '
     'SET form_id = 5162, `order` = 2 '
     'WHERE id = 5162'),

    ('UPDATE operation_form_field '
     'SET form_id = 5162 , `order` = 3 '
     'WHERE id BETWEEN 5171 AND 5177 ',
     'UPDATE tahiti2.operation_form_field t1 '
     'INNER JOIN tahiti2.operation_form_field t2 '
     'ON (t1.id = t2.id AND t1.id BETWEEN 5171 AND 5177) '
     'SET t1.form_id = t1.id'),

    ('UPDATE operation_form_translation '
     'SET name = "Hyperparameters" '
     'WHERE id = 5161 AND locale = "en"',
     'UPDATE operation_form_translation '
     'SET name = "Execution" '
     'WHERE id = 5161 AND locale = "en"'),

    ('UPDATE operation_form_translation '
     'SET name = "Hiperparâmetros" '
     'WHERE id = 5161 AND locale = "pt"',
     'UPDATE operation_form_translation '
     'SET name = "Execução" '
     'WHERE id = 5161 AND locale = "pt"'),

    ('UPDATE operation_form_translation '
     'SET name = "Data" '
     'WHERE id = 5162 AND locale = "en"',
     'UPDATE operation_form_translation '
     'SET name = "Execution" '
     'WHERE id = 5162 AND locale = "en"'),

    ('UPDATE operation_form_translation '
     'SET name = "Dados" '
     'WHERE id = 5162 AND locale = "pt"',
     'UPDATE operation_form_translation '
     'SET name = "Execução" '
     'WHERE id = 5162 AND locale = "pt"'),

    ('UPDATE operation_form '
     'SET `order` = 6 '
     'WHERE id = 5161',
     'UPDATE operation_form '
     'SET `order` = 1 '
     'WHERE id = 5161'),

    ('UPDATE operation_form '
     'SET `order` = 7 '
     'WHERE id = 5162',
     'UPDATE operation_form '
     'SET `order` = 1 '
     'WHERE id = 5162'),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field '
     'WHERE id BETWEEN 5163 AND 5166'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id BETWEEN 5163 AND 5166'),

    (_insert_platform_form,
     'DELETE FROM platform_form '
     'WHERE platform_id = {} AND operation_form_id IN (5161, 5162)'.format(KERAS_PLATAFORM_ID)),

    ('DELETE FROM operation_category_operation WHERE operation_id BETWEEN 5061 AND 5062',
     _insert_operation_category_operation),

    ('DELETE FROM operation_category_translation WHERE id = 5060',
     _insert_operation_category_translation),

    ('DELETE FROM operation_category WHERE id BETWEEN 5060 AND 5062',
     _insert_operation_category),

    ('DELETE FROM operation_platform '
     'WHERE operation_id BETWEEN 5061 AND 5062 AND platform_id = {}'.format(KERAS_PLATAFORM_ID),
     _insert_operation_platform),
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

