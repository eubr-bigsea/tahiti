# -*- coding: utf-8 -*-
"""fix_ml

Revision ID: 1214d3ffa0ce
Revises: 6e79129492af
Create Date: 2017-08-30 15:20:42.169515

"""

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '1214d3ffa0ce'
down_revision = '6e79129492af'
branch_labels = None
depends_on = None


def _add_classifiers_fields_translations():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = [c.name for c in tb.columns]
    data = [
        [134, 'en', u'Features', u'Features'],
        [135, 'en', u'Label', u'Label'],
        [135, 'pt', u'Rótulo', u'Rótulo'],
        [137, 'en', u'Features', u'Label'],
        [137, 'pt', u'Features', u'Features'],
        [138, 'en', u'Label', u'Label'],
        [138, 'pt', u'Rótulo', u'Rótulo'],
        [140, 'en', u'Features', u'Label'],
        [140, 'pt', u'Features', u'Features'],
        [141, 'en', u'Label', u'Label'],
        [141, 'pt', u'Rótulo', u'Rótulo'],
        [143, 'en', u'Features', u'Label'],
        [143, 'pt', u'Features', u'Features'],
        [144, 'en', u'Label', u'Label'],
        [144, 'pt', u'Rótulo', u'Rótulo'],
        [146, 'en', u'Features', u'Features'],
        [146, 'pt', u'Features', u'Features'],
        [147, 'en', u'Label', u'Label'],
        [147, 'pt', u'Rótulo', u'Rótulo'],

        [183, 'pt', u'Features', u'Features'],
        [183, 'en', u'Label', u'Label'],
        [184, 'en', u'Label', u'Label'],
        [184, 'pt', u'Rótulo', u'Rótulo'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _add_classifiers_fields():
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
        [134, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 64],
        [135, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 64],
        [137, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 65],
        [138, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 65],
        [140, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 66],
        [141, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 66],
        [143, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 67],
        [144, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 67],
        [146, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 68],
        [147, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 68],
        [183, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 34],
        [184, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 34],

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _add_field_apply_model():
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
        [346, 'features', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 52],
        # Clustering model
        [347, 'prediction', 'TEXT', 0, 2, 'prediction', 'text', None, None, 'EXECUTION',
         10],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = [c.name for c in tb.columns]
    data = [
        [346, 'en', u'Features attribute', u'Features attribute'],
        [346, 'pt', u'Atributo com as features', u'Atributo com as features'],

        # Clustering model
        [347, 'en', u'Prediction (new attribute)',
         u'Prediction (new attribute)'],
        [347, 'pt', u'Atributo com a predição (novo)',
         u'Atributo com a predição (novo)'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _add_output_to_classification_model():
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
    data = [
        [
            200, 'OUTPUT', None, 1, 1, 'MANY', 'output data'
        ]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = [c.name for c in tb.columns]
    data = [[200, 1]]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (200, 'en', 'output data', 'Output data'),
        (200, 'pt', u'dados de saída', u'Dados de saída'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _add_outputs_to_clustering_algorithms():
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
    data = [
        [
            201, 'OUTPUT', None, 56, 1, 'MANY', 'algorithm'
        ]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = [c.name for c in tb.columns]
    data = [
        [201, 11]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (201, 'en', 'algorithm', 'Algorithm'),
        (201, 'pt', u'algoritmo', u'Algoritmo'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

all_commands = [
    [
        """
            UPDATE operation_translation SET name = 'Publish as dashboard',
            description = 'Publish results as a visualization dashboard'
             WHERE id = 26 AND locale = 'en'
        """,
        """
            UPDATE operation_translation SET name = 'Publish as visualization',
            description = 'Publishes result as a visualization'
             WHERE id = 26 AND locale = 'en'
        """
    ],
    [
        u"""
            UPDATE operation_translation SET name = 'Publicar como dashboard',
            description = 'Publica os resultados como um dashboard'
             WHERE id = 26 AND locale = 'pt'
        """,
        u"""
            UPDATE operation_translation
            SET name = 'Publicar como visualização',
            description = 'Publica o resultado como uma visualização'
             WHERE id = 26 AND locale = 'pt'
        """
    ],
    [
        'UPDATE operation SET enabled = 0 WHERE id BETWEEN 63 AND 67',
        'UPDATE operation SET enabled = 1 WHERE id BETWEEN 63 AND 67',
    ],
    [
        'UPDATE operation_form_field SET required = 1 WHERE id IN (242, 243)',
        'UPDATE operation_form_field SET required = 0 WHERE id IN (242, 243)',
    ],
    [
        '''DELETE FROM operation_form_field_translation
            WHERE id in (134, 135, 137, 138, 140, 141, 143, 144, 146, 147,
                183, 184)'''
        , _add_classifiers_fields_translations
    ],
    [
        '''DELETE FROM operation_form_field
            WHERE id in (134, 135, 137, 138, 140, 141, 143, 144, 146, 147,
            183, 184)'''
        , _add_classifiers_fields
    ],
    [
        _add_field_apply_model,
        ['DELETE FROM operation_form_field_translation WHERE id IN (346, 347)',
         'DELETE FROM operation_form_field WHERE id IN (346, 347)'],
    ],
    [
        _add_output_to_classification_model,
        [
            '''
            DELETE FROM operation_port_interface_operation_port
            WHERE operation_port_id = 200
            ''',
            '''DELETE FROM operation_port_translation WHERE id = 200''',
            '''DELETE FROM operation_port WHERE id = 200''',

        ],
    ],
    [
        '''
        UPDATE `operation_category_operation`
            SET `operation_category_id` = 15
            WHERE operation_id = 26 AND operation_category_id = 9''',
        '''
        UPDATE `operation_category_operation`
            SET `operation_category_id` = 9
            WHERE operation_id = 26 AND operation_category_id = 15''',
    ],
    [
        '''UPDATE operation SET icon = 'fa-dashboard' WHERE id = 26''',
        '''UPDATE operation SET icon = 'fa-pie-chart' WHERE id = 26''',
    ],

    [
        """
            INSERT INTO operation_port_interface_operation_port
            (operation_port_id, operation_port_interface_id) VALUES(93, 14)""",
        """DELETE FROM operation_port_interface_operation_port
            WHERE operation_port_id = 93 AND operation_port_interface_id = 14
        """,
    ],
    [
        """
        UPDATE operation_script
            SET body = 'copyInputAddField(task, \\'prediction\\', false, null)'
            WHERE operation_id = 10
        """,

        """
        INSERT INTO operation_script(id, type, enabled, body, operation_id)
            VALUES(NULL, 'JS_CLIENT', 1,
              'copyInputAddField(task, \\'prediction\\', false, null)', 10)""",
        """
           DELETE FROM operation_script WHERE operation_id = 10
        """,
    ],
    [
        _add_outputs_to_clustering_algorithms,
        [
            '''
            DELETE FROM operation_port_interface_operation_port
            WHERE operation_port_id = 201
            ''',
            '''DELETE FROM operation_port_translation WHERE id = 201''',
            '''DELETE FROM operation_port WHERE id = 201''',

        ],

    ]

]


def upgrade():
    cntxt = context.get_context()
    session = sessionmaker(bind=cntxt.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], (unicode, str)):
                connection.execute(cmd[0])
            else:
                cmd[0]()
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    cntxt = context.get_context()
    session = sessionmaker(bind=cntxt.bind)()
    connection = session.connection()

    try:
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], (unicode, str)):
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
