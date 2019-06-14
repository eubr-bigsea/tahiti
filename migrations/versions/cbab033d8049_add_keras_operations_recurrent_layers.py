# -*- coding: utf-8 -*-
"""Add keras operations - Recurrent Layers

Revision ID: cbab033d8049
Revises: 7ad853b09a58
Create Date: 2018-12-04 10:36:34.936002

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
revision = 'cbab033d8049'
down_revision = '7ad853b09a58'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')
    data = [
        (5052, KERAS_PLATAFORM_ID), #CuDNNLSTM
        # 5041 - LSTM - Was added with the keras platform review "86dd15ad5169"
        # 5042 - Simple-RNN - Was added with the keras platform review "86dd15ad5169"
        (5043, KERAS_PLATAFORM_ID), #RNN - not implemented, yet.
        (5044, KERAS_PLATAFORM_ID), #GRU
        (5045, KERAS_PLATAFORM_ID), #ConvLSTM2D
        (5046, KERAS_PLATAFORM_ID), #SimpleRNNCell
        (5047, KERAS_PLATAFORM_ID), #GRUCell
        (5048, KERAS_PLATAFORM_ID), #LSTMCell
        (5049, KERAS_PLATAFORM_ID), #CuDNNGRU

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
        (5052, "cu-dnn-lstm", 0, 'ACTION', ''), #Can only be run on GPU, with the TensorFlow backend. enabled=0
        # 5041 - LSTM - Was added with the keras platform review "86dd15ad5169"
        # 5042 - Simple-RNN - Was added with the keras platform review "86dd15ad5169"
        (5043, "rnn", 1, 'ACTION', ''),
        (5044, "gru", 1, 'ACTION', ''),
        (5045, "conv-lstm-2D", 1, 'ACTION', ''),
        (5046, "simple-rnn-cell", 1, 'ACTION', ''),
        (5047, "gru-cell", 1, 'ACTION', ''),
        (5048, "lstm-cell", 1, 'ACTION', ''),
        (5049, "cu-dnn-gru", 0, 'ACTION', ''), #Can only be run on GPU, with the TensorFlow backend. enabled=0
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
        (5052, "subgroup", 3, 3),
        # 5041 - LSTM - Was added with the keras platform review "86dd15ad5169"
        # 5042 - Simple-RNN - Was added with the keras platform review "86dd15ad5169"
        (5043, "subgroup", 4, 4),
        (5044, "subgroup", 5, 5),
        (5045, "subgroup", 6, 6),
        (5046, "subgroup", 7, 7),
        (5047, "subgroup", 8, 8),
        (5048, "subgroup", 9, 9),
        (5049, "subgroup", 10, 10),
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
        (5040, 5052),
        (5040, 5043),
        (5040, 5044),
        (5040, 5045),
        (5040, 5046),
        (5040, 5047),
        (5040, 5048),
        (5040, 5049),
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
        (5052, "en", 'CuDNNLSTM', 'Fast LSTM implementation with CuDNN. '
                                  'Can only be run on GPU, with the TensorFlow backend.'),
        (5043, "en", 'RNN', 'Base class for recurrent layers.'),
        (5044, "en", 'GRU', 'Gated Recurrent Unit - Cho et al. 2014. There are two variants. '
                            'The default one is based on 1406.1078v3 and has reset gate '
                            'applied to hidden state before matrix multiplication. '
                            'The other one is based on original 1406.1078v1 and has the order '
                            'reversed. The second variant is compatible with CuDNNGRU '
                            '(GPU-only) and allows inference on CPU. Thus it has separate '
                            'biases for kernel and recurrent_kernel. Use \'reset_after\'=True '
                            'and recurrent_activation=\'sigmoid\'.'),
        (5045, "en", 'ConvLSTM2D', 'Convolutional LSTM. It is similar to an LSTM layer, but the input '
                                   'transformations and recurrent transformations are both convolutional.'),
        (5046, "en", 'SimpleRNNCell', 'Cell class for SimpleRNN.'),
        (5047, "en", 'GRUCell', 'Cell class for the GRU layer.'),
        (5048, "en", 'LSTMCell', 'Cell class for the LSTM layer.'),
        (5049, "en", 'CuDNNGRU', 'Fast GRU implementation backed by CuDNN. '
                                 'Can only be run on GPU, with the TensorFlow backend.'),
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
        #CuDNNLSTM
        (5140, 'INPUT', '', 1, 'ONE', 5052, 'input data'),
        (5240, 'OUTPUT', '', 1, 'ONE', 5052, 'output data'),
        #RNN
        (5143, 'INPUT', '', 1, 'ONE', 5043, 'input data'),
        (5243, 'OUTPUT', '', 1, 'ONE', 5043, 'output data'),
        #GRU
        (5144, 'INPUT', '', 1, 'ONE', 5044, 'input data'),
        (5244, 'OUTPUT', '', 1, 'ONE', 5044, 'output data'),
        #ConvLSTM2D
        (5145, 'INPUT', '', 1, 'ONE', 5045, 'input data'),
        (5245, 'OUTPUT', '', 1, 'ONE', 5045, 'output data'),
        #SimpleRNNCell
        (5146, 'INPUT', '', 1, 'ONE', 5046, 'input data'),
        (5246, 'OUTPUT', '', 1, 'ONE', 5046, 'output data'),
        #GRUCell
        (5147, 'INPUT', '', 1, 'ONE', 5047, 'input data'),
        (5247, 'OUTPUT', '', 1, 'ONE', 5047, 'output data'),
        #LSTMCell
        (5148, 'INPUT', '', 1, 'ONE', 5048, 'input data'),
        (5248, 'OUTPUT', '', 1, 'ONE', 5048, 'output data'),
        #CuDNNGRU
        (5149, 'INPUT', '', 1, 'ONE', 5049, 'input data'),
        (5249, 'OUTPUT', '', 1, 'ONE', 5049, 'output data'),

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
        #CuDNNLSTM
        (5140, 1),
        (5240, 1),
        #RNN
        (5143, 1),
        (5243, 1),
        #GRU
        (5144, 1),
        (5244, 1),
        #ConvLSTM2D
        (5145, 1),
        (5245, 1),
        #SimpleRNNCell
        (5146, 1),
        (5246, 1),
        #GRUCell
        (5147, 1),
        (5247, 1),
        #LSTMCell
        (5148, 1),
        (5248, 1),
        #CuDNNGRU
        (5149, 1),
        (5249, 1),
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
        #CuDNNLSTM
        (5140, "en", 'input data', 'Input data'),
        (5240, "en", 'output data', 'Output data'),
        #RNN
        (5143, "en", 'input data', 'Input data'),
        (5243, "en", 'output data', 'Output data'),
        #GRU
        (5144, "en", 'input data', 'Input data'),
        (5244, "en", 'output data', 'Output data'),
        #ConvLSTM2D
        (5145, "en", 'input data', 'Input data'),
        (5245, "en", 'output data', 'Output data'),
        #SimpleRNNCell
        (5146, "en", 'input data', 'Input data'),
        (5246, "en", 'output data', 'Output data'),
        #GRUCell
        (5147, "en", 'input data', 'Input data'),
        (5247, "en", 'output data', 'Output data'),
        #LSTMCell
        (5148, "en", 'input data', 'Input data'),
        (5248, "en", 'output data', 'Output data'),
        #CuDNNGRU
        (5149, "en", 'input data', 'Input data'),
        (5249, "en", 'output data', 'Output data'),

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
        #LSTM
        (5191, 1, 1, 'execution'), #units
        (5192, 1, 1, 'execution'), #activation
        (5178, 1, 1, 'execution'), #recurrent_activation
        (5193, 1, 1, 'execution'), #use_bias
        (5194, 1, 1, 'execution'), #kernel_initializer
        (5190, 1, 1, 'execution'), #recurrent_initializer
        (5195, 1, 1, 'execution'), #bias_initializer
        (5179, 1, 1, 'execution'), #unit_forget_bias
        (5196, 1, 1, 'execution'), #kernel_regularizer
        (5180, 1, 1, 'execution'), #recurrent_regularizer
        (5197, 1, 1, 'execution'), #bias_regularizer
        (5198, 1, 1, 'execution'), #activity_regularizer
        (5199, 1, 1, 'execution'), #kernel_constraint
        (5181, 1, 1, 'execution'), #recurrent_constraint
        (5200, 1, 1, 'execution'), #bias_constraint
        (5182, 1, 1, 'execution'), #dropout
        (5183, 1, 1, 'execution'), #recurrent_dropout
        (5184, 1, 1, 'execution'), #implementation
        (5185, 1, 1, 'execution'), #return_sequences
        (5186, 1, 1, 'execution'), #return_state
        (5187, 1, 1, 'execution'), #go_backwards
        (5188, 1, 1, 'execution'), #stateful
        (5189, 1, 1, 'execution'), #unroll

        #SimpleRNN
        (5201, 1, 1, 'execution'), #units
        (5202, 1, 1, 'execution'), #activation
        (5203, 1, 1, 'execution'), #use_bias
        (5204, 1, 1, 'execution'), #kernel_initializer
        (5205, 1, 1, 'execution'), #recurrent_initializer
        (5206, 1, 1, 'execution'), #bias_initializer
        (5207, 1, 1, 'execution'), #kernel_regularizer
        (5208, 1, 1, 'execution'), #recurrent_regularizer
        (5209, 1, 1, 'execution'), #bias_regularizer
        (5210, 1, 1, 'execution'), #activity_regularizer
        (5211, 1, 1, 'execution'), #kernel_constraint
        (5212, 1, 1, 'execution'), #recurrent_constraint
        (5213, 1, 1, 'execution'), #bias_constraint
        (5214, 1, 1, 'execution'), #dropout
        (5215, 1, 1, 'execution'), #recurrent_dropout
        (5216, 1, 1, 'execution'), #return_sequences
        (5217, 1, 1, 'execution'), #return_state
        (5218, 1, 1, 'execution'), #go_backwards
        (5219, 1, 1, 'execution'), #stateful
        (5220, 1, 1, 'execution'), #unroll

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
        #LSTM - EN
        (5178, 'en', 'Execution'), #recurrent_activation
        (5179, 'en', 'Execution'), #unit_forget_bias
        (5180, 'en', 'Execution'), #recurrent_regularizer
        (5181, 'en', 'Execution'), #recurrent_constraint
        (5182, 'en', 'Execution'), #dropout
        (5183, 'en', 'Execution'), #recurrent_dropout
        (5184, 'en', 'Execution'), #implementation
        (5185, 'en', 'Execution'), #return_sequences
        (5186, 'en', 'Execution'), #return_state
        (5187, 'en', 'Execution'), #go_backwards
        (5188, 'en', 'Execution'), #stateful
        (5189, 'en', 'Execution'), #unroll
        (5190, 'en', 'Execution'), #recurrent_initializer
        (5191, 'en', 'Execution'), #units
        (5192, 'en', 'Execution'), #activation
        (5193, 'en', 'Execution'), #use_bias
        (5194, 'en', 'Execution'), #kernel_initializer
        (5195, 'en', 'Execution'), #bias_initializer
        (5196, 'en', 'Execution'), #kernel_regularizer
        (5197, 'en', 'Execution'), #bias_regularizer
        (5198, 'en', 'Execution'), #activity_regularizer
        (5199, 'en', 'Execution'), #kernel_constraint
        (5200, 'en', 'Execution'), #bias_constraint
        #LSTM - PT
        (5178, 'pt', 'Execução'), #recurrent_activation
        (5179, 'pt', 'Execução'), #unit_forget_bias
        (5180, 'pt', 'Execução'), #recurrent_regularizer
        (5181, 'pt', 'Execução'), #recurrent_constraint
        (5182, 'pt', 'Execução'), #dropout
        (5183, 'pt', 'Execução'), #recurrent_dropout
        (5184, 'pt', 'Execução'), #implementation
        (5185, 'pt', 'Execução'), #return_sequences
        (5186, 'pt', 'Execução'), #return_state
        (5187, 'pt', 'Execução'), #go_backwards
        (5188, 'pt', 'Execução'), #stateful
        (5189, 'pt', 'Execução'), #unroll
        (5190, 'pt', 'Execução'), #recurrent_initializer
        (5191, 'pt', 'Execução'), #units
        (5192, 'pt', 'Execução'), #activation
        (5193, 'pt', 'Execução'), #use_bias
        (5194, 'pt', 'Execução'), #kernel_initializer
        (5195, 'pt', 'Execução'), #bias_initializer
        (5196, 'pt', 'Execução'), #kernel_regularizer
        (5197, 'pt', 'Execução'), #bias_regularizer
        (5198, 'pt', 'Execução'), #activity_regularizer
        (5199, 'pt', 'Execução'), #kernel_constraint
        (5200, 'pt', 'Execução'), #bias_constraint
        #SimpleRNN - EN
        (5201, 'en', 'Execution'), #units
        (5202, 'en', 'Execution'), #activation
        (5203, 'en', 'Execution'), #use_bias
        (5204, 'en', 'Execution'), #kernel_initializer
        (5205, 'en', 'Execution'), #recurrent_initializer
        (5206, 'en', 'Execution'), #bias_initializer
        (5207, 'en', 'Execution'), #kernel_regularizer
        (5208, 'en', 'Execution'), #recurrent_regularizer
        (5209, 'en', 'Execution'), #bias_regularizer
        (5210, 'en', 'Execution'), #activity_regularizer
        (5211, 'en', 'Execution'), #kernel_constraint
        (5212, 'en', 'Execution'), #recurrent_constraint
        (5213, 'en', 'Execution'), #bias_constraint
        (5214, 'en', 'Execution'), #dropout
        (5215, 'en', 'Execution'), #recurrent_dropout
        (5216, 'en', 'Execution'), #return_sequences
        (5217, 'en', 'Execution'), #return_state
        (5218, 'en', 'Execution'), #go_backwards
        (5219, 'en', 'Execution'), #stateful
        (5220, 'en', 'Execution'), #unroll
        #SimpleRNN - PT
        (5201, 'pt', 'Execução'), #units
        (5202, 'pt', 'Execução'), #activation
        (5203, 'pt', 'Execução'), #use_bias
        (5204, 'pt', 'Execução'), #kernel_initializer
        (5205, 'pt', 'Execução'), #recurrptt_initializer
        (5206, 'pt', 'Execução'), #bias_initializer
        (5207, 'pt', 'Execução'), #kernel_regularizer
        (5208, 'pt', 'Execução'), #recurrptt_regularizer
        (5209, 'pt', 'Execução'), #bias_regularizer
        (5210, 'pt', 'Execução'), #activity_regularizer
        (5211, 'pt', 'Execução'), #kernel_constraint
        (5212, 'pt', 'Execução'), #recurrptt_constraint
        (5213, 'pt', 'Execução'), #bias_constraint
        (5214, 'pt', 'Execução'), #dropout
        (5215, 'pt', 'Execução'), #recurrptt_dropout
        (5216, 'pt', 'Execução'), #return_sequptces
        (5217, 'pt', 'Execução'), #return_state
        (5218, 'pt', 'Execução'), #go_backwards
        (5219, 'pt', 'Execução'), #stateful
        (5220, 'pt', 'Execução'), #unroll

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
        #LSTM
        (5041, 5178),
        (5041, 5179),
        (5041, 5180),
        (5041, 5181),
        (5041, 5182),
        (5041, 5183),
        (5041, 5184),
        (5041, 5185),
        (5041, 5186),
        (5041, 5187),
        (5041, 5188),
        (5041, 5189),
        (5041, 5190),
        (5041, 5191),
        (5041, 5192),
        (5041, 5193),
        (5041, 5194),
        (5041, 5195),
        (5041, 5196),
        (5041, 5197),
        (5041, 5198),
        (5041, 5199),
        (5041, 5200),
        (5041, 41),#appearance

        #SimpleRNN
        (5042, 5201),
        (5042, 5202),
        (5042, 5203),
        (5042, 5204),
        (5042, 5205),
        (5042, 5206),
        (5042, 5207),
        (5042, 5208),
        (5042, 5209),
        (5042, 5210),
        (5042, 5211),
        (5042, 5212),
        (5042, 5213),
        (5042, 5214),
        (5042, 5215),
        (5042, 5216),
        (5042, 5217),
        (5042, 5218),
        (5042, 5219),
        (5042, 5220),
        (5042, 41), #appearance
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
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id', 'enable_conditions')
    data = [
        #LSTM
        #units
        (5191, 'units', 'INTEGER', 1, 1, None, 'integer', None, None, 'EXECUTION', 5191),
        #activation
        (5192, 'activation', 'TEXT', 0, 2, 'tanh', 'dropdown', None,
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
         'EXECUTION', 5192),
        #recurrent_activation
        (5178, 'recurrent_activation', 'TEXT', 0, 3, "hard_sigmoid", 'dropdown', None,
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
         'EXECUTION', 5178),
        #use_bias
        (5193, 'use_bias', 'INTEGER', 0, 4, None, 'checkbox', None, None, 'EXECUTION', 5193),
        #kernel_initializer
        (5194, 'kernel_initializer', 'TEXT', 0, 5, None, 'dropdown', None,
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
         'EXECUTION', 5194),
        #recurrent_initializer
        (5190, 'recurrent_initializer', 'TEXT', 0, 6, None, 'dropdown', None,
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
         'EXECUTION', 5190),
        #bias_initializer
        (5195, 'bias_initializer', 'TEXT', 0, 7, None, 'dropdown', None,
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
         'EXECUTION', 5195),
        #unit_forget_bias
        (5179, 'unit_forget_bias', 'INTEGER', 0, 8, None, 'checkbox', None, None, 'EXECUTION', 5179),
        #kernel_regularizer
        (5196, 'kernel_regularizer', 'TEXT', 0, 9, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5196),
        #recurrent_regularizer
        (5180, 'recurrent_regularizer', 'TEXT', 0, 10, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5180),
        #bias_regularizer
        (5197, 'bias_regularizer', 'TEXT', 0, 11, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5197),
        #activity_regularizer
        (5198, 'activity_regularizer', 'TEXT', 0, 12, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5198),

        #LSTM - kernel_constraint
        (5199, 'kernel_constraint', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5199),
        #recurrent_constraint
        (5181, 'recurrent_constraint', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5181),
        #bias_constraint
        (5200, 'bias_constraint', 'TEXT', 0, 15, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5200),
        #dropout
        (5182, 'dropout', 'FLOAT', 0, 16, 0.0, 'decimal', None, None, 'EXECUTION', 5182),
        #recurrent_dropout
        (5183, 'recurrent_dropout', 'FLOAT', 0, 17, 0.0, 'decimal', None, None, 'EXECUTION', 5183),
        #implementation
        (5184, 'implementation', 'INTEGER', 0, 18, 1, 'dropdown', None,
         json.dumps([
             {"key": 1, "value": 1},
             {"key": 2, "value": 2}
         ]),
         'EXECUTION', 5184),
        #return_sequences
        (5185, 'return_sequences', 'INTEGER', 0, 19, None, 'checkbox', None, None, 'EXECUTION', 5185),
        #return_state
        (5186, 'return_state', 'INTEGER', 0, 20, None, 'checkbox', None, None, 'EXECUTION', 5186),
        #go_backwards
        (5187, 'go_backwards', 'INTEGER', 0, 21, 0, 'checkbox', None, None, 'EXECUTION', 5187),
        #stateful
        (5188, 'stateful', 'INTEGER', 0, 22, 0, 'checkbox', None, None, 'EXECUTION', 5188),
        #unroll
        (5189, 'unroll', 'INTEGER', 0, 23, 0, 'checkbox', None, None, 'EXECUTION', 5189),

        #SimpleRNN
        #units
        (5201, 'units', 'INTEGER', 1, 1, None, 'integer', None, None, 'EXECUTION', 5201),
        #activation
        (5202, 'activation', 'TEXT', 0, 2, 'tanh', 'dropdown', None,
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
         'EXECUTION', 5202),
        #use_bias
        (5203, 'use_bias', 'INTEGER', 0, 4, None, 'checkbox', None, None, 'EXECUTION', 5203),
        #kernel_initializer
        (5204, 'kernel_initializer', 'TEXT', 0, 5, None, 'dropdown', None,
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
         'EXECUTION', 5204),
        #recurrent_initializer
        (5205, 'recurrent_initializer', 'TEXT', 0, 6, None, 'dropdown', None,
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
         'EXECUTION', 5205),
        #bias_initializer
        (5206, 'bias_initializer', 'TEXT', 0, 7, None, 'dropdown', None,
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
         'EXECUTION', 5206),
        #kernel_regularizer
        (5207, 'kernel_regularizer', 'TEXT', 0, 9, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5207),
        #recurrent_regularizer
        (5208, 'recurrent_regularizer', 'TEXT', 0, 10, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5208),
        #bias_regularizer
        (5209, 'bias_regularizer', 'TEXT', 0, 11, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5209),
        #activity_regularizer
        (5210, 'activity_regularizer', 'TEXT', 0, 12, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5210),
        #kernel_constraint
        (5211, 'kernel_constraint', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5211),
        #recurrent_constraint
        (5212, 'recurrent_constraint', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5212),
        #bias_constraint
        (5213, 'bias_constraint', 'TEXT', 0, 15, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5213),
        #dropout
        (5214, 'dropout', 'FLOAT', 0, 16, 0.0, 'decimal', None, None, 'EXECUTION', 5214),
        #recurrent_dropout
        (5215, 'recurrent_dropout', 'FLOAT', 0, 17, 0.0, 'decimal', None, None, 'EXECUTION', 5215),
        #return_sequences
        (5216, 'return_sequences', 'INTEGER', 0, 19, None, 'checkbox', None, None, 'EXECUTION', 5216),
        #return_state
        (5217, 'return_state', 'INTEGER', 0, 20, None, 'checkbox', None, None, 'EXECUTION', 5217),
        #go_backwards
        (5218, 'go_backwards', 'INTEGER', 0, 21, 0, 'checkbox', None, None, 'EXECUTION', 5218),
        #stateful
        (5219, 'stateful', 'INTEGER', 0, 22, 0, 'checkbox', None, None, 'EXECUTION', 5219),
        #unroll
        (5220, 'unroll', 'INTEGER', 0, 23, 0, 'checkbox', None, None, 'EXECUTION', 5220),

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
        #LSTM
        (5178, 'en', 'Recurrent activation', 'Activation function to use for the recurrent step.'),
        (5179, 'en', 'Unit forget bias', 'If True, add 1 to the bias of the forget gate at initialization. '
                                         'Use in combination with bias_initializer="zeros". '
                                         'This is recommended in Jozefowicz et al. (2015).'),
        (5180, 'en', 'Recurrent regularizer', 'Regularizer function applied to the '
                                              'recurrent_kernel weights matrix'),
        (5181, 'en', 'Recurrent constraint', 'Constraint function applied to the recurrent_kernel weights matrix.'),
        (5182, 'en', 'Dropout', 'Float between 0 and 1. Fraction of the units to drop for '
                                'the linear transformation of the inputs.'),
        (5183, 'en', 'Recurrent dropout', 'Float between 0 and 1. Fraction of the units '
                                          'to drop for the linear transformation of the recurrent state.'),
        (5184, 'en', 'Implementation mode', 'Implementation mode, either 1 or 2. Mode 1 will structure '
                                            'its operations as a larger number of smaller dot products '
                                            'and additions, whereas mode 2 will batch them into fewer, '
                                            'larger operations. These modes will have different '
                                            'performance profiles on different hardware and '
                                            'for different applications.'),
        (5185, 'en', 'Return sequences', 'Whether to return the last output in the '
                                         'output sequence, or the full sequence.'),
        (5186, 'en', 'Return state', 'Whether to return the last state in addition to the output.'),
        (5187, 'en', 'Go backwards', 'If True, process the input sequence backwards and return the reversed sequence.'),
        (5188, 'en', 'Stateful', 'If True, the last state for each sample at index i '
                                 'in a batch will be used as initial state for the '
                                 'sample of index i in the following batch.'),
        (5189, 'en', 'Unroll', 'If True, the network will be unrolled, else a symbolic loop '
                               'will be used. Unrolling can speed-up a RNN, although '
                               'it tends to be more memory-intensive. Unrolling is '
                               'only suitable for short sequences.'),
        (5190, 'en', 'Recurrent initializer', 'Initializer for the recurrent_kernel weights matrix, '
                                              'used for the linear transformation of the recurrent state.'),
        (5191, 'en', 'Output dimensions', 'Positive integer, dimensionality of the output space.'),
        (5192, 'en', 'Activation function', 'Activation function to use. If you do not specify anything, '
                                            'no activation is applied (ie. \"linear\" activation: a(x) = x).'),
        (5193, 'en', 'Use bias', 'Boolean (True|False), whether the layer uses a bias vector.'),
        (5194, 'en', 'Weight initialization function', ' Initializer for the kernel weights matrix.'),
        (5195, 'en', 'Bias initialization function', 'Initializer for the bias vector.'),
        (5196, 'en', 'Regularizer for input weight', 'Regularizer function applied to the kernel weights matrix'),
        (5197, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),
        (5198, 'en', 'Activity regularizer', 'Regularizer function applied to the output of '
                                             'the layer (its "activation").'),
        (5199, 'en', 'Weight constraint', 'Constraint function applied to the kernel weights matrix.'),
        (5200, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),

        #SimpleRNN
        (5201, 'en', 'Output dimensions', 'Positive integer, dimensionality of the output space.'),
        (5202, 'en', 'Activation function', 'Activation function to use. If you do not specify anything, '
                                            'no activation is applied (ie. \"linear\" activation: a(x) = x).'),
        (5203, 'en', 'Use bias', 'Boolean (True|False), whether the layer uses a bias vector.'),
        (5204, 'en', 'Weight initialization function', ' Initializer for the kernel weights matrix.'),
        (5205, 'en', 'Recurrent initializer', 'Initializer for the recurrent_kernel weights matrix, '
                                              'used for the linear transformation of the recurrent state.'),
        (5206, 'en', 'Bias initialization function', 'Initializer for the bias vector.'),
        (5207, 'en', 'Regularizer for input weight', 'Regularizer function applied to the kernel weights matrix'),
        (5208, 'en', 'Recurrent regularizer', 'Regularizer function applied to the '
                                              'recurrent_kernel weights matrix'),
        (5209, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),
        (5210, 'en', 'Activity regularizer', 'Regularizer function applied to the output of '
                                             'the layer (its "activation").'),
        (5211, 'en', 'Weight constraint', 'Constraint function applied to the kernel weights matrix.'),
        (5212, 'en', 'Recurrent constraint', 'Constraint function applied to the recurrent_kernel weights matrix.'),
        (5213, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),
        (5214, 'en', 'Dropout', 'Float between 0 and 1. Fraction of the units to drop for '
                                'the linear transformation of the inputs.'),
        (5215, 'en', 'Recurrent dropout', 'Float between 0 and 1. Fraction of the units '
                                          'to drop for the linear transformation of the recurrent state.'),
        (5216, 'en', 'Return sequences', 'Whether to return the last output in the '
                                         'output sequence, or the full sequence.'),
        (5217, 'en', 'Return state', 'Whether to return the last state in addition to the output.'),
        (5218, 'en', 'Go backwards', 'If True, process the input sequence backwards and return the reversed sequence.'),
        (5219, 'en', 'Stateful', 'If True, the last state for each sample at index i '
                                 'in a batch will be used as initial state for the '
                                 'sample of index i in the following batch.'),
        (5220, 'en', 'Unroll', 'If True, the network will be unrolled, else a symbolic loop '
                               'will be used. Unrolling can speed-up a RNN, although '
                               'it tends to be more memory-intensive. Unrolling is '
                               'only suitable for short sequences.'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)



all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id IN (5052, 5043, 5044, 5045, 5046, 5047, 5048, 5049)'),
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id IN (5052, 5043, 5044, 5045, 5046, 5047, 5048, 5049)'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN (5052, 5043, 5044, 5045, 5046, 5047, 5048, 5049)'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id IN (5052, 5043, 5044, 5045, 5046, 5047, 5048, 5049)'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id IN (5052, 5043, 5044, 5045, 5046, 5047, 5048, 5049) '
     'AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE operation_id IN (5052, 5043, 5044, 5045, 5046, 5047, 5048, 5049)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id IN (5140, 5143, '
     '5144, 5145, 5146, 5147, 5148, 5149, 5240, 5243, 5244, 5245, 5246, 5247, 5248, 5249)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN (5140, 5143, 5144, 5145, 5146, '
     '5147, 5148, 5149, 5240, 5243, 5244, 5245, 5246, 5247, 5248, 5249)'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5178 AND 5220'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5178 AND 5220'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5178 AND 5220'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5178 AND 5220'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id BETWEEN 5041 AND 5042'),
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

