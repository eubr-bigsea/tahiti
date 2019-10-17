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
        (PREDICTION_LAYER, 'en', 'Predict', 'Generates predictions for '
                                                  'the input samples from a '
                                                  'data generator.'),
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
        (5401, 'OUTPUT', '', 1, 'ONE', LOAD, 'python code'),

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
        (5401, 28),
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
        (PREDICTION_LAYER, 41),
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

    data = [
        # Model
        (5611, 'advanced_optimizer', 'INTEGER', 0, 2, 0, 'checkbox', None, None,
         'EXECUTION', MODEL_FORM_ID, empty_optimizer),

        # All optimizers
        (5612, 'clipnorm', 'DECIMAL', 0, 4, 1.0, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, advanced_optimizer),
        (5613, 'clipvalue', 'DECIMAL', 0, 5, 0.5, 'decimal', None, None,
        'EXECUTION', MODEL_FORM_ID, advanced_optimizer),

        # SGD optimizer
        (5614, 'learning_rate_sgd', 'DECIMAL', 0, 3, 0.01, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_sgd),
        (5615, 'decay_sgd', 'DECIMAL', 0, 6, 1e-6, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_sgd),
        (5616, 'momentum_sgd', 'DECIMAL', 0, 7, 0.9, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_sgd),
        (5617, 'nesterov_sgd', 'INTEGER', 0, 8, 1, 'checkbox', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_sgd),

        # RMSprop optimizer
        (5618, 'learning_rate_rmsprop', 'DECIMAL', 0, 3, 0.001, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_rmsprop),
        (5619, 'rho_rmsprop', 'DECIMAL', 0, 6, 0.9, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_rmsprop),

        # Adagrad
        (5620, 'learning_rate_adagrad', 'DECIMAL', 0, 3, 0.01, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_adagrad),

        # Adadelta
        (5621, 'learning_rate_adadelta', 'DECIMAL', 0, 3, 1.0, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_adadelta),
        (5622, 'rho_adadelta', 'DECIMAL', 0, 6, 0.95, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adadelta),

        # Adam
        (5623, 'learning_rate_adam', 'DECIMAL', 0, 3, 0.001, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_adam),
        (5624, 'beta_1_adam', 'DECIMAL', 0, 6, 0.9, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adam),
        (5625, 'beta_2_adam', 'DECIMAL', 0, 7, 0.999, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adam),
        (5626, 'amsgrad_adam', 'INTEGER', 0, 8, 0, 'checkbox', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adam),

        # Adamax
        (5627, 'learning_rate_adamax', 'DECIMAL', 0, 3, 0.002, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_adamax),
        (5628, 'beta_1_adamax', 'DECIMAL', 0, 6, 0.9, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adamax),
        (5629, 'beta_2_adamax', 'DECIMAL', 0, 7, 0.999, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_adamax),

        # Nadam
        (5630, 'learning_rate_nadam', 'DECIMAL', 0, 3, 0.002, 'decimal',
         None, None, 'EXECUTION', MODEL_FORM_ID, optimizer_condition_nadam),
        (5631, 'beta_1_nadam', 'DECIMAL', 0, 6, 0.9, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_nadam),
        (5632, 'beta_2_nadam', 'DECIMAL', 0, 7, 0.999, 'decimal', None, None,
         'EXECUTION', MODEL_FORM_ID, optimizer_condition_nadam),
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
        (5611, 'en', 'Advanced optimizer options', 'Advanced option for the '
                                                   'optimazer parameters.'),
        (5612, 'en', 'Clip norm', 'All parameter gradients will be clipped to '
                                  'a maximum norm of 1.'),
        (5613, 'en', 'Clip value', 'All parameter gradients will be clipped to'
                                   ' a maximum value of 0.5 and a minimum '
                                   'value of -0.5.'),
        (5614, 'en', 'Learning rate', 'Learning rate.'),
        (5615, 'en', 'Decay', 'Learning rate decay'),
        (5616, 'en', 'Momentum', 'Parameter that accelerates SGD in the rele'
                                 'vant direction and dampens oscillations.'),
        (5617, 'en', 'Nesterov', 'Whether to apply Nesterov momentum.'),
        (5618, 'en', 'Learning rate', 'Learning rate.'),
        (5619, 'en', 'Rho', 'Rho'),
        (5620, 'en', 'Learning rate', 'Learning rate.'),
        (5621, 'en', 'Learning rate', 'Learning rate.'),
        (5622, 'en', 'Rho', 'Rho'),
        (5623, 'en', 'Learning rate', 'Learning rate.'),
        (5624, 'en', 'Beta 1', ' 0 < beta < 1. Generally close to 1.'),
        (5625, 'en', 'Beta 2', '0 < beta < 1. Generally close to 1.'),
        (5626, 'en', 'Amsgrad', 'Whether to apply the AMSGrad variant of this '
                                'algorithm from the paper "On the Convergence '
                                'of Adam and Beyond".'),
        (5627, 'en', 'Learning rate', 'Learning rate.'),
        (5628, 'en', 'Beta 1', ' 0 < beta < 1. Generally close to 1.'),
        (5629, 'en', 'Beta 2', '0 < beta < 1. Generally close to 1.'),
        (5630, 'en', 'Learning rate', 'Learning rate.'),
        (5631, 'en', 'Beta 1', ' 0 < beta < 1. Generally close to 1.'),
        (5632, 'en', 'Beta 2', '0 < beta < 1. Generally close to 1.'),


    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE '
     'FROM operation '
     'WHERE id BETWEEN {0} AND {0}'.format(PREDICTION_LAYER)),
    (_insert_operation_platform,
     'DELETE '
     'FROM operation_platform '
     'WHERE operation_id BETWEEN {0} AND {0} '
     'AND platform_id = {1}'.format(PREDICTION_LAYER, KERAS_PLATAFORM_ID)),
    (_insert_operation_translation,
     'DELETE '
     'FROM operation_translation '
     'WHERE id BETWEEN {0} AND {0}'.format(PREDICTION_LAYER)),
    (_insert_operation_category_operation,
     'DELETE '
     'FROM operation_category_operation '
     'WHERE operation_id BETWEEN {0} AND {0}'.format(PREDICTION_LAYER)),
    (_insert_operation_port,
     'DELETE '
     'FROM operation_port '
     'WHERE id BETWEEN 5397 AND 5401'),
    (_insert_operation_port_interface_operation_port,
     'DELETE '
     'FROM operation_port_interface_operation_port '
     'WHERE operation_port_id BETWEEN 5397 AND 5401'),
    (_insert_operation_port_translation,
     'DELETE '
     'FROM operation_port_translation '
     'WHERE id BETWEEN 5397 AND 5401'),
    (_insert_operation_operation_form,
     'DELETE '
     'FROM operation_operation_form '
     'WHERE operation_id IN ({})'.format(PREDICTION_LAYER)),

    (_insert_operation_form_field,
     'DELETE '
     'FROM operation_form_field '
     'WHERE id BETWEEN 5611 AND 5632'),
    (_insert_operation_form_field_translation,
     'DELETE '
     'FROM operation_form_field_translation '
     'WHERE id BETWEEN 5611 AND 5632'),

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

