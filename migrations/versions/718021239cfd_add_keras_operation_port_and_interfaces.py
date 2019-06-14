# -*- coding: utf-8 -*-
"""Add keras operation port and interfaces.

Revision ID: 718021239cfd
Revises: 86dd15ad5169
Create Date: 2018-10-02 09:11:38.313666

"""

from alembic import op
from alembic import context
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '718021239cfd'
down_revision = '86dd15ad5169'
branch_labels = None
depends_on = None


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
        #Dense
        (5111, 'INPUT', '', 1, 'ONE', 5011, 'input data'),
        (5211, 'OUTPUT', '', 1, 'ONE', 5011, 'output data'),
        #Dropout
        (5112, 'INPUT', '', 1, 'ONE', 5012, 'input data'),
        (5212, 'OUTPUT', '', 1, 'ONE', 5012, 'output data'),
        #Flatten
        (5113, 'INPUT', '', 1, 'ONE', 5013, 'input data'),
        (5213, 'OUTPUT', '', 1, 'ONE', 5013, 'output data'),
        #Convolution2D
        (5121, 'INPUT', '', 1, 'ONE', 5021, 'input data'),
        (5221, 'OUTPUT', '', 1, 'ONE', 5021, 'output data'),
        #ZeroPadding2D
        (5122, 'INPUT', '', 1, 'ONE', 5022, 'input data'),
        (5222, 'OUTPUT', '', 1, 'ONE', 5022, 'output data'),
        #MaxPooling2D
        (5131, 'INPUT', '', 1, 'ONE', 5031, 'input data'),
        (5231, 'OUTPUT', '', 1, 'ONE', 5031, 'output data'),
        #LSTM
        (5141, 'INPUT', '', 1, 'ONE', 5041, 'input data'),
        (5241, 'OUTPUT', '', 1, 'ONE', 5041, 'output data'),
        #SimpleRNN
        (5142, 'INPUT', '', 1, 'ONE', 5042, 'input data'),
        (5242, 'OUTPUT', '', 1, 'ONE', 5042, 'output data'),
        #BatchNormalization
        (5151, 'INPUT', '', 1, 'ONE', 5051, 'input data'),
        (5251, 'OUTPUT', '', 1, 'ONE', 5051, 'output data'),
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
        #Dense
        (5111, 1),
        (5211, 1),
        #Dropout
        (5112, 1),
        (5212, 1),
        #Flatten
        (5113, 1),
        (5213, 1),
        #Convolution2D
        (5121, 1),
        (5221, 1),
        #ZeroPadding2D
        (5122, 1),
        (5222, 1),
        #MaxPooling2D
        (5131, 1),
        (5231, 1),
        #LSTM
        (5141, 1),
        (5241, 1),
        #SimpleRNN
        (5142, 1),
        (5242, 1),
        #BatchNormalization
        (5151, 1),
        (5251, 1),
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
        (5111, "en", 'input data', 'Input data'),
        (5211, "en", 'output data', 'Output data'),
        (5112, "en", 'input data', 'Input data'),
        (5212, "en", 'output data', 'Output data'),
        (5113, "en", 'input data', 'Input data'),
        (5213, "en", 'output data', 'Output data'),

        (5121, "en", 'input data', 'Input data'),
        (5221, "en", 'output data', 'Output data'),
        (5122, "en", 'input data', 'Input data'),
        (5222, "en", 'output data', 'Output data'),

        (5131, "en", 'input data', 'Input data'),
        (5231, "en", 'output data', 'Output data'),

        (5141, "en", 'input data', 'Input data'),
        (5241, "en", 'output data', 'Output data'),
        (5142, "en", 'input data', 'Input data'),
        (5242, "en", 'output data', 'Output data'),

        (5151, "en", 'input data', 'Input data'),
        (5251, "en", 'output data', 'Output data'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 5111 AND 5251'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 5111 AND 5251'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 5111 AND 5251'),
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

