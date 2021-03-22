"""Inserting entity resolution operations.

Revision ID: d4d1ab2c8ac8
Revises: bc13b419c5bc
Create Date: 2021-03-19 10:33:39.886189

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
revision = 'd4d1ab2c8ac8'
down_revision = 'bc13b419c5bc'
branch_labels = None
depends_on = None

EVALUATION_ID = 4050
INDEXING_ID = 4051
COMPARING_ID = 4052
CLASSIFICATION_ID = 4053

PLATFORM_ID = 4

EVALUATION_FORM_ID = 4051
INDEXING_FORM_ID = 4052
COMPARING_FORM_ID = 4053
CLASSIFICATION_FORM_ID = 4054

def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')

    data = [
        (INDEXING_ID, PLATFORM_ID),
        (COMPARING_ID, PLATFORM_ID),
        (CLASSIFICATION_ID, PLATFORM_ID),
        (EVALUATION_ID, PLATFORM_ID),
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
        (INDEXING_ID, "indexing", 1, 'ACTION', ''),
        (COMPARING_ID, "comparing", 1, 'ACTION', ''),
        (CLASSIFICATION_ID, "classification", 1, 'ACTION', ''),
        (EVALUATION_ID, "evaluation", 1, 'ACTION', ''),
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
        (4003, INDEXING_ID),
        (4003, COMPARING_ID),
        (4003, CLASSIFICATION_ID),
        (4003, EVALUATION_ID),
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
        (INDEXING_ID, "pt", '1 - Blocagem', ''),
        (INDEXING_ID, "en", '1 - Indexing', 'The indexing module is used to make pairs of records. These pairs are'
                                            'called candidate links or candidate matches.'),

        (COMPARING_ID, "pt", '2 - Comparação', ''),
        (COMPARING_ID, "en", '2 - Comparing', 'A set of informative, discriminating and independent features is'
                                              'important for a good classification of record pairs into matching and'
                                              'distinct pairs.'),

        (CLASSIFICATION_ID, "pt", '3 - Classificação', ''),
        (CLASSIFICATION_ID, "en", '3 - Classification', 'Classification is the step in the record linkage process were'
                                                    'record pairs are classified into matches, non-matches and possible'
                                                    'matches. Classification algorithms can be supervised or'
                                                    'unsupervised (with or without training data).'),

        (EVALUATION_ID, "pt", '4 - Avaliação', ''),
        (EVALUATION_ID, "en", '4 - Evaluation', 'Evaluation of classifications plays an important role in record'
                                                'linkage. Express your classification quality in terms accuracy,'
                                                'recall and F-score based on true positives, false positives, true'
                                                'negatives and false negatives.'),
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
        #Flatten - data_format
        (INDEXING_ID, 41),  #appearance
        (INDEXING_ID, INDEXING_FORM_ID),  # own execution form
        (INDEXING_ID, 110),

        (COMPARING_ID, 41),  #appearance
        (COMPARING_ID, COMPARING_FORM_ID),  # own execution form
        (COMPARING_ID, 110),

        (CLASSIFICATION_ID, 41),  #appearance
        (CLASSIFICATION_ID, CLASSIFICATION_FORM_ID),  # own execution form
        (CLASSIFICATION_ID, 110),

        (EVALUATION_ID, 41),  #appearance
        (EVALUATION_ID, EVALUATION_FORM_ID),  # own execution form
        (EVALUATION_ID, 110),
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
        #Flatten
        (INDEXING_FORM_ID, 1, 1, 'execution'), #data_format
        (COMPARING_FORM_ID, 1, 1, 'execution'), #data_format
        (CLASSIFICATION_FORM_ID, 1, 1, 'execution'), #data_format
        (EVALUATION_FORM_ID, 1, 1, 'execution'), #data_format
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
        #Flatten - data_format
        (INDEXING_FORM_ID, 'en', 'Execution'),
        (INDEXING_FORM_ID, 'pt', 'Execução'),

        (COMPARING_FORM_ID, 'en', 'Execution'),
        (COMPARING_FORM_ID, 'pt', 'Execução'),

        (CLASSIFICATION_FORM_ID, 'en', 'Execution'),
        (CLASSIFICATION_FORM_ID, 'pt', 'Execução'),

        (EVALUATION_FORM_ID, 'en', 'Execution'),
        (EVALUATION_FORM_ID, 'pt', 'Execução'),
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
        #Reshape
        (4114, 'INPUT', '', 1, 'ONE', INDEXING_ID, 'input data 1'),
        (4115, 'OUTPUT', '', 1, 'ONE', INDEXING_ID, 'output data'),

        (4116, 'INPUT', '', 1, 'ONE', COMPARING_ID, 'input data'),
        (4117, 'OUTPUT', '', 1, 'ONE', COMPARING_ID, 'output data'),

        (4118, 'INPUT', '', 1, 'ONE', CLASSIFICATION_ID, 'input data'),
        (4119, 'OUTPUT', '', 1, 'ONE', CLASSIFICATION_ID, 'output data'),

        (4112, 'INPUT', '', 1, 'ONE', EVALUATION_ID, 'input data'),
        (4113, 'OUTPUT', '', 1, 'ONE', EVALUATION_ID, 'output data'),
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
        #Reshape
        (4112, 1),
        (4113, 1),

        (4114, 1),
        (4115, 1),

        (4116, 1),
        (4117, 1),

        (4118, 1),
        (4119, 1),
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
        #Reshape
        (4112, "en", 'input data', 'Input data'),
        (4112, "pt", 'dados de entrada', 'Dados de entrada'),
        (4113, "en", 'output data', 'Output data'),
        (4113, "pt", 'dados de saída', 'Dados de saída'),

        (4114, "en", 'input data', 'Input data'),
        (4114, "pt", 'dados de entrada', 'Dados de entrada'),
        (4115, "en", 'output data', 'Output data'),
        (4115, "pt", 'dados de saída', 'Dados de saída'),

        (4116, "en", 'input data', 'Input data'),
        (4116, "pt", 'dados de entrada', 'Dados de entrada'),
        (4117, "en", 'output data', 'Output data'),
        (4117, "pt", 'dados de saída', 'Dados de saída'),

        (4118, "en", 'input data', 'Input data'),
        (4118, "pt", 'dados de entrada', 'Dados de entrada'),
        (4119, "en", 'output data', 'Output data'),
        (4119, "pt", 'dados de saída', 'Dados de saída'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)

all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id BETWEEN 4050 AND 4053'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 4050 AND 4053'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id BETWEEN 4050 AND 4053'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id BETWEEN 4050 AND 4053 AND platform_id = {}'.format(PLATFORM_ID)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 4051 AND 4054'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 4051 AND 4054'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id BETWEEN 4050 AND 4053'),
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4112 AND 4119'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 4112 AND 4119'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4112 AND 4119'),
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
