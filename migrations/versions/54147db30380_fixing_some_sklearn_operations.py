"""fixing some sklearn operations.

Revision ID: 54147db30380
Revises: 29ecca388884
Create Date: 2020-01-23 12:51:44.638796

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '54147db30380'
down_revision = '29ecca388884'
branch_labels = None
depends_on = None


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
        column('enable_conditions', String))

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
    data = [
        (4372, 'output_distribution', 'TEXT', 0, 4, 'uniform', 'dropdown', None,
         '[{"key": \"quantile\", \"value\": \"quantile\"}, '
         '{\"key\": \"uniform\", \"value\": \"uniform\"}, '
         '{\"key\": \"kmeans\", \"value\": \"kmeans\"}]', 'EXECUTION', 4014,
         None),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _undo_operation_form_field():
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
        column('enable_conditions', String)
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
    data = [
        (4088, 'feature', 'TEXT', 0, 3, None, 'attribute-selector', None,
         '{\"multiple\": false}', 'EXECUTION', 4017,
         None),
        (4073, 'output_distribution', 'TEXT', 0, 4, 'uniform', 'dropdown', None,
         '[{"key": \"normal\", \"value\": \"normal\"}, '
         '{\"key\": \"uniform\", \"value\": \"uniform\"}]', 'EXECUTION',
         4014, None),
        (4074, 'seed', 'INTEGER', 0, 5, None, 'integer', None, None,
         'EXECUTION', 4014, None),

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
        (4372, 'en', 'Strategy',
         'Strategy used to define the widths of the bins.'),
        (4372, 'pt', 'Estratégia',
         'Estratégia utilizada para definir o range dos bins.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    # alterando o quantile-discretizer
    ("DELETE FROM operation_form_field_translation WHERE id = 4073 or id = 4074",
     """
     INSERT INTO operation_form_field_translation VALUES (4073, 'en', 'Distribuition',
         'Marginal distribution for the transformed data.'), (4074, 'en', 'Seed',
         'The seed of the pseudo random number generator to use when shuffling the data.'),
         (4073, 'pt', 'Distribuição', 'Distribuição marginal para os dados transformados.'),
        (4074, 'pt', 'Seed', 'The seed of the pseudo random number generator to use when shuffling the data.');
    """),
    ("DELETE FROM operation_form_field WHERE id = 4073 or id = 4074", ""),
    (_insert_operation_form_field, "DELETE FROM operation_form_field WHERE id = 4372"),
    (_insert_operation_form_field_translation, 'DELETE FROM operation_form_field_translation WHERE id = 4372'),
    ("UPDATE operation_form_field SET `default`= 5 WHERE id = 4072", ""),

    # desabilitar o campo feature attribute
    ("DELETE FROM operation_form_field_translation WHERE id = 4088",
     """
    INSERT INTO operation_form_field_translation (id, locale, label, help) VALUES 
    (4088, 'en', 'Feature attribute (if clustering)', 'Feature attribute (only if is clustering model).'),
    (4088, 'pt', 'Atributo de features', 'Atributo usado como features (apenas se é modelo de agrupamento).');
    """),
    ("DELETE FROM operation_form_field WHERE id = 4088", _undo_operation_form_field),

    # desabilitar a operação evaluate with cross-validation
    ("DELETE FROM operation_platform WHERE operation_id = 43 AND platform_id = 4;",
     "INSERT INTO operation_platform VALUES (43, 4);"),

    # habilitando o scatter plot
    ('UPDATE operation SET enabled=0 where id = 80', 'UPDATE operation SET enabled=1 where id = 80'),
    ('INSERT INTO operation_platform VALUES (87, 4);',
     'DELETE FROM operation_platform WHERE operation_id = 87 and platform_id = 4;'),

    # remover bars do Map
    ("UPDATE operation_form_field SET `values` = "
     "'[{\"en\": \"Points\", \"key\": \"points\", \"value\": \"Points\", \"pt\": \"Pontos\"}, "
     " {\"en\": \"Heatmap\", \"key\": \"heatmap\", \"value\": \"Heatmap\", \"pt\": \"Mapa de calor (heatmap)\"},"
     " {\"en\": \"Polygon (Geo JSON)\", \"key\": \"polygon\", \"value\": \"Polygon (Geo JSON)\", "
     "\"pt\": \"Polígono (Geo JSON)\"}]' "
     "WHERE id = 332;",
     "UPDATE operation_form_field SET `values` = "
     "'[{\"en\": \"Bar\", \"key\": \"bar\", \"value\": \"Bar\", \"pt\": \"Barras\"},"
     " {\"en\": \"Points\", \"key\": \"points\", \"value\": \"Points\", \"pt\": \"Pontos\"}, "
     " {\"en\": \"Heatmap\", \"key\": \"heatmap\", \"value\": \"Heatmap\", \"pt\": \"Mapa de calor (heatmap)\"},"
     " {\"en\": \"Polygon (Geo JSON)\", \"key\": \"polygon\", \"value\": \"Polygon (Geo JSON)\", \"pt\": "
     "\"Polígono (Geo JSON)\"}]' "
     "WHERE id = 332;"),

    # execute-sql
    ('UPDATE operation_port SET slug="input data 1" WHERE id = 4025;', ''),

    # read-shapefile
    ("UPDATE operation_form_field SET type='INTEGER', suggested_widget='lookup', "
     "values_url='`${LIMONERO_URL}/datasources?format=SHAPEFILE&simple=true&list=true&enabled=1`' WHERE id=3104",
     "UPDATE operation_form_field SET type='TEXT', suggested_widget='text', values_url='' WHERE id=3104"),

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

