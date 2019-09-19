# -*- coding: utf-8 -*-
"""Keras layers advanced parameters

Revision ID: 6aaa467a1b11
Revises: f4e270f5197b
Create Date: 2019-08-12 14:18:13.974533

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
revision = '6aaa467a1b11'
down_revision = 'f4e270f5197b'
branch_labels = None
depends_on = None

ENABLED_CONDITION = 'this.advanced_options.internalValue === "1"'

DENSE_FORM = 5100
DROPOUT_FORM = 5120
INPUT_FORM = 5175
LAMBDA_FORM = 5136
CONV2D_TRANSPOSE_FORM = 5149
CONV3D_TRANSPOSE_FORM = 5151
CONV1D = 5145
CONV2D = 5143
CONV3D = 5150
CROPPING1D = 5152
CROPPING2D = 5153
CROPPING3D = 5154
DEPTHWISE_CONV2D = 5148
SEPARABLE_CONV1D = 5146
SEPARABLE_CONV2D = 5147
AVERAGE_POOLING_1D = 5223
AVERAGE_POOLING_2D = 5224
AVERAGE_POOLING_3D = 5225
MAX_POOLING_1D = 5221
MAX_POOLING_2D = 5232
MAX_POOLING_3D = 5222
SIMPLE_RNN_FORM = 5201
LSTM_FORM = 5178
BATCH_NORMALIZATION_FORM = 5160
INCEPTIONV3_FORM = 5164
VGG16_FORM = 5163
ADD_FORM = 5167
SUBTRACT_FORM = 5168
MULTIPLY_FORM = 5169
AVERAGE_FORM = 5170
MAXIMUM_FORM = 5171
MINIMUM_FORM = 5172
CONCATENATE_FORM = 5173
DOT_FORM = 5174
UP_SAMPLING2D_FORM = 5156
UP_SAMPLING3D_FORM = 5157
ZERO_PADDING2D_FORM = 5144
ZERO_PADDING3D_FORM = 5159
GLOBAL_AVERAGE_POOLING1D_FORM = 5227
GLOBAL_AVERAGE_POOLING2D_FORM = 5229
GLOBAL_AVERAGE_POOLING3D_FORM = 5231

GLOBAL_MAX_POOLING1D_FORM = 5226
GLOBAL_MAX_POOLING2D_FORM = 5228
GLOBAL_MAX_POOLING3D_FORM = 5230
SPATIAL_DROPOUT2D_3D_FORM = 5142

FIT_GENERATOR_FORM = 5245

FORMS = (DENSE_FORM, DROPOUT_FORM, INPUT_FORM, LAMBDA_FORM,
         CONV2D_TRANSPOSE_FORM, CONV3D_TRANSPOSE_FORM,
         CONV1D, CONV2D, CONV3D, CROPPING1D, CROPPING2D, CROPPING3D,
         DEPTHWISE_CONV2D, SEPARABLE_CONV1D, SEPARABLE_CONV2D,
         AVERAGE_POOLING_1D, AVERAGE_POOLING_2D, AVERAGE_POOLING_3D,
         MAX_POOLING_1D, MAX_POOLING_2D, MAX_POOLING_3D,
         SIMPLE_RNN_FORM, LSTM_FORM, BATCH_NORMALIZATION_FORM,
         ADD_FORM, SUBTRACT_FORM, MULTIPLY_FORM, AVERAGE_FORM, MAXIMUM_FORM,
         MINIMUM_FORM, CONCATENATE_FORM, DOT_FORM, UP_SAMPLING2D_FORM,
         UP_SAMPLING3D_FORM, ZERO_PADDING2D_FORM, ZERO_PADDING3D_FORM,
         GLOBAL_AVERAGE_POOLING1D_FORM, GLOBAL_AVERAGE_POOLING2D_FORM,
         GLOBAL_AVERAGE_POOLING3D_FORM, GLOBAL_MAX_POOLING1D_FORM,
         GLOBAL_MAX_POOLING2D_FORM, GLOBAL_MAX_POOLING3D_FORM,
         SPATIAL_DROPOUT2D_3D_FORM, FIT_GENERATOR_FORM)


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

    data = [(5562, 'data_format', 'TEXT', 0, 1, None, 'dropdown', None,
             json.dumps([
                     {'key': 'channels_last', 'value': 'channels_last'},
                     {'key': 'channels_first', 'value': 'channels_first'},
                 ]), 'EXECUTION', SPATIAL_DROPOUT2D_3D_FORM, ENABLED_CONDITION),
            ]

    i = 5562
    for form in FORMS:
        i += 1
        data.append((i, 'advanced_options', 'INTEGER', 0, 0, 0, 'checkbox',
                     None, None, 'EXECUTION', form, None),)

    data.append((i+1, 'advanced_options', 'INTEGER', 0, 0, 0, 'checkbox',
                 None, None, 'EXECUTION', INCEPTIONV3_FORM, None),)
    data.append((i+2, 'advanced_options', 'INTEGER', 0, 0, 0, 'checkbox',
                 None, None, 'EXECUTION', VGG16_FORM, None),)

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
    data = [(5562, 'en', 'Data format', """'channels_first' or 'channels_last'. 
    In 'channels_first' mode, the channels dimension (the depth) is at index 1, 
    in 'channels_last' mode is it at index 3. It defaults to the 
    image_data_format value found in your Keras config file at 
    ~/.keras/keras.json. If you never set it, then it will be 
    'channels_last'.""")]
    for i in range(5563, (5563+len(FORMS))):
        data.append((i, 'en', 'Advanced options',
                     'Enable advanced options.'))
        data.append((i, 'pt', 'Opções avançadas',
                     'Habilita as opções avançadas.')),

    data.append((i+1, 'en', 'Advanced options',
                 'Enable advanced options.'))
    data.append((i+1, 'pt', 'Opções avançadas',
                 'Habilita as opções avançadas.')),
    data.append((i+2, 'en', 'Advanced options',
                 'Enable advanced options.'))
    data.append((i+2, 'pt', 'Opções avançadas',
                 'Habilita as opções avançadas.')),

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field 
        SET `form_id`=5100 
        WHERE `id` BETWEEN 5100 AND 5109""",
     ""),
    ("""DELETE 
        FROM operation_operation_form 
        WHERE operation_form_id BETWEEN 5101 AND 5109""",
     ""),

    ("""UPDATE operation_form_field 
        SET `form_id`=5120 
        WHERE `id` BETWEEN 5120 AND 5122""",
     ""),
    ("""DELETE 
        FROM operation_operation_form 
        WHERE operation_form_id BETWEEN 5121 AND 5122""",
     ""),

    ("""UPDATE operation_form_field 
        SET `form_id`=5136 
        WHERE `id` IN (5136, 5137, 5138, 5418)""",
     ""),
    ("""DELETE 
        FROM operation_operation_form 
        WHERE operation_form_id BETWEEN 5137 AND 5138""",
     ""),

    ("""UPDATE operation_translation 
        SET `name`='Conv2DTranspose' 
        WHERE `id` = 5077""",
     ""),

    ("""UPDATE operation_form_field 
        SET `form_id`=5201 
        WHERE `id` BETWEEN 5201 AND 5220""",
     ""),
    ("""DELETE 
        FROM operation_operation_form 
        WHERE operation_form_id BETWEEN 5202 AND 5220""",
     ""),

    ("""UPDATE operation_form_field 
        SET `form_id`=5178 
        WHERE `id` BETWEEN 5178 AND 5200""",
     ""),
    ("""DELETE 
        FROM operation_operation_form 
        WHERE operation_form_id BETWEEN 5179 AND 5200""",
     ""),

    ("""UPDATE operation_form_field AS A
        INNER JOIN operation_form_field_translation AS B ON A.id = B.id
        SET A.required = 0
        WHERE 
            B.label = "Kernel size" 
            AND A.required = 1 AND 
            A.id > 5000 AND 
            A.id < 6000""",
     """UPDATE operation_form_field AS A
        INNER JOIN operation_form_field_translation AS B ON A.id = B.id
        SET A.required = 1
        WHERE 
            B.label = "Kernel size" AND 
            A.required = 0 AND 
            A.id > 5000 AND 
            A.id < 6000"""),

    ("""UPDATE operation_form_field AS A
        INNER JOIN operation_form_field_translation AS B ON A.id = B.id
        SET A.required = 0
        WHERE 
            B.label = "Strides" AND 
            A.required = 1 AND 
            A.id > 5000 AND 
            A.id < 6000""",
     """UPDATE operation_form_field AS A
        INNER JOIN operation_form_field_translation AS B ON A.id = B.id
        SET A.required = 1
        WHERE 
            B.label = "Strides" AND 
            A.required = 0 AND 
            A.id > 5000 AND 
            A.id < 6000"""),

    ("""UPDATE operation_form_field AS A
        INNER JOIN operation_form_field_translation AS B ON A.id = B.id
        SET A.required = 0
        WHERE 
            B.label = "Activation" AND 
            A.required = 1 AND 
            A.id > 5000 AND 
            A.id < 6000""",
     """UPDATE operation_form_field AS A
        INNER JOIN operation_form_field_translation AS B ON A.id = B.id
        SET A.required = 1
        WHERE 
            B.label = "Activation" AND 
            A.required = 0 AND 
            A.id > 5000 AND 
            A.id < 6000"""),

    ("""UPDATE operation_form_field 
        SET `required`=1 
        WHERE `id` IN (5419, 5291, 5253, 5237, 5222, 5322)""",
     ""),

    ("""UPDATE operation_form_field 
        SET `suggested_widget`='text', `required`=1
        WHERE `id` = 5251""",
     ""),

    ("""UPDATE operation_form_field 
        SET `DEFAULT`=2, `type`='INTEGER', `suggested_widget`='integer'
        WHERE `id` = 5438""",
     ""),

    ('''UPDATE operation_form_field
        SET enable_conditions = '{enabled_condition}'
        WHERE 
            form_id IN {forms} AND 
            required = 0 AND 
            `name` NOT IN ("advanced_options")'''.format(
                                    enabled_condition=ENABLED_CONDITION,
                                    forms=FORMS),
     '''UPDATE operation_form_field
        SET enable_conditions = NULL
        WHERE 
            form_id IN {forms} AND 
            required = 0 AND 
            `name` NOT IN ("advanced_options")'''.format(forms=FORMS)),

    ('''UPDATE operation_form_field
        SET enable_conditions = '{enabled_condition}'
        WHERE 
            id NOT IN (5386, 5387, 5392) AND form_id = 5164'''.format(
                                    enabled_condition=ENABLED_CONDITION),
     '''UPDATE operation_form_field
        SET enable_conditions = NULL
        WHERE 
            ID NOT IN (5386, 5387, 5392) AND form_id = 5164'''),

    ('''UPDATE operation_form_field
        SET enable_conditions = '{enabled_condition}'
        WHERE 
            ID NOT IN (5379, 5380, 5385) AND form_id = 5163'''.format(
        enabled_condition=ENABLED_CONDITION),
     '''UPDATE operation_form_field
        SET enable_conditions = NULL
        WHERE 
            ID NOT IN (5379, 5380, 5385) AND form_id = 5163'''),

    ("""UPDATE operation_form_field 
        SET `name`='size_up_sampling'
        WHERE `name`='size' AND `id` > 5000 AND `id` < 6000""",
     ""),

    ("""UPDATE operation_form_field 
        SET `required`=0, `default`='nearest'
        WHERE id=5360""",
     ""),

    (_insert_operation_form_field,
     'DELETE '
     'FROM operation_form_field '
     'WHERE id BETWEEN 5562 AND 5700'),
    (_insert_operation_form_field_translation,
     'DELETE '
     'FROM operation_form_field_translation '
     'WHERE id BETWEEN 5562 AND 5700'),

    ("""UPDATE operation 
        SET `enabled`=0
        WHERE id IN (5045, 5048, 5044, 5047, 5043, 5046)""",
     """UPDATE operation
        SET `enabled`=1
        WHERE id IN (5045, 5048, 5044, 5047, 5043, 5046)"""),

    ("""UPDATE operation
        SET `slug`='convolution-3d'
        WHERE id = 5078""",
     """UPDATE operation 
        SET `slug`='conv-3d'
        WHERE id = 5078"""),
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


