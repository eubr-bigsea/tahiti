# coding=utf-8
"""updating association rules
Revision ID: af14b067a480
Revises: 3334e8c55632
Create Date: 2019-11-08 15:50:29.883138
"""
import json

from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'af14b067a480'
down_revision = '3334e8c55632'
branch_labels = None
depends_on = None


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
        column('enable_conditions', Integer),
    )

    columns = [c.name for c in tb.columns]

    data = [
        (513, 'attribute', 'TEXT', 0, 3, None, 'attribute-selector', None,
         '{"multiple": false}', 'EXECUTION', 108, None),
        (514, 'freq', 'TEXT', 0, 4, None, 'attribute-selector',
         None, '{"multiple": false}', 'EXECUTION', 108, None),
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

    columns = [c.name for c in tb.columns]
    data = [
        (513, 'en', 'Field with the itemset', 'The column name of the items.'),
        (513, 'pt', 'Coluna com os itemsets', 'Coluna com os itemsets.'),
        (514, 'en', 'Field with the support',
         'The column name of the support.'),
        (514, 'pt', 'Coluna com os suportes de cada itemset',
         'Coluna com os suportes de cada itemset.'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("DELETE FROM operation_form_field_translation WHERE id = 290",
     """
     INSERT INTO operation_form_field_translation VALUES
     (290,'en','Attribute with transactions (empty = first attribute)', 
      'Attribute with transactions (empty = first attribute)'),
     (290,'pt','Atributo com transações (vazio = primeiro atributo)', 
      'Atributo com transações (vazio = primeiro atributo)')
     """
     ),

    ('DELETE FROM operation_form_field WHERE id = 290',
     """
     INSERT INTO operation_form_field VALUES      
     (290,'attribute','TEXT',0,3, 'NULL','attribute-selector', 'NULL',
     '{"multiple": false}','EXECUTION',108,'NULL')
     """),
    (_insert_operation_form_field,
     "DELETE FROM operation_form_field WHERE id IN (513, 514)"),

    (_insert_operation_form_field_translation,
     "DELETE FROM operation_form_field_translation WHERE id IN (513, 514)")

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
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    session.commit()
