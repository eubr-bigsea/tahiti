# -*- coding: utf-8 -*-

"""
Updating the COMPSs Operations and adding new ones.


(COMPSs Operations)

Revision ID: abc9192ljsj3
Revises: abc0603ljsj2
Create Date: 2017-10-27 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column,text


# revision identifiers, used by Alembic.
revision = 'abc9192ljsj3'
down_revision = 'abc0603ljsj2'
branch_labels = None
depends_on = None

def _insert_operation():
    tb = table('operation',
                            column("id", Integer),
                            column("slug", String),
                            column('enabled', Integer),
                            column('type', String),
                            column('icon', String),
                            )
    columns = ['id', 'slug', 'enabled', 'type', 'icon']
    data = [
        (3032, 'pca',1, 'TRANSFORMATION', 'fa-arrows-h'),

    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_new_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (3032, 3),#pca
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_id', 'operation_category_id')
    data = [
		    (3032, 8),#pca
			(3032, 23),
			(3032, 3001),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        (3032, 1, 1, 'execution'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(operation_form_table, rows)

def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
		(3032, 'pt', 'Execução'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)

def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        #pca
		(3032, 39),
		(3032, 40),
		(3032, 41),
		(3032, 43),
		(3032, 110),
		(3032,3032),


    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (3032,'en','PCA',
            'Principal component analysis (PCA) is a statistical procedure that reduce the dimensionality.'),
        (3032,'pt','PCA',
            'Principal componente de análise (PCA) é um procedimento estatistico capaz de reduzir a dimensionalidade dos dados.'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

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
            (3064, 'INPUT', None, 3032, 1, 'ONE','input data'),
            (3065, 'OUTPUT', None, 3032, 1, 'MANY','output data'),
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

            #pca
            (3064, 'en', 'input data', 'Input Data'),
		    (3064, 'pt', 'dados de entrada', 'Dados de entrada'),
            (3065, 'en', 'output data','Output Data'),
			(3065, 'pt', 'dados de saída','Dados de saída'),
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
        (3064, 1),#pca
        (3065, 1),

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
		#pca
        (3108,'attributes','TEXT',1,0,None,'attribute-selector',None,None,'EXECUTION',3032),
        (3109, 'aliases','TEXT',0,1, 'feature_PCA','text',None,None,'EXECUTION', 3032),
        (3110,'NComponents','INTEGER',1,3,2,'integer',None,None,'EXECUTION',3032),

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
		#pca
        (3108,'en','Feature','Feature to reduce the dimensionality.'),
        (3108,'pt','Feature','Feature para reduzir a dimensionalidade.'),
        (3109, 'en', 'Alias', 'Alias to the new feature.'),
        (3109, 'pt', 'Alias', 'Nome para a nova coluna.'),
        (3110,'en','Number of components',
            'The PCA algorithm will try to reduce the dimensionality to this value.'),
        (3110,'pt','Número de componentes',
            'O algoritmo PCA irá tentar reduzir a dimensionalidade para esse valor.'),

	]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


#--------------------------------------------------------------------------------

all_commands = [

	(_insert_operation,
        'DELETE FROM operation WHERE id >= 3032'),
	(_insert_new_operation_platform,
        'DELETE FROM operation_platform WHERE operation_id >= 3032' ),
	(_insert_operation_category_operation,
        'DELETE FROM operation_category_operation WHERE operation_id >= 3032'),
	(_insert_operation_form,
        'DELETE FROM operation_form WHERE id >= 3032'),
	(_insert_operation_form_translation,
        'DELETE FROM operation_form_translation WHERE id >= 3032'),
	(_insert_operation_operation_form,
        'DELETE FROM operation_operation_form WHERE operation_id >= 3032'),
	(_insert_operation_translation,
    	'DELETE FROM operation_translation WHERE id >= 3032'),
	(_insert_operation_port,
        'DELETE FROM operation_port WHERE id >= 3064' ),
	(_insert_operation_port_translation,
        'DELETE FROM operation_port_translation WHERE id >= 3064' ),
	(_insert_operation_port_interface_operation_port,
        'DELETE FROM operation_port_interface_operation_port '
        'WHERE operation_port_id >= 3048'),
	(_insert_operation_form_field,
        'DELETE FROM operation_form_field WHERE id >= 3108'),
	(_insert_operation_form_field_translation,
        'DELETE FROM operation_form_field_translation WHERE id >= 3108' ),

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
