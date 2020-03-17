# -*- coding: utf-8 -*-
"""Add keras layers

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
        (5088, KERAS_PLATAFORM_ID),
        (5089, KERAS_PLATAFORM_ID),
        (5090, KERAS_PLATAFORM_ID),
        (5091, KERAS_PLATAFORM_ID),
        (5092, KERAS_PLATAFORM_ID),
        (5093, KERAS_PLATAFORM_ID),
        (5094, KERAS_PLATAFORM_ID),
        (5095, KERAS_PLATAFORM_ID),
        (5096, KERAS_PLATAFORM_ID),
        (5097, KERAS_PLATAFORM_ID),
        (5098, KERAS_PLATAFORM_ID),
        (5099, KERAS_PLATAFORM_ID),
        (5100, KERAS_PLATAFORM_ID),
        (5101, KERAS_PLATAFORM_ID),
        (5102, KERAS_PLATAFORM_ID),
        (5103, KERAS_PLATAFORM_ID),
        (5104, KERAS_PLATAFORM_ID),
        (5105, KERAS_PLATAFORM_ID),
        (5106, KERAS_PLATAFORM_ID),
        (5107, KERAS_PLATAFORM_ID),
        (5108, KERAS_PLATAFORM_ID),
        (5109, KERAS_PLATAFORM_ID),
        (5110, KERAS_PLATAFORM_ID),
        (5111, KERAS_PLATAFORM_ID),
        (5112, KERAS_PLATAFORM_ID),# Model
        (5113, KERAS_PLATAFORM_ID),# Save Model
        (5114, KERAS_PLATAFORM_ID),# Evaluate Model
        (5115, KERAS_PLATAFORM_ID),# Load Model
        (5116, KERAS_PLATAFORM_ID),# Image Generator

        (5117, KERAS_PLATAFORM_ID),# Image reader
        (5118, KERAS_PLATAFORM_ID),# Text reader
        (5119, KERAS_PLATAFORM_ID),# Sequence reader
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
        (5077, "conv-2d-transpose", 1, 'ACTION', ''),
        (5078, "conv-3d", 1, 'ACTION', ''),
        (5079, "conv-3d-transpose", 1, 'ACTION', ''),
        (5080, "cropping-1d", 1, 'ACTION', ''),
        (5081, "cropping-2d", 1, 'ACTION', ''),
        (5082, "cropping-3d", 1, 'ACTION', ''),
        (5083, "up-sampling-1d", 1, 'ACTION', ''),
        (5084, "up-sampling-2d", 1, 'ACTION', ''),
        (5085, "up-sampling-3d", 1, 'ACTION', ''),
        (5086, "zero-padding-1d", 1, 'ACTION', ''),
        (5087, "zero-padding-3d", 1, 'ACTION', ''),
        # Pre-trained
        (5088, "vgg-16", 1, 'ACTION', ''),
        (5089, "inception-v3", 1, 'ACTION', ''),

        # Advanced
        (5090, "python-code", 1, 'ACTION', ''),

        # Pooling Layers
        (5091, "global-average-pooling-2d", 1, 'ACTION', ''),

        # Merge Layers
        (5092, "add", 1, 'ACTION', ''),
        (5093, "subtract", 1, 'ACTION', ''),
        (5094, "multiply", 1, 'ACTION', ''),
        (5095, "average", 1, 'ACTION', ''),
        (5096, "maximum", 1, 'ACTION', ''),
        (5097, "minimum", 1, 'ACTION', ''),
        (5098, "concatenate", 1, 'ACTION', ''),
        (5099, "dot", 1, 'ACTION', ''),

        # Input
        (5100, "input", 1, 'ACTION', ''),

        # Pooling Layers
        (5101, "max-pooling-1d", 1, 'ACTION', ''),
        (5102, "max-pooling-3d", 1, 'ACTION', ''),
        (5103, "average-pooling-1d", 1, 'ACTION', ''),
        (5104, "average-pooling-2d", 1, 'ACTION', ''),
        (5105, "average-pooling-3d", 1, 'ACTION', ''),
        (5106, "global-max-pooling-1d", 1, 'ACTION', ''),
        (5107, "global-average-pooling-1d", 1, 'ACTION', ''),
        (5108, "global-max-pooling-2d", 1, 'ACTION', ''),
        (5109, "global-average-pooling-2d", 1, 'ACTION', ''),
        (5110, "global-max-pooling-3d", 1, 'ACTION', ''),
        (5111, "global-average-pooling-3d", 1, 'ACTION', ''),

        # Model
        (5112, "model", 1, 'ACTION', ''),
        (5113, "save-model", 1, 'ACTION', ''),
        (5114, "evaluate-model", 1, 'ACTION', ''),
        (5115, "load-model", 1, 'ACTION', ''),

        # Image Generator
        (5116, "image-generator", 1, 'ACTION', ''),

        # Input and output data
        (5117, "image-reader", 1, 'ACTION', ''),
        (5118, "text-reader", 1, 'ACTION', ''),
        (5119, "sequence-reader", 1, 'ACTION', ''),
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
        (5060, "group", 8, 10),
        (5061, "group", 10, 10),# Advanced
        (5062, "group", 9, 10),# Merge Layers
        (5063, "group", 11, 10),# Model
        (5064, "group", 11, 10),# Preprocessing
        (5065, "group", 1, 1),# Input and output data
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
        (5060, 5088),
        (5060, 5089),
        (5061, 5090),
        (5030, 5091),
        (5062, 5092),
        (5062, 5093),
        (5062, 5094),
        (5062, 5095),
        (5062, 5096),
        (5062, 5097),
        (5062, 5098),
        (5062, 5099),
        (5010, 5100),
        (5030, 5101),
        (5030, 5102),
        (5030, 5103),
        (5030, 5104),
        (5030, 5105),
        (5030, 5106),
        (5030, 5107),
        (5030, 5108),
        (5030, 5109),
        (5030, 5110),
        (5030, 5111),
        (5063, 5112),
        (5063, 5113),
        (5063, 5114),
        (5063, 5115),
        (5064, 5116),
        (5065, 5117),
        (5065, 5118),
        (5065, 5119),
    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (5060, "en", 'Pre-trained Layers'),
        (5061, "en", 'Advanced'),
        (5062, "en", 'Merge Layers'),
        (5063, "en", 'Model'),
        (5064, "en", 'Preprocessing'),
        (5065, "en", 'Input and output data'),
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
        (5078, 'en', 'Convolution3D', '3D convolution layer (e.g. spatial convolution '
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
        (5088, 'en', 'VGG16', 'VGG16 model, with weights pre-trained on '
                              'ImageNet. This model can be built both with '
                              '"channels_first" data format (channels, height, '
                              'width) or "channels_last" data format (height, '
                              'width, channels). The default input size for '
                              'this model is 224x224.'),
        (5089, 'en', 'InceptionV3', 'Inception V3 model, with weights '
                                    'pre-trained on ImageNet. This model and '
                                    'can be built both with "channels_first" '
                                    'data format (channels, height, width) or '
                                    '"channels_last" data format (height, '
                                    'width, channels). The default input size '
                                    'for this model is 299x299.'),
        (5090, 'en', 'PythonCode', 'Add Python code to workflow. It enables '
                                   'the creation of functions, classes and/or '
                                   'simple lines of code to promote '
                                   'transformations in the data or addition of '
                                   'new layers.'),

        (5091, 'en', 'GlobalAveragePooling2D', 'Global average pooling '
                                               'operation for spatial data.'),

        (5092, 'en', 'Add', 'Layer that adds a list of inputs. It takes as '
                            'input a list of tensors, all of the same shape, '
                            'and returns a single tensor (also of the same '
                            'shape).'),
        (5093, 'en', 'Subtract', 'Layer that subtracts two inputs. It takes as '
                                 'input a list of tensors of size 2, both of '
                                 'the same shape, and returns a single tensor, '
                                 '(inputs[0] - inputs[1]), also of the same '
                                 'shape. '),
        (5094, 'en', 'Multiply', 'Layer that multiplies (element-wise) a list '
                                 'of inputs. It takes as input a list of '
                                 'tensors, all of the same shape, and returns '
                                 'a single tensor (also of the same shape).'),
        (5095, 'en', 'Average', 'Layer that averages a list of inputs. It '
                                'takes as input a list of tensors, all of the '
                                'same shape, and returns a single tensor (also '
                                'of the same shape).'),
        (5096, 'en', 'Maximum', 'Layer that computes the maximum '
                                '(element-wise) a list of inputs. It takes as '
                                'input a list of tensors, all of the same '
                                'shape, and returns a single tensor (also of '
                                'the same shape).'),
        (5097, 'en', 'Minimum', 'Layer that computes the minimum '
                                '(element-wise) a list of inputs. It takes '
                                'as input a list of tensors, all of the same '
                                'shape, and returns a single tensor (also of '
                                'the same shape).'),
        (5098, 'en', 'Concatenate', 'Layer that concatenates a list of inputs. '
                                    'It takes as input a list of tensors, all '
                                    'of the same shape except for the '
                                    'concatenation axis, and returns a single '
                                    'tensor, the concatenation of all inputs. '),
        (5099, 'en', 'Dot', 'Layer that computes a dot product between samples '
                            'in two tensors. E.g. if applied to a list of two '
                            'tensors a and b of shape (batch_size, n), the '
                            'output will be a tensor of shape (batch_size, 1) '
                            'where each entry i will be the dot product '
                            'between a[i] and b[i].'),

        (5100, 'en', 'Input', 'Input layer is used to instantiate a Keras '
                              'tensor.'),

        (5101, 'en', 'MaxPooling1D', 'Max pooling operation for temporal '
                                     'data.'),
        (5102, 'en', 'MaxPooling3D', 'Max pooling operation for 3D data '
                                     '(spatial or spatio-temporal).'),
        (5103, 'en', 'AveragePooling1D', 'Average pooling for temporal data.'),
        (5104, 'en', 'AveragePooling2D', 'Average pooling operation for spatial '
                                         'data.'),
        (5105, 'en', 'AveragePooling3D', 'Average pooling operation for 3D data'
                                         ' (spatial or spatio-temporal).'),
        (5106, 'en', 'GlobalMaxPooling1D', 'Global max pooling operation for '
                                           'temporal data.'),
        (5107, 'en', 'GlobalAveragePooling1D', 'Global average pooling '
                                               'operation for temporal data.'),
        (5108, 'en', 'GlobalMaxPooling2D', 'Global max pooling operation for '
                                           'patial data.'),
        (5109, 'en', 'GlobalAveragePooling2D', 'Global average pooling '
                                               'operation for spatial data.'),
        (5110, 'en', 'GlobalMaxPooling3D', 'Global Max pooling operation for '
                                           '3D data.'),
        (5111, 'en', 'GlobalAveragePooling3D', 'Global Average pooling '
                                               'operation for 3D data.'),

        (5112, 'en', 'Model', 'Given some input tensor(s) and output '
                                        'tensor(s), you can instantiate a '
                                        'Model. This model will include all '
                                        'layers required in the computation and'
                                        ' trains the model on data generated '
                                        'batch-by-batch by'),
        (5113, 'en', 'Save model', 'Saves the model.'),
        (5114, 'en', 'Evaluate model', 'Evaluates the model on a data'
                                                 ' generator.'),
        (5115, 'en', 'Load model', 'Load a pre existing model.'),

        (5116, 'en', 'Image generator', 'Takes the dataset of images and '
                                        'generates batches of tensor image data'
                                        ' with real-time data augmentation.'),

        (5117, 'en', 'Image reader', 'Reads images from a data source.'),
        (5118, 'en', 'Text reader', 'Reads texts from a data source.'),
        (5119, 'en', 'Sequence reader', 'Reads sequences of any data type '
                                        'from a data source.'),
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
        (5173, 'INPUT', '', 2, 'ONE', 5073, 'input data'),
        (5174, 'INPUT', '', 2, 'ONE', 5074, 'input data'),
        (5175, 'INPUT', '', 2, 'ONE', 5075, 'input data'),
        (5176, 'INPUT', '', 2, 'ONE', 5076, 'input data'),
        (5177, 'INPUT', '', 2, 'ONE', 5077, 'input data'),
        (5178, 'INPUT', '', 2, 'ONE', 5078, 'input data'),
        (5179, 'INPUT', '', 2, 'ONE', 5079, 'input data'),
        (5180, 'INPUT', '', 2, 'ONE', 5080, 'input data'),
        (5181, 'INPUT', '', 2, 'ONE', 5081, 'input data'),
        (5182, 'INPUT', '', 2, 'ONE', 5082, 'input data'),
        (5183, 'INPUT', '', 2, 'ONE', 5083, 'input data'),
        (5184, 'INPUT', '', 2, 'ONE', 5084, 'input data'),
        (5185, 'INPUT', '', 2, 'ONE', 5085, 'input data'),
        (5186, 'INPUT', '', 2, 'ONE', 5086, 'input data'),
        (5187, 'INPUT', '', 2, 'ONE', 5087, 'input data'),
        (5188, 'INPUT', '', 2, 'ONE', 5088, 'input data'),
        (5189, 'INPUT', '', 2, 'ONE', 5089, 'input data'),
        (5190, 'INPUT', '', 2, 'ONE', 5090, 'input data'),
        (5191, 'INPUT', '', 2, 'ONE', 5071, 'input data'),
        (5192, 'INPUT', '', 2, 'ONE', 5091, 'input data'),
        (5193, 'INPUT', '', 2, 'MANY', 5092, 'input data'),
        (5194, 'INPUT', '', 2, 'MANY', 5093, 'input data'),
        (5195, 'INPUT', '', 2, 'MANY', 5094, 'input data'),
        (5196, 'INPUT', '', 2, 'MANY', 5095, 'input data'),
        (5197, 'INPUT', '', 2, 'MANY', 5096, 'input data'),
        (5198, 'INPUT', '', 2, 'MANY', 5097, 'input data'),
        (5199, 'INPUT', '', 2, 'MANY', 5098, 'input data'),
        (5200, 'INPUT', '', 2, 'MANY', 5099, 'input data'),
        #(5201, 'INPUT', '', 2, 'ONE', 5100, 'input data'),
        (5202, 'INPUT', '', 2, 'ONE', 5101, 'input data'),
        (5203, 'INPUT', '', 2, 'ONE', 5102, 'input data'),
        (5204, 'INPUT', '', 2, 'ONE', 5103, 'input data'),
        (5205, 'INPUT', '', 2, 'ONE', 5104, 'input data'),
        (5206, 'INPUT', '', 2, 'ONE', 5105, 'input data'),
        (5207, 'INPUT', '', 2, 'ONE', 5106, 'input data'),
        (5208, 'INPUT', '', 2, 'ONE', 5107, 'input data'),
        (5209, 'INPUT', '', 2, 'ONE', 5108, 'input data'),
        (5210, 'INPUT', '', 2, 'ONE', 5109, 'input data'),

        (5227, 'INPUT', '', 2, 'ONE', 5110, 'input data'),
        (5228, 'INPUT', '', 2, 'ONE', 5111, 'input data'),
        (5229, 'INPUT', '', 4, 'ONE', 5112, 'train-generator'),
        (5230, 'INPUT', '', 1, 'ONE', 5113, 'model'), #save model
        (5232, 'INPUT', '', 1, 'ONE', 5114, 'model'), #evaluate model
        (5233, 'INPUT', '', 1, 'ONE', 5116, 'image data'), #image-generator
        #(5234, 'INPUT', '', 1, 'ONE', 5116, 'validation-image'), #image-generator
        (5235, 'INPUT', '', 3, 'ONE', 5112, 'validation-generator'),
        (5236, 'INPUT', '', 2, 'MANY', 5112, 'input layer'), #model inputs
        (5237, 'INPUT', '', 1, 'MANY', 5112, 'output layer'), #model outputs

        (5273, 'OUTPUT', '', 1, 'MANY', 5073, 'output data'),
        (5274, 'OUTPUT', '', 1, 'MANY', 5074, 'output data'),
        (5275, 'OUTPUT', '', 1, 'MANY', 5075, 'output data'),
        (5276, 'OUTPUT', '', 1, 'MANY', 5076, 'output data'),
        (5277, 'OUTPUT', '', 1, 'MANY', 5077, 'output data'),
        (5278, 'OUTPUT', '', 1, 'MANY', 5078, 'output data'),
        (5279, 'OUTPUT', '', 1, 'MANY', 5079, 'output data'),
        (5280, 'OUTPUT', '', 1, 'MANY', 5080, 'output data'),
        (5281, 'OUTPUT', '', 1, 'MANY', 5081, 'output data'),
        (5282, 'OUTPUT', '', 1, 'MANY', 5082, 'output data'),
        (5283, 'OUTPUT', '', 1, 'MANY', 5083, 'output data'),
        (5284, 'OUTPUT', '', 1, 'MANY', 5084, 'output data'),
        (5285, 'OUTPUT', '', 1, 'MANY', 5085, 'output data'),
        (5286, 'OUTPUT', '', 1, 'MANY', 5086, 'output data'),
        (5287, 'OUTPUT', '', 1, 'MANY', 5087, 'output data'),
        (5288, 'OUTPUT', '', 1, 'MANY', 5088, 'output data'),
        (5289, 'OUTPUT', '', 1, 'MANY', 5089, 'output data'),
        (5290, 'OUTPUT', '', 1, 'ONE', 5090, 'python code'),
        (5291, 'OUTPUT', '', 1, 'MANY', 5091, 'output data'),
        (5292, 'OUTPUT', '', 1, 'MANY', 5092, 'output data'),
        (5293, 'OUTPUT', '', 1, 'MANY', 5093, 'output data'),
        (5294, 'OUTPUT', '', 1, 'MANY', 5094, 'output data'),
        (5295, 'OUTPUT', '', 1, 'MANY', 5095, 'output data'),
        (5296, 'OUTPUT', '', 1, 'MANY', 5096, 'output data'),
        (5297, 'OUTPUT', '', 1, 'MANY', 5097, 'output data'),
        (5298, 'OUTPUT', '', 1, 'MANY', 5098, 'output data'),
        (5299, 'OUTPUT', '', 1, 'MANY', 5099, 'output data'),
        (5300, 'OUTPUT', '', 1, 'MANY', 5100, 'output data'),
        (5301, 'OUTPUT', '', 1, 'MANY', 5101, 'output data'),
        (5302, 'OUTPUT', '', 1, 'MANY', 5102, 'output data'),
        (5303, 'OUTPUT', '', 1, 'MANY', 5103, 'output data'),
        (5304, 'OUTPUT', '', 1, 'MANY', 5104, 'output data'),
        (5305, 'OUTPUT', '', 1, 'MANY', 5105, 'output data'),
        (5306, 'OUTPUT', '', 1, 'MANY', 5106, 'output data'),
        (5307, 'OUTPUT', '', 1, 'MANY', 5107, 'output data'),
        (5308, 'OUTPUT', '', 1, 'MANY', 5108, 'output data'),
        (5309, 'OUTPUT', '', 1, 'MANY', 5109, 'output data'),
        (5310, 'OUTPUT', '', 1, 'MANY', 5110, 'output data'),
        (5311, 'OUTPUT', '', 1, 'MANY', 5111, 'output data'),
        (5312, 'OUTPUT', '', 1, 'MANY', 5112, 'model'),# model
        (5313, 'OUTPUT', '', 1, 'MANY', 5115, 'model'),# load model
        (5314, 'OUTPUT', '', 1, 'MANY', 5116, 'generator'),# image generator
        #(5315, 'OUTPUT', '', 1, 'MANY', 5116, 'generator'),# image generator

        (5316, 'OUTPUT', '', 2, 'ONE', 5117, 'train-image'), #image-reader
        (5317, 'OUTPUT', '', 1, 'ONE', 5117, 'validation-image'), #image-reader
        (5318, 'OUTPUT', '', 2, 'ONE', 5118, 'train-text'), #text-reader
        (5319, 'OUTPUT', '', 1, 'ONE', 5118, 'validation-text'), #text-reader
        (5320, 'OUTPUT', '', 2, 'ONE', 5119, 'train-sequence'), #sequence-reader
        (5321, 'OUTPUT', '', 1, 'ONE', 5119, 'validation-sequence'), #sequence-reader
        (5322, 'OUTPUT', '', 2, 'MANY', 5112, 'output data'),# model output data

        # Python code ports
        (5323, 'INPUT', '', 1, 'ONE', 5011, 'python code'),
        (5324, 'INPUT', '', 1, 'ONE', 5012, 'python code'),
        (5325, 'INPUT', '', 1, 'ONE', 5013, 'python code'),
        (5326, 'INPUT', '', 1, 'ONE', 5014, 'python code'),
        (5327, 'INPUT', '', 1, 'ONE', 5015, 'python code'),
        (5328, 'INPUT', '', 1, 'ONE', 5016, 'python code'),
        (5329, 'INPUT', '', 1, 'ONE', 5017, 'python code'),
        (5330, 'INPUT', '', 1, 'ONE', 5018, 'python code'),
        (5331, 'INPUT', '', 1, 'ONE', 5019, 'python code'),
        (5332, 'INPUT', '', 1, 'ONE', 5021, 'python code'),
        (5333, 'INPUT', '', 1, 'ONE', 5022, 'python code'),
        (5334, 'INPUT', '', 1, 'ONE', 5023, 'python code'),
        (5335, 'INPUT', '', 1, 'ONE', 5024, 'python code'),
        (5336, 'INPUT', '', 1, 'ONE', 5025, 'python code'),
        (5337, 'INPUT', '', 1, 'ONE', 5026, 'python code'),
        (5338, 'INPUT', '', 1, 'ONE', 5031, 'python code'),
        (5339, 'INPUT', '', 1, 'ONE', 5041, 'python code'),
        (5340, 'INPUT', '', 1, 'ONE', 5042, 'python code'),
        (5341, 'INPUT', '', 1, 'ONE', 5043, 'python code'),
        (5342, 'INPUT', '', 1, 'ONE', 5044, 'python code'),
        (5343, 'INPUT', '', 1, 'ONE', 5045, 'python code'),
        (5344, 'INPUT', '', 1, 'ONE', 5046, 'python code'),
        (5345, 'INPUT', '', 1, 'ONE', 5047, 'python code'),
        (5346, 'INPUT', '', 1, 'ONE', 5048, 'python code'),
        (5347, 'INPUT', '', 1, 'ONE', 5051, 'python code'),
        (5348, 'INPUT', '', 1, 'ONE', 5061, 'python code'),
        (5349, 'INPUT', '', 1, 'ONE', 5062, 'python code'),
        (5350, 'INPUT', '', 1, 'ONE', 5073, 'python code'),
        (5351, 'INPUT', '', 1, 'ONE', 5074, 'python code'),
        (5352, 'INPUT', '', 1, 'ONE', 5075, 'python code'),
        (5353, 'INPUT', '', 1, 'ONE', 5076, 'python code'),
        (5354, 'INPUT', '', 1, 'ONE', 5077, 'python code'),
        (5355, 'INPUT', '', 1, 'ONE', 5078, 'python code'),
        (5356, 'INPUT', '', 1, 'ONE', 5079, 'python code'),
        (5357, 'INPUT', '', 1, 'ONE', 5080, 'python code'),
        (5358, 'INPUT', '', 1, 'ONE', 5081, 'python code'),
        (5359, 'INPUT', '', 1, 'ONE', 5082, 'python code'),
        (5360, 'INPUT', '', 1, 'ONE', 5083, 'python code'),
        (5361, 'INPUT', '', 1, 'ONE', 5084, 'python code'),
        (5362, 'INPUT', '', 1, 'ONE', 5085, 'python code'),
        (5363, 'INPUT', '', 1, 'ONE', 5086, 'python code'),
        (5364, 'INPUT', '', 1, 'ONE', 5087, 'python code'),
        (5365, 'INPUT', '', 1, 'ONE', 5088, 'python code'),
        (5366, 'INPUT', '', 1, 'ONE', 5089, 'python code'),
        #(5367, 'INPUT', '', 1, 'ONE', 5090, 'python code'),
        (5368, 'INPUT', '', 1, 'ONE', 5092, 'python code'),
        (5369, 'INPUT', '', 1, 'ONE', 5093, 'python code'),
        (5370, 'INPUT', '', 1, 'ONE', 5094, 'python code'),
        (5371, 'INPUT', '', 1, 'ONE', 5095, 'python code'),
        (5372, 'INPUT', '', 1, 'ONE', 5096, 'python code'),
        (5373, 'INPUT', '', 1, 'ONE', 5097, 'python code'),
        (5374, 'INPUT', '', 1, 'ONE', 5098, 'python code'),
        (5375, 'INPUT', '', 1, 'ONE', 5099, 'python code'),
        (5376, 'INPUT', '', 1, 'ONE', 5100, 'python code'),
        (5377, 'INPUT', '', 1, 'ONE', 5101, 'python code'),
        (5378, 'INPUT', '', 1, 'ONE', 5102, 'python code'),
        (5379, 'INPUT', '', 1, 'ONE', 5103, 'python code'),
        (5380, 'INPUT', '', 1, 'ONE', 5104, 'python code'),
        (5381, 'INPUT', '', 1, 'ONE', 5105, 'python code'),
        (5382, 'INPUT', '', 1, 'ONE', 5106, 'python code'),
        (5383, 'INPUT', '', 1, 'ONE', 5107, 'python code'),
        (5384, 'INPUT', '', 1, 'ONE', 5108, 'python code'),
        (5385, 'INPUT', '', 1, 'ONE', 5109, 'python code'),
        (5386, 'INPUT', '', 1, 'ONE', 5110, 'python code'),
        (5387, 'INPUT', '', 1, 'ONE', 5111, 'python code'),

    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface():
    tb = table(
        'operation_port_interface',
        column('id', Integer),
        column('color', String))

    columns = ('id', 'color')
    data = [
        (22, '#FF2A00'),
        (23, '#009900'),
        (24, '#CCCC00'),
        (25, '#276cce'),
        (26, '#a867af'),
        (27, '#111'),
        (28, '#022776'),
    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_translation():
    tb = table(
        'operation_port_interface_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (22, 'en', 'Model'),
        (22, 'pt', 'Model'),
        (23, 'en', 'Generator'),
        (23, 'pt', 'Generator'),
        (24, 'en', 'ImageData'),
        (24, 'pt', 'ImageData'),
        (25, 'en', 'TextData'),
        (25, 'pt', 'TextData'),
        (26, 'en', 'SequenceData'),
        (26, 'pt', 'SequenceData'),
        (27, 'en', 'Layer'),
        (27, 'pt', 'Layer'),
        (28, 'en', 'PythonCode'),
        (28, 'pt', 'PythonCode'),
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
        (5188, 1),
        (5189, 1),
        (5190, 28),
        (5191, 1),
        (5192, 1),
        (5193, 1),
        (5194, 1),
        (5195, 1),
        (5196, 1),
        (5197, 1),
        (5198, 1),
        (5199, 1),
        (5200, 1),
        #(5201, 1),
        (5202, 1),
        (5203, 1),
        (5204, 1),
        (5205, 1),
        (5206, 1),
        (5207, 1),
        (5208, 1),
        (5209, 1),
        (5210, 1),

        (5227, 1),
        (5228, 1),
        (5229, 23),
        (5230, 22),
        (5232, 22),
        (5233, 24),
        #(5234, 24),
        (5235, 23),
        (5236, 27),
        (5237, 27),

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
        (5288, 1),
        (5289, 1),
        (5290, 28),
        (5291, 1),
        (5292, 1),
        (5293, 1),
        (5294, 1),
        (5295, 1),
        (5296, 1),
        (5297, 1),
        (5298, 1),
        (5299, 1),
        (5300, 1),
        (5301, 1),
        (5302, 1),
        (5303, 1),
        (5304, 1),
        (5305, 1),
        (5306, 1),
        (5307, 1),
        (5308, 1),
        (5309, 1),
        (5310, 1),
        (5311, 1),
        (5312, 22),
        (5313, 22),
        (5314, 23),
        #(5315, 23),
        (5316, 24),
        (5317, 24),
        (5318, 25),
        (5319, 25),
        (5320, 26),
        (5321, 26),
        (5322, 1),

        (5323, 28),
        (5324, 28),
        (5325, 28),
        (5326, 28),
        (5327, 28),
        (5328, 28),
        (5329, 28),
        (5330, 28),
        (5331, 28),
        (5332, 28),
        (5333, 28),
        (5334, 28),
        (5335, 28),
        (5336, 28),
        (5337, 28),
        (5338, 28),
        (5339, 28),
        (5340, 28),
        (5341, 28),
        (5342, 28),
        (5343, 28),
        (5344, 28),
        (5345, 28),
        (5346, 28),
        (5347, 28),
        (5348, 28),
        (5349, 28),
        (5350, 28),
        (5351, 28),
        (5352, 28),
        (5353, 28),
        (5354, 28),
        (5355, 28),
        (5356, 28),
        (5357, 28),
        (5358, 28),
        (5359, 28),
        (5360, 28),
        (5361, 28),
        (5362, 28),
        (5363, 28),
        (5364, 28),
        (5365, 28),
        (5366, 28),
        #(5367, 28),
        (5368, 28),
        (5369, 28),
        (5370, 28),
        (5371, 28),
        (5372, 28),
        (5373, 28),
        (5374, 28),
        (5375, 28),
        (5376, 28),
        (5377, 28),
        (5378, 28),
        (5379, 28),
        (5380, 28),
        (5381, 28),
        (5382, 28),
        (5383, 28),
        (5384, 28),
        (5385, 28),
        (5386, 28),
        (5387, 28),
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
        (5188, 'en', 'input data', 'Input data'),
        (5189, 'en', 'input data', 'Input data'),
        (5190, 'en', 'python code', 'Python code'),
        (5191, 'en', 'input data', 'Input data'),
        (5192, 'en', 'input data', 'Input data'),
        (5193, 'en', 'input data', 'Input data'),
        (5194, 'en', 'input data', 'Input data'),
        (5195, 'en', 'input data', 'Input data'),
        (5196, 'en', 'input data', 'Input data'),
        (5197, 'en', 'input data', 'Input data'),
        (5198, 'en', 'input data', 'Input data'),
        (5199, 'en', 'input data', 'Input data'),
        (5200, 'en', 'input data', 'Input data'),
        #(5201, 'en', 'input data', 'Input data'),
        (5202, 'en', 'input data', 'Input data'),
        (5203, 'en', 'input data', 'Input data'),
        (5204, 'en', 'input data', 'Input data'),
        (5205, 'en', 'input data', 'Input data'),
        (5206, 'en', 'input data', 'Input data'),
        (5207, 'en', 'input data', 'Input data'),
        (5208, 'en', 'input data', 'Input data'),
        (5209, 'en', 'input data', 'Input data'),
        (5210, 'en', 'input data', 'Input data'),
        (5227, 'en', 'input data', 'Input data'),
        (5228, 'en', 'input data', 'Input data'),
        (5229, 'en', 'train generator', 'Generator'),
        (5230, 'en', 'model', 'Model'),
        (5232, 'en', 'model', 'Model'),
        (5233, 'en', 'image data', 'Image Data'),
        #(5234, 'en', 'validation image data', 'Image Data'),
        (5235, 'en', 'validation generator', 'Generator'),
        (5236, 'en', 'input layers', 'Input data'),
        (5237, 'en', 'output layers', 'Input data'),

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
        (5288, 'en', 'output data', 'Output data'),
        (5289, 'en', 'output data', 'Output data'),
        (5290, 'en', 'python code', 'Python code'),
        (5291, 'en', 'output data', 'Output data'),
        (5292, 'en', 'output data', 'Output data'),
        (5293, 'en', 'output data', 'Output data'),
        (5294, 'en', 'output data', 'Output data'),
        (5295, 'en', 'output data', 'Output data'),
        (5296, 'en', 'output data', 'Output data'),
        (5297, 'en', 'output data', 'Output data'),
        (5298, 'en', 'output data', 'Output data'),
        (5299, 'en', 'output data', 'Output data'),
        (5300, 'en', 'output data', 'Output data'),
        (5301, 'en', 'output data', 'Output data'),
        (5302, 'en', 'output data', 'Output data'),
        (5303, 'en', 'output data', 'Output data'),
        (5304, 'en', 'output data', 'Output data'),
        (5305, 'en', 'output data', 'Output data'),
        (5306, 'en', 'output data', 'Output data'),
        (5307, 'en', 'output data', 'Output data'),
        (5308, 'en', 'output data', 'Output data'),
        (5309, 'en', 'output data', 'Output data'),
        (5310, 'en', 'output data', 'Output data'),
        (5311, 'en', 'output data', 'Output data'),
        (5312, 'en', 'model', 'Model'),
        (5313, 'en', 'model', 'Model'),
        (5314, 'en', 'generator', 'Generator'),
        #(5315, 'en', 'validation generator', 'Generator'),

        (5316, 'en', 'train image data', 'Image Data'),
        (5317, 'en', 'validation image data', 'Image Data'),
        (5318, 'en', 'text data', 'Text Data'),
        (5319, 'en', 'validation text data', 'Text Data'),
        (5320, 'en', 'sequence data', 'Sequence Data'),
        (5321, 'en', 'validation sequence data', 'Sequence Data'),
        (5322, 'en', 'output data', 'Output data'),

        (5323, 'en', 'python code', 'Python code'),
        (5324, 'en', 'python code', 'Python code'),
        (5325, 'en', 'python code', 'Python code'),
        (5326, 'en', 'python code', 'Python code'),
        (5327, 'en', 'python code', 'Python code'),
        (5328, 'en', 'python code', 'Python code'),
        (5329, 'en', 'python code', 'Python code'),
        (5330, 'en', 'python code', 'Python code'),
        (5331, 'en', 'python code', 'Python code'),
        (5332, 'en', 'python code', 'Python code'),
        (5333, 'en', 'python code', 'Python code'),
        (5334, 'en', 'python code', 'Python code'),
        (5335, 'en', 'python code', 'Python code'),
        (5336, 'en', 'python code', 'Python code'),
        (5337, 'en', 'python code', 'Python code'),
        (5338, 'en', 'python code', 'Python code'),
        (5339, 'en', 'python code', 'Python code'),
        (5340, 'en', 'python code', 'Python code'),
        (5341, 'en', 'python code', 'Python code'),
        (5342, 'en', 'python code', 'Python code'),
        (5343, 'en', 'python code', 'Python code'),
        (5344, 'en', 'python code', 'Python code'),
        (5345, 'en', 'python code', 'Python code'),
        (5346, 'en', 'python code', 'Python code'),
        (5347, 'en', 'python code', 'Python code'),
        (5348, 'en', 'python code', 'Python code'),
        (5349, 'en', 'python code', 'Python code'),
        (5350, 'en', 'python code', 'Python code'),
        (5351, 'en', 'python code', 'Python code'),
        (5352, 'en', 'python code', 'Python code'),
        (5353, 'en', 'python code', 'Python code'),
        (5354, 'en', 'python code', 'Python code'),
        (5355, 'en', 'python code', 'Python code'),
        (5356, 'en', 'python code', 'Python code'),
        (5357, 'en', 'python code', 'Python code'),
        (5358, 'en', 'python code', 'Python code'),
        (5359, 'en', 'python code', 'Python code'),
        (5360, 'en', 'python code', 'Python code'),
        (5361, 'en', 'python code', 'Python code'),
        (5362, 'en', 'python code', 'Python code'),
        (5363, 'en', 'python code', 'Python code'),
        (5364, 'en', 'python code', 'Python code'),
        (5365, 'en', 'python code', 'Python code'),
        (5366, 'en', 'python code', 'Python code'),
        #(5367, 'en', 'python code', 'Python code'),
        (5368, 'en', 'python code', 'Python code'),
        (5369, 'en', 'python code', 'Python code'),
        (5370, 'en', 'python code', 'Python code'),
        (5371, 'en', 'python code', 'Python code'),
        (5372, 'en', 'python code', 'Python code'),
        (5373, 'en', 'python code', 'Python code'),
        (5374, 'en', 'python code', 'Python code'),
        (5375, 'en', 'python code', 'Python code'),
        (5376, 'en', 'python code', 'Python code'),
        (5377, 'en', 'python code', 'Python code'),
        (5378, 'en', 'python code', 'Python code'),
        (5379, 'en', 'python code', 'Python code'),
        (5380, 'en', 'python code', 'Python code'),
        (5381, 'en', 'python code', 'Python code'),
        (5382, 'en', 'python code', 'Python code'),
        (5383, 'en', 'python code', 'Python code'),
        (5384, 'en', 'python code', 'Python code'),
        (5385, 'en', 'python code', 'Python code'),
        (5386, 'en', 'python code', 'Python code'),
        (5387, 'en', 'python code', 'Python code'),
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
        (5160, 1, 1, 'execution'),
        (5163, 1, 1, 'execution'),
        (5164, 1, 1, 'execution'),
        (5165, 1, 1, 'execution'),
        (5166, 1, 1, 'execution'),
        (5167, 1, 1, 'execution'),
        (5168, 1, 1, 'execution'),
        (5169, 1, 1, 'execution'),
        (5170, 1, 1, 'execution'),
        # (5171, 1, 1, 'execution'),
        # (5172, 1, 1, 'execution'),
        # (5173, 1, 1, 'execution'),
        # (5174, 1, 1, 'execution'),
        # (5175, 1, 1, 'execution'),
        (5221, 1, 1, 'execution'),
        (5222, 1, 1, 'execution'),
        (5223, 1, 1, 'execution'),
        (5224, 1, 1, 'execution'),
        (5225, 1, 1, 'execution'),
        (5226, 1, 1, 'execution'),
        (5227, 1, 1, 'execution'),
        (5228, 1, 1, 'execution'),
        (5229, 1, 1, 'execution'),
        (5230, 1, 1, 'execution'),
        (5231, 1, 1, 'execution'),
        (5232, 1, 1, 'execution'),
        (5233, 1, 1, 'execution'),
        (5234, 1, 1, 'execution'),
        (5235, 1, 1, 'execution'),
        (5236, 1, 1, 'execution'),
        (5237, 1, 1, 'execution'),
        (5238, 1, 1, 'execution'),
        (5239, 1, 1, 'execution'),
        (5240, 1, 1, 'execution'),
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
        (5160, 'en', 'Execution'),
        (5163, 'en', 'Execution'),
        (5164, 'en', 'Execution'),
        (5165, 'en', 'Execution'),
        (5166, 'en', 'Execution'),
        (5167, 'en', 'Execution'),
        (5168, 'en', 'Execution'),
        (5169, 'en', 'Execution'),
        (5170, 'en', 'Execution'),
        # (5171, 'en', 'Execution'),
        # (5172, 'en', 'Execution'),
        # (5173, 'en', 'Execution'),
        # (5174, 'en', 'Execution'),
        # (5175, 'en', 'Execution'),
        (5221, 'en', 'execution'),
        (5222, 'en', 'Execution'),
        (5223, 'en', 'Execution'),
        (5224, 'en', 'Execution'),
        (5225, 'en', 'Execution'),
        (5226, 'en', 'Execution'),
        (5227, 'en', 'Execution'),
        (5228, 'en', 'Execution'),
        (5229, 'en', 'Execution'),
        (5230, 'en', 'Execution'),
        (5231, 'en', 'Execution'),
        (5232, 'en', 'Execution'),
        (5233, 'en', 'Execution'),
        (5234, 'en', 'Execution'),
        (5235, 'en', 'Execution'),
        (5236, 'en', 'Execution'),
        (5237, 'en', 'Execution'),
        (5238, 'en', 'Execution'),
        (5239, 'en', 'Execution'),
        (5240, 'en', 'Execution'),
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
        (5160, 'pt', 'Execução'),
        (5163, 'pt', 'Execução'),
        (5164, 'pt', 'Execução'),
        (5165, 'pt', 'Execução'),
        (5166, 'pt', 'Execução'),
        (5167, 'pt', 'Execução'),
        (5168, 'pt', 'Execução'),
        (5169, 'pt', 'Execução'),
        (5170, 'pt', 'Execução'),
        # (5171, 'pt', 'Execução'),
        # (5172, 'pt', 'Execução'),
        # (5173, 'pt', 'Execução'),
        # (5174, 'pt', 'Execução'),
        # (5175, 'pt', 'Execução'),
        (5221, 'pt', 'Execução'),
        (5222, 'pt', 'Execução'),
        (5223, 'pt', 'Execução'),
        (5224, 'pt', 'Execução'),
        (5225, 'pt', 'Execução'),
        (5226, 'pt', 'Execução'),
        (5227, 'pt', 'Execução'),
        (5228, 'pt', 'Execução'),
        (5229, 'pt', 'Execução'),
        (5230, 'pt', 'Execução'),
        (5231, 'pt', 'Execução'),
        (5232, 'pt', 'Execução'),
        (5233, 'pt', 'Execução'),
        (5234, 'pt', 'Execução'),
        (5235, 'pt', 'Execução'),
        (5236, 'pt', 'Execução'),
        (5237, 'pt', 'Execução'),
        (5238, 'pt', 'Execução'),
        (5239, 'pt', 'Execução'),
        (5240, 'pt', 'Execução'),
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
        (5051, 41),
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
        (5088, 41),
        (5089, 41),
        (5090, 41),
        (5091, 41),
        (5092, 41),
        (5093, 41),
        (5094, 41),
        (5095, 41),
        (5096, 41),
        (5097, 41),
        (5098, 41),
        (5099, 41),
        (5100, 41),
        (5101, 41),
        (5102, 41),
        (5103, 41),
        (5104, 41),
        (5105, 41),
        (5106, 41),
        (5107, 41),
        (5108, 41),
        (5109, 41),
        (5110, 41),
        (5111, 41),
        (5031, 41),
        (5112, 41),
        (5113, 41),
        (5114, 41),
        (5115, 41),
        (5116, 41),
        (5117, 41),
        (5118, 41),
        (5119, 41),
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
        (5051, 5160),
        (5088, 5163),
        (5089, 5164),
        (5090, 5165),
        (5091, 5166),
        (5092, 5167),
        (5093, 5168),
        (5094, 5169),
        (5095, 5170),
        (5096, 5171),
        (5097, 5172),
        (5098, 5173),
        (5099, 5174),
        (5100, 5175),
        (5101, 5221),
        (5102, 5222),
        (5103, 5223),
        (5104, 5224),
        (5105, 5225),
        (5106, 5226),
        (5107, 5227),
        (5108, 5228),
        (5109, 5229),
        (5110, 5230),
        (5111, 5231),
        (5031, 5232),
        (5112, 5233),
        (5113, 5234),
        (5114, 5235),
        (5115, 5236),
        (5116, 5237),
        (5117, 5238),
        (5118, 5239),
        (5119, 5240),
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

    LIMONERO_IMAGE = "`${LIMONERO_URL}/datasources?simple=true&list=" \
                     "true&enabled=1&formats=TAR_IMAGE_FOLDER," \
                     "HAR_IMAGE_FOLDER,IMAGE_FOLDER`"

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
        (5225, 'data_format', 'TEXT', 0, 5, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5145),
        (5226, 'dilation_rate', 'TEXT', 0, 6, 1, 'text', None, None, 'EXECUTION', 5145),
        (5227, 'activation', 'TEXT', 1, 7, None, 'dropdown', None,
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
        (5236, 'filters', 'TEXT', 1, 1, 0, 'text', None, None, 'EXECUTION', 5143),
        (5237, 'kernel_size', 'TEXT', 1, 2, 0, 'text', None, None, 'EXECUTION', 5143),
        (5238, 'strides', 'TEXT', 1, 3, "(1, 1)", 'text', None, None, 'EXECUTION', 5143),
        (5478, 'input_shape', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION', 5143),
        (5239, 'padding', 'TEXT', 0, 4, None, 'dropdown', None,
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
        (5244, 'kernel_initializer', 'TEXT', 0, 9, None, 'dropdown', None,
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
        (5245, 'bias_initializer', 'TEXT', 0, 10, None, 'dropdown', None,
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
        (5256, 'padding', 'TEXT', 0, 4, None, 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5146),
        (5257, 'data_format', 'TEXT', 0, 5, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5146),
        (5258, 'dilation_rate', 'TEXT', 0, 6, "1", 'text', None, None, 'EXECUTION', 5146),
        (5259, 'depth_multiplier', 'INTEGER', 0, 7, 1, 'integer', None, None, 'EXECUTION', 5146),
        (5260, 'activation', 'TEXT', 0, 8, None, 'dropdown', None,
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
        (5262, 'depthwise_initializer', 'TEXT', 0, 10, None, 'dropdown', None,
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
        (5263, 'pointwise_initializer', 'TEXT', 0, 11, None, 'dropdown', None,
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
        (5264, 'bias_initializer', 'TEXT', 0, 12, None, 'dropdown', None,
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
        (5275, 'padding', 'TEXT', 0, 4, None, 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5147),
        (5276, 'data_format', 'TEXT', 0, 5, None, 'dropdown', None,
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
        (5281, 'depthwise_initializer', 'TEXT', 0, 10, None, 'dropdown', None,
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
        (5282, 'pointwise_initializer', 'TEXT', 0, 11, None, 'dropdown', None,
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
        (5283, 'bias_initializer', 'TEXT', 0, 12, None, 'dropdown', None,
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
        (5293, 'padding', 'TEXT', 0, 3, None, 'dropdown', None,
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
        (5298, 'depthwise_initializer', 'TEXT', 0, 8, None, 'dropdown', None,
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
        (5299, 'bias_initializer', 'TEXT', 0, 9, None, 'dropdown', None,
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
        (5308, 'padding', 'TEXT', 0, 4, None, 'dropdown', None,
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
        (5314, 'kernel_initializer', 'TEXT', 0, 10, None, 'dropdown', None,
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
        (5315, 'bias_initializer', 'TEXT', 0, 11, None, 'dropdown', None,
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
        (5324, 'padding', 'TEXT', 0, 4, None, 'dropdown', None,
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
        (5329, 'kernel_initializer', 'TEXT', 0, 9, None, 'dropdown', None,
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
        (5330, 'bias_initializer', 'TEXT', 0, 10, None, 'dropdown', None,
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
        (5339, 'padding', 'TEXT', 0, 4, None, 'dropdown', None,
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
        (5345, 'kernel_initializer', 'TEXT', 0, 10, None, 'dropdown', None,
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
        (5346, 'bias_initializer', 'TEXT', 0, 11, None, 'dropdown', None,
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
        (5360, 'interpolation', 'TEXT', 1, 3, None, 'dropdown', None,
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

        # BatchNormalization
        (5366, 'axis', 'INTEGER', 0, 1, -1, 'integer', None, None, 'EXECUTION', 5160),
        (5367, 'momentum', 'DECIMAL', 0, 2, 0.99, 'decimal', None, None, 'EXECUTION', 5160),
        (5368, 'epsilon', 'DECIMAL', 0, 3, 0.001, 'decimal', None, None, 'EXECUTION', 5160),
        (5369, 'center', 'INTEGER', 0, 4, 1, 'checkbox', None, None, 'EXECUTION', 5160),
        (5370, 'scale', 'INTEGER', 0, 5, 1, 'checkbox', None, None, 'EXECUTION', 5160),
        (5371, 'beta_initializer', 'TEXT', 0, 6, None, 'dropdown', None,
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
         ), 'EXECUTION', 5160),
        (5372, 'gamma_initializer', 'TEXT', 0, 7, None, 'dropdown', None,
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
         ), 'EXECUTION', 5160),
        (5373, 'moving_mean_initializer', 'TEXT', 0, 8, None, 'dropdown', None,
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
         ), 'EXECUTION', 5160),
        (5374, 'moving_variance_initializer', 'TEXT', 0, 9, None, 'dropdown', None,
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
         ), 'EXECUTION', 5160),
        (5375, 'beta_regularizer', 'TEXT', 0, 10, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ), 'EXECUTION', 5160),
        (5376, 'gamma_regularizer', 'TEXT', 0, 11, None, 'dropdown', None,
         json.dumps([
             {"key": "l1", "value": "l1"},
             {"key": "l2", "value": "l2"},
             {"key": "l1_l2", "value": "l1_l2"}]
         ), 'EXECUTION', 5160),
        (5377, 'beta_constraint', 'TEXT', 0, 12, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]), 'EXECUTION', 5160),
        (5378, 'gamma_constraint', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {"key": "max_norm", "value": "max_norm"},
             {"key": "min_max_norm", "value": "min_max_norm"},
             {"key": "non_neg", "value": "non_neg"},
             {"key": "unit_norm", "value": "unit_norm"}
         ]), 'EXECUTION', 5160),

        #VGG16
        (5379, 'include_top', 'INTEGER', 0, 1, 1, 'checkbox', None, None, 'EXECUTION', 5163),
        (5380, 'weights', 'TEXT', 0, 3, 'imagenet', 'text', None, None, 'EXECUTION', 5163),
        (5381, 'input_tensor', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION', 5163),
        (5382, 'input_shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5163),
        (5383, 'pooling', 'TEXT', 0, 6, None, 'dropdown', None,
         json.dumps([
             {"key": "avg", "value": "avg"},
             {"key": "max", "value": "max"},
         ]), 'EXECUTION', 5163),
        (5384, 'classes', 'INTEGER', 0, 7, None, 'integer', None, None, 'EXECUTION', 5163),
        (5385, 'trainable', 'INTEGER', 0, 2, 0, 'checkbox', None, None, 'EXECUTION', 5163),

        #InceptionV3
        (5386, 'include_top', 'INTEGER', 0, 1, 1, 'checkbox', None, None, 'EXECUTION', 5164),
        (5387, 'weights', 'TEXT', 0, 3, 'imagenet', 'text', None, None, 'EXECUTION', 5164),
        (5388, 'input_tensor', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION', 5164),
        (5389, 'input_shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5164),
        (5390, 'pooling', 'TEXT', 0, 6, None, 'dropdown', None,
         json.dumps([
             {"key": "avg", "value": "avg"},
             {"key": "max", "value": "max"},
         ]), 'EXECUTION', 5164),
        (5391, 'classes', 'INTEGER', 0, 7, None, 'integer', None, None, 'EXECUTION', 5164),
        (5392, 'trainable', 'INTEGER', 0, 2, 0, 'checkbox', None, None, 'EXECUTION', 5164),

        #PythonCode
        (5393, 'code', 'TEXT', 0, 2, "# Write your Python code here", 'code', None, json.dumps({"language": "python"}), 'EXECUTION', 5165),
        (5394, 'out_code', 'INTEGER', 0, 1, 0, 'checkbox', None, None, 'EXECUTION', 5165),

        #Input Layer
        (5395, 'shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5177),

        # Conv2D
        (5396, 'weights', 'TEXT', 0, 16, None, 'text', None, None, 'EXECUTION', 5143),

        # GlobalAveragePooling2D
        (5397, 'data_format', 'TEXT', 0, 2, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5166),

        # Conv2D
        (5398, 'trainable', 'INTEGER', 0, 8, 0, 'checkbox', None, None, 'EXECUTION', 5143),

        # Merge Add
        (5399, 'inputs', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 5167),
        (5400, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5167),

        # Merge Subtract
        (5401, 'inputs', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 5168),
        (5402, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5168),

        # Merge Multiply
        (5403, 'inputs', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 5169),
        (5404, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5169),

        # Merge Average
        (5405, 'inputs', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 5170),
        (5406, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5170),

        # Merge Maximum
        (5407, 'inputs', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 5171),
        (5408, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5171),

        # Merge Minimum
        (5409, 'inputs', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 5172),
        (5410, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5172),

        # Merge Concatenate
        (5411, 'inputs', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 5173),
        (5412, 'axis', 'INTEGER', 0, 1, -1, 'integer', None, None, 'EXECUTION', 5173),
        (5413, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5173),

        # Merge Dot
        (5414, 'inputs', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 5174),
        (5415, 'axes', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5174),
        (5416, 'normalize', 'INTEGER', 0, 3, 0, 'checkbox', None, None, 'EXECUTION', 5174),
        (5417, 'kwargs', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION', 5174),

        # Lambda
        (5418, 'output_shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5138),

        # Input Layer
        (5419, 'shape', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 5175),
        (5420, 'batch_shape', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5175),
        (5421, 'dtype', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION', 5175),
        (5422, 'sparse', 'INTEGER', 0, 4, 0, 'checkbox', None, None, 'EXECUTION', 5175),

        # MaxPooling1D
        (5423, 'pool_size', 'INTEGER', 1, 1, 2, 'integer', None, None, 'EXECUTION', 5221),
        (5424, 'strides', 'INTEGER', 0, 2, None, 'integer', None, None, 'EXECUTION', 5221),
        (5425, 'padding', 'TEXT', 0, 3, None, 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5221),
        (5426, 'data_format', 'TEXT', 0, 4, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5221),
        (5427, 'kwargs', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5221),

        # MaxPooling2D
        (5428, 'pool_size', 'TEXT', 1, 1, "(2, 2)", 'text', None, None, 'EXECUTION', 5232),
        (5429, 'strides', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5232),
        (5430, 'padding', 'TEXT', 0, 3, None, 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5232),
        (5431, 'data_format', 'TEXT', 0, 4, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5232),
        (5432, 'kwargs', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5232),

        # MaxPooling3D
        (5433, 'pool_size', 'TEXT', 1, 1, "(2, 2, 2)", 'text', None, None, 'EXECUTION', 5222),
        (5434, 'strides', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5222),
        (5435, 'padding', 'TEXT', 0, 3, None, 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5222),
        (5436, 'data_format', 'TEXT', 0, 4, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5222),
        (5437, 'kwargs', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5222),

        # AveragePooling1D
        (5438, 'pool_size', 'TEXT', 1, 1, "(2, 2, 2)", 'text', None, None, 'EXECUTION', 5223),
        (5439, 'strides', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5223),
        (5440, 'padding', 'TEXT', 0, 3, None, 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5223),
        (5441, 'data_format', 'TEXT', 0, 4, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5223),
        (5442, 'kwargs', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5223),

        # AveragePooling2D
        (5443, 'pool_size', 'TEXT', 1, 1, "(2, 2)", 'text', None, None, 'EXECUTION', 5224),
        (5444, 'strides', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5224),
        (5445, 'padding', 'TEXT', 0, 3, None, 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5224),
        (5446, 'data_format', 'TEXT', 0, 4, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5224),
        (5447, 'kwargs', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5224),

        # AveragePooling3D
        (5448, 'pool_size', 'TEXT', 1, 1, "(2, 2, 2)", 'text', None, None, 'EXECUTION', 5225),
        (5449, 'strides', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5225),
        (5450, 'padding', 'TEXT', 0, 3, None, 'dropdown', None,
         json.dumps([
             {'key': 'valid', 'value': 'valid'},
             {'key': 'same', 'value': 'same'},
         ]), 'EXECUTION', 5225),
        (5451, 'data_format', 'TEXT', 0, 4, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5225),
        (5452, 'kwargs', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5225),

        # GlobalMaxPooling1D
        (5453, 'data_format', 'TEXT', 0, 1, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5226),
        (5454, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5226),

        # GlobalAveragePooling1D
        (5455, 'data_format', 'TEXT', 0, 1, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5227),
        (5456, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5227),

        # GlobalMaxPooling2D
        (5457, 'data_format', 'TEXT', 0, 1, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5228),
        (5458, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5228),

        # GlobalAveragePooling2D
        (5459, 'data_format', 'TEXT', 0, 1, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5229),
        (5460, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5229),

        # GlobalMaxPooling3D
        (5461, 'data_format', 'TEXT', 0, 1, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5230),
        (5462, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5230),

        # GlobalAveragePooling3D
        (5463, 'data_format', 'TEXT', 0, 1, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5231),
        (5464, 'kwargs', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5231),

        # Model
        (5465, 'optimizer', 'TEXT', 1, 1, None, 'dropdown', None,
         json.dumps([
             {"key": "adadelta", "value": "adadelta"},
             {"key": "adagrad", "value": "adagrad"},
             {"key": "adam", "value": "adam"},
             {"key": "adamax", "value": "adamax"},
             {"key": "nadam", "value": "nadam"},
             {"key": "rmsprop", "value": "rmsprop"},
             {"key": "sgd", "value": "sgd"},
         ]), 'EXECUTION', 5233),
        (5466, 'loss', 'TEXT', 1, 2, None, 'select2', None,
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
         ]), 'EXECUTION', 5233),
        (5467, 'metrics', 'TEXT', 1, 3, "Categorical Accuracy", 'select2', None,
         json.dumps([
             {"value": "Binary Accuracy", "key": "acc"},
             {"value": "Categorical Accuracy", "key": "acc"},
             {"value": "Cosine Proximity", "key": "cosine"},
             {"value": "Mean Absolute Error", "key": "mae"},
             {"value": "Mean Absolute Percentage Error", "key": "mape"},
             {"value": "Mean Squared Error", "key": "mse"},
             {"value": "Sparse Categorical Accuracy", "key": "sparse_categorical_accuracy"},
             {"value": "Sparse Top k Categorical Accuracy", "key": "sparse_top_k_categorical_accuracy"},
             {"value": "Top k Categorical Accuracy", "key": "top_k_categorical_accuracy"},
         ]), 'EXECUTION', 5233),
        (5468, 'k', 'INTEGER', 0, 4, 5, 'integer', None, None, 'EXECUTION', 5233),
        (5469, 'loss_weights', 'TEXT', 0, 7, None, 'text', None, None, 'EXECUTION', 5233),
        (5470, 'sample_weight_mode', 'TEXT', 0, 8, None, 'text', None, None, 'EXECUTION', 5233),
        (5471, 'weighted_metrics', 'TEXT', 0, 9, None, 'text', None, None, 'EXECUTION', 5233),
        (5472, 'target_tensors', 'TEXT', 0, 10, None, 'text', None, None, 'EXECUTION', 5233),
        (5473, 'kwargs', 'TEXT', 0, 11, None, 'text', None, None, 'EXECUTION', 5233),

        (5474, 'steps_per_epoch', 'INTEGER', 1, 5, 32, 'integer', None, None, 'EXECUTION', 5233),
        (5475, 'epochs', 'INTEGER', 1, 6, 10, 'integer', None, None, 'EXECUTION', 5233),
        (5476, 'verbose', 'TEXT', 0, 12, 1, 'dropdown', None,
         json.dumps([
             {"key": 0, "value": "silent"},
             {"key": 1, "value": "progress bar"},
             {"key": 2, "value": "one line per epoch"},
         ]), 'EXECUTION', 5233),
        (5477, 'callbacks', 'TEXT', 0, 13, "TensorBoard", 'select2', None,
         json.dumps([
             {"value": "BaseLogger", "key": "BaseLogger"},
             {"value": "CSVLogger", "key": "CSVLogger"},
             {"value": "EarlyStopping", "key": "EarlyStopping"},
             {"value": "History", "key": "History"},
             {"value": "LambdaCallback", "key": "LambdaCallback"},
             {"value": "LearningRateScheduler", "key": "LearningRateScheduler"},
             {"value": "ModelCheckpoint", "key": "ModelCheckpoint"},
             {"value": "ProgbarLogger", "key": "ProgbarLogger"},
             {"value": "ReduceLROnPlateau", "key": "ReduceLROnPlateau"},
             {"value": "RemoteMonitor", "key": "RemoteMonitor"},
             {"value": "TensorBoard", "key": "TensorBoard"},
             {"value": "TerminateOnNaN", "key": "TerminateOnNaN"},
         ]), 'EXECUTION', 5233),
        (5479, 'validation_steps', 'DECIMAL', 0, 15, None, 'decimal', None, None, 'EXECUTION', 5233),
        (5480, 'validation_freq', 'INTEGER', 0, 16, None, 'integer', None, None, 'EXECUTION', 5233),
        (5481, 'class_weight', 'TEXT', 0, 17, None, 'text', None, None, 'EXECUTION', 5233),
        (5482, 'max_queue_size', 'INTEGER', 0, 18, 10, 'integer', None, None, 'EXECUTION', 5233),
        (5483, 'workers', 'INTEGER', 0, 19, 1, 'integer', None, None, 'EXECUTION', 5233),
        (5484, 'use_multiprocessing', 'INTEGER', 0, 20, 0, 'checkbox', None, None, 'EXECUTION', 5233),
        (5485, 'shuffle', 'INTEGER', 0, 21, 0, 'checkbox', None, None, 'EXECUTION', 5233),
        (5486, 'initial_epoch', 'INTEGER', 0, 22, None, 'integer', None, None, 'EXECUTION', 5233),

        # Image Generator
        (5487, 'featurewise_center', 'INTEGER', 0, 1, 0, 'checkbox', None, None, 'EXECUTION', 5237),
        (5488, 'samplewise_center', 'INTEGER', 0, 2, 0, 'checkbox', None, None, 'EXECUTION', 5237),
        (5489, 'featurewise_std_normalization', 'INTEGER', 0, 3, 0, 'checkbox', None, None, 'EXECUTION', 5237),
        (5490, 'samplewise_std_normalization', 'INTEGER', 0, 4, 0, 'checkbox', None, None, 'EXECUTION', 5237),
        (5491, 'zca_epsilon', 'DECIMAL', 0, 5, 1e-6, 'decimal', None, None, 'EXECUTION', 5237),
        (5492, 'zca_whitening', 'INTEGER', 0, 6, 0, 'checkbox', None, None, 'EXECUTION', 5237),
        (5493, 'rotation_range', 'INTEGER', 0, 7, 0, 'integer', None, None, 'EXECUTION', 5237),
        (5494, 'width_shift_range', 'TEXT', 0, 8, "0.0", 'text', None, None, 'EXECUTION', 5237),
        (5495, 'height_shift_range', 'TEXT', 0, 9, "0.0", 'text', None, None, 'EXECUTION', 5237),
        (5496, 'brightness_range', 'TEXT', 0, 10, None, 'text', None, None, 'EXECUTION', 5237),
        (5497, 'shear_range', 'DECIMAL', 0, 11, 0.0, 'decimal', None, None, 'EXECUTION', 5237),
        (5498, 'zoom_range', 'DECIMAL', 0, 12, 0.0, 'decimal', None, None, 'EXECUTION', 5237),
        (5499, 'channel_shift_range', 'DECIMAL', 0, 13, 0.0, 'decimal', None, None, 'EXECUTION', 5237),
        (5500, 'fill_mode', 'TEXT', 0, 14, 'nearest', 'dropdown', None,
         json.dumps([
             {"key": "constant", "value": "constant"},
             {"key": "nearest", "value": "nearest"},
             {"key": "reflect", "value": "reflect"},
             {"key": "wrap", "value": "wrap"},
         ]), 'EXECUTION', 5237),
        (5501, 'cval', 'DECIMAL', 0, 15, 0.0, 'decimal', None, None, 'EXECUTION', 5237),
        (5502, 'horizontal_flip', 'INTEGER', 0, 16, 0, 'checkbox', None, None, 'EXECUTION', 5237),
        (5503, 'vertical_flip', 'INTEGER', 0, 17, 0, 'checkbox', None, None, 'EXECUTION', 5237),
        (5504, 'rescale', 'TEXT', 0, 18, None, 'text', None, None, 'EXECUTION', 5237),
        (5505, 'preprocessing_function', 'TEXT', 0, 19, None, 'text', None, None, 'EXECUTION', 5237),
        (5506, 'data_format', 'TEXT', 0, 20, None, 'dropdown', None,
         json.dumps([
             {'key': 'channels_last', 'value': 'channels_last'},
             {'key': 'channels_first', 'value': 'channels_first'},
         ]), 'EXECUTION', 5237),
        (5507, 'validation_split', 'DECIMAL', 0, 21, 0.0, 'decimal', None, None, 'EXECUTION', 5237),
        (5508, 'dtype', 'TEXT', 0, 22, None, 'text', None, None, 'EXECUTION', 5237),

        # image reader
        (5509, 'train_images', 'INTEGER', 1, 1, None, 'lookup', LIMONERO_IMAGE, None, 'EXECUTION', 5238),
        (5510, 'validation_images', 'INTEGER', 0, 2, None, 'lookup', LIMONERO_IMAGE, None, 'EXECUTION', 5238),

        # text reader
        (5511, 'train_text', 'INTEGER', 1, 1, None, 'lookup', LIMONERO_IMAGE, None, 'EXECUTION', 5239),
        (5512, 'validation_text', 'INTEGER', 0, 2, None, 'lookup', LIMONERO_IMAGE, None, 'EXECUTION', 5239),

        # Sequence reader
        (5513, 'train_sequence', 'INTEGER', 1, 1, None, 'lookup', LIMONERO_IMAGE, None, 'EXECUTION', 5240),
        (5514, 'validation_sequence', 'INTEGER', 0, 2, None, 'lookup', LIMONERO_IMAGE, None, 'EXECUTION', 5240),

        #Flow from directory add to Image Generator Operation
        (5515, 'target_size', 'TEXT', 1, 23, "(256, 256)", 'text', None, None, 'EXECUTION', 5237),
        (5516, 'color_mode', 'TEXT', 0, 24, 'rgb', 'dropdown', None,
         json.dumps([
             {"key": "grayscale", "value": "grayscale"},
             {"key": "rgb", "value": "rgb"},
             {"key": "rgba", "value": "rgba"},
         ]), 'EXECUTION', 5237),
        # (5517, 'class_mode', 'TEXT', 0, 25, None, 'dropdown', None,
        #  json.dumps([
        #      {"key": "binary", "value": "binary"},
        #      {"key": "categorical", "value": "categorical"},
        #      {"key": "input", "value": "input"},
        #      {"key": "sparse", "value": "sparse"},
        #  ]), 'EXECUTION', 5237),
        (5518, 'batch_size', 'INTEGER', 1, 26, 32, 'integer', None, None, 'EXECUTION', 5237),
        (5519, 'shuffle', 'INTEGER', 0, 27, 1, 'checkbox', None, None, 'EXECUTION', 5237),
        (5520, 'seed', 'INTEGER', 0, 28, None, 'integer', None, None, 'EXECUTION', 5237),
        (5521, 'subset', 'TEXT', 0, 29, None, 'dropdown', None,
         json.dumps([
             {"key": "training", "value": "training"},
             {"key": "validation", "value": "validation"},
         ]), 'EXECUTION', 5237),
        (5522, 'interpolation', 'TEXT', 0, 30, "nearest", 'dropdown', None,
         json.dumps([
             {"key": "bicubic", "value": "bicubic"},
             {"key": "bilinear", "value": "bilinear"},
             {"key": "nearest", "value": "nearest"},
             #{"key": "lanczos", "value": "lanczos"},
             #{"key": "box", "value": "box"},
             #{"key": "hamming", "value": "hamming"},
         ]), 'EXECUTION', 5237),

        # Conv1D
        (5523, 'trainable', 'INTEGER', 0, 16, 0, 'checkbox', None, None, 'EXECUTION', 5145),
        (5524, 'input_shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5145),

        # SeparableConv1D
        (5525, 'input_shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5146),

        # SeparableConv2D
        (5526, 'input_shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5147),

        # DepthwiseConv2D
        (5527, 'input_shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5148),

        # Conv2DTranspose
        (5528, 'input_shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5149),

        # Conv3D
        (5529, 'input_shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5150),

        # Conv3DTranspose
        (5530, 'input_shape', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5151),

        # Cropping1D
        (5531, 'input_shape', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5152),

        # Cropping2D
        (5532, 'input_shape', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5153),

        # Cropping3D
        (5533, 'input_shape', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5154),


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
        (5478, 'en', 'Input shape', '3D tensor with shape: (batch, steps, channels).'),
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

        # BatchNormalization
        (5366, 'en', 'Axis', 'Integer, the axis that should be normalized (typically the features axis). For instance, after a Conv2D layer with  data_format="channels_first", set axis=1 in BatchNormalization.'),
        (5367, 'en', 'Momentum', 'Momentum for the moving mean and the moving variance.'),
        (5368, 'en', 'Epsilon', 'Small float added to variance to avoid dividing by zero.'),
        (5369, 'en', 'Center', 'If True, add offset of beta to normalized tensor. If False, beta is ignored.'),
        (5370, 'en', 'Scale', 'If True, multiply by gamma. If False, gamma is not used. When the next layer is linear (also e.g. nn.relu), this can be disabled since the scaling will be done by the next layer.'),
        (5371, 'en', 'Beta initializer', 'Initializer for the beta weight.'),
        (5372, 'en', 'Gamma initializer', 'Initializer for the gamma weight.'),
        (5373, 'en', 'Moving mean initializer', 'Initializer for the moving mean.'),
        (5374, 'en', 'Moving variance initializer', 'Initializer for the moving variance.'),
        (5375, 'en', 'Beta regularizer', 'Optional regularizer for the beta weight.'),
        (5376, 'en', 'Gamma regularizer', 'Optional regularizer for the gamma weight.'),
        (5377, 'en', 'Beta constraint', 'Optional constraint for the beta weight.'),
        (5378, 'en', 'Gamma constraint', 'Optional constraint for the gamma weight.'),

        # VGG16
        (5379, 'en', 'Include top', 'Whether to include the 3 fully-connected layers at the top of the network.'),
        (5380, 'en', 'Weights', 'One of None (random initialization) or "imagenet" (pre-training on ImageNet).'),
        (5381, 'en', 'Input tensor', 'Optional Keras tensor (i.e. output of layers.Input()) to use as image input for the model.'),
        (5382, 'en', 'Input shape', 'Optional shape tuple, only to be specified if include_top is False (otherwise the input shape has to be (224, 224, 3) (with "channels_last" data format) or (3, 224, 224) (with "channels_first" data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. (200, 200, 3) would be one valid value.'),
        (5383, 'en', 'Pooling', 'Optional pooling mode for feature extraction when include_top is False. None means that the output of the model will be the 4D tensor output of the last convolutional layer. "avg" means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor. "max" means that global max pooling will be applied.'),
        (5384, 'en', 'Classes', 'Optional number of classes to classify images into, only to be specified if include_top is  True, and if no weights argument is specified.'),
        (5385, 'en', 'Trainable', 'Indicates whether the layer in the model is trainable.'),

        # InceptionV3
        (5386, 'en', 'Include top', 'Whether to include the 3 fully-connected layers at the top of the network.'),
        (5387, 'en', 'Weights', 'One of None (random initialization) or "imagenet" (pre-training on ImageNet).'),
        (5388, 'en', 'Input tensor', 'Optional Keras tensor (i.e. output of layers.Input()) to use as image input for the model.'),
        (5389, 'en', 'Input shape', 'Optional shape tuple, only to be specified if include_top is False (otherwise the input shape has to be (224, 224, 3) (with "channels_last" data format) or (3, 224, 224) (with "channels_first" data format). It should have exactly 3 inputs channels, and width and height should be no smaller than 32. E.g. (200, 200, 3) would be one valid value.'),
        (5390, 'en', 'Pooling', 'Optional pooling mode for feature extraction when include_top is False. None means that the output of the model will be the 4D tensor output of the last convolutional layer. "avg" means that global average pooling will be applied to the output of the last convolutional layer, and thus the output of the model will be a 2D tensor. "max" means that global max pooling will be applied.'),
        (5391, 'en', 'Classes', 'Optional number of classes to classify images into, only to be specified if include_top is  True, and if no weights argument is specified.'),
        (5392, 'en', 'Trainable', 'Indicates whether the layer in the model is trainable.'),

        # PythonCode
        (5393, 'en', 'Code', 'Possible to add simple lines, functions, classes or an entire Python code.'),
        (5394, 'en', 'Out code', 'Code used out of the method to generate the Keras layers.'),

        # Input Layer
        (5395, 'en', 'Shape', 'A shape tuple (integer), not including the batch size. For instance, shape=(32,) indicates that the expected input will be batches of 32-dimensional vectors.'),

        #Conv2D
        (5396, 'en', 'Weights', 'Array of weights. It was probably defined as a variable in a previously created Python code layer.'),

        #GlobalAveragePooling2D
        (5397, 'en', 'Data format', 'A string, one of channels_last (default) or channels_first. The ordering of the dimensions in the inputs.  channels_last corresponds to inputs with shape  (batch, height, width, channels) while channels_first corresponds to inputs with shape  (batch, channels, height, width). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".'),

        #Conv2D
        (5398, 'en', 'Trainable', 'Indicates whether the layer in the model is trainable.'),

        # Add
        (5399, 'en', 'Inputs', 'A list of input tensors (at least 2).'),
        (5400, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # Subtract
        (5401, 'en', 'Inputs', 'A list of input tensors (at least 2).'),
        (5402, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # Multiply
        (5403, 'en', 'Inputs', 'A list of input tensors (at least 2).'),
        (5404, 'en', '**Kwargs', 'Standard layer keyword arguments.'),

        # Average
        (5405, 'en', 'Inputs', 'A list of input tensors (at least 2).'),
        (5406, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # Maximum
        (5407, 'en', 'Inputs', 'A list of input tensors (at least 2).'),
        (5408, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # Minimum
        (5409, 'en', 'Inputs', 'A list of input tensors (at least 2).'),
        (5410, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # Concatenate
        (5411, 'en', 'Inputs', 'A list of input tensors (at least 2).'),
        (5412, 'en', 'Axis', 'Concatenation axis.'),
        (5413, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # Dot
        (5414, 'en', 'Inputs', 'A list of input tensors (at least 2).'),
        (5415, 'en', 'Axes', 'Integer or tuple of integers, axis or axes along '
                             'which to take the dot product.'),
        (5416, 'en', 'Normalize', 'Whether to L2-normalize samples along the '
                                  'dot product axis before taking the dot '
                                  'product. If set to True, then the output '
                                  'of the dot product is the cosine proximity '
                                  'between the two samples.'),
        (5417, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # Lambda output_shape
        (5418, 'en', 'Output shape', 'Expected output shape from function. '
                                     'Only relevant when using Theano. Can be '
                                     'a tuple or function. If a tuple, it only '
                                     'specifies the first dimension onward; '
                                     'sample dimension is assumed either the '
                                     'same as the input: output_shape = (input_'
                                     'shape[0], ) + output_shape or, the input '
                                     'is None and the sample dimension is also '
                                     'None: output_shape = (None, ) + '
                                     'output_shape If a function, it specifies '
                                     'the entire shape as a function of the '
                                     'input shape: '
                                     'output_shape = f(input_shape).'),

        # Input
        (5419, 'en', 'Shape', 'A shape tuple (integer), not including the '
                              'batch size. For instance, shape=(32,) indicates'
                              ' that the expected input will be batches of '
                              '32-dimensional vectors.'),
        (5420, 'en', 'Batch shape', 'A shape tuple (integer), including the '
                                    'batch size. For instance, '
                                    'batch_shape=(10, 32) indicates that the '
                                    'expected input will be batches of 10 '
                                    '32-dimensional vectors. batch_shape='
                                    '(None, 32) indicates batches of an '
                                    'arbitrary number of 32-dimensional '
                                    'vectors.'),
        (5421, 'en', 'Data type', 'The data type expected by the input, as a '
                                  'string (float32, float64, int32...)'),
        (5422, 'en', 'Sparse', 'A boolean specifying whether the placeholder '
                               'to be created is sparse.'),

        # MaxPooling1D
        (5423, 'en', 'Pool size', 'Integer, size of the max pooling windows.'),
        (5424, 'en', 'Strides', 'Integer, or None. Factor by which to '
                                'downscale. E.g. 2 will halve the input. If '
                                'None, it will default to pool_size.'),
        (5425, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5426, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape '
                                    '(batch, steps, features) while '
                                    'channels_first corresponds to inputs '
                                    'with shape (batch, features, steps).'),
        (5427, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # MaxPooling2D
        (5428, 'en', 'Pool size', 'Integer or tuple of 2 integers, factors by '
                                  'which to downscale (vertical, horizontal). '
                                  '(2, 2) will halve the input in both spatial '
                                  'dimension. If only one integer is specified,'
                                  ' the same window length will be used for '
                                  'both dimensions.'),
        (5429, 'en', 'Strides', 'Integer, tuple of 2 integers, or None. Strides'
                                ' values. If None, it will default to '
                                'pool_size.'),
        (5430, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5431, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape (batch, '
                                    'height, width, channels) while '
                                    'channels_first corresponds to inputs with'
                                    ' shape (batch, channels, height, width).'),
        (5432, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # MaxPooling3D
        (5433, 'en', 'Pool size', 'Tuple of 3 integers, factors by which to '
                                  'downscale (dim1, dim2, dim3). (2, 2, 2) will'
                                  ' halve the size of the 3D input in each '
                                  'dimension.'),
        (5434, 'en', 'Strides', 'Tuple of 3 integers, or None. Strides values.'),
        (5435, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5436, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape '
                                    '(batch, spatial_dim1, spatial_dim2, '
                                    'spatial_dim3, channels) while '
                                    'channels_first corresponds to inputs with'
                                    ' shape  (batch, channels, spatial_dim1, '
                                    'spatial_dim2, spatial_dim3).'),
        (5437, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # AveragePooling1D
        (5438, 'en', 'Pool size', 'Integer size of the average pooling windows.'),
        (5439, 'en', 'Strides', 'Integer, or None. Factor by which to '
                                'downscale. E.g. 2 will halve the input. If '
                                'None, it will default to pool_size.'),
        (5440, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5441, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape '
                                    '(batch, steps, features) while '
                                    'channels_first corresponds to inputs with '
                                    'shape  (batch, features, steps).'),
        (5442, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # AveragePooling2D
        (5443, 'en', 'Pool size', 'Integer or tuple of 2 integers, factors by '
                                  'which to downscale (vertical, horizontal). '
                                  '(2, 2) will halve the input in both spatial '
                                  'dimension. If only one integer is specified,'
                                  ' the same window length will be used for '
                                  'both dimensions.'),
        (5444, 'en', 'Strides', 'Integer, tuple of 2 integers, or None. Strides'
                                ' values. If None, it will default to '
                                'pool_size.'),
        (5445, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5446, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape (batch, '
                                    'height, width, channels) while '
                                    'channels_first corresponds to inputs with'
                                    ' shape (batch, channels, height, width).'),
        (5447, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # AveragePooling3D
        (5448, 'en', 'Pool size', 'Tuple of 3 integers, factors by which to '
                                  'downscale (dim1, dim2, dim3). (2, 2, 2) will'
                                  ' halve the size of the 3D input in each '
                                  'dimension.'),
        (5449, 'en', 'Strides', 'Tuple of 3 integers, or None. Strides values.'),
        (5450, 'en', 'Padding', 'One of "valid" or "same" (case-insensitive).'),
        (5451, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape '
                                    '(batch, spatial_dim1, spatial_dim2, '
                                    'spatial_dim3, channels) while '
                                    'channels_first corresponds to inputs with'
                                    ' shape  (batch, channels, spatial_dim1, '
                                    'spatial_dim2, spatial_dim3).'),
        (5452, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # GlobalMaxPooling1D
        (5453, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape '
                                    '(batch, steps, features) while '
                                    'channels_first corresponds to inputs with '
                                    'shape  (batch, features, steps).'),
        (5454, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # GlobalAveragePooling1D
        (5455, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape '
                                    '(batch, steps, features) while '
                                    'channels_first corresponds to inputs with '
                                    'shape  (batch, features, steps).'),
        (5456, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # GlobalMaxPooling2D
        (5457, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape  (batch, '
                                    'height, width, channels) while '
                                    'channels_first corresponds to inputs with '
                                    'shape  (batch, channels, height, width).'),
        (5458, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # GlobalAveragePooling2D
        (5459, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape  (batch, '
                                    'height, width, channels) while '
                                    'channels_first corresponds to inputs with '
                                    'shape  (batch, channels, height, width).'),
        (5460, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # GlobalMaxPooling3D
        (5461, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape '
                                    '(batch, spatial_dim1, spatial_dim2, '
                                    'spatial_dim3, channels) while '
                                    'channels_first corresponds to inputs with'
                                    ' shape  (batch, channels, spatial_dim1, '
                                    'spatial_dim2, spatial_dim3).'),
        (5462, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # GlobalAveragePooling3D
        (5463, 'en', 'Data format', 'A string, one of channels_last (default) '
                                    'or channels_first. The ordering of the '
                                    'dimensions in the inputs.  channels_last '
                                    'corresponds to inputs with shape '
                                    '(batch, spatial_dim1, spatial_dim2, '
                                    'spatial_dim3, channels) while '
                                    'channels_first corresponds to inputs with'
                                    ' shape  (batch, channels, spatial_dim1, '
                                    'spatial_dim2, spatial_dim3).'),
        (5464, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # Model Generator
        (5465, 'en', 'Optimizer', 'An optimizer is one of the two arguments '
                                  'required for compiling a Keras model.'),
        (5466, 'en', 'Loss', 'If the model has multiple outputs, you can use a '
                             'different loss on each output by passing a '
                             'dictionary or a list of losses. The loss value '
                             'that will be minimized by the model will then be '
                             'the sum of all individual losses.'),
        (5467, 'en', 'Metrics', 'A metric is a function that is used to judge '
                                'the performance of your model.'),
        (5468, 'en', 'K', 'K is a parameter required for the metrics related '
                          'to the Top K Categorical Accuracy functions.'),
        (5469, 'en', 'Loss weights', 'Optional list or dictionary specifying '
                                     'scalar coefficients (Python floats) to '
                                     'weight the loss contributions of '
                                     'different model outputs. The loss value '
                                     'that will be minimized by the model will '
                                     'then be the weighted sum of all '
                                     'individual losses, weighted by the '
                                     'loss_weights coefficients. If a list, it '
                                     'is expected to have a 1:1 mapping to the '
                                     'model\'s outputs. If a tensor, it is '
                                     'expected to map output names (strings) '
                                     'to scalar coefficients.'),
        (5470, 'en', 'Sample weight mode', 'If you need to do timestep-wise '
                                           'sample weighting (2D weights), '
                                           'set this to "temporal". None '
                                           'defaults to sample-wise weights '
                                           '(1D). If the model has multiple '
                                           'outputs, you can use a different '
                                           'sample_weight_mode on each output '
                                           'by passing a dictionary or a list '
                                           'of modes.'),
        (5471, 'en', 'Weighted metrics', 'List of metrics to be evaluated and '
                                         'weighted by sample_weight or '
                                         'class_weight during training and '
                                         'testing.'),
        (5472, 'en', 'Target tensors', 'By default, Keras will create '
                                       'placeholders for the model\'s target, '
                                       'which will be fed with the target data '
                                       'during training. If instead you would '
                                       'like to use your own target tensors '
                                       '(in turn, Keras will not expect '
                                       'external Numpy data for these targets '
                                       'at training time), you can specify '
                                       'them via the target_tensors argument. '
                                       'It can be a single tensor (for a '
                                       'single-output model), a list of '
                                       'tensors, or a dict mapping output '
                                       'names to target tensors.'),
        (5473, 'en', 'Kwargs', 'For the TensorFlow backend, these arguments are'
                               ' passed into tf.Session.run.'),

        (5474, 'en', 'Steps per epoch', 'Total number of steps (batches of '
                                        'samples) to yield from generator '
                                        'before declaring one epoch finished '
                                        'and starting the next epoch. It should'
                                        ' typically be equal to ceil'
                                        '(num_samples / batch_size) Optional '
                                        'for Sequence: if unspecified, will '
                                        'use the len(generator) as a number of '
                                        'steps.'),
        (5475, 'en', 'Epochs', 'Number of epochs to train the model. An epoch '
                               'is an iteration over the entire data provided, '
                               'as defined by steps_per_epoch. Note that in '
                               'conjunction with initial_epoch, epochs is to '
                               'be understood as "final epoch". The model is '
                               'not trained for a number of iterations given '
                               'by epochs, but merely until the epoch of index '
                               'epochs is reached.'),
        (5476, 'en', 'Verbose', 'Integer. 0, 1, or 2. Verbosity mode. 0 = '
                                'silent, 1 = progress bar, 2 = one line per '
                                'epoch.'),
        (5477, 'en', 'Callbacks', 'A callback is a set of functions to be '
                                  'applied at given stages of the training '
                                  'procedure. You can use callbacks to get a '
                                  'view on internal states and statistics of '
                                  'the model during training. You can pass a '
                                  'list of callbacks (as the keyword argument '
                                  'callbacks) to the .fit() method of the '
                                  'Sequential or  Model classes. The relevant '
                                  'methods of the callbacks will then be '
                                  'called at each stage of the training.'),
        (5479, 'en', 'Validation steps', 'Only relevant if validation_data is a'
                                         ' generator. Total number of steps '
                                         '(batches of samples) to yield from '
                                         'validation_data generator before '
                                         'stopping at the end of every epoch. '
                                         'It should typically be equal to the '
                                         'number of samples of your validation '
                                         'dataset divided by the batch size. '
                                         'Optional for Sequence: if '
                                         'unspecified, will use the '
                                         'len(validation_data) as a number of '
                                         'steps.'),
        (5480, 'en', 'Validation freq', 'Only relevant if validation data is '
                                        'provided. Integer or collections. '
                                        'Container instance (e.g. list, tuple, '
                                        'etc.). If an integer, specifies how '
                                        'many training epochs to run before a '
                                        'new validation run is performed, e.g. '
                                        'validation_freq=2 runs validation '
                                        'every 2 epochs. If a Container, '
                                        'specifies the epochs on which to run '
                                        'validation, e.g. validation_freq=[1, '
                                        '2, 10] runs validation at the end of '
                                        'the 1st, 2nd, and 10th epochs.'),
        (5481, 'en', 'Class weight', 'Optional dictionary mapping class indices'
                                     ' (integers) to a weight (float) value, '
                                     'used for weighting the loss function '
                                     '(during training only). This can be '
                                     'useful to tell the model to "pay more '
                                     'attention" to samples from an under-'
                                     'represented class.'),
        (5482, 'en', 'Max queue size', 'Maximum size for the generator queue. '
                                       'If unspecified, max_queue_size will '
                                       'default to 10.'),
        (5483, 'en', 'Workers', 'Maximum number of processes to spin up when '
                                'using process-based threading. If unspecified,'
                                ' workers will default to 1. If 0, will execute'
                                ' the generator on the main thread.'),
        (5484, 'en', 'Use multiprocessing', 'If True, use process-based '
                                            'threading. If unspecified, '
                                            'use_multiprocessing will default '
                                            'to False. Note that because this '
                                            'implementation relies on '
                                            'multiprocessing, you should not '
                                            'pass non-picklable arguments to '
                                            'the generator as they can\'t be '
                                            'passed easily to children '
                                            'processes.'),
        (5485, 'en', 'Shuffle', 'Whether to shuffle the order of the batches at'
                                ' the beginning of each epoch. Only used with '
                                'instances of Sequence (keras.utils.Sequence). '
                                'Has no effect when steps_per_epoch is not '
                                'None.'),
        (5486, 'en', 'Initial epoch', 'Epoch at which to start training '
                                      '(useful for resuming a previous '
                                      'training run).'),

        (5487, 'en', 'Featurewise center', 'Set input mean to 0 over the '
                                           'dataset, feature-wise.'),
        (5488, 'en', 'Samplewise center', 'Set each sample mean to 0.'),
        (5489, 'en', 'Featurewise std normalization', 'Divide inputs by std of '
                                                      'the dataset, '
                                                      'feature-wise.'),
        (5490, 'en', 'Samplewise std normalization', 'Divide each input by its '
                                                     'std.'),
        (5491, 'en', 'ZCA epsilon', 'Epsilon for ZCA whitening. Default is '
                                    '1e-6.'),
        (5492, 'en', 'ZCA whitening', 'Apply ZCA whitening.'),
        (5493, 'en', 'Rotation range', 'Degree range for random rotations.'),
        (5494, 'en', 'Width shift range', 'Float, 1-D array-like or int float: '
                                          'fraction of total width, if < 1, or '
                                          'pixels if >= 1. 1-D array-like: '
                                          'random elements from the array. int:'
                                          ' integer number of pixels from '
                                          'interval (-width_shift_range, '
                                          '+width_shift_range) With '
                                          'width_shift_range=2 possible values'
                                          ' are integers [-1, 0, +1], same as '
                                          'with width_shift_range=[-1, 0, +1], '
                                          'while with width_shift_range=1.0 '
                                          'possible values are floats in the '
                                          'half-open interval [-1.0, +1.0[.'),
        (5495, 'en', 'Height shift range', 'Float, 1-D array-like or int float:'
                                           ' fraction of total height, if < 1, '
                                           'or pixels if >= 1. 1-D array-like: '
                                           'random elements from the array. '
                                           'int: integer number of pixels from '
                                           'interval (-height_shift_range, '
                                           '+height_shift_range) With '
                                           'height_shift_range=2 possible '
                                           'values are integers [-1, 0, +1], '
                                           'same as with height_shift_range='
                                           '[-1, 0, +1], while with '
                                           'height_shift_range=1.0 possible '
                                           'values are floats in the half-open '
                                           'interval [-1.0, +1.0[.'),
        (5496, 'en', 'Brightness range', 'Tuple or list of two floats. Range '
                                         'for picking a brightness shift value '
                                         'from.'),
        (5497, 'en', 'Shear range', 'Float. Shear Intensity (Shear angle in '
                                    'counter-clockwise direction in degrees)'),
        (5498, 'en', 'Zoom range', 'Float or [lower, upper]. Range for random '
                                   'zoom. If a float, [lower, upper] = '
                                   '[1-zoom_range, 1+zoom_range].'),
        (5499, 'en', 'Channel shift range', 'Float. Range for random channel '
                                            'shifts.'),
        (5500, 'en', 'Fill mode', 'One of {"constant", "nearest", "reflect" or'
                                  ' "wrap"}. Default is "nearest". Points '
                                  'outside the boundaries of the input are '
                                  'filled according to the given mode: '
                                  '"constant": kkkkkkkk|abcd|kkkkkkkk (cval=k) '
                                  '"nearest": aaaaaaaa|abcd|dddddddd "reflect":'
                                  ' abcddcba|abcd|dcbaabcd "wrap": '
                                  'abcdabcd|abcd|abcdabcd'),
        (5501, 'en', 'Cval', 'Float or Int. Value used for points outside the '
                             'boundaries when fill_mode = "constant".'),
        (5502, 'en', 'Horizontal flip', 'Randomly flip inputs horizontally.'),
        (5503, 'en', 'Vertical flip', 'Randomly flip inputs vertically.'),
        (5504, 'en', 'Rescale', 'Rescaling factor. Defaults to None. If None '
                                'or 0, no rescaling is applied, otherwise we '
                                'multiply the data by the value provided (after'
                                ' applying all other transformations).'),
        (5505, 'en', 'Preprocessing function', 'function that will be implied '
                                               'on each input. The function '
                                               'will run after the image is '
                                               'resized and augmented. The '
                                               'function should take one '
                                               'argument: one image (Numpy '
                                               'tensor with rank 3), and should'
                                               ' output a Numpy tensor with '
                                               'the same shape.'),
        (5506, 'en', 'Data format', 'Image data format, either "channels_first"'
                                    ' or "channels_last". "channels_last" mode'
                                    ' means that the images should have shape '
                                    '(samples, height, width, channels), '
                                    '"channels_first" mode means that the '
                                    'images should have shape  (samples, '
                                    'channels, height, width). It defaults to '
                                    'the image_data_format value found in your '
                                    'Keras config file at ~/.keras/keras.json. '
                                    'If you never set it, then it will be '
                                    '"channels_last".'),
        (5507, 'en', 'Validation split', 'Float. Fraction of images reserved '
                                         'for validation (strictly between 0 '
                                         'and 1).'),
        (5508, 'en', 'Dtype', 'Data type to use for the generated arrays.'),

        (5509, 'en', 'Train images', ''),
        (5510, 'en', 'Validation images', ''),
        (5511, 'en', 'Train texts', ''),
        (5512, 'en', 'Validation texts', ''),
        (5513, 'en', 'Train sequences', ''),
        (5514, 'en', 'Validation sequences', ''),

        (5515, 'en', 'Target size', 'Tuple of integers (height, width), '
                                    'default: (256, 256). The dimensions to '
                                    'which all images found will be resized.'),
        (5516, 'en', 'Color mode', 'One of "grayscale", "rgb", "rgba". '
                                   'Whether the images will be converted to '
                                   'have 1, 3, or 4 channels.'),
        # (5517, 'en', 'Class mode', 'One of "categorical", "binary", "sparse", '
        #                            '"input", or None. Default: "categorical". '
        #                            'Determines the type of label arrays that '
        #                            'are returned: "categorical" will be 2D '
        #                            'one-hot encoded labels, "binary" will be '
        #                            '1D binary labels, "sparse" will be 1D '
        #                            'integer labels, "input" will be images '
        #                            'identical to input images (mainly used to '
        #                            'work with autoencoders). If None, no '
        #                            'labels are returned (the generator will '
        #                            'only yield batches of image data, which '
        #                            'is useful to use with '
        #                            'model.predict_generator()). Please note '
        #                            'that in case of class_mode None, the '
        #                            'data still needs to reside in a '
        #                            'subdirectory of directory for it to work '
        #                            'correctly.'),
        (5518, 'en', 'Batch size', 'Size of the batches of data (default: 32).'),
        (5519, 'en', 'Shuffle', 'Whether to shuffle the data (default: True) '
                                'If set to False, sorts the data in '
                                'alphanumeric order.'),
        (5520, 'en', 'Seed', 'Optional random seed for shuffling and '
                             'transformations.'),
        (5521, 'en', 'Subset', 'Subset of data ("training" or "validation") if'
                               '  validation_split is set in '
                               'ImageDataGenerator.'),
        (5522, 'en', 'Interpolation', 'Interpolation method used to resample '
                                      'the image if the target size is '
                                      'different from that of the loaded image.'
                                      ' Supported methods are "nearest", '
                                      '"bilinear", and "bicubic". '),
        # Conv1D
        (5523, 'en', 'Trainable', 'Indicates whether the layer in the model is '
                                  'trainable.'),
        (5524, 'en', 'Input shape', '3D tensor with shape: (batch, steps, '
                                    'channels).'),

        # SeparableConv1D
        (5525, 'en', 'Input shape', '3D tensor with shape: (batch, channels, '
                                    'steps) if data_format is "channels_first" '
                                    'or 3D tensor with shape: (batch, steps, '
                                    'channels) if data_format is '
                                    '"channels_last".'),

        # SeparableConv2D
        (5526, 'en', 'Input shape', '4D tensor with shape: (batch, channels, '
                                    'rows, cols) if data_format is '
                                    '"channels_first" or 4D tensor with '
                                    'shape: (batch, rows, cols, channels) '
                                    'if data_format is "channels_last".'),

        # DepthwiseConv2D
        (5527, 'en', 'Input shape', '4D tensor with shape: (batch, channels, '
                                    'rows, cols) if data_format is '
                                    '"channels_first" or 4D tensor with '
                                    'shape: (batch, rows, cols, channels) '
                                    'if data_format is "channels_last".'),

        # Conv2DTranspose
        (5528, 'en', 'Input shape', '4D tensor with shape: (batch, channels, '
                                    'rows, cols) if data_format is '
                                    '"channels_first" or 4D tensor with '
                                    'shape: (batch, rows, cols, channels) '
                                    'if data_format is "channels_last".'),

        # Conv3D
        (5529, 'en', 'Input shape', '5D tensor with shape: (batch, channels, '
                                    'conv_dim1, conv_dim2, conv_dim3) if '
                                    'data_format is "channels_first" or 5D '
                                    'tensor with shape: (batch, conv_dim1, '
                                    'conv_dim2, conv_dim3, channels) if '
                                    'data_format is "channels_last".s) '
                                    'if data_format is "channels_last".'),

        # Conv3DTranspose
        (5530, 'en', 'Input shape', '5D tensor with shape: (batch, filters, '
                                     'new_depth, new_rows, new_cols) if '
                                     'data_format is "channels_first" or 5D '
                                     'tensor with shape: (batch, new_depth, '
                                     'new_rows, new_cols, filters) if '
                                     'data_format is "channels_last". depth '
                                     'and rows and cols values might have '
                                     'changed due to padding. If output_padding'
                                     ' is specified'),

        # Cropping1D
        (5531, 'en', 'Input shape', '3D tensor with shape (batch, axis_to_crop,'
                                    ' features)'),

        # Cropping2D
        (5532, 'en', 'Input shape', '4D tensor with shape: - If data_format is '
                                    '"channels_last":  (batch, rows, cols, '
                                    'channels) - If data_format is '
                                    '"channels_first": (batch, channels, rows, '
                                    'cols)'),

        # Cropping3D
        (5533, 'en', 'Input shape', '5D tensor with shape: - If data_format is '
                                    '"channels_last": (batch, '
                                    'first_axis_to_crop, second_axis_to_crop, '
                                    'third_axis_to_crop, depth) - If '
                                    'data_format is "channels_first": (batch, '
                                    'depth, first_axis_to_crop, '
                                    'second_axis_to_crop, third_axis_to_crop)'),

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id BETWEEN 5073 AND 5119'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 5073 AND 5119'),

    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id BETWEEN 5060 AND 5065'),
    (_insert_operation_category_translation,
     'DELETE FROM operation_category_translation WHERE id BETWEEN 5060 AND 5065'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id BETWEEN 5073 AND 5119'),

    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE operation_id BETWEEN 5073 AND 5119 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    (_insert_operation_port_interface,
     'DELETE FROM operation_port_interface WHERE id BETWEEN 22 AND 28'),
    (_insert_operation_port_interface_translation,
     'DELETE FROM operation_port_interface_translation WHERE id BETWEEN 22 AND 28'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE (id BETWEEN 5173 AND 5210) OR (id BETWEEN 5273 AND 5387) OR (id BETWEEN 5227 AND 5230) OR (id BETWEEN 5232 AND 5237)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE (operation_port_id BETWEEN 5173 AND 5210) OR (operation_port_id BETWEEN 5273 AND 5387) OR (operation_port_id BETWEEN 5227 AND 5230) OR (operation_port_id BETWEEN 5232 AND 5237)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE (id BETWEEN 5173 AND 5210) OR (id BETWEEN 5273 AND 5387) OR (id BETWEEN 5227 AND 5230) OR (id BETWEEN 5232 AND 5237)'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5143 AND 5160 OR id BETWEEN 5163 AND 5175 OR id BETWEEN 5221 AND 5240'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5221 AND 5533'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5143 AND 5160 OR id BETWEEN 5163 AND 5175 OR id BETWEEN 5221 AND 5240'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5221 AND 5533'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE (operation_id IN (5021, 5022, 5031, 5051) OR (operation_id BETWEEN 5073 AND 5119))'),

    ('UPDATE operation_port SET multiplicity = "MANY" WHERE type = "OUTPUT"',
     'UPDATE operation_port SET multiplicity = "ONE" WHERE type = "OUTPUT" AND id NOT BETWEEN 5092 AND 5100'),

    ('UPDATE operation_port SET multiplicity = "MANY" WHERE id = 5118',
     'UPDATE operation_port SET multiplicity = "ONE" WHERE id = 5118'),

    ('UPDATE operation_form_field SET type = "TEXT", suggested_widget = "text" WHERE id = 5100',
     'UPDATE operation_form_field SET type = "INTEGER", suggested_widget = "integer" WHERE id = 5100'),

    ('UPDATE operation_form_field SET type = "TEXT", suggested_widget = "text" WHERE id = 5137',
     'UPDATE operation_form_field SET type = "DECIMAL", suggested_widget = "decimal" WHERE id = 5137'),

    ('UPDATE operation SET enabled = 0, slug = "input-old" WHERE id = 5071',
     'UPDATE operation SET enabled = 1, slug = "input" WHERE id = 5071'),
    ('UPDATE operation SET enabled = 0, slug = "output-old" WHERE id = 5072',
     'UPDATE operation SET enabled = 1, slug = "output" WHERE id = 5072'),

    ('DELETE FROM platform_form WHERE operation_form_id IN (5161)',
     'INSERT INTO platform_form (`platform_id`, `operation_form_id`) VALUES (5, 5161)'),
    ('DELETE FROM platform_form WHERE operation_form_id IN (5162)',
     'INSERT INTO platform_form (`platform_id`, `operation_form_id`) VALUES (5, 5162)'),

    ("""UPDATE operation SET cssClass = 'circle-layout' WHERE id IN (SELECT operation_id FROM `operation_platform` WHERE platform_id = 5)""",
     ""),

    ("""UPDATE operation SET enabled = 0 WHERE id = 5091""",
     """UPDATE operation SET enabled = 1 WHERE id = 5091"""),

    ("""UPDATE operation_port_interface_operation_port SET operation_port_interface_id = 27 WHERE operation_port_id >= 5000 AND operation_port_interface_id = 1""",
     """UPDATE operation_port_interface_operation_port SET operation_port_interface_id = 1 WHERE operation_port_id >= 5000 AND operation_port_interface_id = 27"""),

    ("""UPDATE operation_port_translation SET name = 'input layer', description = 'Input layer' WHERE id IN (SELECT operation_port_id FROM `operation_port_interface_operation_port` WHERE operation_port_interface_id = 27 AND operation_port_id >= 5000) AND name = 'input data'""",
     """UPDATE operation_port_translation SET name = 'input data', description = 'Input data' WHERE id IN (SELECT operation_port_id FROM `operation_port_interface_operation_port` WHERE operation_port_interface_id = 1 AND operation_port_id >= 5000) AND name = 'input layer'"""),

    ("""UPDATE operation_port_translation SET name = 'output layer', description = 'Output layer' WHERE id IN (SELECT operation_port_id FROM `operation_port_interface_operation_port` WHERE operation_port_interface_id = 27 AND operation_port_id >= 5000) AND name = 'output data'""",
     """UPDATE operation_port_translation SET name = 'output data', description = 'Output data' WHERE id IN (SELECT operation_port_id FROM `operation_port_interface_operation_port` WHERE operation_port_interface_id = 1 AND operation_port_id >= 5000) AND name = 'output layer'"""),

    ("""UPDATE operation_port_translation SET description = 'Input layer' WHERE id IN (5236, 5237)""",
     """UPDATE operation_port_translation SET description = 'Input data' WHERE id IN (5236, 5237)"""),

    ("""UPDATE operation_port SET slug = 'input layer' WHERE slug = 'input data' AND id >= 5000""",
     """UPDATE operation_port SET slug = 'input data' WHERE slug = 'input layer' AND id >= 5000"""),

    ("""UPDATE operation_port SET slug = 'output layer' WHERE slug = 'output data' AND id >= 5000""",
     """UPDATE operation_port SET slug = 'output data' WHERE slug = 'output layer' AND id >= 5000"""),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if cmd[0]:
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
            if cmd[1]:
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
