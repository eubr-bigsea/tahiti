# -*- coding: utf-8 -*-}
"""Adding missing port interfaces

Revision ID: 38745782554d
Revises: b2b823fe47b1
Create Date: 2017-06-07 15:16:30.224298

"""

from alembic import op
from sqlalchemy import Integer, String
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '38745782554d'
down_revision = 'b2b823fe47b1'
branch_labels = None
depends_on = None

data = [
    (34, 5),
    (55, 1),
    (56, 1),
    (57, 11),
    (37, 2),
    (37, 18),

    # (46, 2),
    # (46, 18),

    (63, 1),
    (64, 1),
    (73, 19),
    (100, 2),
    (100, 19),
    (161, 17)
]


def upgrade():
    try:

        op.execute(text('START TRANSACTION'))
        insert_operation_port_interface()
        insert_operation_port_interface_translation()
        insert_operation_port_interface_operation_port()
        insert_operation_platform()
        insert_operation_translation()

    except:
        op.execute(text('ROLLBACK'))
        raise


def insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )
    columns = ('id', 'locale', 'name', 'description')

    rows_data = [
        (73, 'en', 'Regression Model', 'Regression Model'),
        (73, 'pt', 'Modelo de Regressão', 'Modelo de Regressão'),
        (74, 'en', 'Isotonic Regression', 'Isotonic Regression'),
        (74, 'pt', 'Regressão Isotônica', 'Regressão Isotônica'),
        (75, 'en', 'One Hot Encoder',
         'One hot encoding transforms categorical '
         'features to a format that works better with '
         'classification and regression algorithms.'),
        (75, 'pt', 'One Hot Encoder',
         'One Hot encoding é uma transformação que fazemos nos '
         'dados para representarmos uma variável categórica de '
         'forma binária (indica presença ou ausência de um valor).'),
        (76, 'en', 'AFT Survival Regression',
         'Accelerated Failure Time (AFT) Model Survival Regression'),
        (76, 'pt', 'Regressão AFT Survival',
         'Accelerated Failure Time (AFT) Model Survival Regression'),
        (77, 'en', 'GBT Regressor',
         'Gradient-Boosted Trees (GBTs) learning algorithm for '
         'regression. It supports both continuous and categorical featur'),
        (77, 'pt', 'Regressor GBT',
         'Gradient-Boosted Trees (GBTs) learning algorithm for '
         'regression. It supports both continuous and categorical feature'),
        (78, 'en', 'Random Forest Regressor',
         'Random Forest learning algorithm for regression. '
         'It supports both continuous and categorical features.'),
        (78, 'pt', 'Regressor Random Forest',
         'Random Forest learning algorithm for regression. '
         'It supports both continuous and categorical features.'),
        (79, 'en', 'Generalized Linear Regressor',
         'Generalized Linear Regressor'),
        (79, 'pt', 'Regressor Linear Generalizado',
         'Regressor Linear Generalizado'),
    ]
    rows = [dict(list(zip(columns, row))) for row in rows_data]

    op.bulk_insert(tb, rows)


def insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')
    rows_data = [
        (73, 1),
        (74, 1),
        (75, 1),
        (76, 1),
        (77, 1),
        (78, 1),
        (79, 1),

    ]
    rows = [dict(list(zip(columns, row))) for row in rows_data]

    op.bulk_insert(tb, rows)


def insert_operation_port_interface():
    tb = table(
        'operation_port_interface',
        column('id', Integer),
        column('color', String), )

    columns = ('id', 'color')
    interface_data = [
        (19, '#AACC22')
    ]
    rows = [dict(list(zip(columns, row))) for row in interface_data]

    op.bulk_insert(tb, rows)


def insert_operation_port_interface_translation():
    tb = table(
        'operation_port_interface_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String), )

    columns = ('id', 'locale', 'name')
    interface_data = [
        (19, 'pt', 'Visualização'),
        (19, 'en', 'Visualization'),
    ]
    rows = [dict(list(zip(columns, row))) for row in interface_data]

    op.bulk_insert(tb, rows)


def insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = ('operation_port_id', 'operation_port_interface_id')

    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def downgrade():
    try:
        for d in data:
            op.execute(
                text('DELETE FROM '
                     'operation_port_interface_operation_port '
                     'WHERE operation_port_id = {} '
                     '  AND operation_port_interface_id = {}'.format(*d)))
        op.execute(text('DELETE FROM operation_port_interface_translation '
                        'WHERE id = 19'))
        op.execute(text('DELETE FROM operation_port_interface '
                        'WHERE id = 19'))
        op.execute(text('DELETE FROM operation_platform '
                        'WHERE operation_id BETWEEN 73 AND 79'))

        op.execute(text('DELETE FROM operation_translation '
                        'WHERE id BETWEEN 73 AND 79'))
    except:
        op.execute(text('ROLLBACK'))
        raise
