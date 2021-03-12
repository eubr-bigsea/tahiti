"""updating sklearn scalers

Revision ID: a73c21a49894
Revises: 21de6c275230
Create Date: 2021-03-11 14:37:46.273275

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
revision = 'a73c21a49894'
down_revision = '21de6c275230'
branch_labels = None
depends_on = None

OPERATION_ID = 4047
FORM_ID = 4048
PORT_ID = 4103
FIELD_ID = 4383
SCRIPT_ID = 4000


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
        (OPERATION_ID, "standard-scaler", 1, "TRANSFORMATION",
         "fa-balance-scale"),
        (OPERATION_ID + 1, "min-max-scaler", "1", "TRANSFORMATION",
         "fa-arrows-alt-v"),
        (OPERATION_ID + 2, "max-abs-scaler", "1", "TRANSFORMATION", "fa-lemon")
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
        (OPERATION_ID, 4),
        (OPERATION_ID + 1, 4),
        (OPERATION_ID + 2, 4),
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
        (OPERATION_ID, 32),
        (OPERATION_ID, 34),
        (OPERATION_ID, 4001),

        (OPERATION_ID + 1, 32),
        (OPERATION_ID + 1, 34),
        (OPERATION_ID + 1, 4001),

        (OPERATION_ID + 2, 32),
        (OPERATION_ID + 2, 34),
        (OPERATION_ID + 2, 4001),
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
        (FORM_ID, 1, 1, 'execution'),
        (FORM_ID + 1, 1, 1, 'execution'),
        (FORM_ID + 2, 1, 1, 'execution'),
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
        (FORM_ID, 'en', 'Execution'),
        (FORM_ID, 'pt', 'Execução'),
        (FORM_ID + 1, 'en', 'Execution'),
        (FORM_ID + 1, 'pt', 'Execução'),
        (FORM_ID + 2, 'en', 'Execution'),
        (FORM_ID + 2, 'pt', 'Execução'),
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
        (OPERATION_ID, 41),
        (OPERATION_ID, 110),
        (OPERATION_ID, FORM_ID),

        (OPERATION_ID + 1, 41),
        (OPERATION_ID + 1, 110),
        (OPERATION_ID + 1, FORM_ID + 1),

        (OPERATION_ID + 2, 41),
        (OPERATION_ID + 2, 110),
        (OPERATION_ID + 2, FORM_ID + 2),
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
        (OPERATION_ID, "en", "Standard (Z-score)",
         "Transforms the input (vector rows), normalizing each feature to have "
         "unit standard deviation and/or zero mean."),
        (OPERATION_ID, "pt", "Padrão (Z-score)",
         "Transforma a entrada (linhas com vetores), normalizando-os de forma "
         "que cada caracteristica (feature) tenha desvio-padrão unitário e/ou "
         "média zero."),
        (OPERATION_ID + 1,  "en", "Min-Max",
         "Transforms the input (vector rows), rescaling each feature to a "
         "specific range (often [0, 1]). "),
        (OPERATION_ID + 1,  "pt", "Mínimo-Máximo",
         "Transforma a entrada (linhas com vetores), reescalando cada "
         "caracteristica para uma faixa específica (geralmente [0, 1])"),
        (OPERATION_ID + 2,  "en", "Max-Abs",
         "Transforms the input (vector rows), rescaling each value (feature) "
         "to range [-1, 1] by dividing through the maximum absolute value in "
         "each value (feature)."),
        (OPERATION_ID + 2,  "pt", "Máximo-Absoluto",
         "Transforma a entrada (linhas com vetores), reescalando cada "
         "caracteristica(feature) para a faixa [-1, 1], através da divisão "
         "pelo valor absoluto máximo de cada caracteristica"),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port():
    tb = table(
            'operation_port',
            column('id', Integer),
            column('type', String),
            column('tags', String),
            column('order', Integer),
            column('multiplicity', String),
            column('operation_id', Integer),
            column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (PORT_ID, "INPUT", None, "1", "ONE", OPERATION_ID, "input data"),
        (PORT_ID + 1,  "OUTPUT", None, "1", "MANY", OPERATION_ID,
         "output data"),
        (PORT_ID + 2, "OUTPUT", None, "2", "MANY", OPERATION_ID,
         "transformation model"),

        (PORT_ID + 3, "INPUT", None, "1", "ONE", OPERATION_ID + 1,
         "input data"),
        (PORT_ID + 4, "OUTPUT", None, "1", "MANY", OPERATION_ID + 1,
         "output data"),
        (PORT_ID + 5, "OUTPUT", None, "2", "MANY", OPERATION_ID + 1,
         "transformation model"),

        (PORT_ID + 6, "INPUT", None, "1", "ONE", OPERATION_ID + 2,
         "input data"),
        (PORT_ID + 7, "OUTPUT", None, "1", "MANY", OPERATION_ID + 2,
         "output data"),
        (PORT_ID + 8, "OUTPUT", None, "2", "MANY", OPERATION_ID + 2,
         "transformation model"),

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
        (PORT_ID, "en", "input data", "Input data"),
        (PORT_ID, "pt", "dados de entrada", "Dados de entrada"),
        (PORT_ID + 1, "en", "output data", "Output data"),
        (PORT_ID + 1, "pt", "dados de saída", "Dados de saída"),
        (PORT_ID + 2, "en", "transformation model", "Transformation model"),
        (PORT_ID + 2, "pt", "modelo de transformação",
         "Modelo de transformação"),

        (PORT_ID + 3, "en", "input data", "Input data"),
        (PORT_ID + 3, "pt", "dados de entrada", "Dados de entrada"),
        (PORT_ID + 4, "en", "output data", "Output data"),
        (PORT_ID + 4, "pt", "dados de saída", "Dados de saída"),
        (PORT_ID + 5, "en", "transformation model", "Transformation model"),
        (PORT_ID + 5, "pt", "modelo de transformação",
         "Modelo de transformação"),

        (PORT_ID + 6, "en", "input data", "Input data"),
        (PORT_ID + 6, "pt", "dados de entrada", "Dados de entrada"),
        (PORT_ID + 7, "en", "output data", "Output data"),
        (PORT_ID + 7, "pt", "dados de saída", "Dados de saída"),
        (PORT_ID + 8, "en", "transformation model", "Transformation model"),
        (PORT_ID + 8, "pt", "modelo de transformação",
         "Modelo de transformação"),
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
        (PORT_ID, 1),
        (PORT_ID + 1, 1),
        (PORT_ID + 2, 20),

        (PORT_ID + 3, 1),
        (PORT_ID + 4, 1),
        (PORT_ID + 5, 20),

        (PORT_ID + 6, 1),
        (PORT_ID + 7, 1),
        (PORT_ID + 8, 20),

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

        (FIELD_ID, "attributes", "TEXT", 1, 1, None, "attribute-selector",
         None, None, "EXECUTION", FORM_ID),
        (FIELD_ID + 1, "alias", "TEXT", 0, 2, None, "text", None, None,
         "EXECUTION", FORM_ID),
        (FIELD_ID + 2, "with_mean", "INTEGER", 1, 3, 0, "checkbox", None, None,
         "EXECUTION", FORM_ID),
        (FIELD_ID + 3, "with_std", "INTEGER", 1, 4, 1, "checkbox", None,
         None, "EXECUTION", FORM_ID),

        (FIELD_ID + 4, "attributes", "TEXT", 1, 1, None, "attribute-selector",
         None, None, "EXECUTION", FORM_ID + 1),
        (FIELD_ID + 5, "alias", "TEXT", 0, 2, None, "text", None,
         None, "EXECUTION", FORM_ID + 1),
        (FIELD_ID + 6, "min", "FLOAT", 0, 3, 0.0, "decimal", None, None,
         "EXECUTION", FORM_ID + 1),
        (FIELD_ID + 7, "max", "FLOAT", 0, 4, 1.0, "decimal", None, None,
         "EXECUTION", FORM_ID + 1),

        (FIELD_ID + 8, "attributes",  "TEXT", 1, 1, None, "attribute-selector",
         None, None, "EXECUTION", FORM_ID + 2),
        (FIELD_ID + 9, "alias", "TEXT", 0, 2, None, "text", None, None,
         "EXECUTION", FORM_ID + 2),

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
        (FIELD_ID, "en", "Features", "Features"),
        (FIELD_ID, "pt", "Atributo(s) previsor(es)",
         "Atributo(s) previsor(es)"),

        (FIELD_ID + 1, "en", "Name(s) for new attribute(s)",
         "Name(s) for new attribute(s). If omitted, the name of original "
         "attribute with a suffix will be used."),
        (FIELD_ID + 1, "pt", "Nome do(s) novo(s) attributo(s)",
         "Nome do(s) novo(s) atributo(s). Se omitido, o nome do atributo "
         "original com um sufixo será usado."),

        (FIELD_ID + 2, "en", "Center data with mean",
         "Center data with mean (default: false)."),
        (FIELD_ID + 2, "pt", "Centralizar os dados com a média",
         "Centralizar os dados com a média (falso por padrão)"),
        (FIELD_ID + 3, "en", "Scale to unit standard deviation",
         "Scale to unit standard deviation (default: true)."),
        (FIELD_ID + 3, "pt", "Escalar os dados para desvio-padrão unitário",
         "Escalar os dados para desvio-padrão unitário (verdadeiro por "
         "padrão)"),

        (FIELD_ID + 4, "en", "Features", "Features"),
        (FIELD_ID + 4, "pt", "Atributo(s) previsor(es)",
         "Atributo(s) previsor(es)"),
        (FIELD_ID + 5, "en", "Name(s) for new attribute(s)",
         "Name(s) for new attribute(s). If omitted, the "
         "name of original attribute with a suffix will be used."),
        (FIELD_ID + 5, "pt", "Nome do(s) novo(s) attributo(s)",
         "Nome do(s) novo(s) atributo(s). Se omitido, o nome do atributo "
         "original com um sufixo será usado."),
        (FIELD_ID + 6, "en", "Lower bound of the output feature range",
         "Lower bound of the output feature range (default: 0.0)."),
        (FIELD_ID + 6, "pt", "Limite inferior para a faixa",
         "Limite inferior para a faixa (valor padrão: 0.0)."),
        (FIELD_ID + 7, "en", "Upper bound of the output feature range",
         "Upper bound of the output feature range (default: 1.0)."),
        (FIELD_ID + 7, "pt", "Limite superior para a faixa",
         "Limite superior para a faixa (valor padrão: 1.0)."),

        (FIELD_ID + 8, "en", "Features", "Features"),
        (FIELD_ID + 8, "pt", "Atributo(s) previsor(es)",
         "Atributo(s) previsor(es)"),
        (FIELD_ID + 9, "en", "Name(s) for new attribute(s)",
         "Name(s) for new attribute(s). If omitted, the "
         "name of original attribute with a suffix will be used."),
        (FIELD_ID + 9, "pt", "Nome do(s) novo(s) attributo(s)",
         "Nome do(s) novo(s) atributo(s). Se omitido, o nome do atributo "
         "original com um sufixo será usado."),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


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
        (SCRIPT_ID, "JS_CLIENT", 1,
         "copyInputAddAttributesSplitAlias(task, 'attributes', 'alias', "
         "'_norm');",
         OPERATION_ID),
        (SCRIPT_ID + 1, "JS_CLIENT", 1,
         "copyInputAddAttributesSplitAlias(task, 'attributes', 'alias', "
         "'_norm');",
         OPERATION_ID+1),
        (SCRIPT_ID + 2, "JS_CLIENT", 1,
         "copyInputAddAttributesSplitAlias(task, 'attributes', 'alias', "
         "'_norm');",
         OPERATION_ID + 2),
        (SCRIPT_ID + 3, "JS_CLIENT", 1,
         "copyInputAddAttributesSplitAlias(task, 'attribute', 'alias', "
         "'_disc');",
         4014),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     "DELETE FROM operation WHERE id BETWEEN {} AND {}"
     .format(OPERATION_ID, OPERATION_ID+2)),
    (_insert_new_operation_platform,
     "DELETE FROM operation_platform WHERE operation_id BETWEEN {} AND {}"
     .format(OPERATION_ID, OPERATION_ID + 2)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN {} AND {}'
     .format(OPERATION_ID, OPERATION_ID + 2)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {} AND {}'
     .format(FORM_ID, FORM_ID + 2)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN {} AND {}'
     .format(FORM_ID, FORM_ID + 2)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id BETWEEN {} AND {}'
     .format(OPERATION_ID, OPERATION_ID + 2)),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN {} AND {}'
     .format(OPERATION_ID, OPERATION_ID + 2)),
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE operation_id BETWEEN {} AND {}'
     .format(OPERATION_ID, OPERATION_ID + 2)),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN {} AND {}'
     .format(PORT_ID, PORT_ID + 8)),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE '
     'operation_port_id BETWEEN {} AND {}'
     .format(PORT_ID, PORT_ID + 8)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN {} AND {}'
     .format(FIELD_ID, FIELD_ID + 9)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN {} AND {}'
     .format(FIELD_ID, FIELD_ID + 9)),
    ("DELETE FROM operation_platform WHERE platform_id = 4 AND "
     "operation_id IN (90, 91, 92)",
     "INSERT INTO operation_platform VALUES (90, 4), (91, 4), (92, 4) "),
    (_insert_operation_script,
     'DELETE FROM operation_script WHERE id BETWEEN {} AND {}'
     .format(SCRIPT_ID, SCRIPT_ID + 3)),

    # updating quantile-discretizer field
    ("""
         UPDATE operation_form_field_translation 
         SET `label` = 'The number of bins to produce', 
             `help` = 'The number of bins to produce. n_bins > 2'  
         WHERE id = 4072 AND locale = 'en'
     """,
     """
          UPDATE operation_form_field_translation 
          SET `label` = 'Number of quantiles', 
              `help` = 'Number of quantiles to be computed. It corresponds '
              'to the number of landmarks used to discretize the cumulative '
              'density function' 
          WHERE id = 4072 AND locale = 'en'
          """
     ),
    ("""
         UPDATE operation_form_field_translation 
         SET `label` = 'Número de bins', 
             `help` = 'Número de bin para ser transformado. n_bins > 2'  
         WHERE id = 4072 AND locale = 'pt'
    """, """
         UPDATE operation_form_field_translation 
         SET `label` = 'Número de quantis', 
              `help` = 'Número de quantis a serem calculados. Corresponde ao '
              'número de pontos de referência usados para discretizar a '
              'função de densidade acumulada' 
         WHERE id = 4072 AND locale = 'pt'
    """),

    # updating quantile-discretizer alias
    ("""
         UPDATE operation_form_field_translation 
         SET `label` = 'Name(s) for new attribute(s)', 
             `help` = 'Name(s) for new attribute(s). If omitted, the name '
             'of original attribute with a suffix will be used.'  
         WHERE id = 4071 AND locale = 'en'
     """,
     """
          UPDATE operation_form_field_translation 
          SET `label` = 'Alias', 
              `help` = 'Alias for generated indexed fields.' 
          WHERE id = 4071 AND locale = 'en'
          """
     ),
    ("""
        UPDATE operation_form_field_translation 
        SET `label` = 'Nome do(s) novo(s) attributo(s)', 
            `help` = 'Nome do(s) novo(s) atributo(s). ' 
        'Se omitido, o nome do atributo original com um sufixo será usado.'   
        WHERE id = 4071 AND locale = 'pt';
     """, """
        UPDATE operation_form_field_translation 
        SET `label` = 'Alias', 
            `help` = 'Alias para os campos indexados gerados.' 
        WHERE id = 4071 AND locale = 'pt';
     """),

    # updating quantile-discretizer slug to kbins-discretizer
    ("UPDATE operation SET `slug` = 'kbins-discretizer' WHERE id = 4014;",
     "UPDATE operation SET `slug` = 'quantile-discretizer' WHERE id = 4014;"),

    # updating quantile-discretizer translation
    ("""
        UPDATE operation_translation 
        SET `name` = 'KBins discretizer', 
            `description` = 'Bin continuous data into intervals.' 
        WHERE id = 4014 AND locale = 'en'
    """, """
        UPDATE operation_translation 
        SET `name` = 'Quantile discretizer', 
            `description` = 'Quantile discretizer takes an attribute with '
            'continuous features and outputs an attribute with binned '
            'categorical features.' 
        WHERE id = 4014 AND locale = 'en'
    """),
    ("""
        UPDATE operation_translation 
        SET `name` = 'Discretizador KBins', 
            `description` = 'Divide dados contínuos em intervalos.' 
        WHERE id = 4014 AND locale = 'pt'
    """, """
        UPDATE operation_translation 
        SET `name` = 'Discretizador em quantis', 
            `description` = 'Discretizador em quantis recebe um atributo e '
            'associa-o a quantis especificados em faixas de valores.' 
        WHERE id = 4014 AND locale = 'pt'
     """)

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
