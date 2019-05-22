"""fix output ports with models

Revision ID: 910243d8f820
Revises: 500f09c2325d
Create Date: 2017-12-19 16:19:33.927563

"""
import json

from alembic import context
from alembic import op
from sqlalchemy import String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '910243d8f820'
down_revision = '500f09c2325d'
branch_labels = None
depends_on = None


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('operation_id', Integer),
        column('order', Integer),
        column('multiplicity', String),
        column('slug', String))

    all_ops = [
        (15, 'OUTPUT', None, 52, 3, 'MANY', 'vector-model'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    all_ops = [
        (15, 'en', 'vector model', 'Vector model'),
        (15, 'pt', 'modelo de vetores', 'Modelo de vetores'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (15, 20),
        (83, 20),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


new_values = [
    {"key": "count", "value": "Count term frequency"},
    {"key": "word2vec", "value": "Use word2vec algorithm"},
    {"key": "hashing_tf",
     "value": "Map the sequence of terms to their TF using hashing trick"},
]
old_values = [
    {"key": "count", "value": "Count term frequency"},
    {"key": "word2vec", "value": "Use word2vec algorithm"},
]


all_commands = [
    [_insert_operation_port, 'DELETE from operation_port WHERE id IN (15)'],
    [_insert_operation_port_translation,
     'DELETE from operation_port_translation WHERE id IN (15)'],
    [
        _insert_operation_port_interface_operation_port,
        'DELETE FROM operation_port_interface_operation_port '
        'WHERE operation_port_id IN (15, 83) '
        '   AND operation_port_interface_id = 20',
    ],
    [
        "UPDATE operation_form_field SET `values` = '{}' WHERE id = 123".format(
            json.dumps(new_values)),
        "UPDATE operation_form_field SET `values` = '{}' WHERE id = 123".format(
            json.dumps(old_values))
    ]
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
