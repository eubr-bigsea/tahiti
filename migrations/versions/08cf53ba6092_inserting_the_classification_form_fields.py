"""Inserting the classification form fields.

Revision ID: 08cf53ba6092
Revises: 308d123bd104
Create Date: 2021-03-24 13:31:58.087283

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
revision = '08cf53ba6092'
down_revision = '308d123bd104'
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

    data = [
        #Flatten - data_format
        (4397, 'intercept', 'FLOAT', 1, 1, None, 'decimal', None, None, 'EXECUTION', CLASSIFICATION_FORM_ID, None),
        (4398, 'coefficients', 'TEXT', 1, 2, None, 'text', None, None, 'EXECUTION', CLASSIFICATION_FORM_ID, None),
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
        (4397, 'en', 'Intercept', 'The interception value.'),
        (4397, 'pt', 'Intercept', 'O valor de interceptação.'),

        (4398, 'en', 'Coefficients (Enter values separated by commas)',
         'The coefficients of the logistic regression.'),
        (4398, 'pt', 'Coeficientes (Informe os valores separados por vírgula)',
         'Os coeficientes da regressão logística.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN (4397, 4398)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (4397, 4398)'),
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