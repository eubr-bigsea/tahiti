# -*- coding: utf-8 -*-
"""Add Keras - Core Layers - Dense forms

Revision ID: cbcb14e49217
Revises: 718021239cfd
Create Date: 2018-10-03 14:19:05.693947

"""
from alembic import op
import sqlalchemy as sa
import json
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = 'cbcb14e49217'
down_revision = '718021239cfd'
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
        #Dense
        (5100, 1, 1, 'execution'), #units
        (5101, 1, 1, 'execution'), #activation
        (5102, 1, 1, 'execution'), #use_bias
        (5103, 1, 1, 'execution'), #kernel_initializer
        (5104, 1, 1, 'execution'), #bias_initializer
        (5105, 1, 1, 'execution'), #kernel_regularizer
        (5106, 1, 1, 'execution'), #bias_regularizer
        (5107, 1, 1, 'execution'), #activity_regularizer
        (5108, 1, 1, 'execution'), #kernel_constraint
        (5109, 1, 1, 'execution'), #bias_constraint
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
        #Dense - units
        (5100, 'en', 'Execution'),
        (5100, 'pt', 'Execução'),

        #Dense - activation
        (5101, 'en', 'Execution'),
        (5101, 'pt', 'Execução'),

        #Dense - use_bias
        (5102, 'en', 'Execution'),
        (5102, 'pt', 'Execução'),

        #Dense - kernel_initializer
        (5103, 'en', 'Execution'),
        (5103, 'pt', 'Execução'),

        #Dense - bias_initializer
        (5104, 'en', 'Execution'),
        (5104, 'pt', 'Execução'),

        #Dense - kernel_regularizer
        (5105, 'en', 'Execution'),
        (5105, 'pt', 'Execução'),

        #Dense - bias_regularizer
        (5106, 'en', 'Execution'),
        (5106, 'pt', 'Execução'),

        #Dense - activity_regularizer
        (5107, 'en', 'Execution'),
        (5107, 'pt', 'Execução'),

        #Dense - kernel_constraint
        (5108, 'en', 'Execution'),
        (5108, 'pt', 'Execução'),

        #Dense - bias_constraint
        (5109, 'en', 'Execution'),
        (5109, 'pt', 'Execução'),
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
        (5011, 41),  #appearance

        #Dense - units
        (5011, 5100),  # own execution form

        #Dense - activation
        (5011, 5101),  # own execution form

        #Dense - use_bias
        (5011, 5102),  # own execution form

        #Dense - kernel_initializer
        (5011, 5103),  # own execution form

        #Dense - bias_initializer
        (5011, 5104),  # own execution form

        #Dense - kernel_regularizer
        (5011, 5105),  # own execution form

        #Dense - bias_regularizer
        (5011, 5106),  # own execution form

        #Dense - activity_regularizer
        (5011, 5107),  # own execution form

        #Dense - kernel_constraint
        (5011, 5108),  # own execution form

        #Dense - bias_constraint
        (5011, 5109),  # own execution form
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
        #Dense - units
        (5100, 'units', 'INTEGER', 1, 1, None, 'integer', None, None, 'EXECUTION', 5100),

        #Dense - activation
        (5101, 'activation', 'TEXT', 0, 2, 'linear', 'dropdown', None,
         json.dumps([
             {"key": "elu", "value": "elu"},
             {"key": "exponential", "value": "exponential"},
             {"key": "hard_sigmoid", "value": "hard_sigmoid"},
             {"key": "linear", "value": "linear"},
             {"key": "relu", "value": "relu"},
             {"key": "selu", "value": "selu"},
             {"key": "sigmoid", "value": "sigmoid"},
             {"key": "softmax", "value": "softmax"},
             {"key": "softplus", "value": "softplus"},
             {"key": "softsign", "value": "softsign"},
             {"key": "tanh", "value": "tanh"}
         ]),
         'EXECUTION', 5101),

        #Dense - use_bias
        (5102, 'use_bias', 'INTEGER', 0, 3, None, 'checkbox', None, None, 'EXECUTION', 5102),

        #Dense - kernel_initializer
        (5103, 'kernel_initializer', 'TEXT', 0, 4, None, 'dropdown', None,
         json.dumps([
             {"key": "constant", "value": "constant"},
             {"key": "glorot_normal", "value": "glorot_normal"},
             {"key": "glorot_uniform", "value": "glorot_uniform"},
             {"key": "he_normal", "value": "he_normal"},
             {"key": "he_uniform", "value": "he_uniform"},
             {"key": "identity", "value": "identity"},
             {"key": "initializer", "value": "initializer"},
             {"key": "lecun_normal", "value": "lecun_normal"},
             {"key": "lecun_uniform", "value": "lecun_uniform"},
             {"key": "ones", "value": "ones"},
             {"key": "orthogonal", "value": "orthogonal"},
             {"key": "randomNormal", "value": "randomNormal"},
             {"key": "randomUniform", "value": "randomUniform"},
             {"key": "truncatedNormal", "value": "truncatedNormal"},
             {"key": "varianceScaling", "value": "varianceScaling"},
             {"key": "zeros", "value": "zeros"}
         ]),
         'EXECUTION', 5103),

        #Dense - bias_initializer
        (5104, 'bias_initializer', 'TEXT', 0, 5, None, 'dropdown', None,
         json.dumps([
              {"key": "constant", "value": "constant"},
              {"key": "glorot_normal", "value": "glorot_normal"},
              {"key": "glorot_uniform", "value": "glorot_uniform"},
              {"key": "he_normal", "value": "he_normal"},
              {"key": "he_uniform", "value": "he_uniform"},
              {"key": "identity", "value": "identity"},
              {"key": "initializer", "value": "initializer"},
              {"key": "lecun_normal", "value": "lecun_normal"},
              {"key": "lecun_uniform", "value": "lecun_uniform"},
              {"key": "ones", "value": "ones"},
              {"key": "orthogonal", "value": "orthogonal"},
              {"key": "randomNormal", "value": "randomNormal"},
              {"key": "randomUniform", "value": "randomUniform"},
              {"key": "truncatedNormal", "value": "truncatedNormal"},
              {"key": "varianceScaling", "value": "varianceScaling"},
              {"key": "zeros", "value": "zeros"}]
         ),
         'EXECUTION', 5104),

        #Dense - kernel_regularizer
        (5105, 'kernel_regularizer', 'TEXT', 0, 6, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5105),

        #Dense - bias_regularizer
        (5106, 'bias_regularizer', 'TEXT', 0, 7, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5106),

        #Dense - activity_regularizer
        (5107, 'activity_regularizer', 'TEXT', 0, 8, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5107),

        #Dense - kernel_constraint
        (5108, 'kernel_constraint', 'TEXT', 0, 9, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5108),

        #Dense - bias_constraint
        (5109, 'bias_constraint', 'TEXT', 0, 10, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
        ]),
         'EXECUTION', 5109),
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
        #Dense - units
        (5100, 'en', 'Output dimensions', 'Positive integer, dimensionality of the output space.'),

        #Dense - activation
        (5101, 'en', 'Activation function', 'Activation function to use. If you do not specify anything, no activation is applied (ie. \"linear\" activation: a(x) = x).'),

        #Dense - use_bias
        (5102, 'en', 'Use bias', 'Boolean (True|False), whether the layer uses a bias vector.'),

        #Dense - kernel_initializer
        (5103, 'en', 'Weight initialization function', ' Initializer for the kernel weights matrix.'),

        #Dense - bias_initializer
        (5104, 'en', 'Bias initialization function', 'Initializer for the bias vector.'),

        #Dense - kernel_regularizer
        (5105, 'en', 'Regularizer for input weight', 'Regularizer function applied to the kernel weights matrix'),

        #Dense - bias_regularizer
        (5106, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),

        #Dense - activity_regularizer
        (5107, 'en', 'Activity regularizer', 'Regularizer function applied to the output of the layer (its "activation").'),

        #Dense - kernel_constraint
        (5108, 'en', 'Weight constraint', 'Constraint function applied to the kernel weights matrix.'),

        #Dense - bias_constraint
        (5109, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5100 AND 5109'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5100 AND 5109'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5100 AND 5109'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5100 AND 5109'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 5011'),
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
