# coding=utf-8
"""empty message

Revision ID: 06a74bba9db8
Revises: abc1509ljsj2
Create Date: 2017-09-27 10:12:31.229528

"""
import json

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '06a74bba9db8'
down_revision = 'abc1509ljsj2'
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
    rows = (
        (93, 'execute-sql', 1, 'TRANSFORMATION', 'fa-flash'),

    )
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in
            rows]

    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (93, 'en', 'Execute SQL query',
         'Executes a query using SQL language available in Spark.'),
        (93, 'pt', 'Executar consulta SQL',
         'Executa uma consulta usando a linguagem SQL disponível no Spark.'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    rows = [
        (93, 1),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

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
        column('slug', String))

    rows = [
        (212, 'INPUT', None, 93, 1, 'ONE', 'input data 1'),
        (213, 'INPUT', None, 93, 1, 'ONE', 'input data 2'),
        (214, 'OUTPUT', None, 93, 1, 'MANY', 'output data'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (212, 'en', 'input data 1', 'Input data 1'),
        (212, 'pt', 'dados de entrada 1', 'Dados de entrada 1'),

        (213, 'en', 'input data 2', 'Input data 2'),
        (213, 'pt', 'dados de entrada 2', 'Dados de entrada 2'),

        (214, 'en', 'output data', 'Output data'),
        (214, 'pt', 'dados de saída', 'Dados de saída'),

    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (212, 1),
        (213, 1),
        (214, 1),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


def _insert_operation_script():
    tb = table(
        'operation_script',
        column('id', Integer),
        column('type', String),
        column('enabled', Integer),
        column('body', String),
        column('operation_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        [33, 'JS_CLIENT', 1, "copyAllInputsRemoveDuplicated(task, 'names');",
         93],
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (93, 1),
        (93, 7),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form():
    tb = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (118, 1, 1, 'execution'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (93, 118),
        (93, 110),
        (93, 41),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String)
    )

    columns = [c.name for c in tb.columns]
    data = [
        (118, 'en', 'Execution'),
        (118, 'pt', 'Execução'),
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

    columns = [c.name for c in tb.columns]

    data = [
        [364, 'query', 'TEXT', 1, 1, None, 'code', None, None,
         'EXECUTION', 118],
        [365, 'names', 'TEXT', 0, 2, None, 'text', None, None,
         'EXECUTION', 118],
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

    columns = [c.name for c in tb.columns]
    data = [
        [364, 'en',
         'SQL Query, (inputs are available as tables named ds1 and ds2)',
         'SQL query compatible with Apache Spark. For more information, see '
         'https://docs.databricks.com/spark/latest/spark-sql'
         '/language-manual/select.html or https://spark.apache.org/docs/latest/'
         'sql-programming-guide.html.'],
        [364, 'pt', 'Consulta (entradas estão disponíveis '
                    'como tabelas chamadas ds1 e ds2)',
         'Consulta SQL compatível com o Apache Spark. Para mais informações, '
         'veja https://docs.databricks.com/spark/latest/spark-sql'
         '/language-manual/select.html ou https://spark.apache.org/docs/latest/'
         'sql-programming-guide.html.'],

        [365, 'en', 'Names of attributes after the query',
         'Name of the new attributes after executing the query '
         '(optional, helps attribute suggestion).'],
        [365, 'pt', 'Nome dos novos atributos após a consulta',
         ('Nome dos novos atributos após executar a consulta '
          '(opcional. auxilia na sugestão de atributos).')],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


agg_functions = {
    "functions":
        [
            {"key": "avg", "value": "Average (AVG)",
             "help": "Computes the average of each group"},
            {"key": "collect_list", "value": "Collect List",
             "help": ("Aggregate function: returns a list of objects with "
                      "duplicates.")},
            {"key": "collect_set", "value": "Collect Set",
             "help": ("Aggregate function: returns a set of objects with "
                      "duplicate elements eliminated.")},
            {"key": "count", "value": "Count",
             "help": "Counts the total of records of each group"},
            {"key": "first", "value": "First",
             "help": "Returns the first element of group"},
            {"key": "last", "value": "Last",
             "help": "Returns the last element of group"},
            {"key": "max", "value": "Maximum (MAX)",
             "help": "Returns the max value of each group for one attribute"},
            {"key": "min", "value": "Minimum (MIN)",
             "help": "Returns the min value of each group for one attribute"},
            {"key": "sum", "value": "Sum",
             "help": "Returns the sum of values of each "
                     "group for one attribute"}
        ],
    "options": {
        "title": "Aggregate operation",
        "description": ("Add one of more lines with attribute to be used, "
                        "function and alias to compute aggregate "
                        "function over groups."),
        "show_alias": True}
}
agg_functions_old = {
    "functions":
        [
            {"key": "avg", "value": "Average (AVG)",
             "help": "Computes the average of each group"},
            {"key": "count", "value": "Count",
             "help": "Counts the total of records of each group"},
            {"key": "first", "value": "First",
             "help": "Returns the first element of group"},
            {"key": "last", "value": "Last",
             "help": "Returns the last element of group"},
            {"key": "max", "value": "Maximum (MAX)",
             "help": "Returns the max value of each group for one attribute"},
            {"key": "min", "value": "Minimum (MIN)",
             "help": "Returns the min value of each group for one attribute"},
            {"key": "sum", "value": "Sum",
             "help": "Returns the sum of values of each "
                     "group for one attribute"}
        ],
    "options": {
        "title": "Aggregate operation",
        "description": ("Add one of more lines with attribute to be used, "
                        "function and alias to compute aggregate "
                        "function over groups."),
        "show_alias": True}
}

all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN 93 AND 93'),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 93 AND 93'),
    (_insert_operation_port,
     'DELETE FROM operation_port '
     'WHERE (operation_id BETWEEN 93 AND 93)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE (operation_id BETWEEN 93 AND 93))'),
    (_insert_operation_script,
     [
         '''DELETE FROM operation_script WHERE operation_id BETWEEN 93 AND 93
         ''',
     ]
     ),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE (operation_id BETWEEN 93 AND 93))'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN 93 AND 93;'),
    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN 93 AND 93'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 118 AND 118'),
    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN 93 AND 93'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 118 AND 118'),
    (_insert_operation_form_field,
     """DELETE FROM operation_form_field
        WHERE (form_id BETWEEN 118 AND 118)"""),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE (form_id BETWEEN 118 AND 118))'),

    # Add new aggregation functions
    (
        """UPDATE operation_form_field SET `values` = '{}'
            WHERE id = 71 """.format(json.dumps(agg_functions)),
        """UPDATE operation_form_field SET `values` = '{}'
            WHERE id = 71 """.format(json.dumps(agg_functions_old)),
    )

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
