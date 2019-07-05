# -*- coding: utf-8 -*-
"""Add keras input and output layers

Revision ID: 8647edf5eaad
Revises: 73f22f178b14
Create Date: 2018-10-16 14:11:56.645275

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json


# revision identifiers, used by Alembic.
revision = '8647edf5eaad'
down_revision = '73f22f178b14'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5


def _insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (5070, "en", 'Input/Output Layers'),
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
        (5071, KERAS_PLATAFORM_ID),#Input
        (5072, KERAS_PLATAFORM_ID),#Output
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
        (5070, "group", 7, 7),
        (5071, "subgroup", 1, 1),
        (5072, "subgroup", 2, 2),
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
        (5071, "input", 1, 'ACTION', ''),
        (5072, "output", 1, 'ACTION', ''),
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
        (5070, 5071),
        (5070, 5072),
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
        (5071, "en", "Input", ''),
        (5072, "en", "Output", ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

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
        column('slug', String),)

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        #Input
        (5271, 'OUTPUT', '', 1, 'ONE', 5071, 'output data'),
        #Output
        (5172, 'INPUT', '', 1, 'ONE', 5072, 'input data'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        #input
        (5271, 1),
        #Output
        (5172, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

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
        (5271, "en", 'output data', 'Output data'),
        (5172, "en", 'input data', 'Input data'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

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
        #Input
        (5171, 1, 1, 'execution'),
        (5172, 1, 2, 'execution'),
        (5173, 1, 3, 'execution'),
        (5174, 1, 4, 'execution'),
        (5175, 1, 5, 'execution'),
        (5176, 1, 6, 'execution'),
        (5177, 1, 6, 'execution'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(operation_form_table, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        #Input
        (5171, 'en', 'Execution'),
        (5171, 'pt', 'Execução'),
        (5172, 'en', 'Execution'),
        (5172, 'pt', 'Execução'),
        (5173, 'en', 'Execution'),
        (5173, 'pt', 'Execução'),
        (5174, 'en', 'Execution'),
        (5174, 'pt', 'Execução'),
        (5175, 'en', 'Execution'),
        (5175, 'pt', 'Execução'),
        (5176, 'en', 'Execution'),
        (5176, 'pt', 'Execução'),
        (5177, 'en', 'Execution'),
        (5177, 'pt', 'Execução'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        #Input
        (5071, 5171),  # own execution form
        (5071, 5172),  # own execution form
        (5071, 5173),  # own execution form
        (5071, 5174),  # own execution form
        (5071, 5175),  # own execution form
        (5071, 5176),  # own execution form
        (5071, 5177),  # own execution form
        (5071, 41),  #appearance
        (5072, 41),  #appearance
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
        column('form_id', Integer), )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [
        #Dataset
        (5171, 'dataset', 'TEXT', 1, 1, None, 'text', None, None, 'EXECUTION', 5171),
        #Train/Validation/test split
        (5172, 'train_validation_test_split', 'TEXT', 0, 2, '60%-20%-20%', 'text', None, None, 'EXECUTION', 5172),
        #K-fold cross validation
        (5173, 'use_k_fold_cross_validation', 'INTEGER', 0, 3, None, 'checkbox', None, None, 'EXECUTION', 5173),
        #Train/Validation/test split
        (5174, 'percent_of_train_data', 'INTEGER', 0, 4, None, 'integer', None, None, 'EXECUTION', 5174),
        #Shuffle data
        (5175, 'shuffle_data', 'INTEGER', 0, 5, None, 'checkbox', None, None, 'EXECUTION', 5175),
        (5176, 'load_dataset_in_memory', 'TEXT', 0, 6, 'one batch at a time', 'dropdown', None,
         json.dumps([
             {"key": "one batch at a time", "value": "one batch at a time"},
             {"key": "full dataset", "value": "full dataset"},
         ]),
         'EXECUTION', 5176),
        (5177, 'seed', 'INTEGER', 0, 7, 17, 'integer', None, None, 'EXECUTION', 5177),
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
        (5171, 'en', 'Dataset', 'Path for the dataset.'),
        (5172, 'en', 'Train-Validation-Test split', 'Percentage for Train, '
                                                    'Validation and Test to split the data automatically. '
                                                    'The sum of them needs to be equal to 100.'),
        (5173, 'en', 'Use K-fold cross validation', 'The dataset will be split in different k-fold train and test.'),
        (5174, 'en', '% of train data', 'Percentage of training data to compose '
                                        'the each fold for the cross validation. '
                                        'The test data is 100 - (% of train).'),
        (5175, 'en', 'Shuffle data', 'Shuffle the instances in the dataset to ensure a random learning space.'),
        (5176, 'en', 'Load dataset in memory', 'Load the dataset in memory in two ways. '
                                               '1- Full dataset in memory (recommended for small dataset). '
                                               '2- One batch at time (recommended for large dataset).'),
        (5177, 'en', 'Seed', 'Fix random seed for reproducibility.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id BETWEEN 5071 AND 5072'),
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id BETWEEN 5070 AND 5072'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 5071 AND 5072'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id BETWEEN 5071 AND 5072'),
    (_insert_operation_category_translation,
     'DELETE FROM operation_category_translation WHERE id = 5070'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id BETWEEN 5071 AND 5072 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    # Port and interfaces
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id IN (5172, 5271)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id IN (5172, 5271)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN (5172, 5271)'),

    # Forms
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5171 AND 5177'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5171 AND 5177'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5171 AND 5177'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5171 AND 5177'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id IN (5071, 5072)'),
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

