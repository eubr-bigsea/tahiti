# -*- coding: utf-8 -*-
"""empty message

Revision ID: 223eb6c3933b
Revises: 20ba8618b49d
Create Date: 2017-08-16 16:03:57.007907

"""
import json

from alembic import op, context
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '223eb6c3933b'
down_revision = '20ba8618b49d'
branch_labels = None
depends_on = None


def upgrade():
    cntxt = context.get_context()
    session = sessionmaker(bind=cntxt.bind)()
    connection = session.connection()

    connection.execute('''
        DELETE FROM operation_operation_form
        WHERE operation_id = 71 AND operation_form_id = 86''')
    connection.execute("""
        INSERT INTO operation_operation_form (operation_id, operation_form_id)
        VALUES(71, 83)
    """)

    connection.execute("""UPDATE operation_form_field
        SET suggested_widget = 'attribute-selector', required = 1,
        name = 'value_attribute'
        WHERE id = 200""")

    connection.execute("""UPDATE operation_form_field
        SET `order` = 3 WHERE id = 201""")

    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Attribute with value',
        help =
            'Attribute with value'
        WHERE locale = 'en' AND id = 200
        """)
    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Atributo com o valor',
        help =
            'Atributo com o valor'
        WHERE locale = 'pt' AND id = 200
        """)

    # Fields
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

    supported_formats = [
        {"key": "%Y-%m-%dT%H:%M:%S.%LZ",
         "value": "%Y-%m-%dT%H:%M:%S.%LZ"},
        {"key": "%m-%d", "value": "%m-%d"},
        {"key": "%d-%", "value": "%d-%m"},
        {"key": "%Y-%m-%d", "value": "%Y-%m-%d"},
        {"key": "%m-%Y-%d", "value": "%m-%Y-%d"},
        {"key": "%m-%Y-%d", "value": "%m-%Y-%d"},
        {"key": "%m-%Y-%d %H:%M",
         "value": "%m-%Y-%d %H:%M"},
        {"key": "%m-%Y-%d %H:%M",
         "value": "%m-%Y-%d %H:%M"},
        {"key": "%m-%Y-%d %H:%M:%S", "value": "%m-%Y-%d %H:%M:%S"},
        {"key": "%m-%Y-%d %H:%M:%S",
         "value": "%m-%Y-%d %H:%M:%S"},
        {"key": "%H:%M", "value": "%H:%M"},
        {"key": "%H:%M:%S", "value": "%H:%M:%S"},

        {"key": ".2", "value": ".2"},
        {"key": ".4", "value": ".4"},
        {"key": "%", "value": "%"},
        {"key": "p", "value": "p"},
        {"key": "d", "value": "d"}
    ]
    columns = [c.name for c in tb.columns]
    data = [
        [305, 'id_attribute', 'TEXT', 0, 2, None, 'attribute-selector', None,
         None, 'EXECUTION', 85],
        [307, 'x_format', 'TEXT', 0, 7, None, 'select2', None,
         json.dumps(supported_formats), 'EXECUTION', 85],
        [308, 'x_prefix', 'TEXT', 0, 8, None, 'text', None, None, 'EXECUTION',
         85],
        [309, 'x_suffix', 'TEXT', 0, 9, None, 'text', None, None, 'EXECUTION',
         85],
        [310, 'legend', 'INTEGER', 0, 5, '1', 'checkbox', None, None,
         'EXECUTION', 85],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = [c.name for c in tb.columns]
    data = [
        [305, 'en', 'Optional label attribute (blank: use value as label',
         'Attribute used as label'],
        [307, 'en', 'X-axis values format',
         'Format to be applied to the values in X-axis'],
        [308, 'en', 'X-axis prefix (added to the value when displaying it)',
         'X-axis prefix (added to the value display)'],
        [309, 'en', 'X-axis suffix (added to the value when displaying it)',
         'X-axis suffix(added to the value display)'],
        [310, 'en', 'Display legend', 'Display legend'],

        [305, 'pt',
         'Atributo usado como rótulo (vazio: usar o valor como rótulo)',
         'Atributo usado para o rótulo'],
        [307, 'pt', 'Formato para eixo X', 'Formato para valores eixo X'],
        [308, 'pt', 'Prefixo para eixo X',
         'Prefixo para eixo X (adicionado ao valor ao exibi-lo)'],
        [309, 'pt', 'Sufixo para eixo X',
         'Sufixo para eixo X (adicionado ao valor ao exibi-lo)'],
        [310, 'pt', 'Exibir legenda', 'Exibir legenda'],

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)
    session.commit()


def downgrade():
    cntxt = context.get_context()
    session = sessionmaker(bind=cntxt.bind)()
    connection = session.connection()

    connection.execute('''
        DELETE FROM operation_operation_form
        WHERE operation_id = 71 AND operation_form_id = 83''')
    connection.execute("""
        INSERT INTO operation_operation_form (operation_id, operation_form_id)
        VALUES(71, 86)
    """)

    connection.execute("""UPDATE operation_form_field
        SET suggested_widget = 'text', required = 0,
        name = 'column_names'
        WHERE id = 200""")

    connection.execute("""UPDATE operation_form_field
        SET `order` = 2 WHERE id = 201""")

    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Column names, comma separated (empty = use data source names)',
        help =
            'Column names, comma separated (empty = use data source names)'
        WHERE locale = 'en' AND id = 200
        """)
    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Nomes das colunas, separadas por vírgula (vazio = usar nomes da fonte de dados)',
        help =
            'Nomes das colunas, separadas por vírgula (vazio = usar nomes da fonte de dados)'
        WHERE locale = 'pt' AND id = 200
        """)

    connection.execute('''DELETE FROM operation_form_field_translation
            WHERE id BETWEEN 305 AND 310 ''')
    connection.execute('''DELETE FROM operation_form_field
            WHERE id BETWEEN 305 AND 310 ''')

    session.commit()
