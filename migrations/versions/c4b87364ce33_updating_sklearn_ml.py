"""updating sklearn ml

Revision ID: c4b87364ce33
Revises: a73c21a49894
Create Date: 2021-03-24 09:12:31.884160

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
revision = 'c4b87364ce33'
down_revision = 'a73c21a49894'
branch_labels = None
depends_on = None

SCRIPT_ID_SPARK = 73
SCRIPT_ID_SKLEARN = 4004


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
        # frequent-item-set
        (SCRIPT_ID_SPARK, 'JS_CLIENT', 1,
         'task.uiPorts.output = ["items", "freq"];', 3),
        # association-rules
        (SCRIPT_ID_SPARK + 1, 'JS_CLIENT', 1,
         'task.uiPorts.output = ["antecedent", "consequent", "confidence", '
         '"lift", "conviction", "leverage", "jaccard"];', 85),
        # sequence-mining
        (SCRIPT_ID_SPARK + 2, 'JS_CLIENT', 1,
         'task.uiPorts.output = ["sequence", "freq"];', 86),
        # k-fold
        (SCRIPT_ID_SKLEARN, "JS_CLIENT", 1,
         "copyInputAddField(task, 'alias', false, 'fold');", 4041)

    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


scripts = [str(SCRIPT_ID_SPARK + i) for i in range(3)] + \
          [str(SCRIPT_ID_SKLEARN)]

all_commands = [
    # Aglomerative Clustering
    ("""
    UPDATE operation_form_field SET `enable_conditions` = '' WHERE id = 4075;
    """, """
        UPDATE operation_form_field SET `enable_conditions` = '{json}' 
        WHERE id = 4075;
    """.format(json=json.dumps({"multiple": False}))),
    # Gaussian Mixture clustering
    ("UPDATE operation_form_field SET `default` = 3 WHERE id = 4075",
     "UPDATE operation_form_field SET `default` = 1 WHERE id = 4316"),

    # Cross-validation
    ("UPDATE operation SET `enabled` = 0 WHERE id = 43",
     "UPDATE operation SET `enabled` = 1 WHERE id = 43"),

    # k-fold
    ("UPDATE operation_form_field SET `values` = '{}' WHERE id = 4147"
     .format(json.dumps({"multiple": False})),
     "UPDATE operation_form_field SET `values` = 1 WHERE id = 4147"),

    ("UPDATE operation_form_field SET `name` = 'alias' WHERE id = 4145",
     "UPDATE operation_form_field SET `name` = 'attribute' WHERE id = 4145"),

    ("UPDATE operation_form_field SET `form_id` = 4 WHERE id = 4144",
     "UPDATE operation_form_field SET `form_id` = 4028 WHERE id = 4144"),

    ("""
     UPDATE operation_form_field_translation 
     SET `label` = 'Label', 
          `help` = 'Stratification is done based on a label.'
     WHERE id = 4147 AND locale = 'en'
    """, """
      UPDATE operation_form_field_translation 
      SET `label` = 'Database column', 
          `help` = 'Database column that will be used in the K Fold.'
      WHERE id = 4147 AND locale = 'en'
      """
     ),
    ("""
     UPDATE operation_form_field_translation 
     SET `label` = 'Label', 
         `help` = 'Estratificação é feita a partir de um rótulo'
     WHERE id = 4147 AND locale = 'pt'
    """, """
     UPDATE operation_form_field_translation 
     SET `label` = 'Coluna da base de dados', 
          `help` = 'Coluna da base de dados que será '
          'utilizada pra realizar o K Fold.'
     WHERE id = 4147 AND locale = 'pt'
    """),


    # scripts
    (_insert_operation_script,
     'DELETE FROM operation_script WHERE id IN ({})'.format(",".join(scripts)))
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
