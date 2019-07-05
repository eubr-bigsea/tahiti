# -*- coding: utf-8 -*-
"""Add keras plataform

Revision ID: 86dd15ad5169
Revises: 8035ec45650b
Create Date: 2018-10-01 15:41:55.368398

"""

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '86dd15ad5169'
down_revision = '8035ec45650b'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5


def _insert_platform():
    tb = table(
        'platform',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('icon', String), )

    columns = ('id', 'slug', 'enabled', 'icon')
    data = [
        (KERAS_PLATAFORM_ID, 'keras', 1, ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_platform_translation():
    tb = table(
        'platform_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (KERAS_PLATAFORM_ID, 'en',
         'Keras', 'Keras is a high-level neural networks API, written in Python and capable of '
                  'running on top of TensorFlow, CNTK, or Theano.'),
        (KERAS_PLATAFORM_ID, 'pt', 'Keras', 'Keras é uma API de mais alto nível para redes neurais, escrita em Python '
                                            'capaz de executar sobre o TensorFlow, CNTK ou Theano.'),
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
        (5011, KERAS_PLATAFORM_ID),
        (5012, KERAS_PLATAFORM_ID),
        (5013, KERAS_PLATAFORM_ID),
        (5021, KERAS_PLATAFORM_ID),
        (5022, KERAS_PLATAFORM_ID),
        (5031, KERAS_PLATAFORM_ID),
        (5041, KERAS_PLATAFORM_ID),
        (5042, KERAS_PLATAFORM_ID),
        (5051, KERAS_PLATAFORM_ID),

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
        (5011, "dense", 1, 'ACTION', ''),
        (5012, "dropout", 1, 'ACTION', ''),
        (5013, "flatten", 1, 'ACTION', ''),
        (5021, "convolution-2d", 1, 'ACTION', ''),
        (5022, "zero-padding-2d", 1, 'ACTION', ''),
        (5031, "max-pooling-2d", 1, 'ACTION', ''),
        (5041, "lstm", 1, 'ACTION', ''),
        (5042, "simple-rnn", 1, 'ACTION', ''),
        (5051, "batch-normalization", 1, 'ACTION', ''),
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
        (5010, "group", 1, 1),
            (5011, "subgroup", 1, 1),
            (5012, "subgroup", 2, 2),
            (5013, "subgroup", 3, 3),
        (5020, "group", 2, 2),
            (5021, "subgroup", 1, 1),
            (5022, "subgroup", 2, 2),
        (5030, "group", 3, 3),
            (5031, "subgroup", 1, 1),
        (5040, "group", 4, 4),
            (5041, "subgroup", 1, 1),
            (5042, "subgroup", 2, 2),
        (5050, "group", 5, 5),
            (5051, "subgroup", 1, 1),
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
         (5010, 5011),
         (5010, 5012),
         (5010, 5013),
         #Convolutional Layers
         (5020, 5021),
         (5020, 5022),
         #Pooling Layers
         (5030, 5031),
         #Recurrent Layers
         (5040, 5041),
         (5040, 5042),
         #Normalization Layers
         (5050, 5051),
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
        (5010, "en", 'Core Layers'),
        (5020, "en", 'Convolutional Layers'),
        (5030, "en", 'Pooling Layers'),
        (5040, "en", 'Recurrent Layers'),
        (5050, "en", 'Normalization Layers'),
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
        (5011, "en", 'Dense', 'Just your regular densely-connected NN layer.'),
        (5012, "en", 'Dropout', 'Applies Dropout to the input. '
                                'Dropout consists in randomly setting a fraction '
                                'rate of input units to 0 at each update during '
                                'training time, which helps prevent overfitting.'),
        (5013, "en", 'Flatten', 'Flattens the input. Does not affect the batch size.'),
        (5021, "en", 'Convolution2D', '2D convolution layer (e.g. spatial convolution over images). '
                                      'This layer creates a convolution kernel that is convolved with '
                                      'the layer input to produce a tensor of outputs. If use_bias is '
                                      'True, a bias vector is created and added to the outputs. Finally, '
                                      'if activation is not None, it is applied to the outputs as well. '
                                      'When using this layer as the first layer in a model, provide the '
                                      'keyword argument input_shape (tuple of integers, does not include '
                                      'the batch axis), e.g. input_shape=(128, 128, 3) for 128x128 RGB '
                                      'pictures in data_format="channels_last".'),
        (5022, "en", 'ZeroPadding2D', 'Zero-padding layer for 2D input (e.g. picture). This layer can '
                                      'add rows and columns of zeros at the top, bottom, '
                                      'left and right side of an image tensor.'),
        (5031, "en", 'MaxPooling2D', 'Max pooling operation for spatial data.'),
        (5041, "en", 'LSTM', 'Long Short-Term Memory layer - Hochreiter 1997.'),
        (5042, "en", 'SimpleRNN', 'Fully-connected RNN where the output is to be fed back to input.'),
        (5051, "en", 'BatchNormalization', 'Batch normalization layer (Ioffe and Szegedy, 2014). '
                                           'Normalize the activations of the previous layer at each '
                                           'batch, i.e. applies a transformation that maintains the '
                                           'mean activation close to 0 and the activation '
                                           'standard deviation close to 1.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_platform,
        'DELETE FROM platform WHERE id = {}'.format(KERAS_PLATAFORM_ID)),
    (_insert_platform_translation,
        'DELETE FROM platform_translation WHERE id = {}'.format(KERAS_PLATAFORM_ID)),
    (_insert_operation,
        'DELETE FROM operation WHERE id BETWEEN 5001 AND 5100'),
    (_insert_operation_category,
        'DELETE FROM operation_category WHERE id BETWEEN 5010 AND 5051'),
    (_insert_operation_translation,
        'DELETE FROM operation_translation WHERE id BETWEEN 5011 AND 5051'),
    (_insert_operation_category_operation,
        'DELETE FROM operation_category_operation WHERE operation_id BETWEEN 5011 AND 5051'),
    (_insert_operation_category_translation,
        'DELETE FROM operation_category_translation WHERE id BETWEEN 5001 AND 5100'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id BETWEEN 5001 AND 5100 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),
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
        connection.execute('SET foreign_key_checks = 0;')
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
        connection.execute('SET foreign_key_checks = 1;')
    except:
        session.rollback()
        raise
    session.commit()

