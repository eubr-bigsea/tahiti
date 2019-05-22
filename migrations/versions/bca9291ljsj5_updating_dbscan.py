# -*- coding: utf-8 -*-

"""
Updating the COMPSs Operations and adding new ones.


(COMPSs Operations)

Revision ID: bca9291ljsj5
Revises: bca9192ljsj4
Create Date: 2018-06-13 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column,text


# revision identifiers, used by Alembic.
revision = 'bca9291ljsj5'
down_revision = 'bca9192ljsj4'
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
        column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [
            (3067, 'INPUT', None, 3020, 1, 'ONE','input data'),
            (3068, 'OUTPUT', None, 3020, 1, 'MANY','output data'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_port_back():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('operation_id', Integer),
        column('order', Integer),
        column('multiplicity', String),
        column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [
            (3041, "OUTPUT", None, 3020, 1, "ONE", "algorithm")
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [

            #dbscan
            (3067, 'en', 'input data', 'Input Data'),
		    (3067, 'pt', 'dados de entrada', 'Dados de entrada'),
            (3068, 'en', 'output data','Output Data'),
			(3068, 'pt', 'dados de saída','Dados de saída'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_port_translation_back():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [

            #dbscan
            (3041, "en", "algorithm", "Clustering model"),
            (3041, "pt", "algoritmo", "Modelo de agrupamento")
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
        (3067, 1),
        (3068, 1),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_port_interface_operation_port_back():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (3041, 11),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

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
		#dbscan
        (3111, 'features', 'TEXT',   1, 3, None, 'attribute-selector', None, None, 'EXECUTION', 3020),
		(3112, 'prediction', 'TEXT', 0, 4, 'prediction', 'text', None, None, 'EXECUTION', 3020),

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
		(3111, 'en', 'Features', 'Feature'),
		(3111, 'pt', 'Atributos', 'Atributos'),
		(3112, 'en', 'Prediction attribute', 'Prediction attribute'),
		(3112, 'pt', 'Atributo para predição', 'Atributo para predição'),

	]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


#--------------------------------------------------------------------------------

all_commands = [

    ('DELETE FROM operation_port_interface_operation_port WHERE '
    'operation_port_id = 3041 AND operation_port_interface_id = 11;',
    _insert_operation_port_interface_operation_port_back),

    ('DELETE FROM operation_port_translation WHERE id = 3041;',
    _insert_operation_port_translation_back),

    ('DELETE FROM operation_port WHERE id = 3041;',
    _insert_operation_port_back),

	(_insert_operation_port,
        'DELETE FROM operation_port WHERE id >= 3067' ),

	(_insert_operation_port_translation,
        'DELETE FROM operation_port_translation WHERE id >= 3067' ),

    (_insert_operation_port_interface_operation_port,
        'DELETE FROM operation_port_interface_operation_port WHERE '
        'operation_port_id >= 3066;'),

	(_insert_operation_form_field,
        'DELETE FROM operation_form_field WHERE id >= 3111'),

	(_insert_operation_form_field_translation,
        'DELETE FROM operation_form_field_translation WHERE id >= 3111' ),
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
