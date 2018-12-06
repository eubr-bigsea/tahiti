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
        (5052, KERAS_PLATAFORM_ID),
        # 5041 - LSTM - Was added with the keras platform review "86dd15ad5169"
        # 5042 - Simple-RNN - Was added with the keras platform review "86dd15ad5169"
        (5043, KERAS_PLATAFORM_ID),
        (5044, KERAS_PLATAFORM_ID),
        (5045, KERAS_PLATAFORM_ID),
        (5046, KERAS_PLATAFORM_ID),
        (5047, KERAS_PLATAFORM_ID),
        (5048, KERAS_PLATAFORM_ID),
        (5049, KERAS_PLATAFORM_ID),

    ]
    rows = [dict(zip(columns, row)) for row in data]
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
        (5052, "cu-dnn-lstm", 0, 'ACTION', ''),
        # 5041 - LSTM - Was added with the keras platform review "86dd15ad5169"
        # 5042 - Simple-RNN - Was added with the keras platform review "86dd15ad5169"
        (5043, "rnn", 1, 'ACTION', ''),
        (5044, "gru", 1, 'ACTION', ''),
        (5045, "conv-lstm-2D", 1, 'ACTION', ''),
        (5046, "simple-rnn-cell", 1, 'ACTION', ''),
        (5047, "gru-cell", 1, 'ACTION', ''),
        (5048, "lstm-cell", 1, 'ACTION', ''),
        (5049, "cu-dnn-gru", 0, 'ACTION', ''),
    ]
    rows = [dict(zip(columns, row)) for row in data]

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
    rows = [dict(zip(columns, row)) for row in data]

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
    rows = [dict(zip(columns, row)) for row in data]

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
    rows = [dict(zip(columns, row)) for row in data]

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
    rows = [dict(zip(columns, row)) for row in data]

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
    rows = [dict(zip(columns, row)) for row in data]

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
    rows = [dict(zip(columns, row)) for row in data]

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

    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(operation_form_table, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
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
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
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
    ]

    rows = [dict(zip(columns, row)) for row in data]
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

        #LSTM - units
        (5191, 'units', 'INTEGER', 1, 1, None, 'integer', None, None, 'EXECUTION', 5191),

        #LSTM - activation
        (5192, 'activation', 'TEXT', 0, 2, 'linear', 'dropdown', None,
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

        #LSTM - recurrent_activation
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

        #LSTM - use_bias
        (5193, 'use_bias', 'INTEGER', 0, 4, None, 'checkbox', None, None, 'EXECUTION', 5193),

        #LSTM - kernel_initializer
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

        #LSTM - recurrent_initializer
        (5190, 'recurrent_initializer', 'TEXT', 0, 6, 0, 'dropdown', None,
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

        #LSTM - bias_initializer
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

        #LSTM - unit_forget_bias
        (5179, 'unit_forget_bias', 'INTEGER', 0, 8, None, 'checkbox', None, None, 'EXECUTION', 5179),

        #LSTM - kernel_regularizer
        (5196, 'kernel_regularizer', 'TEXT', 0, 9, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5196),

        #LSTM - recurrent_regularizer
        (5180, 'recurrent_regularizer', 'TEXT', 0, 10, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5180),

        #LSTM - bias_regularizer
        (5197, 'bias_regularizer', 'TEXT', 0, 11, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5197),

        #LSTM - activity_regularizer
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

        #LSTM - recurrent_constraint
        (5181, 'recurrent_constraint', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5181),

        #LSTM - bias_constraint
        (5200, 'bias_constraint', 'TEXT', 0, 15, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5200),

        #LSTM - dropout
        (5182, 'dropout', 'FLOAT', 0, 16, 0.0, 'decimal', None, None, 'EXECUTION', 5182),

        #LSTM - recurrent_dropout
        (5183, 'recurrent_dropout', 'FLOAT', 0, 17, 0.0, 'decimal', None, None, 'EXECUTION', 5183),

        #LSTM - implementation
        (5184, 'implementation', 'INTEGER', 0, 18, None, 'dropdown', None,
         json.dumps([
             {"key": 1, "value": 1},
             {"key": 2, "value": 2}
         ]),
         'EXECUTION', 5184),

        #LSTM - return_sequences
        (5185, 'return_sequences', 'INTEGER', 0, 19, None, 'checkbox', None, None, 'EXECUTION', 5185),

        #LSTM - return_state
        (5186, 'return_sequences', 'INTEGER', 0, 20, None, 'checkbox', None, None, 'EXECUTION', 5186),

        #LSTM - go_backwards
        (5187, 'go_backwards', 'INTEGER', 0, 21, 0, 'checkbox', None, None, 'EXECUTION', 5187),

        #LSTM - stateful
        (5188, 'stateful', 'INTEGER', 0, 22, 0, 'checkbox', None, None, 'EXECUTION', 5188),

        #LSTM - unroll
        (5189, 'unroll', 'INTEGER', 0, 23, 0, 'checkbox', None, None, 'EXECUTION', 5189),


    ]
    rows = [dict(zip(columns, row)) for row in data]
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

        # LSTM - recurrent_activation
        (5178, 'en', 'Recurrent activation', 'Activation function to use for the recurrent step.'),
        # LSTM - unit_forget_bias
        (5179, 'en', 'Unit forget bias', 'If True, add 1 to the bias of the forget gate at initialization. '
                                         'Use in combination with bias_initializer="zeros". '
                                         'This is recommended in Jozefowicz et al. (2015).'),
        # LSTM - recurrent_regularizer
        (5180, 'en', 'Recurrent regularizer', 'Regularizer function applied to the '
                                              'recurrent_kernel weights matrix'),
        # LSTM - recurrent_constraint
        (5181, 'en', 'Recurrent constraint', 'Constraint function applied to the recurrent_kernel weights matrix.'),
        # LSTM - dropout
        (5182, 'en', 'Dropout', 'Float between 0 and 1. Fraction of the units to drop for '
                                'the linear transformation of the inputs.'),
        # LSTM - recurrent_dropout
        (5183, 'en', 'Recurrent dropout', 'Float between 0 and 1. Fraction of the units '
                                          'to drop for the linear transformation of the recurrent state.'),
        # LSTM - implementation
        (5184, 'en', 'Implementation mode', 'Implementation mode, either 1 or 2. Mode 1 will structure '
                                            'its operations as a larger number of smaller dot products '
                                            'and additions, whereas mode 2 will batch them into fewer, '
                                            'larger operations. These modes will have different '
                                            'performance profiles on different hardware and '
                                            'for different applications.'),
        # LSTM - return_sequences
        (5185, 'en', 'Return sequences', 'Whether to return the last output in the '
                                         'output sequence, or the full sequence.'),
        # LSTM - return_state
        (5186, 'en', 'Return state', 'Whether to return the last state in addition to the output.'),
        # LSTM - go_backwards
        (5187, 'en', 'Go backwards', 'If True, process the input sequence backwards and return the reversed sequence.'),
        # LSTM - stateful
        (5188, 'en', 'Stateful', 'If True, the last state for each sample at index i '
                                 'in a batch will be used as initial state for the '
                                 'sample of index i in the following batch.'),
        # LSTM - unroll
        (5189, 'en', 'Unroll', 'If True, the network will be unrolled, else a symbolic loop '
                               'will be used. Unrolling can speed-up a RNN, although '
                               'it tends to be more memory-intensive. Unrolling is '
                               'only suitable for short sequences.'),

        # LSTM - recurrent_initializer
        (5190, 'en', 'Recurrent initializer', 'Initializer for the recurrent_kernel weights matrix, '
                                              'used for the linear transformation of the recurrent state.'),

        # LSTM - units
        (5191, 'en', 'Output dimensions', 'Positive integer, dimensionality of the output space.'),

        # LSTM - activation
        (5192, 'en', 'Activation function', 'Activation function to use. If you do not specify anything, '
                                            'no activation is applied (ie. \"linear\" activation: a(x) = x).'),

        # LSTM - use_bias
        (5193, 'en', 'Use bias', 'Boolean (True|False), whether the layer uses a bias vector.'),

        # LSTM - kernel_initializer
        (5194, 'en', 'Weight initialization function', ' Initializer for the kernel weights matrix.'),

        # LSTM - bias_initializer
        (5195, 'en', 'Bias initialization function', 'Initializer for the bias vector.'),

        # LSTM - kernel_regularizer
        (5196, 'en', 'Regularizer for input weight', 'Regularizer function applied to the kernel weights matrix'),

        # LSTM - bias_regularizer
        (5197, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),

        # LSTM - activity_regularizer
        (5198, 'en', 'Activity regularizer', 'Regularizer function applied to the output of '
                                             'the layer (its "activation").'),

        # LSTM - kernel_constraint
        (5199, 'en', 'Weight constraint', 'Constraint function applied to the kernel weights matrix.'),

        # LSTM - bias_constraint
        (5200, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),

    ]
    rows = [dict(zip(columns, row)) for row in data]
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
     'DELETE FROM operation_form WHERE id BETWEEN 5178 AND 5200'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5178 AND 5200'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5178 AND 5200'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5178 AND 5200'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 5041'),
]

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], (unicode, str)):
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
            if isinstance(cmd[1], (unicode, str)):
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

