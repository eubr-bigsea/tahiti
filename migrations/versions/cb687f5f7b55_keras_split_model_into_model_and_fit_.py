"""Keras: split model into model and fit generator.

Revision ID: cb687f5f7b55
Revises: 6aaa467a1b11
Create Date: 2019-08-26 09:34:10.526754

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
revision = 'cb687f5f7b55'
down_revision = '6aaa467a1b11'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5
FIT_GENERATOR = 5122
MODEL_CATEGORY = 5063
FIT_MODEL_INPUT_PORT = 5394
MODEL_PORT_INTERFACE = 22
FIT_EXECUTION_FORM = 5245
MODEL_EXECUTION_FORM = 5233
FIT_APPEARANCE_FORM = 41
FIT_VERBOSE_FIELD = 5476
FIT_CALLBACKS_FIELD = 5477
SEED_FIELD = 5520
IMAGE_GENERATOR_FORM = 5237
SUBSET_FIELD = 5521


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
        (FIT_GENERATOR, "fit-generator", 1, 'ACTION', '', 'circle-layout'),
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
        (FIT_GENERATOR, 'en', 'Fit generator',
                                     'Trains the model on data generated batch-'
                                     'by-batch by a Python generator (or an '
                                     'instance of Sequence). The generator is '
                                     'run in parallel to the model, for '
                                     'efficiency. For instance, this allows you'
                                     ' to do real-time data augmentation on '
                                     'images on CPU in parallel to training '
                                     'your model on GPU.'),
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
        (FIT_GENERATOR, KERAS_PLATAFORM_ID),
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
        # Fit
        (MODEL_CATEGORY, FIT_GENERATOR),
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

    columns = ('id', 'type', 'tags', 'order', 'multiplicity',
               'operation_id', 'slug')
    data = [
        (FIT_MODEL_INPUT_PORT, 'INPUT', '', 1, 'ONE', 5122, 'model'),

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
        (FIT_MODEL_INPUT_PORT, MODEL_PORT_INTERFACE),
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
        (FIT_MODEL_INPUT_PORT, 'en', 'model', 'Model'),
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
        (FIT_EXECUTION_FORM, 1, 1, 'execution'),
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
        (FIT_EXECUTION_FORM, 'en', 'Execution'),
        (FIT_EXECUTION_FORM, 'pt', 'Execução'),
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
        (FIT_GENERATOR, FIT_APPEARANCE_FORM),
        (FIT_GENERATOR, FIT_EXECUTION_FORM),
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
        (FIT_VERBOSE_FIELD, 'verbose', 'TEXT', 0, 12, 1, 'dropdown', None,
         json.dumps([
             {"key": 0, "value": "silent"},
             {"key": 1, "value": "progress bar"},
             {"key": 2, "value": "one line per epoch"},
         ]), 'EXECUTION', MODEL_EXECUTION_FORM),
        (FIT_CALLBACKS_FIELD, 'callbacks', 'TEXT', 0, 13, "TensorBoard", 'select2', None,
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
         ]), 'EXECUTION', MODEL_EXECUTION_FORM),
        (SEED_FIELD, 'seed', 'INTEGER', 0, 28, None, 'integer', None, None,
         'EXECUTION', IMAGE_GENERATOR_FORM),
        (SUBSET_FIELD, 'subset', 'TEXT', 0, 29, None, 'dropdown', None,
         json.dumps([
             {"key": "training", "value": "training"},
             {"key": "validation", "value": "validation"},
         ]), 'EXECUTION', IMAGE_GENERATOR_FORM),
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
        (FIT_VERBOSE_FIELD, 'en', 'Verbose', 'Integer. 0, 1, or 2. Verbosity '
                                             'mode. 0 = silent, 1 = progress '
                                             'bar, 2 = one line per epoch.'),
        (FIT_CALLBACKS_FIELD, 'en', 'Callbacks',
                                  'A callback is a set of functions to be '
                                  'applied at given stages of the training '
                                  'procedure. You can use callbacks to get a '
                                  'view on internal states and statistics of '
                                  'the model during training. You can pass a '
                                  'list of callbacks (as the keyword argument '
                                  'callbacks) to the .fit() method of the '
                                  'Sequential or  Model classes. The relevant '
                                  'methods of the callbacks will then be '
                                  'called at each stage of the training.'),
        (SEED_FIELD, 'en', 'Seed', 'Optional random seed for shuffling and '
                                   'transformations.'),
        (SUBSET_FIELD, 'en', 'Subset', 'Subset of data ("training" or '
                                       '"validation") if validation_split is '
                                       'set in ImageDataGenerator.'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id BETWEEN '
     '5122 AND 5122'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 5122 AND 5122'),
    (_insert_operation,
     'DELETE FROM operation WHERE id BETWEEN 5122 AND 5122'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE operation_id BETWEEN 5122 AND 5122 AND platform_id = {}'.format(
         KERAS_PLATAFORM_ID)),
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 5394 AND 5394'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id BETWEEN 5394 AND 5394'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 5394 AND 5394'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5245 AND 5245'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5245 AND 5245'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 5122'),

    ('UPDATE operation_port SET operation_id = 5122 WHERE id IN (5229, 5235)',
     'UPDATE operation_port SET operation_id = 5112 WHERE id IN (5229, 5235)'),

    ("""UPDATE operation_form_field 
        SET `default` = "TensorBoard" 
        WHERE id = 5477""",
     ''),

    ('UPDATE operation_form_field '
     'SET form_id = 5245 '
     'WHERE id IN ('
        '5474, 5475, 5476, 5477, 5479, 5480, '
        '5481, 5482, 5483, 5484, 5485, 5486, 5541)',
     'UPDATE operation_form_field '
     'SET form_id = 5233 '
     'WHERE id IN ('
        '5474, 5475, 5476, 5477, 5479, 5480, '
        '5481, 5482, 5483, 5484, 5485, 5486, 5541)'),

    ("""UPDATE operation_operation_form 
        SET operation_id = 5122 
        WHERE operation_form_id = 5241""",
     """UPDATE operation_operation_form 
        SET operation_id = 5112 
        WHERE operation_form_id = 5241"""),

    ("""UPDATE operation_form_field 
        SET `default` = "(1, 1, 1)" 
        WHERE id IN (5323, 5326)""",
     """UPDATE operation_form_field 
        SET `default` = "(1, 1)" 
        WHERE id IN (5323, 5326)"""),

    ("""UPDATE operation_form_field 
        SET `name` = "video_frames" 
        WHERE id = 5555""",
     """UPDATE operation_form_field 
        SET `name` = "frames" 
        WHERE id = 5555"""),

    ("""UPDATE operation_form_field 
        SET `name` = "video_height" 
        WHERE id = 5556""",
     """UPDATE operation_form_field 
        SET `name` = "height" 
        WHERE id = 5556"""),

    ("""UPDATE operation_form_field 
        SET `name` = "video_width" 
        WHERE id = 5557""",
     """UPDATE operation_form_field 
        SET `name` = "width" 
        WHERE id = 5557"""),

    ("""UPDATE operation_form_field 
        SET `name` = "video_channel" 
        WHERE id = 5558""",
     """UPDATE operation_form_field 
        SET `name` = "channel" 
        WHERE id = 5558"""),

    ("DELETE "
     "FROM operation_form_field "
     "WHERE id IN (5476, 5477, 5520, 5521)",
     _insert_operation_form_field),
    ("DELETE "
     "FROM operation_form_field_translation "
     "WHERE id IN (5476, 5477, 5520, 5521)",
     _insert_operation_form_field_translation),
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
