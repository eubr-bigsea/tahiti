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
        (4407, 'alpha', 'FLOAT', 1, 5, 1e-4, 'decimal', None, None, 'EXECUTION', CLASSIFICATION_FORM_ID, enable_condition),
        (4408, 'use_col_names', 'INTEGER', 1, 6, 1, 'checkbox', None, None, 'EXECUTION', CLASSIFICATION_FORM_ID, enable_condition),
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

        (4407, 'en', 'Alpha', ''),
        (4407, 'pt', 'Alpha', ''),

        (4408, 'en', 'Use column names', ''),
        (4408, 'pt', 'Usar os nomes das colunas', ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN (4405, 4406, 4407, 4408)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (4405, 4406, 4407, 4408)'),

    ("""UPDATE operation_form_field SET `order` = 3 WHERE id = 4397""",
     """UPDATE operation_form_field SET `order` = 1 WHERE id = 4397"""),
    ("""UPDATE operation_form_field SET `enable_conditions` = 'this.algorithm.internalValue == "logistic-regression"' WHERE id = 4397""",
     """UPDATE operation_form_field SET `enable_conditions` = NULL WHERE id = 4397"""),
    ("""UPDATE operation_form_field SET `enable_conditions` = 'this.algorithm.internalValue == "logistic-regression"' WHERE id = 4398""",
     """UPDATE operation_form_field SET `enable_conditions` = NULL WHERE id = 4398"""),
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

