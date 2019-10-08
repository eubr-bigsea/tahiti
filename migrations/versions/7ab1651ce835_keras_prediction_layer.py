"""Keras - prediction layer

Revision ID: 7ab1651ce835
Revises: f98150821301
Create Date: 2019-10-03 15:51:03.476889

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
revision = '7ab1651ce835'
down_revision = 'f98150821301'
branch_labels = None
depends_on = None

PREDICTION_LAYER = 5123


def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('type', String),
        column('icon', Integer), )

    columns = ('id', 'slug', 'enabled', 'type', 'icon')
    data = [
        (PREDICTION_LAYER, "convolution-1d", 1, 'ACTION', ''),
    ]
    rows = [dict(zip(columns, row)) for row in data]

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
        (PREDICTION_LAYER, 'en', 'Predict', 'Generates predictions for '
                                                  'the input samples from a '
                                                  'data generator.'),
    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_category_id', 'operation_id')
    data = [
        # Convolutional Layers
        (5063, PREDICTION_LAYER),
    ]
    rows = [dict(zip(columns, row)) for row in data]

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
        column('slug', String), )

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        (5397, 'INPUT', '', 2, 'ONE', PREDICTION_LAYER, 'model'),
        (5398, 'INPUT', '', 1, 'ONE', PREDICTION_LAYER, 'generator'),
        (5399, 'OUTPUT', '', 1, 'MANY', PREDICTION_LAYER, 'output data'),

    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (5397, 22),
        (5398, 23),
        (5399, 1),
    ]
    rows = [dict(zip(columns, row)) for row in data]

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
        (5397, 'en', 'model', 'Model'),
        (5398, 'en', 'generator', 'Generator'),
        (5399, 'en', 'output data', 'Output data'),
    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        (PREDICTION_LAYER, 41),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE '
     'FROM operation '
     'WHERE id BETWEEN 5073 AND 5119'),
    (_insert_operation_translation,
     'DELETE '
     'FROM operation_translation '
     'WHERE id BETWEEN 5073 AND 5119'),
    (_insert_operation_category_operation,
     'DELETE '
     'FROM operation_category_operation '
     'WHERE operation_id BETWEEN 5073 AND 5119'),
    (_insert_operation_port,
     'DELETE '
     'FROM operation_port '
     'WHERE id BETWEEN 5173 AND 5210'),
    (_insert_operation_port_interface_operation_port,
     'DELETE '
     'FROM operation_port_interface_operation_port '
     'WHERE operation_port_id BETWEEN 5173 AND 5210'),
    (_insert_operation_port_translation,
     'DELETE '
     'FROM operation_port_translation '
     'WHERE id BETWEEN 5173 AND 5210'),
    (_insert_operation_operation_form,
     'DELETE '
     'FROM operation_operation_form '
     'WHERE operation_id IN (5021, 5022, 5031, 5051)'),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if cmd[0]:
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
            if cmd[1]:
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

