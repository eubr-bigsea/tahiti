# -*- coding: utf-8 -*-

"""
Updating the COMPSs Operations and adding new ones.


(COMPSs Operations)

Revision ID: bca9192ljsj4
Revises: 2d2652e5209f
Create Date: 2018-06-06 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'bca9192ljsj4'
down_revision = '2d2652e5209f'
branch_labels = None
depends_on = None


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String),
               )
    columns = ['id', 'slug', 'enabled', 'type', 'icon']
    data = [
        (3022, 'normalize', 1, 'TRANSFORMATION', 'fa-text-height'),
        (3012, 'feature-indexer', 1, 'TRANSFORMATION', 'fa-list-ol'),

    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_new_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (3012, 3),
        (3022, 3),  # normalize
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_id', 'operation_category_id')
    data = [
        # normalize
        (3022, 7),
        (3022, 3001),

        (3012, 8),  # feature-indexer'
        (3012, 23),  # feature-indexer'
        (3012, 3001),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        (3012, 1, 1, 'execution'),  # feature-indexer'
        (3022, 1, 1, 'execution'),  # normalize
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
        (3022, 'en', 'Execution'),
        (3022, 'pt', 'Execução'),
        (3012, 'en', 'Execution'),
        (3012, 'pt', 'Execução'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        (3022, 39),  # normalize
        (3022, 40),
        (3022, 41),
        (3022, 43),
        (3022, 110),
        (3022, 3022),

        (3012, 39),  # feature-indexer'
        (3012, 40),
        (3012, 41),
        (3012, 43),
        (3012, 110),
        (3012, 3012),

    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [

        (3012, 'en', 'Feature indexer',
         'Indexes a feature by encoding a string column as a column containing indexes for labels (String type) or by encoding a Vector column as a column containing indexes for these vectors.'),
        (3012, 'pt', 'Indexador feature',
         'Indexa uma feature codificando o texto da coluna como uma coluna contendo os índices para os rótulos ou codificando uma coluna do tipo Vector como uma coluna de índices para esses vetores'),

        (3022, 'en', 'Normalize Data', 'Normalize the selected columns'),
        (3022, 'pt', 'Normalizar Dados', 'Normaliza as colunas selecionadas'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port():
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

        (3019, 'INPUT', None, 3012, 1, 'ONE', 'input data'),
        # feature-indexer'
        (3020, 'OUTPUT', None, 3012, 1, 'MANY', 'output data'),
        # feature-indexer'
        # normalize
        (3044, 'INPUT', None, 3022, 1, 'ONE', 'input data'),
        (3045, 'OUTPUT', None, 3022, 1, 'MANY', 'output data'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [

        (3019, 'en', 'input data', 'Input Data'),  # feature-indexer'
        (3019, 'pt', 'dados de entrada', "Dados de entrada"),
        # feature-indexer'
        (3020, 'en', 'output data', 'Output Data'),  # feature-indexer'
        (3020, 'pt', 'dados de saída', 'Dados de saída'),
        # feature-indexer'
        # normalize
        (3044, 'en', 'input data', 'Input Data'),
        (3044, 'pt', 'dados de entrada', "Dados de entrada"),
        (3045, 'en', 'output data', 'Output Data'),
        (3045, 'pt', 'dados de saída', 'Dados de saída'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (3019, 1),  # feature-indexer'
        (3020, 1),  # feature-indexer'
        # normalize
        (3044, 1),
        (3045, 1),

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
        column('form_id', Integer), )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [
        # normalize
        (3078, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 3022),
        (3079, 'alias', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 3022),
        (3080, 'mode', 'TEXT', 1, 3, 'range', 'dropdown', None,
         '[{\"key\": \"range\", \"value\": \"Range Normalization\"},\r\n  '
         ' {\"key\": \"standard\", \"value\": \"Standard Score Normalization\"}\r\n  ]',
         'EXECUTION', 3022),
        # feature-indexer'
        (3027, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 3012),
        (3028, 'indexer_type', 'TEXT', 1, 3, None, 'dropdown', None,
         '[\r\n  {"key": "string", "value": "String"}\r\n]', 'EXECUTION', 3012),
        (3029, 'alias', 'TEXT', 1, 2, None, 'text', None, None, 'EXECUTION',
         3012),
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
        # normalize
        (3078, 'en', 'Attributes', 'Attributes'),
        (3078, 'pt', 'Attributos', 'Colunas para serem consideradas'),
        (3079, 'en', 'Alias', 'Name of the new column'),
        (3079, 'pt', 'Alias', 'Nome para a nova coluna criada'),
        (3080, 'en', 'Normalization Type', 'Type of Normalization to perform.'),
        (3080, 'pt', 'Tipo de Normalização',
         'Tipo de Normalização para ser feita.'),

        # feature-indexer'
        (3027, 'en', 'Attributes', 'Attributes (features) to be indexed'),
        (3027, 'pt', 'Atributos', 'Atributos (features) a ser indexados'),
        (3028, 'en', 'Indexer type', 'Indexer type'),
        (3028, 'pt', 'Tipo de indexador', 'Tipo de indexador'),
        (3029, 'en', 'Name for new indexed attribute(s)',
         'Name for new indexed attribute(s)'),
        (3029, 'pt', 'Nome para novo(s) atributo(s) indexado(s)',
         'Nome para novo(s) atributo(s) indexado(s)'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _add_operations_platform_from_spark():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (40, 3),
        (90, 3),
        (91, 3),
        (92, 3),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


# --------------------------------------------------------------------------------

all_commands = [
    (
    'DELETE FROM operation_platform WHERE  operation_id >= 90 AND operation_id <= 92 AND platform_id = 3;'
    'DELETE FROM operation_platform WHERE  operation_id = 40 AND platform_id = 3;;'
    , _add_operations_platform_from_spark),
    (_insert_operation,
     'DELETE FROM operation_form_field_translation '
     '   WHERE (id >= 3078 AND  id <= 3080) or (id >= 3027 AND  id <= 3029);'),
    (_insert_new_operation_platform,
     'DELETE FROM operation_form_field WHERE form_id IN (3012, 3022);'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE (operation_port_id >= 3044 AND operation_port_id <= 3045) OR  '
     '  (operation_port_id >= 3019 AND operation_port_id <= 3020);'),
    (_insert_operation_form,
     'DELETE FROM operation_port_translation WHERE (id >= 3044 AND id <= 3045) '
     ' OR (id >= 3019 AND id <= 3020);'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_port WHERE (id >= 3044 AND id <= 3045 ) OR '
     ' (id >= 3019 AND id <= 3020);'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_translation WHERE id IN (3012, 3022);'),
    (_insert_operation_translation,
     'DELETE FROM operation_operation_form WHERE operation_id IN (3012, 3022)'),
    (_insert_operation_port,
     'DELETE FROM operation_form_translation WHERE id IN (3012, 3022)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_form WHERE id IN (3012, 3022)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_category_operation WHERE operation_id IN '
     '(3012, 3022)'),
    (_insert_operation_form_field,
     'DELETE FROM operation_platform WHERE operation_id IN (3012, 3022)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation WHERE id IN (3012, 3022)'),

]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
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


def downgrade():
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
