"""Inserting the evaluation form fields.

Revision ID: 29b1fd063b92
Revises: 08cf53ba6092
Create Date: 2021-03-24 17:30:14.537880

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
revision = '29b1fd063b92'
down_revision = '08cf53ba6092'
branch_labels = None
depends_on = None


EVALUATION_ID = 4050
EVALUATION_FORM_ID = 4051


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
        (4399, 'confusion_matrix', 'INTEGER', 0, 1, 1, 'checkbox', None, None, 'EXECUTION', EVALUATION_FORM_ID, None),
        (4400, 'fscore', 'INTEGER', 0, 2, 1, 'checkbox', None, None, 'EXECUTION', EVALUATION_FORM_ID, None),
        (4401, 'recall', 'INTEGER', 0, 3, 1, 'checkbox', None, None, 'EXECUTION', EVALUATION_FORM_ID, None),
        (4402, 'precision', 'INTEGER', 0, 4, 1, 'checkbox', None, None, 'EXECUTION', EVALUATION_FORM_ID, None),
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
        (4399, 'en', 'Confusion Matrix', ''),
        (4399, 'pt', 'Matriz de Confusão', ''),

        (4400, 'en', 'F-score', ''),
        (4400, 'pt', 'F-score', ''),

        (4401, 'en', 'Recall', ''),
        (4401, 'pt', 'Recall', ''),

        (4402, 'en', 'Precision', ''),
        (4402, 'pt', 'Precisão', ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN (4399, 4400, 4401, 4402)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (4399, 4400, 4401, 4402)'),
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