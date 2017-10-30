# coding=utf-8
"""Adding name to tasks

Revision ID: 049e8dab7779
Revises: 8aa2350c2118
Create Date: 2017-10-30 12:45:18.749118

"""
import json

import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '049e8dab7779'
down_revision = '8aa2350c2118'
branch_labels = None
depends_on = None


def add_name_to_task():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task',
                  sa.Column('name', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def remove_name_from_task():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'name')
    # ### end Alembic commands ###


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
        column('form_id', Integer), )

    columns = [c.name for c in tb.columns]

    values = [
        {"value": "danish", "key": "danish"},
        {"value": "dutch", "key": "dutch"},
        {"value": "english", "key": "english"},
        {"value": "finnish", "key": "finnish"},
        {"value": "french", "key": "french"},
        {"value": "german", "key": "german"},
        {"value": "hungarian", "key": "hungarian"},
        {"value": "italian", "key": "italian"},
        {"value": "norwegian", "key": "norwegian"},
        {"value": "portuguese", "key": "portuguese"},
        {"value": "russian", "key": "russian"},
        {"value": "spanish", "key": "spanish"},
        {"value": "swedish", "key": "swedish"},
        {"value": "turkish", "key": "turkish"}
    ]
    data = [
        [369, 'language', 'TEXT', 0, 5, None, 'dropdown', None,
         json.dumps(values), 'EXECUTION', 60],
    ]
    rows = [dict(zip(columns, row)) for row in data]
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
        [369, 'en', 'Language (optional)',
         'If informed, uses the default stop word list for the language.'],
        [369, 'pt', 'Idioma (opcional)',
         'Se informado, usa o conjunto de stop words padrão para o idioma.'],

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     """DELETE FROM operation_form_field
        WHERE (id BETWEEN 369 AND 369)"""),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE (id BETWEEN 369 AND 369))'),
    (add_name_to_task, remove_name_from_task,),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()
    try:
        for cmd in all_commands:
            if isinstance(cmd[0], (unicode, str)):
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
            if isinstance(cmd[1], (unicode, str)):
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
