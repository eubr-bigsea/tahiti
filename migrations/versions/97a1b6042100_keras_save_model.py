"""keras_save_model

Revision ID: 97a1b6042100
Revises: 49987ba6d4da
Create Date: 2019-07-04 08:45:07.141430

"""
import json

from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '97a1b6042100'
down_revision = '49987ba6d4da'
branch_labels = None
depends_on = None

MODEL_OP_ID = 5112
MODEL_OP_FORM_ID = 5241


def _insert_operation_form():
    tb = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (MODEL_OP_FORM_ID, 1, 1, 'save'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (MODEL_OP_ID, MODEL_OP_FORM_ID)
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = [c.name for c in tb.columns]
    data = [
        (MODEL_OP_FORM_ID, 'en', 'Save model'),
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
        column('form_id', Integer),
        column('enable_conditions', String),
    )

    overwrite_mode = [
        {"en": "Overwrite", "key": "OVERWRITE", "value": "Overwrite",
         "pt": "Sobrescrever"},
        {"en": "Raise error", "key": "ERROR", "value": "Raise error",
         "pt": "Gerar erro"}]

    columns = [c.name for c in tb.columns]
    enabled_condition = 'this.save_enabled.internalValue === "1"'

    subset = [{"en": "Validation", "key": "validation", "value": "Validation",
               "pt": "Validação"},
              {"en": "Training", "key": "training", "value": "Training",
               "pt": "Treino"}]

    data = [
        (5534, 'save_enabled', 'INTEGER', 1, 1, 0, 'checkbox', None, None,
         'EXECUTION', MODEL_OP_FORM_ID, None),

        (5535, 'storage', 'INTEGER', 1, 2, None, 'lookup',
         '`${LIMONERO_URL}/storages`', None, 'EXECUTION', MODEL_OP_FORM_ID,
         enabled_condition),

        (5536, 'save_name', 'TEXT', 1, 3, None, 'text',
         None, None, 'EXECUTION', MODEL_OP_FORM_ID, enabled_condition),

        (5537, 'action_if_exists', 'INTEGER', 1, 4, 0, 'dropdown', None,
         json.dumps(overwrite_mode), 'EXECUTION', MODEL_OP_FORM_ID,
         enabled_condition),

        (5538, 'save_only_weights', 'INTEGER', 1, 5, 0, 'checkbox', None, None,
         'EXECUTION', MODEL_OP_FORM_ID, enabled_condition),

        (5539, 'save_metrics', 'TEXT', 1, 6, None, 'select2', None,
         json.dumps([
             {"value": "Binary Accuracy", "key": "acc"},
             {"value": "Categorical Accuracy", "key": "acc"},
             {"value": "Cosine Proximity", "key": "cosine"},
             {"value": "Loss", "key": "loss"},
             {"value": "Mean Absolute Error", "key": "mae"},
             {"value": "Mean Absolute Percentage Error", "key": "mape"},
             {"value": "Mean Squared Error", "key": "mse"},
             {"value": "Sparse Categorical Accuracy",
              "key": "sparse_categorical_accuracy"},
             {"value": "Sparse Top k Categorical Accuracy",
              "key": "sparse_top_k_categorical_accuracy"},
             {"value": "Top k Categorical Accuracy",
              "key": "top_k_categorical_accuracy"},
         ]), 'EXECUTION', MODEL_OP_FORM_ID, enabled_condition),

        (5540, 'save_subset', 'INTEGER', 1, 7, 'validation', 'dropdown', None,
         json.dumps(subset), 'EXECUTION', MODEL_OP_FORM_ID,
         enabled_condition),
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

    columns = [c.name for c in tb.columns]
    data = [
        (5534, 'en', 'Save model', 'Enable saving model'),
        (5535, 'en', 'Storage', 'Where the model will be stored'),
        (5536, 'en', 'Name', 'The name for the model'),
        (5537, 'en', 'Action if model exists', 'Action if model exists'),
        (5538, 'en', 'Save only weights', 'Save only weights'),
        (5539, 'en', 'Metric to be monitored', 'Metric to be monitored'),
        (5540, 'en', 'Subset to be monitored', 'Subset to be monitored'),

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (
        _insert_operation_form,
        "DELETE FROM operation_form WHERE id = {}".format(MODEL_OP_FORM_ID)
    ),
    (
        _insert_operation_operation_form,
        "DELETE FROM operation_operation_form "
        "WHERE operation_form_id = {}".format(MODEL_OP_FORM_ID)
    ),
    (
        _insert_operation_form_translation,
        "DELETE FROM operation_form_translation WHERE id = {}".format(
            MODEL_OP_FORM_ID)
    ),
    (
        _insert_operation_form_field,
        "DELETE FROM operation_form_field WHERE form_id = {}".format(
            MODEL_OP_FORM_ID)
    ),
    (
        _insert_operation_form_field_translation,
        """DELETE FROM operation_form_field_translation WHERE id IN
          (SELECT id FROM operation_form_field WHERE form_id = {})""".format(
            MODEL_OP_FORM_ID)
    ),

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
