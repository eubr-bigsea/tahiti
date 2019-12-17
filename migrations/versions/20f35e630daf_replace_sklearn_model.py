# -*- coding: utf-8 -*-

"""Replacing load and save sklearn models.

Revision ID: 20f35e630daf
Revises: 7ab1651ce835
Create Date: 2019-11-29 11:22:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '20f35e630daf'
down_revision = '7ab1651ce835'
branch_labels = None
depends_on = None


def _updating_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (22, 4),
        (39, 4),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _downgrade_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (3026, 4),
        (3027, 4),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (4014, 1),
        (4015, 1),
        (4016, 20),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_updating_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE operation_id IN (22, 39) AND platform_id = 4'),
    ('DELETE FROM operation_platform '
     'WHERE operation_id IN (3026, 3027) AND platform_id = 4',
     _downgrade_operation_platform),
    ('DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (4014, 4015, 4016)', ''),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (4014, 4015, 4016)'),

]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                cmds = cmd[0].split(';')
                for new_cmd in cmds:
                    if new_cmd.strip():
                        connection.execute(new_cmd)
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
                cmds = cmd[1].split(';')
                for new_cmd in cmds:
                    if new_cmd.strip():
                        connection.execute(new_cmd)
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    session.commit()
