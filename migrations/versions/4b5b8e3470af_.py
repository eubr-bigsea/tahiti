"""empty message

Revision ID: 4b5b8e3470af
Revises: 49be2ac6780f
Create Date: 2018-07-25 14:43:04.132217

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column,text


# revision identifiers, used by Alembic.
revision = '4b5b8e3470af'
down_revision = '49be2ac6780f'
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
        column('form_id', Integer), )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [
        (3113, 'attributes', 'TEXT',   0, 4, None, 'attribute-selector', None, None, 'EXECUTION', 3031),
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

    columns = ('id', 'locale', 'label', 'help')
    data = [
		(3113, 'en', 'Attributes', 'List of selected shapefile attributes (without polygon field).'),
		(3113, 'pt', 'Atributos', 'Lista dos atributos para selecionar do shapefile.'),
	]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

all_commands = [
    ("""
    UPDATE operation_platform SET operation_id=3030 WHERE operation_id=16 AND platform_id=4;
    """,
    """
    UPDATE operation_platform SET operation_id=16 WHERE operation_id=3030 AND platform_id=4;
    """),
    (_insert_operation_form_field,
        'DELETE FROM operation_form_field WHERE id = 3113'),

	(_insert_operation_form_field_translation,
        'DELETE FROM operation_form_field_translation WHERE id = 3113' ),
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
