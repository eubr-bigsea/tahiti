"""Inserting the indexing form fields.

Revision ID: feefeea4fa7e
Revises: d4d1ab2c8ac8
Create Date: 2021-03-19 14:38:20.373452

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
revision = 'feefeea4fa7e'
down_revision = 'd4d1ab2c8ac8'
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

    data = [
        #Flatten - data_format
        (4393, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', INDEXING_FORM_ID, None),
        (4394, 'algorithm', 'TEXT', 1, 2, 'block', 'dropdown', None,
                 json.dumps([
                     {'key': 'block', 'value': 'Block'},
                     {'key': 'full', 'value': 'Full'},
                     {'key': 'sorted-neighbourhood', 'value': 'Sorted Neighbourhood'},
                     {'key': 'random', 'value': 'Random'},
                 ]),
                 'EXECUTION', INDEXING_FORM_ID, None),
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
        (4393, 'en', 'Attributes', 'Attributes for the indexing.'),
        (4393, 'pt', 'Atributos', 'Atributos para a blocagem.'),

        (4394, 'en', 'Algorithm', 'Algorithm used in the indexing.'),
        (4394, 'pt', 'Algoritmo', 'Atributos para a blocagem.'),
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
        (4120, 'INPUT', '', 2, 'ONE', INDEXING_ID, 'input data 2'),
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
        (4120, 1),
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
        (4120, "en", 'input data', 'Input data'),
        (4120, "pt", 'dados de entrada', 'Dados de entrada'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)

all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN (4393,4394)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (4393,4394)'),
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id=4120'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id=4120'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id=4120'),
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
