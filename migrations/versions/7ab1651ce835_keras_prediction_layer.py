"""Keras - prediction layer

Revision ID: 7ab1651ce835
Revises: f98150821301
Create Date: 2019-10-03 15:51:03.476889

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
revision = '7ab1651ce835'
down_revision = 'f98150821301'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5

PREDICTION_LAYER = 5123
FIT_GENERATOR = 5122
LOAD = 5115
MODEL_FORM_ID = 5233
SEQUENCE_GENERATOR = 5124
SEQUENCE_READER = 5119
SEQUENCE_GENERATOR_FORM_ID = 5247


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
        (PREDICTION_LAYER, "predict", 1, 'ACTION', '', 'circle-layout'),
        (SEQUENCE_GENERATOR, "sequence-generator", 1, 'ACTION', '',
            'circle-layout'),
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
        (PREDICTION_LAYER, KERAS_PLATAFORM_ID),
        (SEQUENCE_GENERATOR, KERAS_PLATAFORM_ID),
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
        (PREDICTION_LAYER, 'en', 'Predict', 'Generates predictions for the '
                                            'input samples from a data '
                                            'generator.'),
        (SEQUENCE_GENERATOR, 'en', 'Sequence generator', 'Takes any type of '
                                                         'data and generates '
                                                         'batches of tensor '
                                                         'data.'),
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
        (5063, PREDICTION_LAYER),
        (5064, SEQUENCE_GENERATOR),
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
        (5397, 'INPUT', '', 3, 'ONE', PREDICTION_LAYER, 'model'),
        (5398, 'INPUT', '', 2, 'ONE', PREDICTION_LAYER, 'generator'),
        (5399, 'OUTPUT', '', 1, 'MANY', FIT_GENERATOR, 'model'),
        (5400, 'INPUT', '', 1, 'ONE', PREDICTION_LAYER, 'examples'),
        (5401, 'OUTPUT', '', 1, 'MANY', LOAD, 'python code'),
        (5402, 'INPUT', '', 1, 'MANY', LOAD, 'python code'),

        (5403, 'INPUT', '', 1, 'ONE', SEQUENCE_GENERATOR, 'sequence data'),
        (5404, 'OUTPUT', '', 1, 'MANY', SEQUENCE_GENERATOR, 'generator'),

        (5405, 'OUTPUT', '', 1, 'ONE', SEQUENCE_READER, 'test-sequence'),
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
        (5397, 22),
        (5398, 23),
        (5399, 22),
        (5400, 24),
        (5400, 29),
        (5401, 28),
        (5402, 28),
        (5403, 26),
        (5404, 23),
        (5405, 26),
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
        (5397, 'en', 'model', 'Model'),
        (5398, 'en', 'generator', 'Generator'),
        (5399, 'en', 'model', 'Model'),
        (5400, 'en', 'image data', 'Examples to classify'),
        (5401, 'en', 'python code', 'Python code'),
        (5402, 'en', 'python code', 'Python code'),
        (5403, 'en', 'sequence data', 'Sequence data'),
        (5404, 'en', 'generator', 'Generator'),
        (5405, 'en', 'test sequence data', 'Sequence data'),
    ]

    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (SEQUENCE_GENERATOR_FORM_ID, 'en', 'Execution'),
        (SEQUENCE_GENERATOR_FORM_ID, 'pt', 'Execução'),
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
        (SEQUENCE_GENERATOR_FORM_ID, 1, 1, 'execution'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(operation_form_table, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        (PREDICTION_LAYER, 41),
        (SEQUENCE_GENERATOR, 41),
        (SEQUENCE_GENERATOR, SEQUENCE_GENERATOR_FORM_ID),
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

    empty_optimizer = 'this.optimizer.internalValue'

    advanced_optimizer = 'this.advanced_optimizer.internalValue === "1"'

    optimizer_condition_sgd = 'this.optimizer.internalValue === "sgd" && ' \
                              'this.advanced_optimizer.internalValue === "1"'

    optimizer_condition_rmsprop = 'this.optimizer.internalValue === "rmsprop"' \
                                  ' && this.advanced_optimizer.internalValue ' \
                                  '=== "1"'

    optimizer_condition_adagrad = 'this.optimizer.internalValue === "adagrad"' \
                                  ' && this.advanced_optimizer.' \
                                  'internalValue === "1"'

    optimizer_condition_adadelta = 'this.optimizer.internalValue === "ada' \
                                   'delta" && this.advanced_optimizer.' \
                                   'internalValue === "1"'

    optimizer_condition_adam = 'this.optimizer.internalValue === "adam" && ' \
                               'this.advanced_optimizer.internalValue === "1"'

    optimizer_condition_adamax = 'this.optimizer.internalValue === "adamax" ' \
                                 '&& this.advanced_optimizer.internalValue' \
                                 ' === "1"'

    optimizer_condition_nadam = 'this.optimizer.internalValue === "nadam" && ' \
                                 'this.advanced_optimizer.internalValue === "1"'

    LIMONERO_IMAGE = "`${LIMONERO_URL}/datasources?simple=true&list=true&" \
                     "enabled=1&formats=IMAGE_FOLDER,SEQUENCE_FOLDER," \
                     "VIDEO_FOLDER`"

    data = [
        # Model
        (5612, 'advanced_optimizer', 'INTEGER', 0, 2, 0, 'checkbox', None, None,
         'EXECUTION', MODEL_FORM_ID, empty_optimizer),

        # All optimizers
        (5613, 'clipnorm', 'DECIMAL', 0, 4, 1.0, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, advanced_optimizer),
        (5614, 'clipvalue', 'DECIMAL', 0, 5, 0.5, 'decimal', None, None,
        'EXECUTION', MODEL_FORM_ID, advanced_optimizer),

        # SGD optimizer
        (5615, 'learning_rate_sgd', 'DECIMAL', 0, 3, 0.01, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_sgd),
        (5616, 'decay_sgd', 'DECIMAL', 0, 6, 1e-6, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_sgd),
        (5617, 'momentum_sgd', 'DECIMAL', 0, 7, 0.9, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_sgd),
        (5618, 'nesterov_sgd', 'INTEGER', 0, 8, 1, 'checkbox', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_sgd),

        # RMSprop optimizer
        (5619, 'learning_rate_rmsprop', 'DECIMAL', 0, 3, 0.001, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_rmsprop),
        (5620, 'rho_rmsprop', 'DECIMAL', 0, 6, 0.9, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_rmsprop),

        # Adagrad
        (5621, 'learning_rate_adagrad', 'DECIMAL', 0, 3, 0.01, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_adagrad),

        # Adadelta
        (5622, 'learning_rate_adadelta', 'DECIMAL', 0, 3, 1.0, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_adadelta),
        (5623, 'rho_adadelta', 'DECIMAL', 0, 6, 0.95, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adadelta),

        # Adam
        (5624, 'learning_rate_adam', 'DECIMAL', 0, 3, 0.001, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_adam),
        (5625, 'beta_1_adam', 'DECIMAL', 0, 6, 0.9, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adam),
        (5626, 'beta_2_adam', 'DECIMAL', 0, 7, 0.999, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adam),
        (5627, 'amsgrad_adam', 'INTEGER', 0, 8, 0, 'checkbox', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adam),

        # Adamax
        (5628, 'learning_rate_adamax', 'DECIMAL', 0, 3, 0.002, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_adamax),
        (5629, 'beta_1_adamax', 'DECIMAL', 0, 6, 0.9, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adamax),
        (5630, 'beta_2_adamax', 'DECIMAL', 0, 7, 0.999, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adamax),

        # Nadam
        (5631, 'learning_rate_nadam', 'DECIMAL', 0, 3, 0.002, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_nadam),
        (5632, 'beta_1_nadam', 'DECIMAL', 0, 6, 0.9, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_nadam),
        (5633, 'beta_2_nadam', 'DECIMAL', 0, 7, 0.999, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_nadam),

        # Sequence reader
        (5634, 'test_sequence', 'INTEGER', 0, 3, None, 'lookup',
         LIMONERO_IMAGE, None, 'EXECUTION', 5240, None),

        # Sequence generator
        (5635, 'batch_size', 'INTEGER', 1, 1, 32, 'integer', None, None,
         'EXECUTION', SEQUENCE_GENERATOR_FORM_ID, None),
        (5636, 'shuffle', 'INTEGER', 0, 3, 1, 'checkbox', None, None,
         'EXECUTION', SEQUENCE_GENERATOR_FORM_ID, None),
        (5637, 'validation_split', 'DECIMAL', 0, 4, 0.0, 'decimal', None, None,
         'EXECUTION', SEQUENCE_GENERATOR_FORM_ID, None),
        (5638, 'shape', 'TEXT', 1, 2, None, 'text', None, None,
         'EXECUTION', SEQUENCE_GENERATOR_FORM_ID, None),
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
        # Model
        (5612, 'en', 'Advanced optimizer options', 'Advanced option for the '
                                                   'optimazer parameters.'),
        (5613, 'en', 'Clip norm', 'All parameter gradients will be clipped to '
                                  'a maximum norm of 1.'),
        (5614, 'en', 'Clip value', 'All parameter gradients will be clipped to'
                                   ' a maximum value of 0.5 and a minimum '
                                   'value of -0.5.'),
        (5615, 'en', 'Learning rate', 'Learning rate.'),
        (5616, 'en', 'Decay', 'Learning rate decay'),
        (5617, 'en', 'Momentum', 'Parameter that accelerates SGD in the rele'
                                 'vant direction and dampens oscillations.'),
        (5618, 'en', 'Nesterov', 'Whether to apply Nesterov momentum.'),
        (5619, 'en', 'Learning rate', 'Learning rate.'),
        (5620, 'en', 'Rho', 'Rho'),
        (5621, 'en', 'Learning rate', 'Learning rate.'),
        (5622, 'en', 'Learning rate', 'Learning rate.'),
        (5623, 'en', 'Rho', 'Rho'),
        (5624, 'en', 'Learning rate', 'Learning rate.'),
        (5625, 'en', 'Beta 1', ' 0 < beta < 1. Generally close to 1.'),
        (5626, 'en', 'Beta 2', '0 < beta < 1. Generally close to 1.'),
        (5627, 'en', 'Amsgrad', 'Whether to apply the AMSGrad variant of this '
                                'algorithm from the paper "On the Convergence '
                                'of Adam and Beyond".'),
        (5628, 'en', 'Learning rate', 'Learning rate.'),
        (5629, 'en', 'Beta 1', ' 0 < beta < 1. Generally close to 1.'),
        (5630, 'en', 'Beta 2', '0 < beta < 1. Generally close to 1.'),
        (5631, 'en', 'Learning rate', 'Learning rate.'),
        (5632, 'en', 'Beta 1', ' 0 < beta < 1. Generally close to 1.'),
        (5633, 'en', 'Beta 2', '0 < beta < 1. Generally close to 1.'),
        (5634, 'en', 'Test sequences', ''),
        (5635, 'en', 'Batch size', 'Size of the batches of data '
                                   '(default: 32).'),
        (5636, 'en', 'Shuffle', 'Whether to shuffle the order of the batches at'
                                ' the beginning of each epoch. '),
        (5637, 'en', 'Validation split', 'Float. Fraction of data reserved '
                                         'for validation (strictly between 0 '
                                         'and 1).'),
        (5638, 'en', 'Shape', 'A shape tuple (integer), not including the '
                              'batch size. For instance, shape=(32,) indicates '
                              'that the expected input will be batches of '
                              '32-dimensional vectors.'),


    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE '
     'FROM operation '
     'WHERE id IN ({0}, {1})'.format(PREDICTION_LAYER, SEQUENCE_GENERATOR)),
    (_insert_operation_platform,
     'DELETE '
     'FROM operation_platform '
     'WHERE operation_id IN ({0}, {1}) '
     'AND platform_id = {2}'.format(PREDICTION_LAYER,
                                    SEQUENCE_GENERATOR,
                                    KERAS_PLATAFORM_ID)),
    (_insert_operation_translation,
     'DELETE '
     'FROM operation_translation '
     'WHERE id IN ({0}, {1})'.format(PREDICTION_LAYER, SEQUENCE_GENERATOR)),
    (_insert_operation_category_operation,
     'DELETE '
     'FROM operation_category_operation '
     'WHERE operation_id IN ({0}, {1})'.format(PREDICTION_LAYER,
                                               SEQUENCE_GENERATOR)),
    (_insert_operation_port,
     'DELETE '
     'FROM operation_port '
     'WHERE id BETWEEN 5397 AND 5405'),
    (_insert_operation_port_interface_operation_port,
     'DELETE '
     'FROM operation_port_interface_operation_port '
     'WHERE operation_port_id BETWEEN 5397 AND 5405'),
    (_insert_operation_port_translation,
     'DELETE '
     'FROM operation_port_translation '
     'WHERE id BETWEEN 5397 AND 5405'),
    (_insert_operation_operation_form,
     'DELETE '
     'FROM operation_operation_form '
     'WHERE operation_id IN ({0}, {1})'.format(PREDICTION_LAYER,
                                               SEQUENCE_GENERATOR)),

    (_insert_operation_form,
     'DELETE '
     'FROM operation_form '
     'WHERE id IN ({0})'.format(SEQUENCE_GENERATOR_FORM_ID)),
    (_insert_operation_form_translation,
     'DELETE '
     'FROM operation_form_translation '
     'WHERE id IN ({0})'.format(SEQUENCE_GENERATOR_FORM_ID)),

    (_insert_operation_form_field,
     'DELETE '
     'FROM operation_form_field '
     'WHERE id BETWEEN 5612 AND 5638'),
    (_insert_operation_form_field_translation,
     'DELETE '
     'FROM operation_form_field_translation '
     'WHERE id BETWEEN 5612 AND 5638'),

    ('''
        UPDATE operation_form_field 
        SET `required` = 0 
        WHERE id = 5509    
     ''',
     '''
        UPDATE operation_form_field 
        SET `required` = 1 
        WHERE id = 5509
     '''),

    ('''
        UPDATE operation_port 
        SET `order` = 3 
        WHERE id = 5394    
     ''',
     '''
        UPDATE operation_port 
        SET `order` = 1 
        WHERE id = 5394
     '''),
    ('''
        UPDATE operation_port 
        SET `order` = 2 
        WHERE id = 5229    
     ''',
     '''
        UPDATE operation_port 
        SET `order` = 3 
        WHERE id = 5229
     '''),
    ('''
        UPDATE operation_port 
        SET `order` = 1 
        WHERE id = 5235    
     ''',
     '''
        UPDATE operation_port 
        SET `order` = 2 
        WHERE id = 5235
     '''),

    ('''
        UPDATE operation_form_field 
        SET `default` = 1 
        WHERE `name` = "advanced_options" AND id > 5000
     ''',
     '''
        UPDATE operation_form_field 
        SET `default` = 0 
        WHERE `name` = "advanced_options" AND id > 5000
     '''),

    ('''
        UPDATE operation_form_field 
        SET `enable_conditions` = NULL 
        WHERE `name` = "advanced_options" AND id > 5000
     ''',
     ''''''),

    ('''
        UPDATE operation_form_field 
        SET `order` =  10
        WHERE id = 5466
     ''',
     '''
        UPDATE operation_form_field 
        SET `order` =  2
        WHERE id = 5466
     '''),
    ('''
        UPDATE operation_form_field 
        SET `order` =  11
        WHERE id = 5467
     ''',
     '''
        UPDATE operation_form_field 
        SET `order` =  3
        WHERE id = 5467
     '''),
    ('''
        UPDATE operation_form_field 
        SET `order` =  12
        WHERE id = 5469
     ''',
     '''
        UPDATE operation_form_field 
        SET `order` =  4
        WHERE id = 5469
     '''),
    ('''
        UPDATE operation_form_field 
        SET `order` =  13
        WHERE id = 5470
     ''',
     '''
        UPDATE operation_form_field 
        SET `order` =  5
        WHERE id = 5470
     '''),
    ('''
        UPDATE operation_form_field 
        SET `order` =  14
        WHERE id = 5471
     ''',
     '''
        UPDATE operation_form_field 
        SET `order` =  5
        WHERE id = 5471
     '''),
    ('''
        UPDATE operation_form_field 
        SET `order` =  15
        WHERE id = 5472
     ''',
     '''
        UPDATE operation_form_field 
        SET `order` =  6
        WHERE id = 5472
     '''),
    ('''
        UPDATE operation_form_field 
        SET `order` =  16
        WHERE id = 5473
     ''',
     '''
        UPDATE operation_form_field 
        SET `order` =  7
        WHERE id = 5473
     '''),

    ('''
        UPDATE operation_port_translation 
        SET `name` =  'train sequence data'
        WHERE id = 5320
     ''',
     ''''''),
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

