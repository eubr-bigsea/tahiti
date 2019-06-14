# -*- coding: utf-8 -*-
"""Add Keras - Loss and Optimizer Functions Forms

Revision ID: 73f22f178b14
Revises: ec9191676104
Create Date: 2018-10-05 17:39:20.466245

"""
import json
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = '73f22f178b14'
down_revision = 'ec9191676104'
branch_labels = None
depends_on = None


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        #Loss
        (5161, 1, 1, 'execution'), #Loss functions
        #Optimizer
        (5162, 1, 1, 'execution'), #Optimizer functions
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
        #Loss
        (5161, 'en', 'Execution'),
        (5161, 'pt', 'Execução'),
        #Optimizer
        (5162, 'en', 'Execution'),
        (5162, 'pt', 'Execução'),
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
        #Loss Functions
        (5061, 41),  #appearance
        (5061, 5161),  # own execution form

        #Optimizer functions
        (5062, 41),  #appearance
        (5062, 5162),  # own execution form
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

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [
        #Loss functions
        (5161, 'loss', 'TEXT', 0, 1, None, 'dropdown', None,
         json.dumps([
             {"key": "squared_hinge", "value": "squared_hinge"},
             {"key": "hinge", "value": "hinge"},
             {"key": "categorical_hinge", "value": "categorical_hinge"},
             {"key": "logcosh", "value": "logcosh"},
             {"key": "categorical_crossentropy", "value": "categorical_crossentropy"},
             {"key": "sparse_categorical_crossentropy", "value": "sparse_categorical_crossentropy"},
             {"key": "binary_crossentropy", "value": "binary_crossentropy"},
             {"key": "kullback_leibler_divergence", "value": "kullback_leibler_divergence"},
             {"key": "poisson", "value": "poisson"},
             {"key": "cosine_proximity", "value": "cosine_proximity"},
             {"key": "mean_squared_error", "value": "mean_squared_error"},
             {"key": "mean_absolute_error", "value": "mean_absolute_error"},
             {"key": "mean_absolute_percentage_error", "value": "mean_absolute_percentage_error"},
             {"key": "mean_squared_logarithmic_error", "value": "mean_squared_logarithmic_error"},
         ]),
         'EXECUTION', 5161),

        #Optimizer functions
        (5162, 'optimizer', 'TEXT', 1, 2, 'adam', 'dropdown', None,
         json.dumps([
             {"key": "sgd", "value": "sgd"},
             {"key": "rmsprop", "value": "rmsprop"},
             {"key": "adagrad", "value": "adagrad"},
             {"key": "adadelta", "value": "adadelta"},
             {"key": "adam", "value": "adam"},
             {"key": "adamax", "value": "adamax"},
             {"key": "nadam", "value": "nadam"},
         ]),
         'EXECUTION', 5162),
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
        #Loss function
        (5161, 'en', 'Loss function', 'A loss function (or objective function, or optimization score '
                                      'function) is one of the two parameters required to compile a model.'),

        #Optimizer function
        (5162, 'en', 'Optimizer function', 'An optimizer is one of the two arguments required for '
                                          'compiling a Keras model.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5161 AND 5162'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5161 AND 5162'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5161 AND 5162'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5161 AND 5162'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id BETWEEN 5061 AND 5062'),
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

