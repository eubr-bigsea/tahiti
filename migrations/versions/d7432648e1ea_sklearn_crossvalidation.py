# -*- coding: utf-8 -*-

"""Sklearn operations

Revision ID: d7432648e1ea
Revises: 5430536464c7
Create Date: 2018-09-13 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = 'd7432648e1ea'
down_revision = '5430536464c7'
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
        ('4018', 'execute-sql', '1', 'TRANSFORMATION', 'fa-bolt'),

    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_new_operation_platform():
    tb = table(
            'operation_platform',
            column('operation_id', Integer),
            column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [

        (18, 4),  # spark data-reader
        (43, 4),  # cross-validation
        (82, 4),  # execute-python
        (4018, 4),  # execute-sql

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
            'operation_category_operation',
            column('operation_id', Integer),
            column('operation_category_id', Integer))

    columns = ('operation_id', 'operation_category_id')
    data = [
        (4018, 4001),  # execute-sql
        (4018, 7),  # execute-sql
    ]

    rows = [dict(zip(columns, row)) for row in data]
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
        (4018, 1, 1, 'execution'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(operation_form_table, rows)


def _insert_operation_form_translation():
    tb = table(
            'operation_form_translation',
            column('id', Integer),
            column('locale', String),
            column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (4018, 'en', 'Execution'),
        (4018, 'pt', 'Execução'),
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
        (4018, 41),
        (4018, 110),
        (4018, 4018),
    ]

    rows = [dict(zip(columns, row)) for row in data]
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
        (4018, 'pt', 'Executar consulta SQL',
         'Executa uma consulta usando a linguagem SQL disponível no Pandas '
         'SQL.'),
        (4018, 'en', 'Execute SQL query',
         'Executes a query using SQL language available in Pandas SQL.')
    ]

    rows = [dict(zip(columns, row)) for row in data]
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
        (4025, 'INPUT', None, 4018, 1, 'ONE', 'input data 1 '),
        (4026, 'INPUT', None, 4018, 2, 'ONE', 'input data 2'),
        (4027, 'OUTPUT', None, 4018, 1, 'MANY', 'output data'),


    ]
    rows = [dict(zip(columns, row)) for row in data]
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
        (4025, 'en', 'input data 1', 'Input data 1'),
        (4025, 'pt', 'dados de entrada 1', 'Input data 1'),
        (4026, 'en', 'input data 2', 'Input data 2'),
        (4026, 'pt', 'dados de entrada 2', 'Input data 2'),
        (4027, 'en', 'output data', 'Output data'),
        (4027, 'pt', 'dados de saída', 'Dados de saída'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
            'operation_port_interface_operation_port',
            column('operation_port_id', Integer),
            column('operation_port_interface_id', Integer), )

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (4025, 1),
        (4026, 1),
        (4027, 1),
    ]
    rows = [dict(zip(columns, row)) for row in data]
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

        (4089, 'query', 'TEXT', 1, 1, None, 'code', None, None, 'EXECUTION',
         4018),
        (4090, 'names', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION',
         4018),

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

        (4089, 'en',
         'SQL Query, (inputs are available as tables named ds1 and ds2)',
         'SQL query compatible with SQLite sytanx. For more information, '
         'see https://www.sqlite.org/lang.html or '
         'https://github.com/yhat/pandasql.'),
        (4089, 'pt',
         'Consulta (entradas estão disponíveis como tabelas chamadas ds1 e '
         'ds2)',
         'Consulta SQL compatível com o Apache Spark. Para mais informações, '
         'veja https://www.sqlite.org/lang.html ou '
         'https://github.com/yhat/pandasql.'),
        (4090, 'en', 'Names of attributes after the query',
         'Name of the new attributes after executing the query (optional, '
         'helps attribute suggestion).'),
        (4090, 'pt', 'Nome dos novos atributos após a consulta',
         'Nome dos novos atributos após executar a consulta (opcional. auxilia '
         'na sugestão de atributos).'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation, 'DELETE FROM operation WHERE id = 4018'),
    (_insert_new_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 18 AND '
     'platform_id = 4;'
     'DELETE FROM operation_platform WHERE operation_id = 43 AND '
     'platform_id = 4;'
     'DELETE FROM operation_platform WHERE operation_id = 82 AND '
     'platform_id = 4;'
     'DELETE FROM operation_platform WHERE operation_id = 4018'
     ),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id = 4018'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id = 4018'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id = 4018'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4018'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = 4018'),
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4025 AND 4027'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4025 AND 4027'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE '
     'operation_port_id BETWEEN 4025 AND 4027'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4089 AND 4090'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4089 AND '
     '4090'),
    ("""
        DELETE FROM operation_platform WHERE operation_id = 3001 AND 
        platform_id = 4;
        
        UPDATE operation_category_operation 
        SET operation_category_id = 16
        WHERE operation_id = 3004 AND operation_category_id = 12; 
     """,
     """
        INSERT INTO operation_platform (operation_id, platform_id)
        VALUES (3001, 4);
     """),

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
