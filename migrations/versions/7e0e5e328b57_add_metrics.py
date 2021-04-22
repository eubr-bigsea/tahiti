"""Add metrics.

Revision ID: 7e0e5e328b57
Revises: 29b1fd063b92
Create Date: 2021-04-22 10:47:17.206587

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
revision = '7e0e5e328b57'
down_revision = '29b1fd063b92'
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
        (4403, 'accuracy', 'INTEGER', 0, 4, 1, 'checkbox', None, None, 'EXECUTION', EVALUATION_FORM_ID, None),
        (4404, 'specificity', 'INTEGER', 0, 5, 1, 'checkbox', None, None, 'EXECUTION', EVALUATION_FORM_ID, None),
        (4405, 'reduction_ratio', 'INTEGER', 0, 6, 1, 'checkbox', None, None, 'EXECUTION', EVALUATION_FORM_ID, None),
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
        (4403, 'en', 'Accuracy', ''),
        (4403, 'pt', 'Acurácia', ''),

        (4404, 'en', 'Specificity', ''),
        (4404, 'pt', 'Especificidade', ''),

        (4405, 'en', 'Reduction ratio', ''),
        (4405, 'pt', 'Taxa de redução', ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN (4403, 4404, 4405)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (4403, 4404, 4405)'),
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
