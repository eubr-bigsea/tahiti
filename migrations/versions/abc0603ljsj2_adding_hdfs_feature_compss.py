# -*- coding: utf-8 -*-

"""
Updating the COMPSs Operations and adding new ones.


(COMPSs Operations)

Revision ID: abc0603ljsj2
Revises: acb362512a62
Create Date: 2018-03-05 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'abc0603ljsj2'
down_revision = 'acb362512a62'
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
        (3024, 'add-columns', 1, 'TRANSFORMATION', 'fa-copy'),
        (3025, 'aggregation', 1, 'TRANSFORMATION', 'fa-cube'),
        (3026, 'load-model', 1, 'ACTION', 'fa-cloud-download'),
        (3027, 'save-model', 1, 'TRANSFORMATION', 'fa-cloud-upload'),
        (3028, 'association-rules', 1, 'TRANSFORMATION', 'fa-long-arrow-right'),
        (3029, 'clean-missing', 1, 'ACTION', 'fa-check'),
        (3030, 'join', 1, 'TRANSFORMATION', 'fa-link'),
        (3031, 'read-shapefile', 1, 'TRANSFORMATION', 'fa-map-o'),

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
        (3024, 3),  # add-columns
        (3025, 3),  # aggregation
        (3026, 3),  # load-model
        (3027, 3),  # save-model
        (3028, 3),  # association-rules
        (3029, 3),  # clean-missing
        (3030, 3),  # join
        (3031, 3),  # read-shapefile
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
        # add-columns
        (3024, 7),
        (3024, 3001),
        # aggregation
        (3025, 7),
        (3025, 3001),
        # load-model
        (3026, 8),
        (3026, 26),
        (3026, 3001),
        # save-model
        (3027, 8),
        (3027, 26),
        (3027, 3001),
        # association-rules
        (3028, 8),
        (3028, 22),
        (3028, 3001),
        # clean-missings
        (3029, 7),
        (3029, 3001),
        # join
        (3030, 7),
        (3030, 3001),
        # read-shapefile
        (3031, 17),
        (3031, 3001),
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
        (3024, 1, 1, 'execution'),
        (3025, 1, 1, 'execution'),
        (3026, 1, 1, 'execution'),
        (3027, 1, 1, 'execution'),
        (3028, 1, 1, 'execution'),
        (3029, 1, 1, 'execution'),
        (3030, 1, 1, 'execution'),
        (3031, 1, 1, 'execution'),
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
        (3024, 'en', 'Execution'),
        (3024, 'pt', 'Execução'),
        (3025, 'en', 'Execution'),
        (3025, 'pt', 'Execução'),
        (3026, 'en', 'Execution'),
        (3026, 'pt', 'Execução'),
        (3027, 'en', 'Execution'),
        (3027, 'pt', 'Execução'),
        (3028, 'en', 'Execution'),
        (3028, 'pt', 'Execução'),
        (3029, 'en', 'Execution'),
        (3029, 'pt', 'Execução'),
        (3030, 'en', 'Execution'),
        (3030, 'pt', 'Execução'),
        (3031, 'en', 'Execution'),
        (3031, 'pt', 'Execução'),
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
        # add-columns
        (3024, 39),
        (3024, 40),
        (3024, 41),
        (3024, 43),
        (3024, 110),
        (3024, 3024),
        # aggregation
        (3025, 39),
        (3025, 40),
        (3025, 41),
        (3025, 43),
        (3025, 110),
        (3025, 3025),

        # load-model
        # (3026, 21),
        (3026, 39),
        (3026, 40),
        (3026, 41),
        (3026, 43),
        (3026, 3026),

        # save-model
        # (3027, 21),
        (3027, 39),
        (3027, 40),
        (3027, 41),
        (3027, 43),
        (3027, 3027),

        # association-rules
        (3028, 41),
        (3028, 110),
        (3028, 108),
        (3028, 3028),

        # clean-missing
        (3029, 39),
        (3029, 40),
        (3029, 41),
        (3029, 43),
        (3029, 110),
        (3029, 3029),

        # join
        (3030, 39),
        (3030, 40),
        (3030, 41),
        (3030, 43),
        (3030, 110),
        (3030, 3030),

        # read-shapefile
        (3031, 39),
        (3031, 40),
        (3031, 41),
        (3031, 43),
        (3031, 110),
        (3031, 3031),

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
        (3024, 'en', 'Add Columns',
         'Adds columns from one data source to another'),
        (3024, 'pt', 'Adicionar colunas',
         'Adiciona colunas de uma fonte de dados a outra'),
        (3025, 'en', 'Aggregation',
         'Performs aggregation of data grouped by a set of fields'),
        (3025, 'pt', 'Agregação',
         'Realiza a agregação de dados agrupados por um conjunto de atributos'),

        (3026, 'en', 'Load model', 'Loads a previously saved model (COMPSs).'),
        (3026, 'pt', 'Carregar modelo',
         'Carrega um modelo (COMPSs) salvo anteriormente.'),

        (3027, 'en', 'Save model', 'Save a machine learning model (COMPSs).'),
        (3027, 'pt', 'Salvar modelo',
         'Salva um modelo de aprendizado de máquina(COMPSs).'),

        (3028, 'en', 'Association rules', 'Association rules'),
        (3028, 'pt', 'Regras de associação', 'Regras de associação'),

        (3029, 'en', 'Clean missing',
         'Cleans or replaces missing values from fields'),
        (3029, 'pt', 'Limpar dados ausentes',
         'Limpa ou substitui dados ausentes.'),

        (
        3030, 'en', 'Join', 'Joins two data sets using a set of fields (keys)'),
        (3030, 'pt', 'Junção (join)',
         'Realiza a junção de fontes de dados usando um conjunto de atributos (chaves)'),

        (3031, 'en', 'Read shapefile', 'Read a shapefile'),
        (3031, 'pt', 'Ler shapefile', 'Lê um arquivo no formato shapefile'),
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

        (3048, 'INPUT', None, 3024, 1, 'ONE', 'input data 1'),
        (3049, 'INPUT', None, 3024, 1, 'ONE', 'input data 2'),
        (3050, 'OUTPUT', None, 3024, 1, 'MANY', 'output data'),

        (3051, 'INPUT', None, 3025, 1, 'ONE', 'input data'),
        (3053, 'OUTPUT', None, 3025, 1, 'MANY', 'output data'),

        (3054, 'OUTPUT', None, 3026, 1, 'MANY', 'output data'),

        (3055, 'INPUT', None, 3027, 1, 'ONE', 'input data'),

        (3056, 'INPUT', None, 3028, 1, 'ONE', 'input data'),
        (3057, 'OUTPUT', None, 3028, 1, 'MANY', 'output data'),

        (3058, 'INPUT', None, 3029, 1, 'ONE', 'input data'),
        (3059, 'OUTPUT', None, 3029, 1, 'MANY', 'output data'),

        (3060, 'INPUT', None, 3030, 1, 'ONE', 'input data 1'),
        (3061, 'INPUT', None, 3030, 1, 'ONE', 'input data 2'),
        (3062, 'OUTPUT', None, 3030, 1, 'MANY', 'output data'),

        (3063, 'OUTPUT', None, 3031, 1, 'MANY', 'geo data'),
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
        # add-columns
        (3048, 'en', 'input data 1', 'Input Data 1'),
        (3048, 'pt', 'dados de entrada 1', 'Dados de entrada 1'),
        (3049, 'en', 'input data 2', 'Input Data 2'),
        (3049, 'pt', 'dados de entrada 2', 'Dados de entrada 2'),
        (3050, 'en', 'output data', 'Output Data'),
        (3050, 'pt', 'dados de saída', 'Dados de saída'),

        # aggregation
        (3051, 'en', 'input data', 'Input Data'),
        (3051, 'pt', 'dados de entrada', 'Dados de entrada'),
        (3053, 'en', 'output data', 'Output Data'),
        (3053, 'pt', 'dados de saída', 'Dados de saída'),

        # load-model
        (3054, 'pt', 'modelo', 'Modelo carregado'),
        (3054, 'en', 'model', 'Loaded model'),

        # save-model
        (3055, 'pt', 'modelo', 'Modelo a ser salvo'),
        (3055, 'en', 'model', 'Model to be saved'),

        # association-rules
        (3056, 'en', 'input data', 'Input Data'),
        (3056, 'pt', 'dados de entrada', 'Dados de entrada'),
        (3057, 'en', 'output data', 'Output Data'),
        (3057, 'pt', 'dados de saída', 'Dados de saída'),

        # clean-missing
        (3058, 'en', 'input data', 'Input Data'),
        (3058, 'pt', 'dados de entrada', 'Dados de entrada'),
        (3059, 'en', 'output data', 'Output Data'),
        (3059, 'pt', 'dados de saída', 'Dados de saída'),

        # join
        (3060, 'en', 'input data 1', 'Input Data 1'),
        (3060, 'pt', 'dados de entrada 1', 'Dados de entrada 1'),
        (3061, 'en', 'input data 2', 'Input Data 2'),
        (3061, 'pt', 'dados de entrada 2', 'Dados de entrada 2'),
        (3062, 'en', 'output data', 'Output Data'),
        (3062, 'pt', 'dados de saída', 'Dados de saída'),

        (3063, 'pt', 'dados geo', 'Dados geospaciais'),
        (3063, 'en', 'geo data', 'Geospatial data'),
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
        (3048, 1),  # add-columns
        (3049, 1),
        (3050, 1),

        (3051, 1),  # aggregation
        (3053, 1),

        (3054, 2),  # load-model
        (3054, 4),
        (3054, 14),
        (3054, 15),
        (3054, 20),
        (3054, 18),

        (3055, 8),  # save-model
        (3055, 2),
        (3055, 18),
        (3055, 7),
        (3055, 4),

        (3056, 1),  # association-rules
        (3057, 1),

        (3058, 1),  # clean-missing
        (3059, 1),

        (3060, 1),  # join
        (3061, 1),
        (3062, 1),

        (3063, 1),  # read-shapefile

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
        # data-reader
        (3084, 'mode', 'TEXT', 0, 5, 'DROPMALFORMED', 'dropdown', None,
         '[{\"value\": \"Ignore whole corrupted record\", \"key\": \"DROPMALFORMED\"},'
         '{\"value\": \"Stop processing and raise error\", \"key\": \"FAILFAST\"}]'
         , 'EXECUTION', 3001),
        # add-columns
        (
        3085, 'aliases', 'TEXT', 0, 4, '_l,_r', 'text', None, None, 'EXECUTION',
        3024),
        # aggregation
        (3086, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 3025),
        (3087, 'function', 'TEXT', 1, 2, None, 'attribute-function', None,
         '{\"functions\": ['
         '{\"value\": \"Average (AVG)\", \"key\": \"avg\", \"help\": \"Computes the average of each group\"}, '
         '{\"value\": \"Collect List\", \"key\": \"collect_list\", \"help\": \"Aggregate function: returns a list of objects with duplicates.\"}, '
         '{\"value\": \"Collect Set\", \"key\": \"collect_set\", \"help\": \"Aggregate function: returns a set of objects with duplicate elements eliminated.\"}, '
         '{\"value\": \"Count\", \"key\": \"count\", \"help\": \"Counts the total of records of each group\"}, '
         '{\"value\": \"First\", \"key\": \"first\", \"help\": \"Returns the first element of group\"}, '
         '{\"value\": \"Last\", \"key\": \"last\", \"help\": \"Returns the last element of group\"}, '
         '{\"value\": \"Maximum (MAX)\", \"key\": \"max\", \"help\": \"Returns the max value of each group for one attribute\"}, '
         '{\"value\": \"Minimum (MIN)\", \"key\": \"min\", \"help\": \"Returns the min value of each group for one attribute\"}, '
         '{\"value\": \"Sum\", \"key\": \"sum\", \"help\": \"Returns the sum of values of each group for one attribute\"}'
         '], \"options\": {\"show_alias\": true, \"description\": \"Add one of more lines with attribute to be used, function and alias to compute aggregate function over groups.\", '
         '\"title\": \"Aggregate operation\"}}', 'EXECUTION', 3025),
        # load-model
        (3088, 'name', 'TEXT', 1, 1, None, 'text', None, None, 'EXECUTION',
         3026),
        # save-model
        (3089, 'name', 'TEXT', 1, 2, None, 'text', None, None, 'EXECUTION',
         3027),
        (3090, 'write_mode', 'TEXT', 1, 3, 'ERROR', 'dropdown', None,
         '[{\"value\": \"Overwrite\", \"key\": \"OVERWRITE\"}, '
         '{\"value\": \"Raise error\", \"key\": \"ERROR\"}]', 'EXECUTION',
         3027),

        # association-rules
        (3091, 'confidence', 'DECIMAL', 1, 1, 0.9, 'decimal', None, None,
         'EXECUTION', 3028),
        (3092, 'rules_count', 'INTEGER', 1, 2, 200, 'integer', None, None,
         'EXECUTION', 3028),
        (
        3093, 'col_items', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
        'EXECUTION', 3028),
        (3094, 'col_support', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 3028),

        # clean-missing
        (3095, 'attributes', 'TEXT', 1, 0, None, 'attribute-selector', None,
         None, 'EXECUTION', 3029),
        (3096, 'cleaning_mode', 'TEXT', 1, 1, None, 'dropdown', None,
         "[{\"key\": \"MEAN\", \"value\": \"Replace with mean\"}, "
         "{\"key\": \"VALUE\", \"value\": \"Replace with value\"}, "
         "{\"key\": \"MEDIAN\", \"value\": \"Replace with approx. median\"}, "
         "{\"key\": \"MODE\", \"value\": \"Replace with mode\"}, "
         "{\"key\": \"REMOVE_ROW\", \"value\": \"Remove entire row\"}, "
         "{\"key\": \"REMOVE_COLUMN\", \"value\": \"Remove entire column\"}]",
         'EXECUTION', 3029),
        (3097, 'value', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION',
         3029),

        # join
        (
        3098, 'left_attributes', 'TEXT', 1, 0, None, 'attribute-selector', None,
        None, 'EXECUTION', 3030),
        (3099, 'right_attributes', 'TEXT', 1, 0, None, 'attribute-selector',
         None, None, 'EXECUTION', 3030),
        (3100, 'join_type', 'TEXT', 1, 0, None, 'dropdown', None,
         "[{\"key\": \"inner\", \"value\": \"Inner join\"},"
         "{\"key\": \"left_outer\", \"value\": \"Left outer join\"}, "
         "{\"key\": \"right_outer\", \"value\": \"Right outer join\"}]",
         'EXECUTION', 3030),
        (3101, 'keep_right_keys', 'INTEGER', 0, 0, None, 'checkbox', None, None,
         'EXECUTION', 3030),
        (3102, 'match_case', 'INTEGER', 1, 0, 1, 'checkbox', None, None,
         'EXECUTION', 3030),
        (3103, 'aliases', 'TEXT', 0, 4, '_l, _r', 'text', None, None,
         'EXECUTION', 3030),

        (3104, 'shapefile', 'TEXT', 1, 1, None, 'text', None, None, 'EXECUTION',
         3031),
        (3105, 'polygon', 'TEXT', 0, 2, 'points', 'text', None, None,
         'EXECUTION', 3031),
        (3106, 'lat_lon', 'INTEGER', 0, 3, True, 'checkbox', None, None,
         'EXECUTION', 3031),

        # stbscan -- appending
        (
        3107, 'alias', 'TEXT', 0, 6, 'Cluster', 'text', None, None, 'EXECUTION',
        3021),

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
        # data-reader
        (3084, 'en', 'What to do in case of invalid data',
         'What to do in case of invalid data'),
        (3084, 'pt', 'O que fazer em caso de dados inválidos',
         'Opção sobre o que fazer em caso de dados inválidos.'),

        # add-columns
        (3085, 'en', 'Suffixes for attributes (2 values, comma separated)',
         'Attributes are suffixed in order to avoid name collision.'),
        (3085, 'pt',
         'Sufixos para os atributos (2 valores, separados por vírgula)',
         'Os atributos são sufixados a fim de evitar colisão de nomes.'),

        # aggregation
        (3086, 'en', 'Select attribute(s) for aggregation',
         'Choose one or more attributes to aggregate data with'),
        (3086, 'pt', 'Selecione o(s) atributos para agregação',
         'Escola um ou mais atributos para a agregação.'),
        (3087, 'en', 'Aggregation function',
         'Function applied to aggregated data'),
        (3087, 'pt', 'Função de agregação',
         'Função a ser aplicada aos dados agregados'),

        # load-model
        (3088, 'en', 'Model name', 'Model name'),
        (3088, 'pt', 'Nome do modelo', 'Nome do modelo'),

        # save-model
        (3089, 'en', 'Model name', 'Model name'),
        (3089, 'pt', 'Nome do modelo', 'Nome do modelo'),
        (3090, 'en', 'Action if model exists', 'Action if model exists'),
        (
        3090, 'pt', 'Ação caso modelo já exista', 'Ação caso modelo já exista'),

        # association-rules
        (3091, 'en', 'Min. confidence', 'Minimum Confidence'),
        (3091, 'pt', 'Confiança mímina', 'Confiança mímina'),
        (3092, 'en', 'Number of rules to generate',
         'Number of rules to generate'),
        (3092, 'pt', 'Quantidade de regras a serem geradas',
         'Quantidade de regras a serem geradas'),
        (3093, 'en', 'Field with the itemset', 'The column name of the items.'),
        (3093, 'pt', 'Coluna com os itemsets', 'Coluna com os itemsets.'),
        (3094, 'en', 'Field with the support',
         'The column name of the support.'),
        (3094, 'pt', 'Coluna com os suportes de cada itemset',
         'Coluna com os suportes de cada itemset.'),

        # cleaning_mode
        (3095, 'en', 'Attribute(s)',
         'Select one or more attributes to be cleaned'),
        (3095, 'pt', 'Atributo(s)',
         'Selecione um ou mais atributos a ser(em) limpos.'),
        (3096, 'en', 'Cleaning mode', 'Type of cleaning to be performed.'),
        (3096, 'pt', 'Tipo de limpeza', 'Tipo de limpeza a ser realizada.'),
        (3097, 'en', 'Value', 'Value used to replace missing values.'),
        (3097, 'pt', 'Valor',
         'Valor a ser usado para substituir os valores ausentes.'),

        # join
        (3098, 'en', 'Attribute(s) from first data source',
         'Select one or more attributes from the first data source.'),
        (3099, 'en', 'Attribute(s) from second data source',
         'Select one or more attributes from the second data source.'),
        (3100, 'en', 'Join type', 'Type of join to be performed.'),
        (3101, 'en', 'Keep keys from second data source',
         'Keys columns used in the join could be ignored because they are already present in the first data source.'),
        (3102, 'en', 'Match case when comparing keys',
         'If checked, a case sensitive matching will be performed when comparing keys'),
        (3103, 'en', 'Suffixes for attributes (2 values, comma separated)',
         'Attributes are suffixed in order to avoid name collision.'),
        (3098, 'pt', 'Atributo(s) da primeira fonte de dados',
         'Selecione um ou mais atributos da primeira fonte de dados.'),
        (3099, 'pt', 'Atributo(s) da segunda fonte de dados',
         'Selecione um ou mais atributos da segunda fonte de dados.'),
        (3100, 'pt', 'Tipo de junção (join)',
         'Tipo da junção (join) a ser realizada.'),
        (3101, 'pt', 'Manter chaves da segunda fonte de dados',
         'Chaves usads na junção podem ser ignoradas porque elas já estão presentes na primeira fonte de dados.'),
        (3102, 'pt',
         'Diferenciar maiúsculas e minúsculas quando comparar chaves',
         'Se marcado, irá diferenciar maiúsculas e minúsculas quando estiver comparando as chave.'),
        (3103, 'pt',
         'Sufixos para os atributos (2 valores, separados por vírgula)',
         'Os atributos são sufixados a fim de evitar colisão de nomes.'),

        # read-shapefile
        (3104, 'en', 'Shapefile', 'Shapefile'),
        (3104, 'pt', 'Shapefile', 'Shapefile'),
        (
        3105, 'en', 'Alias to the polygon field', 'Alias to the polygon field'),
        (3105, 'pt', 'Nome para o campo do polígono',
         'Nome para o campo do polígono.'),
        (3106, 'en', 'The points are expressed as (LAT, LON):',
         'Whether the points are expressed as (LAT,LON) or (LON,LAT).'),
        (3106, 'pt', 'Os pontos são expressos como (LAT,LON):',
         'Se os pontos são expressos com (LAT,LON) ou (LON,LAT).'),

        # stbscan
        (3107, 'en', 'Alias', 'Alias to the predicted Cluster'),
        (3107, 'pt', 'Alias',
         'Nome para a nova coluna com os clusters previstos.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


# --------------------------------------------------------------------------------

all_commands = [

    (
        'DELETE FROM operation_platform WHERE operation_id IN '
        '(24, 15, 85, 16, 21, 53) and platform_id = 3;',
        'INSERT INTO operation_platform (`operation_id`, `platform_id`) VALUES '
        '(15,3), (16, 3), (21, 3), (24,3), (53, 3), (85,3)'),
    (_insert_operation,
     'DELETE FROM operation WHERE id >= 3024'),
    (_insert_new_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id >= 3024'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id >= 3024'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id >= 3024'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id >= 3024'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id >= 3024'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id >= 3024'),
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id >= 3048'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id >= 3048'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id >= 3048'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id >= 3084'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id >= 3084'),

    ("""
        UPDATE operation_form_field
        SET `values` =
            '[{\"key\": \"error\", \"value\": \"Do not overwrite, raise error\" },\r\n '
            '{\"key\": \"ignore\", \"value\": \"Ignore if file exists\" },\r\n '
            '{\"key\": \"overwrite\", \"value\": \"Overwrite if file exists\" }\r\n]'
        WHERE id=3053;""",
     """
         UPDATE operation_form_field
         SET `values` =
                 '[{ \"key\": \"append\", \"value\": \"Append data to the existing file\" },\r\n '
                 '{\"key\": \"error\", \"value\": \"Do not overwrite, raise error\" },\r\n'
                 '{\"key\": \"ignore\", \"value\": \"Ignore if file exists\" },\r\n '
                 '{\"key\": \"overwrite\", \"value\": \"Overwrite if file exists\" }\r\n]'
             WHERE id=3053;"""),
    ("""UPDATE platform_translation
            SET description = 'COMPSs 2.2 Camellia - Execution platform'
            WHERE id = 3 and locale = 'en';
    """, """
        UPDATE platform_translation
            SET description = 'COMPSs 2.1 Bougainvillea - Execution platform'
            WHERE id = 3 and locale = 'en';
    """),

    ("""
        UPDATE platform_translation
            SET description = 'COMPSs 2.2 Camellia - Plataforma de execução'
            WHERE id = 3 and locale = 'pt';
    """, """
        UPDATE platform_translation
            SET description = 'COMPSs 2.1 Bougainvillea - Plataforma de execução'
            WHERE id = 3 and locale = 'pt';
    """),

    ("""
        UPDATE operation_form_field
        SET `suggested_widget` = 'TEXT'
        WHERE id=3079;
    """,
     """
         UPDATE operation_form_field
         SET `suggested_widget` = 'attribute-selector'
         WHERE id=3079;
     """),

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
