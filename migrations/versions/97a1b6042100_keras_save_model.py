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

metrics = [
    {"value": "Binary accuracy", "key": "binary_accuracy"},
    {"value": "Categorical accuracy", "key": "categorical_accuracy"},
    {"value": "Sparse categorical accuracy", "key": "sparse_categorical_accuracy"},
    # {"value": "Sparse top K categorical accuracy", "key": "sparse_top_k_categorical_accuracy"},
    # {"value": "Top K categorical accuracy", "key": "top_k_categorical_accuracy"},
]

monitor_metrics = [
    {"value": "Binary accuracy", "key": "binary_accuracy"},
    {"value": "Categorical accuracy", "key": "categorical_accuracy"},
    {"value": "Loss", "key": "loss"},
    {"value": "Sparse categorical accuracy", "key": "sparse_categorical_accuracy"}
]


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
               "pt": "Treino"},
              {"en": "Both", "key": "both", "value": "Both",
               "pt": "Ambos"}]

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

        (5538, 'save_weights_only', 'INTEGER', 1, 5, 0, 'checkbox', None, None,
         'EXECUTION', MODEL_OP_FORM_ID, enabled_condition),

        (5539, 'save_metrics', 'TEXT', 1, 6, None, 'select2', None,
         json.dumps(monitor_metrics), 'EXECUTION', MODEL_OP_FORM_ID, enabled_condition),

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


def _insert_operation_form_field_translation_model_upgrade():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (5467, 'en', 'Metrics', 'A metric is a function that is used to judge '
                                'the performance of your model.'),
        (5541, 'en', 'Classification report', 'Show the classification report.'),

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_field_translation_model_downgrade():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (5468, 'en', 'K', 'K is a parameter required for the metrics related '
                          'to the Top K Categorical Accuracy functions.'),

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_field_update():
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
        (5467, 'metrics', 'TEXT', 1, 3, "Categorical Accuracy", 'select2', None,
         json.dumps(metrics), 'EXECUTION', 5233),
        (5541, 'classification_report', 'INTEGER', 0, 21, 0, 'checkbox', None, None, 'EXECUTION', 5233),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_field_downgrade():
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
        (5467, 'metrics', 'TEXT', 1, 3, "Categorical Accuracy", 'select2', None,
         json.dumps([
             {"value": "Binary Accuracy", "key": "acc"},
             {"value": "Categorical Accuracy", "key": "acc"},
             {"value": "Cosine Proximity", "key": "cosine"},
             {"value": "Mean Absolute Error", "key": "mae"},
             {"value": "Mean Absolute Percentage Error", "key": "mape"},
             {"value": "Mean Squared Error", "key": "mse"},
             {"value": "Sparse Categorical Accuracy", "key": "sparse_categorical_accuracy"},
             {"value": "Sparse Top k Categorical Accuracy", "key": "sparse_top_k_categorical_accuracy"},
             {"value": "Top k Categorical Accuracy", "key": "top_k_categorical_accuracy"},
         ]), 'EXECUTION', 5233),
        (5468, 'k', 'INTEGER', 0, 4, 5, 'integer', None, None, 'EXECUTION', 5233),
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
    (
        """DELETE FROM operation_form_field WHERE id IN ({0}, {1}, {2})"""
            .format(5467, 5468, 5541),
        _insert_operation_form_field_downgrade
    ),
    (
        _insert_operation_form_field_update,
        """DELETE FROM operation_form_field WHERE id IN ({0}, {1}, {2})"""
            .format(5467, 5468, 5541),
    ),
    (
        _insert_operation_form_field_translation_model_upgrade,
        _insert_operation_form_field_translation_model_downgrade
    ),
    (
        "",
        """DELETE FROM operation_form_field_translation WHERE id = 5541"""
    )
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if cmd[0]:
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
