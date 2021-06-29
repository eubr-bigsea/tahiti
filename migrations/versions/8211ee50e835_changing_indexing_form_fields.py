"""Changing indexing form fields.

Revision ID: 8211ee50e835
Revises: 6d72f4a5c3a0
Create Date: 2021-05-30 15:52:24.208254

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
revision = '8211ee50e835'
down_revision = '6d72f4a5c3a0'
branch_labels = None
depends_on = None


INDEXING_ID = 4051
INDEXING_FORM_ID = 4052


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
    enable_condition = 'this.algorithm.internalValue == "sorted-neighbourhood"'
    enable_condition_2 = 'this.algorithm.internalValue == "random"'
    data = [
        #Flatten - data_format
        (4409, 'sorting_key_values', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION', INDEXING_FORM_ID, enable_condition),
        (4410, 'block_on', 'TEXT', 0, 5, None, 'attribute-selector', None, None, 'EXECUTION', INDEXING_FORM_ID, enable_condition),
        (4411, 'block_right_on', 'TEXT', 0, 6, None, 'attribute-selector', None, None, 'EXECUTION', INDEXING_FORM_ID, enable_condition),
        (4412, 'block_left_on', 'TEXT', 0, 7, None, 'attribute-selector', None, None, 'EXECUTION', INDEXING_FORM_ID, enable_condition),

        (4413, 'n', 'INTEGER', 0, 8, None, 'integer', None, None, 'EXECUTION', INDEXING_FORM_ID, enable_condition_2),
        (4414, 'replace', 'INTEGER', 0, 9, 1, 'checkbox', None, None, 'EXECUTION', INDEXING_FORM_ID, enable_condition_2),
        (4415, 'random_state', 'INTEGER', 0, 10, None, 'integer', None, None, 'EXECUTION', INDEXING_FORM_ID, enable_condition_2),
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
        (4409, 'en', 'Sorting key values (Inform the values separated by a comma)', 'A list of sorting key values.'),
        (4409, 'pt', 'Sorting key values (Informe os valores separados por vírgula)', ''),

        (4410, 'en', 'Block on', 'Additional columns to apply standard blocking on.'),
        (4410, 'pt', 'Block on', ''),

        (4411, 'en', 'Block right on', 'Additional columns in the left dataframe to apply standard blocking on.'),
        (4411, 'pt', 'Block right on', ''),

        (4412, 'en', 'Block left on', 'Additional columns in the right dataframe to apply standard blocking on.'),
        (4412, 'pt', 'Block left on', ''),

        (4413, 'en', 'N', 'The number of record pairs to return.'),
        (4413, 'pt', 'N', ''),

        (4414, 'en', 'Replace', 'Whether the sample of record pairs is with or without replacement.'),
        (4414, 'pt', 'Replace', ''),

        (4415, 'en', 'Random state', 'Seed for the random number generator.'),
        (4415, 'pt', 'Random state', ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN (4409,4410,4411,4412,4413,4414,4415)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (4409,4410,4411,4412,4413,4414,4415)'),

    ("""UPDATE operation_form_field SET `enable_conditions` = 'this.algorithm.internalValue == "block" ||
        this.algorithm.internalValue == "sorted-neighbourhood"' WHERE id = 4393""",
     """UPDATE operation_form_field SET `enable_conditions` = NULL WHERE id = 4393"""),

    ("""UPDATE operation_form_field SET `order` = 1 WHERE id = 4394""",
     """UPDATE operation_form_field SET `order` = 2 WHERE id = 4394"""),

    ("""UPDATE operation_form_field SET `order` = 2 WHERE id = 4393""",
     """UPDATE operation_form_field SET `order` = 1 WHERE id = 4393"""),
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

