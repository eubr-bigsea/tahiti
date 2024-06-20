"""Add classifiers.

Revision ID: 446e73d62c97
Revises: 7e0e5e328b57
Create Date: 2021-04-22 11:01:32.783528

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
revision = '446e73d62c97'
down_revision = '7e0e5e328b57'
branch_labels = None
depends_on = None


CLASSIFICATION_ID = 4053
CLASSIFICATION_FORM_ID = 4054


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

    enable_condition = 'this.algorithm.internalValue == "naive-bayes"'

    data = [
        #Flatten - data_format
        (4405, 'algorithm', 'TEXT', 1, 1, 'logistic-regression', 'dropdown', None,
         json.dumps([
             {'key': 'logistic-regression', 'value': 'Logistic Regression'},
             {'key': 'svm', 'value': 'SVM'},
             {'key': 'naive-bayes', 'value': 'Naive Bayes'},
         ]),
         'EXECUTION', CLASSIFICATION_FORM_ID, None),
        (4406, 'binarize', 'FLOAT', 0, 4, None, 'decimal', None, None, 'EXECUTION', CLASSIFICATION_FORM_ID, enable_condition),
        (4394, 'alpha', 'FLOAT', 1, 5, 1e-4, 'decimal', None, None, 'EXECUTION', CLASSIFICATION_FORM_ID, enable_condition),
        (4395, 'use_col_names', 'INTEGER', 1, 6, 1, 'checkbox', None, None, 'EXECUTION', CLASSIFICATION_FORM_ID, enable_condition),
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
        (4405, 'en', 'Algorithm', ''),
        (4405, 'pt', 'Algoritmo', ''),

        (4406, 'en', 'Binarize', ''),
        (4406, 'pt', 'Binarize', ''),

        (4394, 'en', 'Alpha', ''),
        (4394, 'pt', 'Alpha', ''),

        (4395, 'en', 'Use column names', ''),
        (4395, 'pt', 'Usar os nomes das colunas', ''),
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
        (4124, 'INPUT', '', 1, 'ONE', CLASSIFICATION_ID, 'input data'),
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
        (4124, 1),
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
        (4124, "en", 'input data', 'Input data'),
        (4124, "pt", 'dados de entrada', 'Dados de entrada'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN (4405, 4406, 4394, 4395)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (4405, 4406, 4394, 4395)'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id = 4124'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id = 4124'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id = 4124'),

    ("""UPDATE operation_form_field SET `order` = 3 WHERE id = 4397""",
     """UPDATE operation_form_field SET `order` = 1 WHERE id = 4397"""),
    ("""UPDATE operation_form_field SET `enable_conditions` = 'this.algorithm.internalValue == "logistic-regression"' WHERE id = 4397""",
     """UPDATE operation_form_field SET `enable_conditions` = NULL WHERE id = 4397"""),
    ("""UPDATE operation_form_field SET `enable_conditions` = 'this.algorithm.internalValue == "logistic-regression"' WHERE id = 4398""",
     """UPDATE operation_form_field SET `enable_conditions` = NULL WHERE id = 4398"""),

    ("""UPDATE operation_port SET `order` = 2 WHERE id = 4118""",
     """UPDATE operation_port SET `order` = 1 WHERE id = 4118"""),
    ("""UPDATE operation_port SET `slug` = 'comparing data' WHERE id = 4118""",
     """UPDATE operation_port SET `slug` = 'input data' WHERE id = 4118"""),
    ("""UPDATE operation_port_translation SET `name` = 'dados da comparação' WHERE id = 4118 AND `locale` = 'pt'""",
     """UPDATE operation_port_translation SET `name` = 'dados de entrada' WHERE id = 4118 AND `locale` = 'pt'"""),
    ("""UPDATE operation_port_translation SET `description` = 'Dados da comparação' WHERE id = 4118 AND `locale` = 'pt'""",
     """UPDATE operation_port_translation SET `description` = 'Dados de entrada' WHERE id = 4118 AND `locale` = 'pt'"""),
    ("""UPDATE operation_port_translation SET `name` = 'comparing data' WHERE id = 4118 AND `locale` = 'en'""",
     """UPDATE operation_port_translation SET `name` = 'input data' WHERE id = 4118 AND `locale` = 'en'"""),
    ("""UPDATE operation_port_translation SET `description` = 'Comparing data' WHERE id = 4118 AND `locale` = 'en'""",
     """UPDATE operation_port_translation SET `description` = 'Input data' WHERE id = 4118 AND `locale` = 'en'"""),
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

