# coding=utf-8
"""fix_may_2019

Revision ID: 69aa591d226b
Revises: f39f7e2623e3
Create Date: 2019-04-29 08:32:43.723078

"""
import json

import pymysql
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '69aa591d226b'
down_revision = 'f39f7e2623e3'
branch_labels = None
depends_on = None

metrics_new = [
    {
        "key": "areaUnderROC",
        "value": "Area under ROC curve (binary classification)",
        "en": "Area under ROC curve(binary classification)",
        "pt": "Área sob a curva ROC (classificação binária)"
    },
    {
        "key": "areaUnderPR",
        "value": "Area under precision-recall curve (binary classification)",
        "en": "Area under precision-recall curve (binary classification)",
        "pt": "Área sob a curva precisão-revocação"
    },
    {
        "key": "f1", "value": "F1 score (multiclass classification)",
        "en": "F1 score (multiclass classification)",
        "pt": "F1"
    },
    {
        "key": "weightedPrecision",
        "value": "Weighted precision (multiclass classification)",
        "en": "Weighted precision (multiclass classification)",
        "pt": "Precisão ponderada"
    },
    {
        "key": "weightedRecall",
        "value": "Weighted recall (multiclass classification)",
        "en": "Weighted recall (multiclass classification)",
        "pt": "Revocação ponderada"
    },
    {
        "key": "accuracy", "value": "Accuracy (multiclass classification)",
        "en": "Accuracy (multiclass classification)",
        "pt": "Acurácia"
    },
    {
        "key": "rmse", "value": "Root mean squared error  (regression)",
        "en": "Root mean squared error  (regression)",
        "pt": "Raíz do erro quadrático médio"
    },
    {
        "mse": "mse", "value": "Mean squared error (regression)",
        "en": "Mean squared error (regression)",
        "pt": "Erro quadrático médio"
    },
    {
        "key": "mae", "value": "Mean absolute error regression)",
        "en": "Mean absolute error (regression)",
        "pt": "Erro absoluto médio"
    }
]


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
        (501, 'perform_cross_validation', 'INTEGER', 0, 9, '0', 'checkbox',
         None, None, 'EXECUTION', 132),
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
        (501, 'en', 'Perform cross-validation',
         'Perform cross-validation (requires an attribute with fold information'),
        (501, 'pt', 'Realizar a validação cruzada',
         'Realizar a validação cruzada (requer um atributo com a informação de partição).')

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field where id = 501'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation where id = 501'),
    (
        """INSERT IGNORE INTO operation_form_field_translation
            (id, locale, label, `help`) VALUES
            (125, 'pt', 'Frequência mínima nos documentos (DF)',
                'Frequência mínima nos documentos (DF)')
        """,
        "DELETE FROM operation_form_field_translation "
        "WHERE locale = 'pt' AND id = 125"
    ),
    (
        """
        UPDATE operation_form_field_translation
        SET label = 'Atributo de saída', `HELP` = 'Atributo de saída'
        WHERE id = 422 AND locale = 'pt'
        """
        , ''
    ),
    ("""UPDATE operation_form_field SET `values` = '{}' WHERE `id` IN (101, 107, 487)
        """.format(pymysql.escape_string(json.dumps(metrics_new))),
     """UPDATE operation_form_field SET `values` = '{}' WHERE `id` IN (101, 107, 487)
     """.format(pymysql.escape_string(json.dumps(metrics_new)))),

    (
        """UPDATE operation_form_field SET enable_conditions =
        'this.perform_cross_validation.internalValue === "1"' WHERE id IN (487, 488)
        """, ''
    ),
    ('UPDATE operation_form_field SET form_id = NULL where id = 247',
     'UPDATE operation_form_field SET form_id = 107 where id = 247'),

    ('UPDATE operation_form_field SET form_id = NULL where id = 281',
     'UPDATE operation_form_field SET form_id = 107 where id = 281'),
    
    ('UPDATE operation_form SET `order` = 2 where id = 102',
     'UPDATE operation_form SET `order` = 1 where id = 102'),
    
    ('UPDATE operation_form_field SET `order` = 5 where id = 282',
     'UPDATE operation_form_field SET `order` = 0 where id = 282'),
    ('UPDATE operation_form_field SET `order` = 6 where id = 283',
     'UPDATE operation_form_field SET `order` = 1 where id = 283'),
    ('UPDATE operation_form_field SET `order` = 7 where id = 284',
     'UPDATE operation_form_field SET `order` = 2 where id = 284'),


    ("UPDATE operation_translation SET description = 'Classificador Naive Bayes. Suporta tanto a versão multinomial, quanto a Bernoulli.' where id = 104 and locale = 'pt'", "UPDATE operation_translation SET description = 'Classificador Naive Bayes. Suporta tanto a versão multinomial, quanto a Bernoulli.' where id = 104 and locale = 'pt'"),
    ("UPDATE operation_translation SET description = 'Naive Bayes Classifiers. It supports both Multinomial and Bernoulli NB' where id = 104 and locale = 'en'", "UPDATE operation_translation SET description = 'Naive Bayes Classifiers. It supports both Multinomial and Bernoulli NB' where id = 104 and locale = 'en'"),
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
                if cmd[1]:
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
