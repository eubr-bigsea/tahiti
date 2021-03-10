"""adding cross evaluation in sklearn

Revision ID: 21de6c275230
Revises: e60c72ccb127
Create Date: 2021-03-09 16:47:05.549578

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
revision = '21de6c275230'
down_revision = 'e60c72ccb127'
branch_labels = None
depends_on = None


FIELD_ID = 4377
FORM_FIELD = 4046


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        # form for cross validation (classification)
        (FORM_FIELD, 1, 1, 'execution'),
        # form for cross validation (regression)
        (FORM_FIELD + 1, 1, 1, 'execution'),
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
        (FORM_FIELD, 'en', 'Execution'),
        (FORM_FIELD, 'pt', 'Execução'),
        (FORM_FIELD + 1, 'en', 'Execution'),
        (FORM_FIELD + 1, 'pt', 'Execução'),
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

        (4021, FORM_FIELD),
        (4022, FORM_FIELD),
        (4023, FORM_FIELD),
        (4024, FORM_FIELD),
        (4025, FORM_FIELD),
        (4031, FORM_FIELD),
        (4032, FORM_FIELD),
        (4034, FORM_FIELD),
        (4036, FORM_FIELD),

        (4026, FORM_FIELD + 1),
        (4027, FORM_FIELD + 1),
        (4028, FORM_FIELD + 1),
        (4029, FORM_FIELD + 1),
        (4030, FORM_FIELD + 1),
        (4035, FORM_FIELD + 1),
        (4038, FORM_FIELD + 1),
        (4046, FORM_FIELD + 1),

        (4038, 4021)

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
            column('form_id', Integer),
            column('enable_conditions', Integer),
    )
    columns = [c.name for c in tb.columns]
    data = [

        (FIELD_ID, "apply_cross_validation", "INTEGER", 0, 20, 0,
         "checkbox", None, None, "EXECUTION", FORM_FIELD, None),

        (FIELD_ID + 1, 'metric_cross_validation', 'INTEGER', 0, 21,
         'f1_weighted', 'dropdown', None, json.dumps([
            {'key': 'balanced_accuracy', 'value': 'Balanced accuracy'},
            {'key': 'f1_weighted', 'value': 'F1 weighted'},
            {'key': 'precision_weighted', 'value': 'Weighted Precision'},
            {'key': 'recall_weighted', 'value': 'Weighted Recall'},
            {'key': 'jaccard_weighted', 'value': 'Weighted Jaccard'},
            {'key': 'roc_auc', 'value': 'Area Under ROC (if binary)'},
            ]), 'EXECUTION',
         FORM_FIELD, "this.apply_cross_validation.internalValue === '1'"),

        (FIELD_ID+2, "folds", "INTEGER", 0, 22, 3, "integer", None, None,
         "EXECUTION", FORM_FIELD,
         "this.apply_cross_validation.internalValue === '1'"),

        (FIELD_ID+3, "apply_cross_validation", "INTEGER", 0, 20, 0,
         "checkbox", None, None, "EXECUTION", FORM_FIELD+1, None),

        (FIELD_ID + 4, 'metric_cross_validation', 'INTEGER', 0, 21,
         'r2', 'dropdown', None, json.dumps([
            {'key': 'explained_variance', 'value': 'Explained variance'},
            {'key': 'max_error', 'value': 'Maximum residual error'},
            {'key': 'neg_mean_absolute_error', 'value': 'Mean absolute error'},
            {'key': 'neg_mean_squared_error', 'value': 'Mean squared error'},
            {'key': 'neg_root_mean_squared_error',
             'value': 'Mean root squared error'},
            {'key': 'neg_mean_squared_log_error',
             'value': 'Mean squared logarithmic error'},
            {'key': 'neg_median_absolute_error',
             'value': 'Median absolute error'},
            {'key': 'r2', 'value': 'R^2 (coefficient of determination)'},
            ]), 'EXECUTION',
         FORM_FIELD+1, "this.apply_cross_validation.internalValue === '1'"),

        (FIELD_ID + 5, "folds", "INTEGER", 0, 22, 3, "integer", None, None,
         "EXECUTION", FORM_FIELD+1,
         "this.apply_cross_validation.internalValue === '1'"),

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

        (FIELD_ID, "en", "Perform cross-validation",
         "Perform cross-validation"),
        (FIELD_ID, 'pt', "Realizar a validação cruzada",
         "Realizar a validação cruzada"),

        (FIELD_ID + 1, "en", "Metric for applying cross-validation",
         "If informed, this metric will be used and cross-validation will be "
         "executed."),
        (FIELD_ID + 1, "pt", "Métrica para validação cruzada",
         "Se informada, essa métrica será usada e a validação cruzada será "
         "executada"),

        (FIELD_ID + 2, "en", "Attribute with fold number",
         "Contains the fold number for the row"),
        (FIELD_ID + 2, "pt", "Atributo com o número da partição (fold)",
         "Contém o número da partição para a linha"),

        (FIELD_ID + 3, "en", "Perform cross-validation",
         "Perform cross-validation"),
        (FIELD_ID + 3, 'pt', "Realizar a validação cruzada",
         "Realizar a validação cruzada"),

        (FIELD_ID + 4, "en", "Metric for applying cross-validation",
         "If informed, this metric will be used and cross-validation will be "
         "executed."),
        (FIELD_ID + 4, "pt", "Métrica para validação cruzada",
         "Se informada, essa métrica será usada e a validação cruzada será "
         "executada"),

        (FIELD_ID + 5, "en", "Attribute with fold number",
         "Contains the fold number for the row"),
        (FIELD_ID + 5, "pt", "Atributo com o número da partição (fold)",
         "Contém o número da partição para a linha"),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation_form,
     "DELETE FROM operation_form WHERE id IN ({}, {})"
     .format(FORM_FIELD, FORM_FIELD + 1)),
    (_insert_operation_form_translation,
     "DELETE FROM operation_form_translation WHERE id IN ({}, {})"
     .format(FORM_FIELD, FORM_FIELD + 1)),

    (_insert_operation_operation_form,
     "DELETE FROM operation_operation_form "
     "WHERE operation_id IN (4021, 4022, 4023, 4024, 4025, 4026, 4027, 4028, "
     "4029, 4030, 4031, 4032, 4034, 4035, 4036, 4038, 4046) and "
     "operation_form_id IN({}, {})"
     .format(FORM_FIELD, FORM_FIELD + 1)),

    (_insert_operation_form_field,
     "DELETE FROM operation_form_field WHERE id BETWEEN {} AND {}"
     .format(FIELD_ID, FIELD_ID + 5)),
    (_insert_operation_form_field_translation,
     "DELETE FROM operation_form_field_translation WHERE id BETWEEN {} AND {}"
     .format(FIELD_ID, FIELD_ID + 5)),

    # removing duplicated fields (feature, label, alias)
    ("DELETE FROM operation_form_field_translation "
     "WHERE id IN (4122, 4148, 4149, 4187, 4188, 4189, 4357, 4358, 4359)",
     ""),
    ("DELETE FROM operation_form_field "
     "WHERE id IN (4122, 4148, 4149, 4187, 4188, 4189,4357, 4358, 4359)", ""),

    # mae critirion is deprecated
    ("""
     UPDATE operation_form_field
     SET `values` = '{}' WHERE id = 4364
     """.format(json.dumps([
        {'key': 'friedman_mse',
         'value': 'Mean squared error with improvement score by Friedman'},
        {'key': 'mse', 'value': 'Mean squared error'}]
        )),
     """
     UPDATE operation_form_field 
     SET `values` = '{}' WHERE id = 4364
     """.format(json.dumps([
         {'key': 'friedman_mse',
          'value': 'Mean squared error with improvement score by Friedman'},
         {'key': 'mse', 'value': 'Mean squared error'},
         {'key': 'mae', 'value': 'Mean absolute error'}]
     ))),

]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                if len(cmd[0]) > 0:
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
                if len(cmd[1]) > 0:
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

