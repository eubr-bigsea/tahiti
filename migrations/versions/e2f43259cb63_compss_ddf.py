# -*- coding: utf-8 -*-

"""Adding Scikit-learn Operations

Revision ID: e2f43259cb63
Revises: 97a1b6042100
Create Date: 2019-10-31 14:49:13.555626

"""
from alembic import context
from alembic import op
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String, Integer, Text
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = 'e2f43259cb63'
down_revision = '3334e8c55632'
branch_labels = None
depends_on = None

COMPSS_PLATFORM = 3
ID_PORT = 3070


def _add_operations_platform_from_spark():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (27, COMPSS_PLATFORM),  # replace-value
        (18, COMPSS_PLATFORM),  # data-reader
        (30, COMPSS_PLATFORM),  # data-writer
        (42, COMPSS_PLATFORM),  # apply-model
        (75, COMPSS_PLATFORM),  # one-hot-encoder
        (51, COMPSS_PLATFORM),  # generate-n-grams
        (35, COMPSS_PLATFORM),  # visualizations
        (68, COMPSS_PLATFORM),  # visualizations
        (69, COMPSS_PLATFORM),  # visualizations
        (70, COMPSS_PLATFORM),  # visualizations
        (71, COMPSS_PLATFORM),  # visualizations
        (80, COMPSS_PLATFORM),  # visualizations
        (81, COMPSS_PLATFORM),  # visualizations
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _adding_new_machine_learning_ports():
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
    data = []
    tmp = ID_PORT
    for id_op in [3005, 3006, 3007, 3008, 3009, 3013]:
        data.append((tmp, 'INPUT', None, id_op, 1,  'ONE', 'train input data'))
        tmp += 1
        data.append((tmp, 'OUTPUT', None, id_op, 2,  'MANY', 'model'))
        tmp += 1
        data.append((tmp, 'OUTPUT', None, id_op, 1, 'MANY', 'output data'))
        tmp += 1

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (3070, 1),
        (3071, 2),
        (3072, 1),

        (3073, 1),
        (3074, 2),
        (3075, 1),

        (3076, 1),
        (3077, 2),
        (3078, 1),

        (3079, 1),
        (3080, 2),
        (3081, 1),

        (3082, 1),
        (3083, 2),
        (3084, 1),

        (3085, 1),
        (3086, 2),
        (3087, 1),
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
    data = []
    tmp = ID_PORT
    for _ in range(6):
        data.append((tmp, 'en', 'train input data', 'Train input data'))
        data.append((tmp, 'pt', 'entrada do treino', 'Train input data'))
        tmp += 1
        data.append((tmp, 'en', 'model', 'Output model'))
        data.append((tmp, 'pt', 'modelo', 'Output model'))
        tmp += 1
        data.append((tmp, 'en', 'output data', 'Output data'))
        data.append((tmp, 'pt', 'dados de saída', 'Dados de saída'))
        tmp += 1

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    # fixing word-vector
    ("DELETE FROM `operation_category_operation` "
     "WHERE operation_id=3004 AND operation_category_id=16;", ""),
    ("INSERT INTO `operation_category_operation` "
     "VALUES (3004, 32), (3004, 37);", ""),
    ("UPDATE `operation_translation` "
     "SET name='Count term frequency' WHERE id=3004 AND locale='en';", ""),
    ("UPDATE `operation_translation` "
     "SET name='Contar frequencia dos termos' WHERE id=3004 AND locale='pt';",
     ""),

    # updating evaluate-model
    ("DELETE FROM `operation_category_operation` "
     "WHERE operation_id=3010 AND operation_category_id IN (8, 26);",
     ""),
    ("INSERT INTO `operation_category_operation` VALUES (3010, 40); ",
     ""),
    ("DELETE FROM `operation_port_translation` WHERE id IN (3015, 3016);", ''),
    ("DELETE FROM `operation_port_interface_operation_port` "
     "WHERE operation_port_id IN (3015, 3016);", ''),
    ("DELETE FROM `operation_port` WHERE id IN (3015, 3016);", ''),

    # desabling some compss boxes to use spark versions
    ('UPDATE operation SET enabled = 0 '
     'WHERE id IN (3001, 3002, 3011, 3015, 3016, 3018, 3019)',
     'UPDATE operation SET enabled = 1 '
     'WHERE id IN (3001, 3002, 3011, 3015, 3016, 3018, 3019)'),

    # adding feature and label to compss machine learning algorithms
    ("""
    INSERT INTO operation_operation_form (`operation_id`, `operation_form_id`) 
        VALUES ('3009', '3016'), ('3005', '3018'), ('3006', '3018'), 
        ('3007', '3018'), ('3008', '3018'), ('3013', '3018');
    """,
     'DELETE FROM `operation_operation_form` '
     'WHERE operation_id IN (3005, 3006, 3007, 3008, 3013, 3009) AND '
     'operation_form_id IN (3018, 3016); '
     ),

    # removing old compss machine learning algorithms ports
    ("DELETE FROM `operation_port_translation` "
     "WHERE id IN (3008, 3009, 3010, 3011, 3012, 3021);", ''),
    ("DELETE FROM `operation_port_interface_operation_port` "
     "WHERE operation_port_id IN (3008, 3009, 3010, 3011, 3012, 3021);", ''),
    ("DELETE FROM `operation_port`  "
     "WHERE operation_id IN (3005, 3006, 3007, 3008, 3009, 3013);", ''),

    # adding new compss machine learning algorithms ports
    (_adding_new_machine_learning_ports,
     "DELETE FROM operation_port WHERE id BETWEEN {} AND 3087;".format(
             ID_PORT)),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM `operation_port_interface_operation_port` '
     'WHERE operation_port_id >= {}'.format(ID_PORT)),
    (_insert_operation_port_translation,
     'DELETE FROM `operation_port_translation` WHERE id >= {}'
     .format(ID_PORT)),

    # adding new operations from spark
    (_add_operations_platform_from_spark,
     ''),
    ("DELETE FROM `operation_platform` "
     "WHERE operation_id=41 AND platform_id=3;",
     "INSERT INTO `operation_platform` VALUES (41, 3);"),

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
