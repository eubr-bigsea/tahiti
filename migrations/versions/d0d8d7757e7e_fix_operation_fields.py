# -*- coding: utf-8 -*-
"""fix_operation_fields

Revision ID: d0d8d7757e7e
Revises: 146dc5127e5e
Create Date: 2017-08-01 14:36:52.541609

"""

from alembic import op, context
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'd0d8d7757e7e'
down_revision = '146dc5127e5e'
branch_labels = None
depends_on = None


def upgrade():

    cntxt = context.get_context()
    session = sessionmaker(bind=cntxt.bind)()
    connection = session.connection()

    connection.execute("""
        UPDATE operation_form_field
            SET type = 'TEXT',
            suggested_widget = 'text'
        WHERE id = 264
        """)

    connection.execute("""UPDATE operation_form_field
        SET suggested_widget = 'attribute-selector' WHERE id = 194""")
    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Atributos (vazio significa todos os atributos da fonte de dados)',
        help =
            'Atributos (vazio significa todos os atributos da fonte de dados)'
        WHERE locale = 'pt' AND id = 194
        """)
    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Attributes (empty = all attributes from data source)',
        help =
            'Attributes (empty = all attributes from data source)'
        WHERE locale = 'en' AND id = 194
        """)

    # connection.execute("""
    #     INSERT INTO operation_form_field_translation(id, locale, label, help)
    #         VALUES(21, 'en', 'Comment', 'Comment')
    #     """)
    # connection.execute(u"""
    #     INSERT INTO operation_form_field_translation(id, locale, label, help)
    #         VALUES(21, 'pt', 'Comentário', 'Comentário')
    #     """)
    # connection.execute("""
    #     INSERT INTO operation_form_field_translation(id, locale, label, help)
    #         VALUES(25, 'en', 'Color', 'Color')
    #     """)
    # connection.execute(u"""
    #     INSERT INTO operation_form_field_translation(id, locale, label, help)
    #         VALUES(25, 'pt', 'Cor', 'Cor')
    #     """)

    connection.execute("""
        DELETE FROM operation_form_field_translation
        WHERE id in (207, 253, 258, 280, 246)
        """)
    connection.execute("""
        DELETE FROM operation_form_field
        WHERE id in (207, 253, 258, 280, 246)
        """)

    # Forms
    connection.execute("""
        INSERT INTO operation_form(id, enabled, `order`, category)
            VALUES(110, 1, 4, 'reports')
        """)
    connection.execute("""
        INSERT INTO operation_form_translation(id, locale, name)
            VALUES(110, 'en', 'Results')
        """)
    connection.execute("""
        INSERT INTO operation_form_translation(id, locale, name)
            VALUES(110, 'pt', 'Resultados')
        """)

    # Associate to operation
    ops = [1, 3, 5, 6, 7, 10, 12, 13, 15, 16, 17, 18, 19, 21, 23, 24, 27, 28,
           32, 33, 37, 40, 41, 42, 43, 49, 50, 51, 52, 53, 55, 57, 59, 73, 75,
           82, 83, 84, 85, 86]
    for op_id in ops:
        connection.execute("""
            INSERT INTO
                operation_operation_form(operation_id, operation_form_id)
            VALUES({}, 110)""".format(op_id))

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

    columns = [c.name for c in tb.columns]
    data = [
        [292, 'display_sample', 'INTEGER', 0, 1, '0', 'checkbox', None,
         None, 'EXECUTION', 110],
        [293, 'display_schema', 'INTEGER', 0, 2, '0', 'checkbox', None,
         None, 'EXECUTION', 110],
        [294, 'display_text', 'INTEGER', 0, 3, '1', 'checkbox', None, None,
         'EXECUTION', 110],
        [295, 'display_image', 'INTEGER', 0, 4, '1', 'checkbox', None,
         None,
         'EXECUTION', 110],
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
        [292, 'en', 'Display sample(s) of output(s) (max. 50 records)',
         'Display sample(s) of output(s) (max. 50 records)'],
        [293, 'en', 'Display output(s) schema(s)',
         'Display output(s) schema(s)'],
        [294, 'en', 'Display text reports (if available)',
         'Display text reports (if available)'],
        [295, 'en', 'Display images and charts (if available)',
         'Display images and charts (if available)'],

        [292, 'pt', 'Exibir amostra(s) da(s) saída(s) (máx. 50 registros)',
         'Exibir amostra(s) da(s) saída(s) (máx. 50 registros)'],
        [293, 'pt', 'Exibir esquema/dicionário da(s) saída(s)',
         'Exibir esquema/dicionário da(s) saída(s)', ],
        [294, 'pt', 'Exibir relatórios textuais (se disponíveis)',
         'Exibir relatórios textuais (se disponíveis)'],
        [295, 'pt', 'Exibir imagens e gráficos (se disponíveis)',
         'Exibir imagens e gráficos (se disponíveis)'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)
    session.commit()


def downgrade():
    cntxt = context.get_context()
    session = sessionmaker(bind=cntxt.bind)()
    connection = session.connection()

    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Nomes das colunas, separadas por vírgula (vazio = usar nomes da fonte de dados)',
        help =
            'Nomes das colunas, separadas por vírgula (vazio = usar nomes da fonte de dados)'
        WHERE locale = 'pt' AND id = 194
        """)
    connection.execute("""
        UPDATE operation_form_field_translation
        SET label =
            'Column names, comma separated (empty = use data source names)',
        help =
            'Column names, comma separated (empty = use data source names)'
        WHERE locale = 'en' AND id = 194
        """)

    connection.execute("""UPDATE operation_form_field
        SET suggested_widget = 'text' WHERE id = 194""")

    connection.execute('''DELETE FROM operation_form_field_translation
            WHERE id IN (292, 293, 294, 295)''')
    connection.execute('''DELETE FROM operation_form_field
            WHERE id IN (292, 293, 294, 295)''')
    connection.execute('DELETE FROM operation_operation_form WHERE '
               'operation_form_id = 110')
    connection.execute('DELETE FROM operation_form_translation WHERE id = 110')
    connection.execute('DELETE FROM operation_form WHERE id = 110')

    # connection.execute('DELETE FROM operation_form_field_translation WHERE id = 21')
    # connection.execute('DELETE FROM operation_form_field_translation WHERE id = 25')
    connection.execute("""
        UPDATE operation_form_field
            SET type = 'INTEGER',
            suggested_widget = 'integer'
        WHERE id = 264
        """)
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
        [207, 'weight', 'TEXT', 0, 4, None, 'attribute-selector', None, None,
         'EXECUTION', 8],
        [253, 'weight', 'TEXT', 0, 4, None, 'attribute-selector', None, None,
         'EXECUTION', 104],
        [258, 'weight', 'TEXT', 0, 4, None, 'attribute-selector', None, None,
         'EXECUTION', 104],
        [280, 'weight', 'TEXT', 0, 3, None, 'attribute-selector', None, None,
         'EXECUTION', 107],
        [246, 'weight', 'TEXT', 0, 5, None, 'attribute-selector', None, None,
         'EXECUTION', 102],
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
        [207, 'en', 'Weight', 'Weight'],
        [253, 'en', 'Weight', 'Weight'],
        [258, 'en', 'Weight', 'Weight'],
        [280, 'en', 'Weight', 'Weight'],
        [246, 'en', 'Weight', 'Weight'],

        [207, 'pt', 'Peso', 'Peso'],
        [253, 'pt', 'Peso', 'Peso'],
        [258, 'pt', 'Peso', 'Peso'],
        [280, 'pt', 'Peso', 'Peso'],
        [246, 'pt', 'Peso', 'Peso'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)
    session.commit()
