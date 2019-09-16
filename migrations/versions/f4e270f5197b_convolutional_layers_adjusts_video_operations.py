# -*- coding: utf-8 -*-
"""Convolutional layers adjusts.

Revision ID: f4e270f5197b
Revises: 97a1b6042100
Create Date: 2019-07-10 17:35:36.658472

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
revision = 'f4e270f5197b'
down_revision = '97a1b6042100'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5

VIDEO_READER_OPERATION = 5120
VIDEO_GENERATOR_OPERATION = 5121
EVALUATE_MODEL_OPERATION = 5114

CONV3D_FORM = 5150
VIDEO_READER_FORM = 5242
VIDEO_GENERATOR_FORM = 5243
VIDEO_GENERATOR_TRANSFORMATION_FORM = 5244
BATCH_NORMALIZATION_FORM = 5160
APPEARANCE_FORM = 41

PREPROCESSING_CATEGORY = 5064
INPUT_OUTPUT_CATEGORY = 5065


def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('type', String),
        column('icon', Integer),
        column('css_class', Integer),)

    columns = ('id', 'slug', 'enabled', 'type', 'icon', 'css_class')
    data = [
        (VIDEO_READER_OPERATION, "video-reader", 1, 'ACTION', '', 'circle-layout'),
        (VIDEO_GENERATOR_OPERATION, "video-generator", 1, 'ACTION', '', 'circle-layout'),
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
        (VIDEO_READER_OPERATION, KERAS_PLATAFORM_ID),
        (VIDEO_GENERATOR_OPERATION, KERAS_PLATAFORM_ID),
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
        (VIDEO_READER_OPERATION, 'en', 'Video reader', 'Reads videos from a '
                                                       'data source.'),
        (VIDEO_GENERATOR_OPERATION, 'en', 'Video generator', 'Takes the dataset'
                                                             ' of videos and '
                                                             'generates batches'
                                                             ' of tensor video '
                                                             'data with real-'
                                                             'time data '
                                                             'augmentation.'),
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
        (INPUT_OUTPUT_CATEGORY, VIDEO_READER_OPERATION),
        (PREPROCESSING_CATEGORY, VIDEO_GENERATOR_OPERATION),
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
        (5388, 'OUTPUT', '', 3, 'MANY', VIDEO_READER_OPERATION, 'train-video'),
        (5389, 'OUTPUT', '', 2, 'MANY', VIDEO_READER_OPERATION, 'validation-video'),
        (5390, 'INPUT', '', 1, 'ONE', VIDEO_GENERATOR_OPERATION, 'video data'),
        (5391, 'OUTPUT', '', 1, 'ONE', VIDEO_GENERATOR_OPERATION, 'generator'),
        (5392, 'OUTPUT', '', 1, 'MANY', VIDEO_READER_OPERATION, 'test-video'),
        (5393, 'INPUT', '', 1, 'ONE', EVALUATE_MODEL_OPERATION, 'generator'),
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
        (29, '#05E8FA'),
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
        (29, 'en', 'VideoData'),
        (29, 'pt', 'VideoData'),
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
        (5388, 29),
        (5389, 29),

        (5390, 29),
        (5391, 23),

        (5392, 29),
        (5393, 23),
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
        (5388, 'en', 'train video data', 'Video Data'),
        (5389, 'en', 'validation video data', 'Video Data'),

        (5390, 'en', 'video data', 'Video Data'),
        (5391, 'en', 'generator', 'Generator'),

        (5392, 'en', 'test video data', 'Video Data'),
        (5393, 'en', 'test generator', 'Generator'),
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
        (VIDEO_READER_FORM, 1, 1, 'execution'),
        (VIDEO_GENERATOR_FORM, 1, 1, 'execution'),
        (VIDEO_GENERATOR_TRANSFORMATION_FORM, 1, 1, 'transformation'),
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
        (VIDEO_READER_FORM, 'en', 'Execution'),
        (VIDEO_READER_FORM, 'pt', 'Execução'),

        (VIDEO_GENERATOR_FORM, 'en', 'Execution'),
        (VIDEO_GENERATOR_FORM, 'pt', 'Execução'),
        (VIDEO_GENERATOR_TRANSFORMATION_FORM, 'en', 'Transformations'),
        (VIDEO_GENERATOR_TRANSFORMATION_FORM, 'pt', 'Transformações'),
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
        (VIDEO_READER_OPERATION, APPEARANCE_FORM),
        (VIDEO_READER_OPERATION, VIDEO_READER_FORM),

        (VIDEO_GENERATOR_OPERATION, APPEARANCE_FORM),
        (VIDEO_GENERATOR_OPERATION, VIDEO_GENERATOR_FORM),
        (VIDEO_GENERATOR_OPERATION, VIDEO_GENERATOR_TRANSFORMATION_FORM),
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
        column('form_id', Integer),
        column('enable_conditions', String)
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')

    LIMONERO_IMAGE = "`${LIMONERO_URL}/datasources?simple=true&list=" \
                     "true&enabled=1&formats=VIDEO_FOLDER`"

    enabled_condition_random = 'this.cropping_strategy.internalValue === ' \
                               '"random" && this.apply_transformations.' \
                               'internalValue === "1"'
    enabled_condition_center = 'this.cropping_strategy.internalValue === ' \
                               '"center" && this.apply_transformations.' \
                               'internalValue === "1"'
    enabled_condition_transformation = 'this.apply_transformations.' \
                                       'internalValue === "1"'

    data = [
        # Conv3D
        (5542, 'trainable', 'INTEGER', 0, 8, 0, 'checkbox', None, None,
         'EXECUTION', CONV3D_FORM, None),

        # video reader
        (5543, 'training_videos', 'INTEGER', 1, 1, None, 'lookup', LIMONERO_IMAGE,
         None, 'EXECUTION', VIDEO_READER_FORM, None),
        (5544, 'validation_videos', 'INTEGER', 0, 2, None, 'lookup',
         LIMONERO_IMAGE, None, 'EXECUTION', VIDEO_READER_FORM, None),

        # video generator
        (5545, 'dimensions', 'TEXT', 1, 1, None, 'text', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM, None),
        (5546, 'channels', 'INTEGER', 1, 2, 3, 'integer', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM, None),
        (5547, 'batch_size', 'INTEGER', 1, 3, 16, 'integer', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM, None),
        (5548, 'shuffle', 'INTEGER', 0, 8, 1, 'checkbox', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM, None),
        (5549, 'validation_split', 'DECIMAL', 0, 9, 0.0, 'decimal', None, None,
         'EXECUTION', VIDEO_GENERATOR_FORM, None),

        (5550, 'cropping_strategy', 'TEXT', 0, 3, None, 'dropdown', None,
         json.dumps([
             {"key": "random", "value": "random"},
             {"key": "center", "value": "center"}
         ]),
         'EXECUTION', VIDEO_GENERATOR_TRANSFORMATION_FORM,
         enabled_condition_transformation),

        # Random
        (5551, 'random_frames', 'TEXT', 0, 4, None, 'text', None, None,
         'EXECUTION', VIDEO_GENERATOR_TRANSFORMATION_FORM,
         enabled_condition_random),
        (5552, 'random_height', 'TEXT', 0, 4, '(0, 16)', 'text', None, None,
         'EXECUTION', VIDEO_GENERATOR_TRANSFORMATION_FORM,
         enabled_condition_random),
        (5553, 'random_width', 'TEXT', 0, 4, '(0, 59)', 'text', None, None,
         'EXECUTION', VIDEO_GENERATOR_TRANSFORMATION_FORM,
         enabled_condition_random),
        (5554, 'random_channel', 'TEXT', 0, 4, None, 'text', None, None,
         'EXECUTION', VIDEO_GENERATOR_TRANSFORMATION_FORM,
         enabled_condition_random),

        # Center
        (5555, 'frames', 'TEXT', 0, 4, None, 'text', None, None,
         'EXECUTION', VIDEO_GENERATOR_TRANSFORMATION_FORM,
         enabled_condition_center),
        (5556, 'height', 'TEXT', 0, 4, '[8:120]', 'text', None, None,
         'EXECUTION', VIDEO_GENERATOR_TRANSFORMATION_FORM,
         enabled_condition_center),
        (5557, 'width', 'TEXT', 0, 4, '[30:142]', 'text', None, None,
         'EXECUTION', VIDEO_GENERATOR_TRANSFORMATION_FORM,
         enabled_condition_center),
        (5558, 'channel', 'TEXT', 0, 4, None, 'text', None, None,
         'EXECUTION', VIDEO_GENERATOR_TRANSFORMATION_FORM,
         enabled_condition_center),

        (5559, 'apply_transformations', 'INTEGER', 0, 0, 0, 'checkbox', None,
         None, 'EXECUTION', VIDEO_GENERATOR_TRANSFORMATION_FORM, None),

        (5560, 'kwargs', 'TEXT', 0, 30, 'fused=False', 'text', None, None,
         'EXECUTION', BATCH_NORMALIZATION_FORM, None),

        # video reader
        (5561, 'test_videos', 'INTEGER', 0, 2, None, 'lookup',
         LIMONERO_IMAGE, None, 'EXECUTION', VIDEO_READER_FORM, None),

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
        # Conv3D
        (5542, 'en', 'Trainable', 'Indicates whether the layer in the model is trainable.'),

        # video reader
        (5543, 'en', 'Training videos', ''),
        (5544, 'en', 'Validation videos', ''),

        # video generator
        (5545, 'en', 'Dimensions', ''),
        (5546, 'en', 'Channels', ''),
        (5547, 'en', 'Batch size', 'Size of the batches of data (default: 16).'),
        (5548, 'en', 'Shuffle', 'Whether to shuffle the data (default: True) '
                                'If set to False, it will be processed in the '
                                'read order of the data set.'),
        (5549, 'en', 'Validation split', 'Float. Fraction of videos reserved '
                                         'for validation (strictly between 0 '
                                         'and 1).'),
        (5550, 'en', 'Cropping strategy', ''),

        # Random
        (5551, 'en', 'Frames', 'Number of frames to apply the cropping. '
                               'It is necessary to inform a interval containing '
                               'the range: initial and final value, for example'
                               ' [0: 1]. After this transformation the video '
                               'size will change. It is important to inform in '
                               'the various dimension fields the new dimension '
                               'after cropping. If this field is empty the '
                               'cropping transformation will be applied to all '
                               'channels.'),
        (5552, 'en', 'Random height', 'Height in number of pixels. '
                                      'It is necessary to inform a tuple '
                                      'containing the range: initial and final '
                                      'value for the random function, for '
                                      'example (0, 59). After this '
                                      'transformation the video size will '
                                      'change. It is important to inform in '
                                      'the various dimension fields the new '
                                      'dimension after cropping. If this field '
                                      'is empty the cropping transformation '
                                      'will be applied to all channels.'),
        (5553, 'en', 'Random width', 'It is necessary to inform a tuple '
                                     'containing the range: initial and final '
                                     'value for the random function, for '
                                     'example  (0, 59). After this '
                                     'transformation the video size  will '
                                     'change. It is important to inform in the '
                                     'various dimension fields the new '
                                     'dimension after  cropping. If this field '
                                     'is empty the cropping  transformation '
                                     'will be applied to all  channels.'),
        (5554, 'en', 'Channel', 'Number of channels to apply the crop. It is '
                                'necessary to inform a tuple containing the '
                                'range: initial and final value, for example '
                                '[0: 1]. After this transformation the video '
                                'size will change. It is important to inform '
                                'in the various dimension fields the new '
                                'dimension after cropping. If this field is '
                                'empty the cropping transformation will be '
                                'applied to all channels.'),

        # Center
        (5555, 'en', 'Frames', 'Number of frames to apply the cropping. '
                               'It is necessary to inform a interval containing '
                               'the range: initial and final value, for example'
                               ' [0: 1]. After this transformation the video '
                               'size will change. It is important to inform in '
                               'the various dimension fields the new dimension '
                               'after cropping. If this field is empty the '
                               'cropping transformation will be applied to all '
                               'channels.'),
        (5556, 'en', 'Height', 'Height in number of pixels. '
                               'It is necessary to inform a interval containing '
                               'the range: initial and final value, for example'
                               ' [0: 1]. After this transformation the video '
                               'size will change. It is important to inform in '
                               'the various dimension fields the new dimension '
                               'after cropping. If this field is empty the '
                               'cropping transformation will be applied to all '
                               'channels.'),
        (5557, 'en', 'Width', 'Width in number of pixels. '
                              'It is necessary to inform a interval containing '
                              'the range: initial and final value, for example '
                              '[0: 1]. After this transformation the video size'
                              ' will change. It is important to inform in the '
                              'various dimension fields the new dimension after'
                              ' cropping. If this field is empty the cropping '
                              'transformation will be applied to all '
                              'channels.'),
        (5558, 'en', 'Channel', 'Number of channels to apply the crop. It is '
                                'necessary to inform a interval containing the '
                                'range: initial and final value, for example '
                                '[0: 1]. After this transformation the video '
                                'size will change. It is important to inform '
                                'in the various dimension fields the new '
                                'dimension after cropping. If this field is '
                                'empty the cropping transformation will be '
                                'applied to all channels.'),

        (5559, 'en', 'Apply transformations', 'Turn on to apply transformations'
                                              ' to the video data set.'),

        (5560, 'en', 'Kwargs', 'Standard layer keyword arguments.'),

        # video reader
        (5561, 'en', 'Test videos', ''),

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id BETWEEN 5120 AND 5121'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 5120 AND 5121'),

    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id BETWEEN 5120 AND 5121'),

    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE operation_id BETWEEN 5120 AND 5121 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    (_insert_operation_port_interface,
     'DELETE FROM operation_port_interface WHERE id BETWEEN 29 AND 29'),
    (_insert_operation_port_interface_translation,
     'DELETE FROM operation_port_interface_translation WHERE id BETWEEN 29 AND 29'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 5388 AND 5393'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 5388 AND 5393'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 5388 AND 5393'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5242 AND 5244'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5542 AND 5561'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5242 AND 5244'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5542 AND 5561'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id BETWEEN 5120 AND 5121'),

    ("UPDATE operation SET `enabled`='0' WHERE `id`='5113'",
     "UPDATE operation SET `enabled`='1' WHERE `id`='5113'"),

    ("UPDATE operation_form SET `order`='1' WHERE `id`='5175'",
     "UPDATE operation_form SET `order`='5' WHERE `id`='5175'"),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if cmd[0]:
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
