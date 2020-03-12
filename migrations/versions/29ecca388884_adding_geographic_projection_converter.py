"""Adding geographic projection converter.

Revision ID: 29ecca388884
Revises: b4a88e0c224e
Create Date: 2020-02-20 12:48:10.392917

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '29ecca388884'
down_revision = 'b4a88e0c224e'
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
        (4045, 'cartographic-projection', 1, 'TRANSFORMATION', 'fa-globe-stand'),

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

        (4045, 4),

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
        (4045, 4001),
        (4045, 41),
        (4045, 42),
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
        (4044, 1, 1, 'execution'),
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
        (4044, 'en', 'Execution'),
        (4044, 'pt', 'Execução'),
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
        (4045, 41),
        (4045, 110),
        (4045, 4044),

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
        (4045, 'pt', 'Conversor de projeções cartográficas',
         'Converte diferentes projeções cartograficas entre si.'),
        (4045, 'en', 'Cartographic projections converter',
         'Converts different cartographic projections to each other.'),

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
        (4098, 'INPUT', None, 4045, 1, 'ONE', 'input data'),
        (4099, 'OUTPUT', None, 4045, 1, 'MANY', 'output data'),

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
        (4098, 'en', 'input data', 'Input data'),
        (4098, 'pt', 'dados de entrada', 'Dados de entrada'),
        (4099, 'en', 'output data', 'Output data'),
        (4099, 'pt', 'dados de saída', 'Dados de saída'),

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
        (4098, 1),
        (4099, 1),

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
        (4344, 'src_projection', 'INTEGER', 1, 1, None, 'integer', None, None, 'EXECUTION', 4044),
        (4345, 'dst_projection', 'INTEGER', 1, 2, None, 'integer', None, None, 'EXECUTION', 4044),
        (4346, 'col_lat', 'TEXT', 1, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', 4044),
        (4347, 'col_lon', 'TEXT', 1, 4, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', 4044),
        (4348, 'alias_lat', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 4044),
        (4349, 'alias_lon', 'TEXT', 0, 6, None, 'text', None, None, 'EXECUTION', 4044),
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

        (4344, 'en', 'Source projection (epsg code)', 'Source projection (epsg)'),
        (4344, 'pt', 'Projeção de origem (epsg)', 'Projeção de origem (epsg)'),
        (4345, 'en', 'Destination projection (epsg code)', 'Destination projection (epsg code).'),
        (4345, 'pt', 'Projeção de destino (epsg)', 'Projeção de destino (epsg).'),
        (4346, 'en', 'Latitude column', 'Latitude column name.'),
        (4346, 'pt', 'Coluna de Latitude', 'Nome da coluna que contem a Latitude.'),
        (4347, 'en', 'Longitude column', 'Longitude column name.'),
        (4347, 'pt', 'Coluna de Longitude', 'Nome da coluna que contem a Longitude.'),
        (4348, 'en', 'New Latitude column', 'Alias for the converted Latitude.'),
        (4348, 'pt', 'Nova coluna de Latitude', 'Novo nome da coluna para as Latitudes convertidas (se vazia, '
                                                'vai substituir a atual).'),
        (4349, 'en', 'New Longitude column', 'Alias for the converted Longitude (if empty will replace it).'),
        (4349, 'pt', 'Nova coluna de Longitude', 'Novo nome da coluna para as Longitudes convertidas (se vazia, '
                                                 'vai substituir a atual).'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation, 'DELETE FROM operation WHERE id = 4045'),
    (_insert_new_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 4045 AND '
     'platform_id = 4;'
     ),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id = 4045'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id = 4044'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id = 4044'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id = 4045'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = 4045'),
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4098 AND 4099'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4098 AND 4099'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE '
     'operation_port_id BETWEEN 4098 AND 4099'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4344 AND 4349;'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4344 AND 4349;'),

    ("""
        DELETE FROM operation_form_field_translation where id = 235; 
        DELETE FROM operation_form_field where id = 235; 
     """,
     """
     INSERT INTO operation_form_field (`id`, `name`, `type`, `required`, `order`, `default`, `suggested_widget`, 
     `values_url`, `values`, `scope`, `form_id`, `enable_conditions`) 
      VALUES (235, 'save_criteria', 'TEXT', 1, 3, 'ALL', 'dropdown', NULL, 
      '[{\"en\": \"Save best model\", \"key\": \"BEST\", \"value\": \"Save best model\", 
      \"pt\": \"Salvar o melhor modelo\"}, {\"en\": \"Save all (names will be suffixed with model rank)\", 
      \"key\": \"ALL\", \"value\": \"Save all (names will be suffixed with model rank)\", 
      \"pt\": \"Salvar todos (nomes ser\\u00e3o sufixados com o ranking do modelo)\"}]', 'EXECUTION', 100, NULL);
      
      INSERT INTO operation_form_field_translation (id, locale, label, help) VALUES 
      (235, 'en', 'Which model to save? (required if many models)', 'Which model to save.'),
      (235, 'pt', 'Qual modelo salvar? (obrigatório se vários modelos)', 'Qual modelo salvar.');
     """)

]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                cmds = cmd[0].split(';')
                for new_cmd in cmds:
                    if new_cmd.strip():
                        connection.execute(new_cmd)
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
                cmds = cmd[1].split(';')
                for new_cmd in cmds:
                    if new_cmd.strip():
                        connection.execute(new_cmd)
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    session.commit()
