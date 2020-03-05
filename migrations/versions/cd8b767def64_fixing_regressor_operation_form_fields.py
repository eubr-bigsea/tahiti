"""Fixing regressor operation form fields

Revision ID: cd8b767def64
Revises: 9fb9c50cf31c
Create Date: 2020-02-20 14:22:27.014135

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json

# revision identifiers, used by Alembic.
revision = 'cd8b767def64'
down_revision = '9fb9c50cf31c'
branch_labels = None
depends_on = None

def _insert_operation_form_field_linear_regression():
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
        column('form_id', Integer),
        column('enable_conditions', String),
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
    enable_condition = 'this.algorithm.internalValue === "ball_tree" or this.algorithm.internalValue === "kd_tree"'
    data = [
        (4342, 'fit_intercept', 'INTEGER', 0, 10, 0, 'checkbox', None, None, 'EXECUTION', 4007, None),
        (4343, 'positive', 'INTEGER', 0, 11, 0, 'checkbox', None, None, 'EXECUTION', 4007, None),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_form_field_translation_linear_regression():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = ('id', 'locale', 'label', 'help')
    data = [
        (4342, 'en', 'Fit intercept', 'Whether the intercept should be estimated or not.'),
        (4342, 'pt', 'Considerar intercepto', 'Estimar, ou não o intercepto.'),

        (4343, 'en', 'Positive coefficients', 'Forces the coefficients to be positive.'),
        (4343, 'pt', 'Coeficientes positivos', 'Força os coeficientes a serem positivos.')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _reinsert_operation_form_field_gradient_boosting():
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
        column('form_id', Integer),
        column('enable_conditions', String),
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
    enable_condition = 'this.algorithm.internalValue === "ball_tree" or this.algorithm.internalValue === "kd_tree"'
    data = [
        (4030, 'presort', 'INTEGER', 0, 4, 0, 'checkbox', None, None, 'EXECUTION', 4006, None)
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _reinsert_operation_form_field_translation_gradient_boosting():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = ('id', 'locale', 'label', 'help')
    data = [
        (4030, 'en', 'Presort', 'Wheter to presort the data to speed up the finding of best splits in fitting.'),
        (4030, 'pt', 'Pré-ordenar', 'Se deve pré-ordenar os dados para acelerar a busca das melhores divisões no ajuste.')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_form_field_gradient_boosting():
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
        column('form_id', Integer),
        column('enable_conditions', String),
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
    enable_condition = 'this.algorithm.internalValue === "ball_tree" or this.algorithm.internalValue === "kd_tree"'
    data = [
        (4030, 'cc_alpha', 'DECIMAL', 0, 23, 0.0, 'decimal', None, None, 'EXECUTION', 4006, None)

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_form_field_translation_gradient_boosting():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = ('id', 'locale', 'label', 'help')
    data = [
        (4030, 'en', 'Cost Complexity Alpha', 'Complexity parameter used for Minimal Cost-Complexity Pruning.'),
        (4030, 'pt', 'Custo de Complexidade Alpha', 'Parâmetro de complexidade usado na poda mínima de custo de complexidade.')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    #Linear Regression
    ("""DELETE FROM operation_operation_form 
            WHERE operation_id=4027 AND operation_form_id=4022""",
    """INSERT INTO operation_operation_form (operation_id, operation_form_id)
            VALUES (4027, 4022)""" ),
    ("""INSERT INTO operation_operation_form (operation_id, operation_form_id)
            VALUES (4027, 4021)""",
    """DELETE FROM operation_operation_form 
            WHERE operation_id=4027 AND operation_form_id=4021"""),
    ("""UPDATE operation_form_field 
            SET `order` = (`order` + 3)
	    WHERE id BETWEEN 4033 AND 4038""",
    """UPDATE operation_form_field 
            SET `order` = (`order` - 3)
	    WHERE id BETWEEN 4033 AND 4038"""),
    (_insert_operation_form_field_linear_regression,
    'DELETE FROM operation_form_field WHERE id BETWEEN 4342 AND 4343'),
    (_insert_operation_form_field_translation_linear_regression,
    'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4342 AND 4343'),

    #Gradiente Boosting
    ('DELETE FROM operation_form_field WHERE id = 4030',
    _reinsert_operation_form_field_gradient_boosting),
    ('DELETE FROM operation_form_field_translation WHERE id=4030',
    _reinsert_operation_form_field_translation_gradient_boosting),
    (_insert_operation_form_field_gradient_boosting,
    'DELETE FROM operation_form_field WHERE id=4030'),
    (_insert_operation_form_field_translation_gradient_boosting,
    'DELETE FROM operation_form_field_translation WHERE id=4030')
]

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
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
