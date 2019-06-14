# -*- coding: utf-8 -*-
"""visualization

Revision ID: 20ba8618b49d
Revises: d0d8d7757e7e
Create Date: 2017-08-08 17:17:32.946789

"""
import json

from alembic import op, context
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '20ba8618b49d'
down_revision = 'd0d8d7757e7e'
branch_labels = None
depends_on = None


def upgrade():
    cntxt = context.get_context()
    session = sessionmaker(bind=cntxt.bind)()
    connection = session.connection()

    connection.execute("""
        UPDATE operation_form_field SET `default` = 'VERTICAL_BARS'
        WHERE id = 192
        """)

    connection.execute(
        """INSERT INTO operation_operation_form
        (`operation_id`, `operation_form_id`) VALUES (69, 83);"""
    )
    connection.execute("""DELETE FROM operation_form_field
        WHERE id IN (188, 189, 190, 191, 198, 199)""")
    #
    connection.execute("""UPDATE operation_form_field
        SET suggested_widget = 'attribute-selector', required = 1
        WHERE id = 196""")
    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Atributos para eixo Y (cada um será uma série)',
        help =
            'Atributos para eixo Y (cada um será uma série)'
        WHERE locale = 'pt' AND id = 196
        """)
    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Attributes for Y-axis (each one will be a series)',
        help =
            'Attributes for Y-axis (each one will be a series)'
        WHERE locale = 'en' AND id = 196
        """)

    connection.execute("""
        UPDATE operation_form_field
        SET values_url =
          '`${LIMONERO_URL}/datasources?simple=true&list=true&enabled=1`'
        WHERE id = '1';
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
        [296, 'x_title', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         83],
        [297, 'y_title', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION',
         83],
        [298, 'x_format', 'TEXT', 0, 5, None, 'select2', None,
         json.dumps(supported_formats), 'EXECUTION',
         83],
        [299, 'y_format', 'TEXT', 0, 6, None, 'select2', None,
         json.dumps(supported_formats), 'EXECUTION',
         83],
        [300, 'x_prefix', 'TEXT', 0, 7, None, 'text', None, None, 'EXECUTION',
         83],
        [301, 'y_prefix', 'TEXT', 0, 8, None, 'text', None, None, 'EXECUTION',
         83],
        [302, 'x_suffix', 'TEXT', 0, 9, None, 'text', None, None, 'EXECUTION',
         83],
        [303, 'y_suffix', 'TEXT', 0, 10, None, 'text', None, None, 'EXECUTION',
         83],
        [304, 'x_axis_attribute', 'TEXT', 1, 0, None, 'attribute-selector',
         None, None, 'EXECUTION',
         83],
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
        [296, 'en', 'X-axis title', 'X-axis title to be shown'],
        [297, 'en', 'Y-axis title', 'Y-axis title to be shown'],
        [298, 'en', 'X-axis values format',
         'Format to be applied to the values in X-axis'],
        [299, 'en', 'Y-axis values format',
         'Format to be applied to values in X-axis'],
        [300, 'en', 'X-axis prefix (added to the value when displaying it)',
         'X-axis prefix (added to the value display)'],
        [301, 'en', 'Y-axis prefix (added to value when displaying it)',
         'Y-axis prefix (added to the value display)'],
        [302, 'en', 'X-axis suffix (added to the value when displaying it)',
         'X-axis suffix(added to the value display)'],
        [303, 'en', 'Y-axis suffix (added to the value when displaying it)',
         'Y-axis suffix (added to the value display)'],
        [304, 'en', 'X-axis attribute', 'Attribute used for X-axis'],

        [296, 'pt', 'Título para eixo X', 'Título a ser exibido para eixo X'],
        [297, 'pt', 'Título para eixo Y',
         'Título a ser exibido  para eixo Y'],
        [298, 'pt', 'Formato para eixo X', 'Formato para valores eixo X'],
        [299, 'pt', 'Formato para eixo Y', 'Formato para valores  eixo Y'],
        [300, 'pt', 'Prefixo para eixo X',
         'Prefixo para eixo X (adicionado ao valor ao exibi-lo)'],
        [301, 'pt', 'Prefixo para eixo Y',
         'Prefixo para eixo Y (adicionado ao valor ao exibi-lo)'],
        [302, 'pt', 'Sufixo para eixo X',
         'Sufixo para eixo X (adicionado ao valor ao exibi-lo)'],
        [303, 'pt', 'Sufixo para eixo Y',
         'Sufixo para eixo Y (adicionado ao valor ao exibi-lo)'],
        [304, 'pt', 'Atributo para eixo X', 'Atributo usado para eixo X'],

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)
    session.commit()


def downgrade():
    cntxt = context.get_context()
    session = sessionmaker(bind=cntxt.bind)()
    connection = session.connection()

    connection.execute(
        """
        DELETE FROM operation_operation_form
        WHERE operation_id = 69 AND operation_form_id = 83
        """)

    connection.execute("""
        UPDATE operation_form_field SET `default`= NULL
        WHERE id = 192
        """)
    connection.execute("""
        INSERT INTO operation_form_field
        (id, `order`, name, type, required, scope, form_id)
        VALUES (188, 1, 'title', 'TEXT', 1, 'EXECUTION', 84)""")
    connection.execute("""
        INSERT INTO operation_form_field
        (id, `order`, name, type, required, scope, form_id)
        VALUES (189, 2, 'labels', 'TEXT', 0, 'EXECUTION', 84)""")
    connection.execute("""
        INSERT INTO operation_form_field
        (id, `order`, name, type, required, scope, form_id)
        VALUES (190, 3, 'id_attribute', 'TEXT', 1, 'EXECUTION', 84)""")
    connection.execute("""
        INSERT INTO operation_form_field
        (id, `order`, name, type, required, scope, form_id)
        VALUES (191, 4, 'column_names', 'TEXT', 1, 'EXECUTION', 84)""")
    connection.execute("""
        INSERT INTO operation_form_field
        (id, `order`, name, type, required, scope, form_id)
        VALUES (198, 5, 'column_names', 'TEXT', 0, 'EXECUTION', 84)""")
    connection.execute("""
        INSERT INTO operation_form_field
        (id, `order`, name, type, required, scope, form_id)
        VALUES (199, 6, 'title', 'TEXT', 0, 'EXECUTION', 84)""")

    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (188, 'en', 'Title', 'Title')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (188, 'pt', 'Título', 'Título')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (189, 'en', 'Labels',
        'Labels. If omitted, id attribute values will be used.')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (189, 'pt', 'Rótulos',
        'Rótulos. Se omitido, os valores do atributo id serão usados.')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (190, 'en', 'Id attribute (x-axis)', 'Id attribute (x-axis)')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (190, 'pt', 'Atributo (x-axis)', 'Atributo (x-axis)')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (191, 'en', 'Value atribute', 'Value atribute')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (191, 'pt', 'Atributo com o valor', 'Atributo com o valor')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (198, 'en', 'Column names, comma separated (empty = use data source names)', 'Column names, comma separated (empty = use data source names)')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (198, 'pt', 'Nomes das colunas, separadas por vírgula (vazio = usar nomes da fonte de dados)', 'Nomes das colunas, separadas por vírgula (vazio = usar nomes da fonte de dados)')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (199, 'en', 'Title', 'Title')""")
    connection.execute("""INSERT INTO operation_form_field_translation
        (id, locale, label, help)
        VALUES (199, 'pt', 'Título', 'Título')""")
    #
    connection.execute("""
        UPDATE operation_form_field
        SET values_url =
          '`${LIMONERO_URL}/datasources?simple=true&list=true`'
        WHERE id = '1';
        """)

    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Nomes das colunas, separadas por vírgula (vazio = usar nomes da fonte de dados)',
        help =
            'Nomes das colunas, separadas por vírgula (vazio = usar nomes da fonte de dados)'
        WHERE locale = 'pt' AND id = 196
        """)
    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Column names, comma separated (empty = use data source names)',
        help =
            'Column names, comma separated (empty = use data source names)'
        WHERE locale = 'en' AND id = 196
        """)

    connection.execute("""UPDATE operation_form_field
        SET suggested_widget = 'text' WHERE id = 196""")

    connection.execute('''DELETE FROM operation_form_field_translation
            WHERE id BETWEEN 296 AND 304 ''')
    connection.execute('''DELETE FROM operation_form_field
            WHERE id BETWEEN 296 AND 304 ''')

    session.commit()
