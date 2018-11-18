# -*- coding: utf-8 -*-
"""Add keras plataform

Revision ID: 86dd15ad5169
Revises: 5430536464c7
Create Date: 2018-10-01 15:41:55.368398

"""

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '86dd15ad5169'
down_revision = '5430536464c7'
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
    rows = [dict(zip(columns, row)) for row in data]

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
    rows = [dict(zip(columns, row)) for row in data]
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
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category():
    tb = table(
        'operation_category',
        column('id', Integer),
        column('type', String))

    columns = ('id', 'type')
    data = [
        (5010, "group"),
            (5011, "subgroup"),
            (5012, "subgroup"),
            (5013, "subgroup"),
        (5020, "group"),
            (5021, "subgroup"),
            (5022, "subgroup"),
        (5030, "group"),
            (5031, "subgroup"),
        (5040, "group"),
            (5041, "subgroup"),
            (5042, "subgroup"),
        (5050, "group"),
            (5051, "subgroup"),
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
        (5010, "en", 'Core Layers'),
        (5020, "en", 'Convolutional Layers'),
        (5030, "en", 'Pooling Layers'),
        (5040, "en", 'Recurrent Layers'),
        (5050, "en", 'Normalization Layers'),
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
        (5011, "en", 'Dense', ''),
        (5012, "en", 'Dropout', ''),
        (5013, "en", 'Flatten', ''),
        (5021, "en", 'Convolution2D', ''),
        (5022, "en", 'ZeroPadding2D', ''),
        (5031, "en", 'MaxPooling2D', ''),
        (5041, "en", 'LSTM', ''),
        (5042, "en", 'SimpleRNN', ''),
        (5051, "en", 'BatchNormalization', ''),
    ]
    rows = [dict(zip(columns, row)) for row in data]

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

