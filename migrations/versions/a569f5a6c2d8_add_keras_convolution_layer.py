# -*- coding: utf-8 -*-
"""Add keras convolution layer

Revision ID: a569f5a6c2d8
Revises: 55605557d9cc
Create Date: 2019-04-30 15:24:38.678319

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
revision = 'a569f5a6c2d8'
down_revision = '55605557d9cc'
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
        (5073, KERAS_PLATAFORM_ID),
        (5074, KERAS_PLATAFORM_ID),
        (5075, KERAS_PLATAFORM_ID),
        (5076, KERAS_PLATAFORM_ID),
        (5077, KERAS_PLATAFORM_ID),
        (5078, KERAS_PLATAFORM_ID),
        (5079, KERAS_PLATAFORM_ID),
        (5080, KERAS_PLATAFORM_ID),
        (5081, KERAS_PLATAFORM_ID),
        (5082, KERAS_PLATAFORM_ID),
        (5083, KERAS_PLATAFORM_ID),
        (5084, KERAS_PLATAFORM_ID),
        (5085, KERAS_PLATAFORM_ID),
        (5086, KERAS_PLATAFORM_ID),
        (5087, KERAS_PLATAFORM_ID),
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
        column('icon', Integer), )

    columns = ('id', 'slug', 'enabled', 'type', 'icon')
    data = [
        (5073, "convolution-1d", 1, 'ACTION', ''),
        (5074, "separable-conv-1d", 1, 'ACTION', ''),
        (5075, "separable-conv-2d", 1, 'ACTION', ''),
        (5076, "depth-wise-conv-2d", 1, 'ACTION', ''),
        (5077, "conv-2d-tranpose", 1, 'ACTION', ''),
        (5078, "conv-3d", 1, 'ACTION', ''),
        (5079, "conv-3d-tranpose", 1, 'ACTION', ''),
        (5080, "cropping-1d", 1, 'ACTION', ''),
        (5081, "cropping-2d", 1, 'ACTION', ''),
        (5082, "cropping-3d", 1, 'ACTION', ''),
        (5083, "up-sampling-1d", 1, 'ACTION', ''),
        (5084, "up-sampling-2d", 1, 'ACTION', ''),
        (5085, "up-sampling-3d", 1, 'ACTION', ''),
        (5086, "zero-padding-1d", 1, 'ACTION', ''),
        (5087, "zero-padding-3d", 1, 'ACTION', ''),

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
        # Convolutional Layers
        (5020, 5073),
        (5020, 5074),
        (5020, 5075),
        (5020, 5076),
        (5020, 5077),
        (5020, 5078),
        (5020, 5079),
        (5020, 5080),
        (5020, 5081),
        (5020, 5082),
        (5020, 5083),
        (5020, 5084),
        (5020, 5085),
        (5020, 5086),
        (5020, 5087),
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
        (5073, 'en', 'Convolution1D', '1D convolution layer (e.g. temporal '
                                      'convolution). This layer creates a '
                                      'convolution kernel that is convolved '
                                      'with the layer input over a single '
                                      'spatial (or temporal) dimension to '
                                      'produce a tensor of outputs. If use_bias'
                                      ' is True, a bias vector is created and '
                                      'added to the outputs. Finally, if '
                                      'activation is not None, it is applied '
                                      'to the outputs as well. When using this '
                                      'layer as the first layer in a model, '
                                      'provide an input_shape argument (tuple '
                                      'of integers or None, does not include '
                                      'the batch axis), e.g. input_shape=(10, '
                                      '128) for time series sequences of 10 '
                                      'time steps with 128 features per step '
                                      'in data_format="channels_last", or '
                                      '(None, 128) for variable-length '
                                      'sequences with 128 features per step.'),
        (5074, 'en', 'SeparableConv1D', 'Depthwise separable 1D convolution. '
                                        'Separable convolutions consist in '
                                        'first performing a depthwise spatial '
                                        'convolution (which acts on each input '
                                        'channel separately) followed by a '
                                        'pointwise convolution which mixes '
                                        'together the resulting output '
                                        'channels. The depth_multiplier '
                                        'argument controls how many output '
                                        'channels are generated per input '
                                        'channel in the depthwise step. '
                                        'Intuitively, separable convolutions '
                                        'can be understood as a way to '
                                        'factorize a convolution kernel into '
                                        'two smaller kernels, or as an extreme '
                                        'version of an Inception block. '),
        (5075, 'en', 'SeparableConv2D', 'Depthwise separable 2D convolution. '
                                        'Separable convolutions consist in '
                                        'first performing a depthwise spatial '
                                        'convolution (which acts on each input '
                                        'channel separately) followed by a '
                                        'pointwise convolution which mixes '
                                        'together the resulting output channels.'
                                        ' The depth_multiplier argument '
                                        'controls how many output channels are '
                                        'generated per input channel in the '
                                        'depthwise step. Intuitively, separable'
                                        ' convolutions can be understood as a '
                                        'way to factorize a convolution kernel '
                                        'into two smaller kernels, or as an '
                                        'extreme version of an Inception block'
                                        '.'),
        (5076, 'en', 'DepthwiseConv2D', 'Depthwise separable 2D convolution. '
                                        'Depthwise Separable convolutions '
                                        'consists in performing just the first '
                                        'step in a depthwise spatial '
                                        'convolution (which acts on each input '
                                        'channel separately). The '
                                        'depth_multiplier argument controls how'
                                        ' many output channels are generated '
                                        'per input channel in the depthwise '
                                        'step.'),
        (5077, 'en', 'Conv2DTranpose', 'Transposed convolution layer (sometimes'
                                       ' called Deconvolution). The need for '
                                       'transposed convolutions generally '
                                       'arises from the desire to use a '
                                       'transformation going in the opposite '
                                       'direction of a normal convolution, '
                                       'i.e., from something that has the '
                                       'shape of the output of some convolution'
                                       ' to something that has the shape of its'
                                       ' input while maintaining a connectivity'
                                       ' pattern that is compatible with said '
                                       'convolution. When using this layer as '
                                       'the first layer in a model, provide the'
                                       ' keyword argument input_shape (tuple of'
                                       ' integers, does not include the batch '
                                       'axis), e.g. input_shape=(128, 128, 3) '
                                       'for 128x128 RGB pictures in data_format'
                                       '="channels_last".'),
        (5078, 'en', 'Conv3D', '3D convolution layer (e.g. spatial convolution '
                               'over volumes). This layer creates a convolution'
                               ' kernel that is convolved with the layer input'
                               ' to produce a tensor of outputs. If use_bias '
                               'is True, a bias vector is created and added to'
                               ' the outputs. Finally, if activation is not '
                               'None, it is applied to the outputs as well. '
                               'When using this layer as the first layer in a '
                               'model, provide the keyword argument '
                               'input_shape (tuple of integers, does not '
                               'include the batch axis), e.g. input_shape=(128,'
                               ' 128, 128, 1) for 128x128x128 volumes with a '
                               'single channel, in data_format='
                               '"channels_last".'),
        (5079, 'en', 'Conv3DTranpose', 'Transposed convolution layer '
                                       '(sometimes called Deconvolution). '
                                       'The need for transposed convolutions '
                                       'generally arises from the desire to '
                                       'use a transformation going in the '
                                       'opposite direction of a normal '
                                       'convolution, i.e., from something '
                                       'that has the shape of the output of '
                                       'some convolution to something that has '
                                       'the shape of its input while '
                                       'maintaining a connectivity pattern '
                                       'that is compatible with said '
                                       'convolution. When using this layer as '
                                       'the first layer in a model, provide '
                                       'the keyword argument input_shape '
                                       '(tuple of integers, does not include '
                                       'the batch axis), e.g. input_shape='
                                       '(128, 128, 128, 3) for a 128x128x128 '
                                       'volume with 3 channels if data_format'
                                       '="channels_last".'),
        (5080, 'en', 'Cropping1D', 'Cropping layer for 1D input (e.g. temporal '
                                   'sequence). It crops along the time '
                                   'dimension (axis 1). '),
        (5081, 'en', 'Cropping2D', 'Cropping layer for 2D input (e.g. picture).'
                                   ' It crops along spatial dimensions, i.e.'
                                   ' height and width.'),
        (5082, 'en', 'Cropping3D', 'Cropping layer for 3D data (e.g. spatial '
                                   'or spatio-temporal).'),
        (5083, 'en', 'UpSampling1D', 'Upsampling layer for 1D inputs. Repeats '
                                     'each temporal step size times along the '
                                     'time axis.'),
        (5084, 'en', 'UpSampling2D', 'Upsampling layer for 2D inputs. Repeats '
                                     'the rows and columns of the data by '
                                     'size[0] and size[1] respectively. '),
        (5085, 'en', 'UpSampling3D', 'Upsampling layer for 3D inputs. Repeats '
                                     'the 1st, 2nd and 3rd dimensions of the '
                                     'data by size[0], size[1] and size[2] '
                                     'respectively.'),
        (5086, 'en', 'ZeroPadding1D', 'Zero-padding layer for 1D input '
                                      '(e.g. temporal sequence).'),
        (5087, 'en', 'ZeroPadding3D', 'Zero-padding layer for 3D data '
                                      '(spatial or spatio-temporal).'),
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
        column('slug', String), )

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        # SpatialDropout1D
        (5173, 'INPUT', '', 1, 'ONE', 5073, 'input data'),
        (5174, 'INPUT', '', 1, 'ONE', 5074, 'input data'),
        (5175, 'INPUT', '', 1, 'ONE', 5075, 'input data'),
        (5176, 'INPUT', '', 1, 'ONE', 5076, 'input data'),
        (5177, 'INPUT', '', 1, 'ONE', 5077, 'input data'),
        (5178, 'INPUT', '', 1, 'ONE', 5078, 'input data'),
        (5179, 'INPUT', '', 1, 'ONE', 5079, 'input data'),
        (5180, 'INPUT', '', 1, 'ONE', 5080, 'input data'),
        (5181, 'INPUT', '', 1, 'ONE', 5081, 'input data'),
        (5182, 'INPUT', '', 1, 'ONE', 5082, 'input data'),
        (5183, 'INPUT', '', 1, 'ONE', 5083, 'input data'),
        (5184, 'INPUT', '', 1, 'ONE', 5084, 'input data'),
        (5185, 'INPUT', '', 1, 'ONE', 5085, 'input data'),
        (5186, 'INPUT', '', 1, 'ONE', 5086, 'input data'),
        (5187, 'INPUT', '', 1, 'ONE', 5087, 'input data'),
        (5273, 'OUTPUT', '', 1, 'ONE', 5073, 'output data'),
        (5274, 'OUTPUT', '', 1, 'ONE', 5074, 'output data'),
        (5275, 'OUTPUT', '', 1, 'ONE', 5075, 'output data'),
        (5276, 'OUTPUT', '', 1, 'ONE', 5076, 'output data'),
        (5277, 'OUTPUT', '', 1, 'ONE', 5077, 'output data'),
        (5278, 'OUTPUT', '', 1, 'ONE', 5078, 'output data'),
        (5279, 'OUTPUT', '', 1, 'ONE', 5079, 'output data'),
        (5280, 'OUTPUT', '', 1, 'ONE', 5080, 'output data'),
        (5281, 'OUTPUT', '', 1, 'ONE', 5081, 'output data'),
        (5282, 'OUTPUT', '', 1, 'ONE', 5082, 'output data'),
        (5283, 'OUTPUT', '', 1, 'ONE', 5083, 'output data'),
        (5284, 'OUTPUT', '', 1, 'ONE', 5084, 'output data'),
        (5285, 'OUTPUT', '', 1, 'ONE', 5085, 'output data'),
        (5286, 'OUTPUT', '', 1, 'ONE', 5086, 'output data'),
        (5287, 'OUTPUT', '', 1, 'ONE', 5087, 'output data'),
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
        (5173, 1),
        (5174, 1),
        (5175, 1),
        (5176, 1),
        (5177, 1),
        (5178, 1),
        (5179, 1),
        (5180, 1),
        (5181, 1),
        (5182, 1),
        (5183, 1),
        (5184, 1),
        (5185, 1),
        (5186, 1),
        (5187, 1),
        (5273, 1),
        (5274, 1),
        (5275, 1),
        (5276, 1),
        (5277, 1),
        (5278, 1),
        (5279, 1),
        (5280, 1),
        (5281, 1),
        (5282, 1),
        (5283, 1),
        (5284, 1),
        (5285, 1),
        (5286, 1),
        (5287, 1),
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
        # SpatialDropout1D
        (5173, 'en', 'input data', 'Input data'),
        (5174, 'en', 'input data', 'Input data'),
        (5175, 'en', 'input data', 'Input data'),
        (5176, 'en', 'input data', 'Input data'),
        (5177, 'en', 'input data', 'Input data'),
        (5178, 'en', 'input data', 'Input data'),
        (5179, 'en', 'input data', 'Input data'),
        (5180, 'en', 'input data', 'Input data'),
        (5181, 'en', 'input data', 'Input data'),
        (5182, 'en', 'input data', 'Input data'),
        (5183, 'en', 'input data', 'Input data'),
        (5184, 'en', 'input data', 'Input data'),
        (5185, 'en', 'input data', 'Input data'),
        (5186, 'en', 'input data', 'Input data'),
        (5187, 'en', 'input data', 'Input data'),
        (5273, 'en', 'output data', 'Output data'),
        (5274, 'en', 'output data', 'Output data'),
        (5275, 'en', 'output data', 'Output data'),
        (5276, 'en', 'output data', 'Output data'),
        (5277, 'en', 'output data', 'Output data'),
        (5278, 'en', 'output data', 'Output data'),
        (5279, 'en', 'output data', 'Output data'),
        (5280, 'en', 'output data', 'Output data'),
        (5281, 'en', 'output data', 'Output data'),
        (5282, 'en', 'output data', 'Output data'),
        (5283, 'en', 'output data', 'Output data'),
        (5284, 'en', 'output data', 'Output data'),
        (5285, 'en', 'output data', 'Output data'),
        (5286, 'en', 'output data', 'Output data'),
        (5287, 'en', 'output data', 'Output data'),
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
        (5143, 1, 1, 'execution'),
        (5144, 1, 1, 'execution'),
        (5145, 1, 1, 'execution'),
        (5146, 1, 1, 'execution'),
        (5147, 1, 1, 'execution'),
        (5148, 1, 1, 'execution'),
        (5149, 1, 1, 'execution'),
        (5150, 1, 1, 'execution'),
        (5151, 1, 1, 'execution'),
        (5152, 1, 1, 'execution'),
        (5153, 1, 1, 'execution'),
        (5154, 1, 1, 'execution'),
        (5155, 1, 1, 'execution'),
        (5156, 1, 1, 'execution'),
        (5157, 1, 1, 'execution'),
        (5158, 1, 1, 'execution'),
        (5159, 1, 1, 'execution'),
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
        (5143, 'en', 'Execution'),
        (5144, 'en', 'Execution'),
        (5145, 'en', 'Execution'),
        (5146, 'en', 'Execution'),
        (5147, 'en', 'Execution'),
        (5148, 'en', 'Execution'),
        (5149, 'en', 'Execution'),
        (5150, 'en', 'Execution'),
        (5151, 'en', 'Execution'),
        (5152, 'en', 'Execution'),
        (5153, 'en', 'Execution'),
        (5154, 'en', 'Execution'),
        (5155, 'en', 'Execution'),
        (5156, 'en', 'Execution'),
        (5157, 'en', 'Execution'),
        (5158, 'en', 'Execution'),
        (5159, 'en', 'Execution'),
        (5143, 'pt', 'Execução'),
        (5144, 'pt', 'Execução'),
        (5145, 'pt', 'Execução'),
        (5146, 'pt', 'Execução'),
        (5147, 'pt', 'Execução'),
        (5148, 'pt', 'Execução'),
        (5149, 'pt', 'Execução'),
        (5150, 'pt', 'Execução'),
        (5151, 'pt', 'Execução'),
        (5152, 'pt', 'Execução'),
        (5153, 'pt', 'Execução'),
        (5154, 'pt', 'Execução'),
        (5155, 'pt', 'Execução'),
        (5156, 'pt', 'Execução'),
        (5157, 'pt', 'Execução'),
        (5158, 'pt', 'Execução'),
        (5159, 'pt', 'Execução'),
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
        (5021, 41),
        (5022, 41),
        (5073, 41),
        (5074, 41),
        (5075, 41),
        (5076, 41),
        (5077, 41),
        (5078, 41),
        (5079, 41),
        (5080, 41),
        (5081, 41),
        (5082, 41),
        (5083, 41),
        (5084, 41),
        (5085, 41),
        (5086, 41),
        (5087, 41),
        (5021, 5143),
        (5022, 5144),
        (5073, 5145),
        (5074, 5146),
        (5075, 5147),
        (5076, 5148),
        (5077, 5149),
        (5078, 5150),
        (5079, 5151),
        (5080, 5152),
        (5081, 5153),
        (5082, 5154),
        (5083, 5155),
        (5084, 5156),
        (5085, 5157),
        (5086, 5158),
        (5087, 5159),
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
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')

    data = [
        # Conv1D
        (5221, 'filters', 'INTEGER', 1, 1, 0, 'integer', None, None, 'EXECUTION', 5145),
        (5222, 'kernel_size', 'TEXT', 1, 2, 0, 'text', None, None, 'EXECUTION', 5145),
        (5223, 'strides', 'TEXT', 1, 3, 0, 'text', None, None, 'EXECUTION', 5145),
        (5224, 'padding', 'TEXT', 0, 4, 'valid', 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'causal', 'value': 'causal'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5145),
        (5225, 'data_format', 'TEXT', 0, 5, 'channels_last', 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5145),
        (5226, 'dilation_rate', 'TEXT', 0, 6, 1, 'text', None, None, 'EXECUTION', 5145),
        (5227, 'activation', 'TEXT', 1, 7, 'linear', 'dropdown', None,
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
         'EXECUTION', 5145),
        (5228, 'use_bias', 'INTEGER', 0, 8, None, 'checkbox', None, None, 'EXECUTION', 5145),
        (5229, 'kernel_initializer', 'TEXT', 0, 9, None, 'dropdown', None,
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
         'EXECUTION', 5145),
        (5230, 'bias_initializer', 'TEXT', 0, 10, None, 'dropdown', None,
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
         'EXECUTION', 5145),
        (5231, 'kernel_regularizer', 'TEXT', 0, 11, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5145),
        (5232, 'bias_regularizer', 'TEXT', 0, 12, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5145),
        (5233, 'activity_regularizer', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5145),
        (5234, 'kernel_constraint', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5145),
        (5235, 'bias_constraint', 'TEXT', 0, 15, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5145),

        # Conv2D
        (5236, 'filters', 'INTEGER', 1, 1, 0, 'integer', None, None, 'EXECUTION', 5143),
        (5237, 'kernel_size', 'TEXT', 1, 2, 0, 'text', None, None, 'EXECUTION', 5143),
        (5238, 'strides', 'TEXT', 1, 3, "(1, 1)", 'text', None, None, 'EXECUTION', 5143),
        (5239, 'padding', 'TEXT', 0, 4, 'valid', 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'causal', 'value': 'causal'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5143),
        (5240, 'data_format', 'TEXT', 0, 5, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5143),
        (5241, 'dilation_rate', 'TEXT', 0, 6, "(1, 1)", 'text', None, None, 'EXECUTION', 5143),
        (5242, 'activation', 'TEXT', 1, 7, None, 'dropdown', None,
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
         'EXECUTION', 5143),
        (5243, 'use_bias', 'INTEGER', 0, 8, 1, 'checkbox', None, None, 'EXECUTION', 5143),
        (5244, 'kernel_initializer', 'TEXT', 0, 9, "glorot_uniform", 'dropdown', None,
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
         'EXECUTION', 5143),
        (5245, 'bias_initializer', 'TEXT', 0, 10, "zeros", 'dropdown', None,
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
         'EXECUTION', 5143),
        (5246, 'kernel_regularizer', 'TEXT', 0, 11, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5143),
        (5247, 'bias_regularizer', 'TEXT', 0, 12, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5143),
        (5248, 'activity_regularizer', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5143),
        (5249, 'kernel_constraint', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5143),
        (5250, 'bias_constraint', 'TEXT', 0, 15, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5143),

        # ZeroPadding2D
        (5251, 'padding', 'TEXT', 0, 1, "(1, 1)", 'dropdown', None, None, 'EXECUTION', 5144),
        (5252, 'data_format', 'TEXT', 0, 2, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5144),

        # SeparableConv1D
        (5253, 'filters', 'INTEGER', 0, 1, 0, 'integer', None, None, 'EXECUTION', 5146),
        (5254, 'kernel_size', 'TEXT', 0, 2, 0, 'text', None, None, 'EXECUTION', 5146),
        (5255, 'strides', 'TEXT', 0, 3, "1", 'text', None, None, 'EXECUTION', 5146),
        (5256, 'padding', 'TEXT', 0, 4, 'valid', 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5146),
        (5257, 'data_format', 'TEXT', 0, 5, 'channels_last', 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5146),
        (5258, 'dilation_rate', 'TEXT', 0, 6, "1", 'text', None, None, 'EXECUTION', 5146),
        (5259, 'depth_multiplier', 'INTEGER', 0, 7, 1, 'integer', None, None, 'EXECUTION', 5146),
        (5260, 'activation', 'TEXT', 1, 8, None, 'dropdown', None,
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
         'EXECUTION', 5146),
        (5261, 'use_bias', 'INTEGER', 0, 9, 1, 'checkbox', None, None, 'EXECUTION', 5146),
        (5262, 'depthwise_initializer', 'TEXT', 0, 10, "glorot_uniform", 'dropdown', None,
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
         'EXECUTION', 5146),
        (5263, 'pointwise_initializer', 'TEXT', 0, 11, "glorot_uniform", 'dropdown', None,
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
         ), 'EXECUTION', 5146),
        (5264, 'bias_initializer', 'TEXT', 0, 12, "zeros", 'dropdown', None,
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
          ), 'EXECUTION', 5146),
        (5265, 'depthwise_regularizer', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5146),
        (5266, 'pointhwise_regularizer', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5146),
        (5267, 'bias_regularizer', 'TEXT', 0, 15, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5146),
        (5268, 'activity_regularizer', 'TEXT', 0, 16, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5146),
        (5269, 'depthwise_constraint', 'TEXT', 0, 17, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5146),
        (5270, 'pointwise_constraint', 'TEXT', 0, 18, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5146),
        (5271, 'bias_constraint', 'TEXT', 0, 19, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5146),

        # SeparableConv2D
        (5272, 'filters', 'INTEGER', 1, 1, 0, 'integer', None, None, 'EXECUTION', 5147),
        (5273, 'kernel_size', 'TEXT', 1, 2, 0, 'text', None, None, 'EXECUTION', 5147),
        (5274, 'strides', 'TEXT', 1, 3, "(1, 1)", 'text', None, None, 'EXECUTION', 5147),
        (5275, 'padding', 'TEXT', 0, 4, 'valid', 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5147),
        (5276, 'data_format', 'TEXT', 0, 5, 'channels_last', 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5147),
        (5277, 'dilation_rate', 'TEXT', 0, 6, "1", 'text', None, None, 'EXECUTION', 5147),
        (5278, 'depth_multiplier', 'INTEGER', 0, 7, 1, 'integer', None, None, 'EXECUTION', 5147),
        (5279, 'activation', 'TEXT', 1, 8, None, 'dropdown', None,
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
         'EXECUTION', 5147),
        (5280, 'use_bias', 'INTEGER', 0, 9, 1, 'checkbox', None, None, 'EXECUTION', 5147),
        (5281, 'depthwise_initializer', 'TEXT', 0, 10, "glorot_uniform", 'dropdown', None,
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
         'EXECUTION', 5147),
        (5282, 'pointwise_initializer', 'TEXT', 0, 11, "glorot_uniform", 'dropdown', None,
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
         ), 'EXECUTION', 5147),
        (5283, 'bias_initializer', 'TEXT', 0, 12, "zeros", 'dropdown', None,
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
         ), 'EXECUTION', 5147),
        (5284, 'depthwise_regularizer', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5147),
        (5285, 'pointhwise_regularizer', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5147),
        (5286, 'bias_regularizer', 'TEXT', 0, 15, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5147),
        (5287, 'activity_regularizer', 'TEXT', 0, 16, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5147),
        (5288, 'depthwise_constraint', 'TEXT', 0, 17, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5147),
        (5289, 'pointwise_constraint', 'TEXT', 0, 18, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5147),
        (5290, 'bias_constraint', 'TEXT', 0, 19, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5147),

        # DepthwiseConv2D
        (5291, 'kernel_size', 'TEXT', 1, 1, 0, 'text', None, None, 'EXECUTION', 5148),
        (5292, 'strides', 'TEXT', 1, 2, "(1, 1)", 'text', None, None, 'EXECUTION', 5148),
        (5293, 'padding', 'TEXT', 0, 3, 'valid', 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5148),
        (5294, 'depth_multiplier', 'INTEGER', 0, 4, 1, 'integer', None, None, 'EXECUTION', 5148),
        (5295, 'data_format', 'TEXT', 0, 5, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5148),
        (5296, 'activation', 'TEXT', 1, 6, None, 'dropdown', None,
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
         'EXECUTION', 5148),
        (5297, 'use_bias', 'INTEGER', 0, 7, 1, 'checkbox', None, None, 'EXECUTION', 5148),
        (5298, 'depthwise_initializer', 'TEXT', 0, 8, "glorot_uniform", 'dropdown', None,
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
         'EXECUTION', 5148),
        (5299, 'bias_initializer', 'TEXT', 0, 9, "zeros", 'dropdown', None,
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
         ), 'EXECUTION', 5148),
        (5300, 'depthwise_regularizer', 'TEXT', 0, 10, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5148),
        (5301, 'bias_regularizer', 'TEXT', 0, 11, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5148),
        (5302, 'activity_regularizer', 'TEXT', 0, 12, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5148),
        (5303, 'depthwise_constraint', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5148),
        (5304, 'bias_constraint', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5148),

        # Conv2DTranspose
        (5305, 'filters', 'INTEGER', 1, 1, 0, 'integer', None, None, 'EXECUTION', 5149),
        (5306, 'kernel_size', 'TEXT', 1, 2, 0, 'text', None, None, 'EXECUTION', 5149),
        (5307, 'strides', 'TEXT', 1, 3, "(1, 1)", 'text', None, None, 'EXECUTION', 5149),
        (5308, 'padding', 'TEXT', 0, 4, 'valid', 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5149),
        (5309, 'output_padding', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5149),
        (5310, 'data_format', 'TEXT', 0, 6, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5149),
        (5311, 'dilation_rate', 'TEXT', 0, 7, "(1, 1)", 'text', None, None, 'EXECUTION', 5149),
        (5312, 'activation', 'TEXT', 1, 8, None, 'dropdown', None,
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
         'EXECUTION', 5149),
        (5313, 'use_bias', 'INTEGER', 0, 9, 1, 'checkbox', None, None, 'EXECUTION', 5149),
        (5314, 'kernel_initializer', 'TEXT', 0, 10, "glorot_uniform", 'dropdown', None,
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
         'EXECUTION', 5149),
        (5315, 'bias_initializer', 'TEXT', 0, 11, "zeros", 'dropdown', None,
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
         ), 'EXECUTION', 5149),
        (5316, 'kernel_regularizer', 'TEXT', 0, 12, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5149),
        (5317, 'bias_regularizer', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5149),
        (5318, 'activity_regularizer', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5149),
        (5319, 'kernel_constraint', 'TEXT', 0, 15, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5149),
        (5320, 'bias_constraint', 'TEXT', 0, 16, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5149),

        # Conv3D
        (5321, 'filters', 'INTEGER', 1, 1, 0, 'integer', None, None, 'EXECUTION', 5150),
        (5322, 'kernel_size', 'TEXT', 1, 2, 0, 'text', None, None, 'EXECUTION', 5150),
        (5323, 'strides', 'TEXT', 1, 3, "(1, 1)", 'text', None, None, 'EXECUTION', 5150),
        (5324, 'padding', 'TEXT', 0, 4, 'valid', 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5150),
        (5325, 'data_format', 'TEXT', 0, 5, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5150),
        (5326, 'dilation_rate', 'TEXT', 0, 6, "(1, 1)", 'text', None, None, 'EXECUTION', 5150),
        (5327, 'activation', 'TEXT', 1, 7, None, 'dropdown', None,
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
         'EXECUTION', 5150),
        (5328, 'use_bias', 'INTEGER', 0, 8, 1, 'checkbox', None, None, 'EXECUTION', 5150),
        (5329, 'kernel_initializer', 'TEXT', 0, 9, "glorot_uniform", 'dropdown', None,
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
         'EXECUTION', 5150),
        (5330, 'bias_initializer', 'TEXT', 0, 10, "zeros", 'dropdown', None,
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
         ), 'EXECUTION', 5150),
        (5331, 'kernel_regularizer', 'TEXT', 0, 11, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5150),
        (5332, 'bias_regularizer', 'TEXT', 0, 12, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5150),
        (5333, 'activity_regularizer', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5150),
        (5334, 'kernel_constraint', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5150),
        (5335, 'bias_constraint', 'TEXT', 0, 15, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5150),

        # Conv3DTranspose
        (5336, 'filters', 'INTEGER', 1, 1, 0, 'integer', None, None, 'EXECUTION', 5151),
        (5337, 'kernel_size', 'TEXT', 1, 2, 0, 'text', None, None, 'EXECUTION', 5151),
        (5338, 'strides', 'TEXT', 1, 3, "(1, 1, 1)", 'text', None, None, 'EXECUTION', 5151),
        (5339, 'padding', 'TEXT', 0, 4, 'valid', 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5151),
        (5340, 'output_padding', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5151),
        (5341, 'data_format', 'TEXT', 0, 6, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5151),
        (5342, 'dilation_rate', 'TEXT', 0, 7, "(1, 1, 1)", 'text', None, None, 'EXECUTION', 5151),
        (5343, 'activation', 'TEXT', 1, 8, None, 'dropdown', None,
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
         'EXECUTION', 5151),
        (5344, 'use_bias', 'INTEGER', 0, 9, 1, 'checkbox', None, None, 'EXECUTION', 5151),
        (5345, 'kernel_initializer', 'TEXT', 0, 10, "glorot_uniform", 'dropdown', None,
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
         'EXECUTION', 5151),
        (5346, 'bias_initializer', 'TEXT', 0, 11, "zeros", 'dropdown', None,
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
         ), 'EXECUTION', 5151),
        (5347, 'kernel_regularizer', 'TEXT', 0, 12, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5151),
        (5348, 'bias_regularizer', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5151),
        (5349, 'activity_regularizer', 'TEXT', 0, 14, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ),
         'EXECUTION', 5151),
        (5350, 'kernel_constraint', 'TEXT', 0, 15, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5151),
        (5351, 'bias_constraint', 'TEXT', 0, 16, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]),
         'EXECUTION', 5151),

        # Cropping1D
        (5352, 'cropping', 'TEXT', 1, 1, "(1, 1)", 'text', None, None, 'EXECUTION', 5152),

        # Cropping2D
        (5353, 'cropping', 'TEXT', 1, 1, "((0, 0), (0, 0))", 'text', None, None, 'EXECUTION', 5153),
        (5354, 'data_format', 'TEXT', 0, 2, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5153),

        # Cropping3D
        (5355, 'cropping', 'TEXT', 1, 1, "((0, 0), (0, 0), (0, 0))", 'text', None, None, 'EXECUTION', 5154),
        (5356, 'data_format', 'TEXT', 0, 2, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5154),

        # UpSampling1D
        (5357, 'size', 'INTEGER', 1, 1, 2, 'integer', None, None, 'EXECUTION', 5155),

        # UpSampling2D
        (5358, 'size', 'TEXT', 1, 1, "(2, 2)", 'text', None, None, 'EXECUTION', 5156),
        (5359, 'data_format', 'TEXT', 0, 2, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5156),
        (5360, 'interpolation', 'TEXT', 1, 3, 'nearest', 'dropdown', None,
         json.dumps([
             {'key': 'nearest', 'value': 'nearest'},
             {'key': 'bilinear', 'value': 'bilinear'},
         ]), 'EXECUTION', 5156),

        # UpSampling3D
        (5361, 'size', 'TEXT', 1, 1, "(2, 2, 2)", 'text', None, None, 'EXECUTION', 5157),
        (5362, 'data_format', 'TEXT', 0, 2, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5157),

        # ZeroPadding1D
        (5363, 'padding', 'TEXT', 1, 1, "1", 'text', None, None, 'EXECUTION', 5158),

        # ZeroPadding3D
        (5364, 'padding', 'TEXT', 1, 1, "(1, 1, 1)", 'text', None, None, 'EXECUTION', 5159),
        (5365, 'data_format', 'TEXT', 0, 2, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5159),

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

        # Conv1D
        (5221, 'en', 'Filters', 'Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).'),
        (5222, 'en', 'Kernel size', 'An integer or tuple/list of a single integer, specifying the length of the 1D convolution window.'),
        (5223, 'en', 'Strides', 'An integer or tuple/list of a single integer, specifying the stride length of the convolution. Specifying any stride value != 1 is incompatible with specifying any dilation_rate value != 1.'),
        (5224, 'en', 'Padding', 'One of "valid", "causal" or "same" (case-insensitive). "valid" means "no padding".  "same" results in padding the input such that the output has the same length as the original input.  "causal" results in causal (dilated) convolutions, e.g. output[t] does not depend on input[t + 1:]. A zero padding is used such that the output has the same length as the original input. Useful when modeling temporal data where the model should not violate the temporal order.'),
        (5225, 'en', 'Data format', 'A string, one of "channels_last" (default) or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, steps, channels) (default format for temporal data in Keras) while "channels_first" corresponds to inputs with shape (batch, channels, steps).'),
        (5226, 'en', 'Dilation rate', 'An integer or tuple/list of a single integer, specifying the dilation rate to use for dilated convolution. Currently, specifying any dilation_rate value != 1 is incompatible with specifying any strides value != 1.'),
        (5227, 'en', 'Activation', 'Activation function to use (see activations). If you don\'t specify anything, no activation is applied (ie. "linear" activation: a(x) = x).'),
        (5228, 'en', 'Use bias', 'Boolean, whether the layer uses a bias vector.'),
        (5229, 'en', 'Kernel initializer', 'Initializer for the kernel weights matrix.'),
        (5230, 'en', 'Bias initializer', 'Initializer for the bias vector.'),
        (5231, 'en', 'Kernel regularizer', 'Regularizer function applied to the kernel weights matrix.'),
        (5232, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),
        (5233, 'en', 'Activity regularizer', 'Regularizer function applied to the output of the layer (its "activation").'),
        (5234, 'en', 'Kernel constraint', 'Constraint function applied to the kernel matrix.'),
        (5235, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),

        #Conv2D
        (5236, 'en', 'Filters', 'Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).'),
        (5237, 'en', 'Kernel size', 'An integer or tuple/list of a single integer, specifying the length of the 1D convolution window.'),
        (5238, 'en', 'Strides', 'An integer or tuple/list of a single integer, specifying the stride length of the convolution. Specifying any stride value != 1 is incompatible with specifying any dilation_rate value != 1.'),
        (5239, 'en', 'Padding', 'One of "valid", "causal" or "same" (case-insensitive). "valid" means "no padding".  "same" results in padding the input such that the output has the same length as the original input.  "causal" results in causal (dilated) convolutions, e.g. output[t] does not depend on input[t + 1:]. A zero padding is used such that the output has the same length as the original input. Useful when modeling temporal data where the model should not violate the temporal order.'),
        (5240, 'en', 'Data format', 'A string, one of "channels_last" (default) or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, steps, channels) (default format for temporal data in Keras) while "channels_first" corresponds to inputs with shape (batch, channels, steps).'),
        (5241, 'en', 'Dilation rate', 'An integer or tuple/list of a single integer, specifying the dilation rate to use for dilated convolution. Currently, specifying any dilation_rate value != 1 is incompatible with specifying any strides value != 1.'),
        (5242, 'en', 'Activation', 'Activation function to use (see activations). If you don\'t specify anything, no activation is applied (ie. "linear" activation: a(x) = x).'),
        (5243, 'en', 'Use bias', 'Boolean, whether the layer uses a bias vector.'),
        (5244, 'en', 'Kernel initializer', 'Initializer for the kernel weights matrix.'),
        (5245, 'en', 'Bias initializer', 'Initializer for the bias vector.'),
        (5246, 'en', 'Kernel regularizer', 'Regularizer function applied to the kernel weights matrix.'),
        (5247, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),
        (5248, 'en', 'Activity regularizer', 'Regularizer function applied to the output of the layer (its "activation").'),
        (5249, 'en', 'Kernel constraint', 'Constraint function applied to the kernel matrix.'),
        (5250, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),

        #ZeroPadding2D
        (5251, 'en', 'Padding', 'Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints. If int: the same symmetric padding is applied to height and width. If tuple of 2 ints: interpreted as two different symmetric padding values for height and width: (symmetric_height_pad, symmetric_width_pad). If tuple of 2 tuples of 2 ints: interpreted as ((top_pad, bottom_pad), (left_pad, right_pad))'),
        (5252, 'en', 'Data format', 'A string, one of "channels_last" or "channels_first". The ordering of the dimensions in the inputs. "channels_last" corresponds to inputs with shape (batch, height, width, channels) while "channels_first" corresponds to inputs with shape (batch, channels, height, width). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".'),

        #SeparableConv1D
        (5253, 'en', 'Filters', 'Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).'),
        (5254, 'en', 'Kernel size', 'An integer or tuple/list of a single integer, specifying the length of the 1D convolution window.'),
        (5255, 'en', 'Strides', 'An integer or tuple/list of a single integer, specifying the stride length of the convolution. Specifying any stride value != 1 is incompatible with specifying any dilation_rate value != 1.'),
        (5256, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5257, 'en', 'Data format', 'A string, one of "channels_last" (default) or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, steps, channels) (default format for temporal data in Keras) while "channels_first" corresponds to inputs with shape (batch, channels, steps).'),
        (5258, 'en', 'Dilation rate', 'An integer or tuple/list of a single integer, specifying the dilation rate to use for dilated convolution. Currently, specifying any dilation_rate value != 1 is incompatible with specifying any strides value != 1.'),
        (5259, 'en', 'Depth multiplier', 'The number of depthwise convolution output channels for each input channel. The total number of depthwise convolution output channels will be equal to filters_in * depth_multiplier.'),
        (5260, 'en', 'Activation', 'Activation function to use (see activations). If you don\'t specify anything, no activation is applied (ie. "linear" activation: a(x) = x).'),
        (5261, 'en', 'Use bias', 'Boolean, whether the layer uses a bias vector.'),
        (5262, 'en', 'Depthwise initializer', 'Initializer for the depthwise kernel matrix.'),
        (5263, 'en', 'Pointwise initializer', 'Initializer for the pointwise kernel matrix.'),
        (5264, 'en', 'Bias initializer', 'Initializer for the bias vector.'),
        (5265, 'en', 'Depthwise regularizer', 'Regularizer function applied to the depthwise kernel matrix.'),
        (5266, 'en', 'Pointwise regularizer', 'Regularizer function applied to the pointwise kernel matrix.'),
        (5267, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),
        (5268, 'en', 'Activity regularizer', 'Regularizer function applied to the output of the layer (its "activation").'),
        (5269, 'en', 'Depthwise constraint', 'Constraint function applied to the depthwise kernel matrix.'),
        (5270, 'en', 'Pointwise constraint', 'Constraint function applied to the pointwise kernel matrix.'),
        (5271, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),

        # SeparableConv2D
        (5272, 'en', 'Filters', 'Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).'),
        (5273, 'en', 'Kernel size', 'An integer or tuple/list of a single integer, specifying the length of the 1D convolution window.'),
        (5274, 'en', 'Strides', 'An integer or tuple/list of 2 integers, specifying the strides of the convolution along the height and width. Can be a single integer to specify the same value for all spatial dimensions. Specifying any stride value != 1 is incompatible with specifying any dilation_rate value != 1.'),
        (5275, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5276, 'en', 'Data format', 'A string, one of "channels_last" (default) or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, steps, channels) (default format for temporal data in Keras) while "channels_first" corresponds to inputs with shape (batch, channels, steps).'),
        (5277, 'en', 'Dilation rate', 'An integer or tuple/list of 2 integers, specifying the dilation rate to use for dilated convolution. Currently, specifying any dilation_rate value != 1 is incompatible with specifying any strides value != 1.'),
        (5278, 'en', 'Depth multiplier', 'The number of depthwise convolution output channels for each input channel. The total number of depthwise convolution output channels will be equal to filters_in * depth_multiplier.'),
        (5279, 'en', 'Activation', 'Activation function to use (see activations). If you don\'t specify anything, no activation is applied (ie. "linear" activation: a(x) = x).'),
        (5280, 'en', 'Use bias', 'Boolean, whether the layer uses a bias vector.'),
        (5281, 'en', 'Depthwise initializer', 'Initializer for the depthwise kernel matrix.'),
        (5282, 'en', 'Pointwise initializer', 'Initializer for the pointwise kernel matrix.'),
        (5283, 'en', 'Bias initializer', 'Initializer for the bias vector.'),
        (5284, 'en', 'Depthwise regularizer', 'Regularizer function applied to the depthwise kernel matrix.'),
        (5285, 'en', 'Pointwise regularizer', 'Regularizer function applied to the pointwise kernel matrix.'),
        (5286, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),
        (5287, 'en', 'Activity regularizer', 'Regularizer function applied to the output of the layer (its "activation").'),
        (5288, 'en', 'Depthwise constraint', 'Constraint function applied to the depthwise kernel matrix.'),
        (5289, 'en', 'Pointwise constraint', 'Constraint function applied to the pointwise kernel matrix.'),
        (5290, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),

        # DepthwiseConv2D
        (5291, 'en', 'Kernel size', 'An integer or tuple/list of a single integer, specifying the length of the 1D convolution window.'),
        (5292, 'en', 'Strides', 'An integer or tuple/list of 2 integers, specifying the strides of the convolution along the height and width. Can be a single integer to specify the same value for all spatial dimensions. Specifying any stride value != 1 is incompatible with specifying any dilation_rate value != 1.'),
        (5293, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5294, 'en', 'Depth multiplier', 'The number of depthwise convolution output channels for each input channel. The total number of depthwise convolution output channels will be equal to filters_in * depth_multiplier.'),
        (5295, 'en', 'Data format', 'A string, one of "channels_last" (default) or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, steps, channels) (default format for temporal data in Keras) while "channels_first" corresponds to inputs with shape (batch, channels, steps).'),
        (5296, 'en', 'Activation', 'Activation function to use. If you don\'t specify anything, no activation is applied (ie. "linear" activation: a(x) = x).'),
        (5297, 'en', 'Use bias', 'Boolean, whether the layer uses a bias vector.'),
        (5298, 'en', 'Depthwise initializer', 'Initializer for the depthwise kernel matrix.'),
        (5299, 'en', 'Bias initializer', 'Initializer for the bias vector.'),
        (5300, 'en', 'Depthwise regularizer', 'Regularizer function applied to the depthwise kernel matrix.'),
        (5301, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),
        (5302, 'en', 'Activity regularizer', 'Regularizer function applied to the output of the layer (its "activation").'),
        (5303, 'en', 'Depthwise constraint', 'Constraint function applied to the depthwise kernel matrix.'),
        (5304, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),

        # Conv2DTranspose
        (5305, 'en', 'Filters', 'Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).'),
        (5306, 'en', 'Kernel size', 'An integer or tuple/list of a single integer, specifying the length of the 1D convolution window.'),
        (5307, 'en', 'Strides', 'An integer or tuple/list of 2 integers, specifying the strides of the convolution along the height and width. Can be a single integer to specify the same value for all spatial dimensions. Specifying any stride value != 1 is incompatible with specifying any dilation_rate value != 1.'),
        (5308, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5309, 'en', 'Output padding', 'An integer or tuple/list of 2 integers, specifying the amount of padding along the height and width of the output tensor. Can be a single integer to specify the same value for all spatial dimensions. The amount of output padding along a given dimension must be lower than the stride along that same dimension. If set to None (default), the output shape is inferred.'),
        (5310, 'en', 'Data format', 'A string, one of "channels_last" (default) or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, steps, channels) (default format for temporal data in Keras) while "channels_first" corresponds to inputs with shape (batch, channels, steps).'),
        (5311, 'en', 'Dilation rate', 'An integer or tuple/list of 2 integers, specifying the dilation rate to use for dilated convolution. Can be a single integer to specify the same value for all spatial dimensions. Currently, specifying any dilation_rate value != 1 is incompatible with specifying any stride value != 1.'),
        (5312, 'en', 'Activation', 'Activation function to use (see activations). If you don\'t specify anything, no activation is applied (ie. "linear" activation: a(x) = x).'),
        (5313, 'en', 'Use bias', 'Boolean, whether the layer uses a bias vector.'),
        (5314, 'en', 'Kernel initializer', 'Initializer for the kernel weights matrix.'),
        (5315, 'en', 'Bias initializer', 'Initializer for the bias vector.'),
        (5316, 'en', 'Kernel regularizer', 'Regularizer function applied to the kernel weights matrix.'),
        (5317, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),
        (5318, 'en', 'Activity regularizer', 'Regularizer function applied to the output of the layer (its "activation").'),
        (5319, 'en', 'Kernel constraint', 'Constraint function applied to the kernel matrix.'),
        (5320, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),

        # Conv3D
        (5321, 'en', 'Filters', 'Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).'),
        (5322, 'en', 'Kernel size', 'An integer or tuple/list of 3 integers, specifying the depth, height and width of the 3D convolution window. Can be a single integer to specify the same value for all spatial dimensions.'),
        (5323, 'en', 'Strides', 'An integer or tuple/list of 3 integers, specifying the strides of the convolution along each spatial dimension. Can be a single integer to specify the same value for all spatial dimensions. Specifying any stride value != 1 is incompatible with specifying any dilation_rate value != 1.'),
        (5324, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5325, 'en', 'Data format', 'A string, one of "channels_last" or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, spatial_dim1, spatial_dim2, spatial_dim3, channels) while "channels_first" corresponds to inputs with shape  (batch, channels, spatial_dim1, spatial_dim2, spatial_dim3). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".'),
        (5326, 'en', 'Dilation rate', 'An integer or tuple/list of 3 integers, specifying the dilation rate to use for dilated convolution. Can be a single integer to specify the same value for all spatial dimensions. Currently, specifying any dilation_rate value != 1 is incompatible with specifying any stride value != 1.'),
        (5327, 'en', 'Activation', 'Activation function to use (see activations). If you don\'t specify anything, no activation is applied (ie. "linear" activation: a(x) = x).'),
        (5328, 'en', 'Use bias', 'Boolean, whether the layer uses a bias vector.'),
        (5329, 'en', 'Kernel initializer', 'Initializer for the kernel weights matrix.'),
        (5330, 'en', 'Bias initializer', 'Initializer for the bias vector.'),
        (5331, 'en', 'Kernel regularizer', 'Regularizer function applied to the kernel weights matrix.'),
        (5332, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),
        (5333, 'en', 'Activity regularizer', 'Regularizer function applied to the output of the layer (its "activation").'),
        (5334, 'en', 'Kernel constraint', 'Constraint function applied to the kernel matrix.'),
        (5335, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),

        # Conv3DTranspose
        (5336, 'en', 'Filters', 'Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).'),
        (5337, 'en', 'Kernel size', 'An integer or tuple/list of 3 integers, specifying the depth, height and width of the 3D convolution window. Can be a single integer to specify the same value for all spatial dimensions.'),
        (5338, 'en', 'Strides', 'An integer or tuple/list of 3 integers, specifying the strides of the convolution along the depth, height and width. Can be a single integer to specify the same value for all spatial dimensions. Specifying any stride value != 1 is incompatible with specifying any dilation_rate value != 1.'),
        (5339, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5340, 'en', 'Output padding', 'An integer or tuple/list of 3 integers, specifying the amount of padding along the depth, height, and width. Can be a single integer to specify the same value for all spatial dimensions. The amount of output padding along a given dimension must be lower than the stride along that same dimension. If set to None (default), the output shape is inferred.'),
        (5341, 'en', 'Data format', 'A string, one of "channels_last" or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, depth, height, width, channels) while "channels_first" corresponds to inputs with shape  (batch, channels, depth, height, width). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".'),
        (5342, 'en', 'Dilation rate', 'An integer or tuple/list of 3 integers, specifying the dilation rate to use for dilated convolution. Can be a single integer to specify the same value for all spatial dimensions. Currently, specifying any dilation_rate value != 1 is incompatible with specifying any stride value != 1.'),
        (5343, 'en', 'Activation', 'Activation function to use (see activations). If you don\'t specify anything, no activation is applied (ie. "linear" activation: a(x) = x).'),
        (5344, 'en', 'Use bias', 'Boolean, whether the layer uses a bias vector.'),
        (5345, 'en', 'Kernel initializer', 'Initializer for the kernel weights matrix.'),
        (5346, 'en', 'Bias initializer', 'Initializer for the bias vector.'),
        (5347, 'en', 'Kernel regularizer', 'Regularizer function applied to the kernel weights matrix.'),
        (5348, 'en', 'Bias regularizer', 'Regularizer function applied to the bias vector.'),
        (5349, 'en', 'Activity regularizer', 'Regularizer function applied to the output of the layer (its "activation").'),
        (5350, 'en', 'Kernel constraint', 'Constraint function applied to the kernel matrix.'),
        (5351, 'en', 'Bias constraint', 'Constraint function applied to the bias vector.'),

        # Cropping1D
        (5352, 'en', 'Cropping', 'Int or tuple of int (length 2) How many units should be trimmed off at the beginning and end of the cropping dimension (axis 1). If a single int is provided, the same value will be used for both.'),

        # Cropping2D
        (5353, 'en', 'Cropping', 'Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints. If int: the same symmetric cropping is applied to height and width. If tuple of 2 ints: interpreted as two different symmetric cropping values for height and width: (symmetric_height_crop, symmetric_width_crop). If tuple of 2 tuples of 2 ints: interpreted as ((top_crop, bottom_crop), (left_crop, right_crop)).'),
        (5354, 'en', 'Data format', 'A string, one of "channels_last" or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, height, width, channels) while "channels_first" corresponds to inputs with shape  (batch, channels, height, width). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".'),

        # Cropping3D
        (5355, 'en', 'Cropping', 'Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints. If int: the same symmetric cropping is applied to depth, height, and width. If tuple of 3 ints: interpreted as two different symmetric cropping values for depth, height, and width: (symmetric_dim1_crop, symmetric_dim2_crop, symmetric_dim3_crop). If tuple of 3 tuples of 2 ints: interpreted as ((left_dim1_crop, right_dim1_crop), (left_dim2_crop, right_dim2_crop), (left_dim3_crop, right_dim3_crop)).'),
        (5356, 'en', 'Data format', 'A string, one of "channels_last" or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, spatial_dim1, spatial_dim2, spatial_dim3, channels) while "channels_first" corresponds to inputs with shape  (batch, channels, spatial_dim1, spatial_dim2, spatial_dim3). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".'),

        # UpSampling1D
        (5357, 'en', 'Size', 'Integer. Upsampling factor.'),

        # UpSampling2D
        (5358, 'en', 'Size', 'Int, or tuple of 2 integers. The upsampling factors for rows and columns.'),
        (5359, 'en', 'Data format', 'A string, one of "channels_last" or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, height, width, channels) while "channels_first" corresponds to inputs with shape  (batch, channels, height, width). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".'),
        (5360, 'en', 'Interpolation', 'A string, one of nearest or bilinear. Note that CNTK does not support yet the bilinear upscaling and that with Theano, only size=(2, 2) is possible.'),

        # UpSampling3D
        (5361, 'en', 'Size', 'Int, or tuple of 3 integers. The upsampling factors for dim1, dim2 and dim3.'),
        (5362, 'en', 'Data format', 'A string, one of "channels_last" or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, spatial_dim1, spatial_dim2, spatial_dim3, channels) while "channels_first" corresponds to inputs with shape  (batch, channels, spatial_dim1, spatial_dim2, spatial_dim3). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".'),

        # ZeroPadding1D
        (5363, 'en', 'Padding', 'Int, or tuple of int (length 2), or dictionary. If int: How many zeros to add at the beginning and end of the padding dimension (axis 1). If tuple of int (length 2): How many zeros to add at the beginning and at the end of the padding dimension ((left_pad, right_pad)).'),

        # ZeroPadding3D
        (5364, 'en', 'Padding', 'Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints. If int: the same symmetric padding is applied to height and width. If tuple of 3 ints: interpreted as two different symmetric padding values for height and width: (symmetric_dim1_pad, symmetric_dim2_pad, symmetric_dim3_pad). If tuple of 3 tuples of 2 ints: interpreted as ((left_dim1_pad, right_dim1_pad), (left_dim2_pad, right_dim2_pad), (left_dim3_pad, right_dim3_pad)).'),
        (5365, 'en', 'Data format', 'A string, one of "channels_last" or "channels_first". The ordering of the dimensions in the inputs.  "channels_last" corresponds to inputs with shape  (batch, spatial_dim1, spatial_dim2, spatial_dim3, channels) while "channels_first" corresponds to inputs with shape  (batch, channels, spatial_dim1, spatial_dim2, spatial_dim3). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".'),

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id BETWEEN 5073 AND 5087'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 5073 AND 5087'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id BETWEEN 5073 AND 5087'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE operation_id BETWEEN 5073 AND 5087 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE (id BETWEEN 5173 AND 5187) OR (id BETWEEN 5273 AND 5287)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE (operation_port_id BETWEEN 5173 AND 5187) OR (operation_port_id BETWEEN 5273 AND 5287)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE (id BETWEEN 5173 AND 5187) OR (id BETWEEN 5273 AND 5287)'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5143 AND 5159'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5221 AND 5365'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5143 AND 5159'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5221 AND 5365'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE (operation_id BETWEEN 5021 AND 5022) OR (operation_id BETWEEN 5073 AND 5087)'),
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
