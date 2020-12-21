""" Change join  

Revision ID: faf6f1c74416
Revises: 5bf9db6d7909
Create Date: 2020-10-26 16:05:37.645929

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
import sqlalchemy as sa
import json



# revision identifiers, used by Alembic.
revision = 'faf6f1c74416'
down_revision = '5bf9db6d7909'
branch_labels = None
depends_on = None


BASE_FORM_FIELD_ID = 584
JOIN_FORM_ID = 16

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
        column('enable_conditions', String),
        column('form_id', Integer), )
    data = [
        [BASE_FORM_FIELD_ID, 'join_parameters', 'TEXT', 1, 0, None, 'join', 
            None, None, 'EXECUTION', None, JOIN_FORM_ID],
    ]
    columns = [c.name for c in tb.columns]
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
        [BASE_FORM_FIELD_ID, 'en', 'Join parameters', 'Allows to define parameters for the join.'],
        [BASE_FORM_FIELD_ID, 'pt', 'Parâmetros para a junção', 'Permite especificar parâmetros para a junção.'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

all_commands = [
        [_insert_operation_form_field, 
            'DELETE FROM operation_form_field WHERE id BETWEEN {s} AND {f}'.format(
                s=BASE_FORM_FIELD_ID, f=BASE_FORM_FIELD_ID)
        ],
        [_insert_operation_form_field_translation, 
            'DELETE FROM operation_form_field_translation  WHERE id BETWEEN {s} AND {f}'.format(
                s=BASE_FORM_FIELD_ID, f=BASE_FORM_FIELD_ID)
        ],
        [
            'UPDATE operation_form_field SET form_id = NULL WHERE id in (11, 12, 13, 362)',
            'UPDATE operation_form_field SET form_id = {} WHERE id in (11, 12, 13, 362)'.format(
                JOIN_FORM_ID),
        ],
        [
            'UPDATE operation_form_field SET `order`=1 WHERE id IN (14, 15) ',
            'UPDATE operation_form_field SET `order`=0 WHERE id IN (14, 15) ',
        ],
        [
            'UPDATE operation_script SET body="joinSuffixDuplicatedAttributes2(task);"  WHERE operation_id=16 ',
            'UPDATE operation_script SET body="joinSuffixDuplicatedAttributes(task);"  WHERE operation_id=16 ',
        ],

]

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()
    cursor = connection.execute('SELECT id, forms from task WHERE operation_id = 16')
    for row in cursor:
        form = json.loads(row[1])
        if 'left_attributes' in form and 'right_attributes' in form:

            conditions = [{'first': f, 'second': s} for (f, s) in 
                    zip(form['left_attributes']['value'], form['right_attributes']['value'])]
            aliases = [x.strip() for x in form.get('aliases', {'value': ''})['value'].split(',')]
            form['join_parameters'] = {
                'value': {
                    'joinType': form.get('join_type', {}).get('value', 'inner'),
                    'firstPrefix': aliases[0],
                    'secondPrefix': aliases[1] if len(aliases) > 1 else '',
                    'firstSelect': [],
                    'conditions': conditions,
                    'firstSelectionType': 1,
                    'secondSelectionType': 1,
                    'secondSelect': [],
                }
            }
            connection.execute('UPDATE task set forms = %s WHERE id = %s',
                    [json.dumps(form), row[0]])
            session.commit()
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
