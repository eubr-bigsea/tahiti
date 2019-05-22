# coding=utf-8
"""changes cross validation

Revision ID: 71866c551e33
Revises: ae54f74392d4
Create Date: 2017-11-22 10:11:24.021401

"""
import json

from alembic import context
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = '71866c551e33'
down_revision = 'ae54f74392d4'
branch_labels = None
depends_on = None

VALUES = [
    {
        "key": "areaUnderROC",
        "value": "Area under ROC (Binary classification only)"
    },
    {
        "key": "areaUnderPR",
        "value": "Area under PR (Binary classification only)"
    },
    {
        "key": "f1", "value": "F1 (Classification only)"
    },
    {
        "key": "weightedPrecision",
        "value": "Weighted precision (Classification only)"
    },
    {
        "key": "weightedRecall",
        "value": "Weighted recall (Classification only)"
    },
    {
        "key": "accuracy", "value": "Accuracy (Classification only)"
    },
    {
        "key": "rmse", "value": "Root mean squared error (Regression only)"
    },
    {
        "mse": "mse", "value": "Mean squared error (Regression only)"
    },
    {
        "key": "mae", "value": "Mean absolute error (Regression only)"
    }
]
all_commands = [

    # Adjust evaluator values for CrossValidation
    (
        "UPDATE operation_form_field SET `values` = '{v}' WHERE id = 107".format(
            v=json.dumps(VALUES)),
        "UPDATE operation_form_field SET `values` = NULL WHERE id = 107"
    ),
    # Updates evaluator field to CrossValidation
    (
        "DELETE FROM operation_form_field_translation WHERE id = 106",
        """
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES (106, 'en', 'Estimator', 'Estimator')
        """
    ),
    (
        "DELETE FROM operation_form_field WHERE id = 106",
        """
        INSERT INTO operation_form_field(id, name, `type`, required, `order`,
            suggested_widget, scope, form_id)
        VALUES (106, 'estimator', 'TEXT', 1, 1, 'dropdown', 'EXECUTION', 53)
        """
    ),
    # Add label and prediction fields to CrossValidation
    # Label
    (
        """
       INSERT INTO operation_form_field(id, name, `type`, required, `order`,
           suggested_widget, scope, form_id)
       VALUES (106, 'label_attribute', 'TEXT', 1, 0, 'attribute-selector',
            'EXECUTION', 53)
       """,
        "DELETE FROM operation_form_field WHERE id = 106",
    ),
    (
        ["""
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES (106, 'en', 'Label attribute', 'Label attribute')
        """,
         """
         INSERT INTO operation_form_field_translation(id, locale, label, help)
         VALUES (106, 'pt', 'Atributo usado como label',
            'Atributo usado como label')""",
         ],
        "DELETE FROM operation_form_field_translation WHERE id = 106",
    ),
    # Prediction
    (
        """
       INSERT INTO operation_form_field(id, name, `type`, required, `order`,
           suggested_widget, scope, form_id, `default`)
       VALUES (137, 'prediction_attribute', 'TEXT', 1, 1, 'text',
            'EXECUTION', 53, 'prediction')
       """,
        "DELETE FROM operation_form_field WHERE id = 137",
    ),
    (
        ["""
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES (137, 'en', 'Prediction attribute (new)',
            'Prediction attribute (new)')
        """,
         """
         INSERT INTO operation_form_field_translation(id, locale, label, help)
         VALUES (137, 'pt', 'Atributo usado para predição (novo)',
            'Atributo usado para predição (novo)')""",
         ],
        "DELETE FROM operation_form_field_translation WHERE id = 137",
    ),

    # Remove unused ports
    (
        """DELETE FROM operation_port_interface_operation_port
            WHERE operation_port_id IN (39, 105, 106)""",
        """
        INSERT INTO operation_port_interface_operation_port (operation_port_id,
            operation_port_interface_id) VALUES
            (39, 7), (105, 10)
        """
    ),
    (
        "DELETE FROM operation_port_translation WHERE id IN (39, 105, 106);",
        """
        INSERT INTO operation_port_translation(id, locale, NAME, description)
        VALUES
            (39, 'en', 'evaluated model', 'Evaluated model'),
            (39, 'pt', 'modelo avaliado', 'Modelo avaliado'),
            (105, 'en', 'evaluator', 'Evaluator for ML model'),
            (105, 'pt', 'avaliador',
                'Avaliador para modelo de aprendizado de máquina');
        """
    ),
    (
        "DELETE FROM operation_port WHERE id IN (39, 105, 106)"
        ,
        """
        INSERT INTO operation_port
            (id, `type`, `order`, multiplicity, operation_id, slug) VALUES
        (39, 'OUTPUT', 1, 'MANY', 19, 'evaluated model'),
        (105, 'OUTPUT', 2, 'MANY', 19, 'evaluator'),
        (106, 'INPUT', 3, 'ONE', 43, 'evaluator')
        """
    ),
    # Port ordering
    (
        "UPDATE operation_port SET `order`= 0 WHERE id = 95",
        "UPDATE operation_port SET `order`= 2 WHERE id = 95",
    ),
    # Adjust port interface
    (
        """
        DELETE FROM operation_port_interface_operation_port
        WHERE operation_port_id = 98 AND
            operation_port_interface_id = 7
        """,
        """
        INSERT INTO operation_port_interface_operation_port(
            operation_port_id, operation_port_interface_id)
            VALUES (98, 7)
        """
    ),
    (
        """
        INSERT INTO operation_port_interface_operation_port(
            operation_port_id, operation_port_interface_id)
            VALUES (98, 2)
        """,
        """
        DELETE FROM operation_port_interface_operation_port
        WHERE operation_port_id = 98 AND
            operation_port_interface_id = 2
        """,
    ),
    (
        """
        INSERT INTO operation_port_interface_operation_port(
            operation_port_id, operation_port_interface_id)
            VALUES (98, 18)
        """,
        """
        DELETE FROM operation_port_interface_operation_port
        WHERE operation_port_id = 98 AND
            operation_port_interface_id = 18
        """,
    ),
    # Ports of Topic Report
    (
        """
        UPDATE operation_port SET multiplicity = 'MANY', slug = 'topics'
            WHERE id = 122
        """,
        """
        UPDATE operation_port SET multiplicity = 'ONE', slug = 'output data'
            WHERE id = 122
        """
    ),
    (
        ["""
            UPDATE operation_translation SET name = 'Processar tópicos',
            description = concat(
                'Processa tópicos de um modelo baseado em features textuais, ',
                'convertendo os índices de volta para o texto correspondente'
                )
            WHERE id = 2 and locale = 'pt'
        """,
         """
         UPDATE operation_translation SET name = 'Process topics',
         description = concat(
             'Process topics from a model using text features, converting ',
             'indexes back to the original text'
             )
         WHERE id = 2 and locale = 'en'
         """,
         ],
        [
            """
            UPDATE operation_translation SET
               name = 'Relatório de tópicos',
               description = 'Relatório de tópicos'
               WHERE id = 2 and locale = 'pt'
           """,
            """
                UPDATE operation_translation SET name = 'Topic report',
                description = 'Topic report'
                WHERE id = 2 and locale = 'en'
            """
        ]
    ),
    (
        ['''UPDATE operation_category_operation SET operation_category_id = 8
            WHERE operation_category_id = 1 AND operation_id = 2''',
         '''UPDATE operation_category_operation SET operation_category_id = 19
            WHERE operation_category_id = 13 AND operation_id = 2''',
         ]
        ,
        ['''UPDATE operation_category_operation SET operation_category_id = 1
            WHERE operation_category_id = 8 AND operation_id = 2''',
         '''UPDATE operation_category_operation SET operation_category_id = 13
            WHERE operation_category_id = 19 AND operation_id = 2''',
         ]
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
