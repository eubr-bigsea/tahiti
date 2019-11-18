# -*- coding: utf-8 -*-

"""Update SGD Regressor (scikit_learn).

Revision ID: 529bd5bd009e
Revises: eff0acabf4fe
Create Date: 2019-11-18 14:28:54.961838

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
revision = '529bd5bd009e'
down_revision = 'eff0acabf4fe'
branch_labels = None
depends_on = None

def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        #Flatten - data_format
        (4029, 41),  #appearance
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
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
        column('enable_conditions', String),
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')

    data = [
        #Flatten - data_format
        (4221, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4009, None),
        (4222, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None, 'EXECUTION', 4009, None),
        (4223, 'prediction', 'TEXT', 0, 3, 'prediction', 'text', None, None, 'EXECUTION', 4009, None),
        (4208, 'power_t', 'DECIMAL', 1, 6, 0.5, 'decimal', None, None, 'EXECUTION', 4009, None),
        (4211, 'early_stopping', 'INTEGER', 1, 7, 0, 'checkbox', None, None, 'EXECUTION', 4009, None),
        (4212, 'validation_fraction', 'DECIMAL', 1, 8, 0.1, 'decimal', None, None, 'EXECUTION', 4009, None),
        (4213, 'epsilon', 'DECIMAL', 1, 9, None, 'decimal', None, None, 'EXECUTION', 4009, None),
        (4214, 'n_iter_no_change', 'INTEGER', 1, 10, 5, 'integer', None, None, 'EXECUTION', 4009, None),
        (4215, 'loss', 'TEXT', 1, 11, 'squared_loss', 'dropdown', None,
         json.dumps([
             {'key': 'squared_loss', 'value': 'squared_loss'},
             {'key': 'huber', 'value': 'huber'},
             {'key': 'epsilon_insensitive', 'value': 'epsilon_insensitive'},
             {'key': 'squared_epsilon_insensitive', 'value': 'squared_epsilon_insensitive'},
         ]),
         'EXECUTION', 4009, None),
        (4216, 'penalty', 'TEXT', 1, 12, 'l2', 'dropdown', None,
         json.dumps([
             {'key': 'none', 'value': 'none'},
             {'key': 'l2', 'value': 'l2'},
             {'key': 'l1', 'value': 'l1'},
             {'key': 'elasticnet', 'value': 'elasticnet'},
         ]),
         'EXECUTION', 4009, None),
        (4217, 'fit_intercept', 'INTEGER', 1, 13, 1, 'integer', None, None, 'EXECUTION', 4009, None),
        (4219, 'eta0', 'DECIMAL', 1, 14, 0.01, 'decimal', None, None, 'EXECUTION', 4009, None),
        (4210, 'warm_start', 'INTEGER', 0, 17, 0, 'checkbox', None, None, 'EXECUTION', 4009, None),
        (4218, 'verbose', 'INTEGER', 0, 18, None, 'integer', None, None, 'EXECUTION', 4009, None),
        (4220, 'average', 'INTEGER', 0, 19, 1, 'integer', None, None, 'EXECUTION', 4009, None),
        (4207, 'learning_rate', 'TEXT', 0, 20, 'invscaling', 'dropdown', None,
         json.dumps([
             {'key': 'constant', 'value': 'constant'},
             {'key': 'invscaling', 'value': 'invscaling'},
             {'key': 'adaptive', 'value': 'adaptive'},
             {'key': 'optimal', 'value': 'optimal'},
         ]),
         'EXECUTION', 4009, None),
        (4209, 'shuffle', 'INTEGER', 0, 21, 1, 'checkbox', None, None, 'EXECUTION', 4009, None),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
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
        #Flatten - data_format
        (4221, 'en', 'Features', 'Features.'),
        (4221, 'pt', 'Atributo(s) previsor(es)', 'Atributo(s) previsor(es).'),

        (4222, 'en', 'Label attribute', 'Label attribute.'),
        (4222, 'pt', 'Atributo com o rótulo', 'Atributo com o rótulo.'),

        (4223, 'en', 'Prediction attribute (new)', 'Prediction attribute (new).'),
        (4223, 'pt', 'Atributo com a predição (novo)', 'Atributo usado para predição (novo).'),

        (4207, 'en', 'Learning rate', 'The learning rate schedule.'),
        (4207, 'pt', 'Taxa de aprendizado', 'The learning rate schedule.'),

        (4208, 'en', 'Power t', 'The exponent for inverse scaling learning rate.'),
        (4208, 'pt', 'Power t', 'The exponent for inverse scaling learning rate.'),

        (4209, 'en', 'Shuffle', 'Whether or not the training data should be shuffled after each epoch.'),
        (4209, 'pt', 'Shuffle', 'Whether or not the training data should be shuffled after each epoch.'),

        (4210, 'en', 'Warm start', 'When set to True, reuse the solution of the previous call to fit as initialization,'
                                   ' otherwise, just erase the previous solution.'),
        (4210, 'pt', 'Warm start', 'When set to True, reuse the solution of the previous call to fit as initialization,'
                                   ' otherwise, just erase the previous solution.'),

        (4211, 'en', 'Early stopping', 'Whether to use early stopping to terminate training when validation score is'
                                       ' not improving.'),
        (4211, 'pt', 'Early stopping', 'Whether to use early stopping to terminate training when validation score is'
                                       ' not improving.'),

        (4212, 'en', 'Validation fraction', 'The proportion of training data to set aside as validation set for early'
                                            ' stopping.'),
        (4212, 'pt', 'Validation fraction', 'The proportion of training data to set aside as validation set for early'
                                            ' stopping.'),

        (4213, 'en', 'Epsilon', 'Epsilon in the epsilon-insensitive loss functions.'),
        (4213, 'pt', 'Epsilon', 'Epsilon in the epsilon-insensitive loss functions.'),

        (4214, 'en', 'N iter no change', 'Number of iterations with no improvement to wait before early stopping.'),
        (4214, 'pt', 'N iter no change', 'Number of iterations with no improvement to wait before early stopping.'),

        (4215, 'en', 'Loss', 'The loss function to be used.'),
        (4215, 'pt', 'Loss', 'The loss function to be used.'),

        (4216, 'en', 'Penalty', 'The penalty (aka regularization term) to be used.'),
        (4216, 'pt', 'Penalty', 'The penalty (aka regularization term) to be used.'),

        (4217, 'en', 'Fit intercept', 'Whether the intercept should be estimated or not.'),
        (4217, 'pt', 'Fit intercept', 'Whether the intercept should be estimated or not.'),

        (4218, 'en', 'Verbose', 'The verbosity level.'),
        (4218, 'pt', 'Verbose', 'The verbosity level.'),

        (4219, 'en', 'Eta', 'The initial learning rate for the ‘constant’, ‘invscaling’ or ‘adaptive’ schedules.'),
        (4219, 'pt', 'Eta', 'The initial learning rate for the ‘constant’, ‘invscaling’ or ‘adaptive’ schedules.'),

        (4220, 'en', 'Average', 'If set to an int greater than 1, averaging will begin once the total number of samples'
                                ' seen reaches average. So average=10 will begin averaging after seeing 10 samples.'),
        (4220, 'pt', 'Average', 'If set to an int greater than 1, averaging will begin once the total number of samples'
                                ' seen reaches average. So average=10 will begin averaging after seeing 10 samples.'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `type` = 'DECIMAL' WHERE id = 4045 OR id = 4046 OR id = 4048""",
     """UPDATE operation_form_field SET `type` = 'FLOAT' WHERE id = 4045 OR id = 4046 OR id = 4048"""),

    ("""UPDATE operation_form_field SET `order` = 15 WHERE id = 4045""",
     """UPDATE operation_form_field SET `order` = 1 WHERE id = 4045"""),

    ("""UPDATE operation_form_field SET `order` = 16 WHERE id = 4046""",
     """UPDATE operation_form_field SET `order` = 2 WHERE id = 4046"""),

    ("""UPDATE operation_form_field SET `order` = 22 WHERE id = 4047""",
     """UPDATE operation_form_field SET `order` = 3 WHERE id = 4047"""),

    ("""UPDATE operation_form_field SET `required` = 1 WHERE id = 4045""",
     """UPDATE operation_form_field SET `required` = 0 WHERE id = 4045"""),

    ("""UPDATE operation_form_field SET `required` = 1 WHERE id = 4046""",
     """UPDATE operation_form_field SET `required` = 0 WHERE id = 4046"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4207 AND 4223'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4207 AND 4223'),

    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4029 AND operation_form_id = 41'),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
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