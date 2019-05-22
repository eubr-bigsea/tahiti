# coding=utf-8
"""index_model_interface, aliases in Add Column and Join

Revision ID: 42d80390b2db
Revises: 6da9e093897c
Create Date: 2017-09-19 11:52:31.797520

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '42d80390b2db'
down_revision = '6da9e093897c'
branch_labels = None
depends_on = None


def _insert_operation_form():
    tb = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (117, 1, 1, 'execution'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String)
    )

    columns = [c.name for c in tb.columns]
    data = [
        (117, 'en', 'Execution'),
        (117, 'pt', 'Execução'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (24, 117),
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

    columns = [c.name for c in tb.columns]
    data = [
        [362, 'aliases', 'TEXT', 0, 4, 'ds0_, ds1_', 'text',
         None, None, 'EXECUTION', 16],
        [363, 'aliases', 'TEXT', 0, 4, 'ds0_, ds1_', 'text',
         None, None, 'EXECUTION', 117],
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

    columns = [c.name for c in tb.columns]
    data = [
        [362, 'en', 'Prefix for attributes (2 values, comma separated)',
         'Attributes are prefixed in order to avoid name collision.'],
        [362, 'pt',
         'Prefixo para os atributos (2 valores, separados por vírgula)',
         'Os atributos são prefixados a fim de evitar colisão de nomes'],
        [363, 'en', 'Prefix for attributes (2 values, comma separated)',
         'Attributes are prefixed in order to avoid name collision.'],
        [363, 'pt',
         'Prefixo para os atributos (2 valores, separados por vírgula)',
         'Os atributos são prefixados a fim de evitar colisão de nomes'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (
        '''INSERT INTO operation_port_interface_operation_port
            (operation_port_id, operation_port_interface_id)
            VALUES(93, 4), (83,4), (46, 4)''',
        '''DELETE FROM operation_port_interface_operation_port WHERE
            (operation_port_id = 93 AND operation_port_interface_id = 4) OR
              (operation_port_id = 83 AND operation_port_interface_id = 4) OR
              (operation_port_id = 46 AND operation_port_interface_id = 4)
            '''
    ),
    ("UPDATE operation_form_field SET `default` = '1' WHERE id = 15",
     "UPDATE operation_form_field SET `default` = NULL WHERE id = 15"),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id = 117'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id = 117'),
    (_insert_operation_operation_form,
     '''DELETE FROM operation_operation_form WHERE operation_form_id = 117
     AND operation_id = 24'''),
    (
        _insert_operation_form_field,
        'DELETE from operation_form_field WHERE id IN (362, 363)'
    ),
    (
        _insert_operation_form_field_translation,
        'DELETE from operation_form_field_translation WHERE id IN (362, 363)'
    ),

    # Translations
    # Citron 391
    ('''UPDATE operation_form_field_translation
        SET label = 'Fonte de dados',
        help = 'Fonte de dados a ser usada como entrada.'
         WHERE id = 1 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Data source',
     help = 'Data source to be used as input.'
      WHERE id = 1 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Usar a primeira linha como cabeçalho',
        help = 'Arquivo contém cabeçalho com informações sobre atributos?'
         WHERE id = 75 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Use first line as header',
     help =
        'Does file the first line contain header information about attributes?'
      WHERE id = 75 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Separador de atributos',
        `help` = concat('Caractere usado como separador de atributo ',
            '(pode usar {tab} ou {new_line}).')
         WHERE id = 76 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Attribute separator',
     help = 'Character used as attribute separator.'
      WHERE id = 76 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Inferir esquema da fonte de dados',
        `help` = 'Inferir esquema da fonte de dados a partir dos registros.'
         WHERE id = 77 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Infer data source schema',
     help = 'Infer data source schema from attribute\\'s values.'
      WHERE id = 77 AND locale = 'pt'
     ''',
     ),

    # 392
    ('''UPDATE operation_form_field_translation
        SET label = 'Nome da fonte de dados',
        `help` = 'Nome da fonte de dados.'
         WHERE id = 81 AND locale = 'pt'
        ''',
     '''UPDATE operation_form_field_translation
     SET label = 'Data source name',
     help = 'Data source name.'
      WHERE id = 81 AND locale = 'pt' ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Caminho da fonte de dados (relativo ao armazenamento)',
        `help` = 'Caminho da fonte de dados (relativo ao armazenamento).'
         WHERE id = 82 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Data source path (relative to storage)',
     help = 'Data source path (relative to storage).'
      WHERE id = 82 AND locale = 'pt'
     ''',
     ),
    (
        '''UPDATE operation_form_field_translation
        SET label = 'Formato de saída',
        help = 'Formato de saída.'
         WHERE id = 83 AND locale = 'pt'
        ''',
        '''UPDATE operation_form_field_translation
        SET label = 'Output format',
        `help` = 'Output format.'
         WHERE id = 83 AND locale = 'pt'
        ''',

    ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Modo de gravação',
        `help` = 'Ação a ser realizada se o arquivo destino já existe.'
         WHERE id = 85 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Overwrite mode',
     help = 'Action in case of trying to write over an existing file.'
      WHERE id = 85 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Salvar cabeçalho',
        `help` = 'Salva o cabeçalho se o formato for CSV.'
         WHERE id = 86 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Save header',
     help = 'Save header information if format is CSV.'
      WHERE id = 86 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Armazenamento',
        `help` = 'Armazenamento onde o arquivo é salvo.'
         WHERE id = 87 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Storage',
     help = 'Storage where data is saved.'
      WHERE id = 87 AND locale = 'pt'
     ''',
     ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(97, 'pt', 'Atributos a serem usados', 'Atributos a serem usados')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 97
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(98, 'pt', 'Nome do novo atributo', 'Nome do novo atributo')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 98
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(99, 'pt', 'Atributo usado para predição',
            'Atributo usado para predição.')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 99
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(100, 'pt', 'Atributo usado como label',
            'Atributo usado como label')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 100
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(101, 'pt', 'Métrica usada para avaliação',
            'Métrica usada para avaliação')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 101
        '''
    ),
    # Citron 397
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(242, 'pt', 'Atributos usado como features',
            'Atributos usado como features')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 242
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(243, 'pt', 'Atributo usado como rótulo (label)',
            'Atributo usado como rótulo (label)')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 243
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(244, 'pt', 'Nome do atributo usado como predição',
            'Nome do atributo usado como predição.')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 244
        '''
    ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Iterações máximas',
        `help` = 'Iterações máximas.'
         WHERE id = 245 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Max. iterations',
     help = 'Max. iterations.'
      WHERE id = 245 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Regularização',
        `help` = 'Regularização.'
         WHERE id = 247 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Regularization',
     help = 'SRegularization.'
      WHERE id = 247 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Mix. para ElasticNet (entre 0 e 1)',
        `help` = 'Mix. para ElasticNet na faixa [0, 1].'
         WHERE id = 248 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'ElasticNet mixing',
     help = 'ElasticNet mixing.'
      WHERE id = 248 AND locale = 'pt'
     ''',
     ),
    # Citron 398
    ('''UPDATE operation_form_field_translation
        SET label = 'Iterações máximas',
        `help` = 'Iterações máximas.'
         WHERE id = 260 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Max. iterations',
     help = 'Maximum number of iterations.'
      WHERE id = 260 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Profundidade máxima da agregação',
        `help` = 'Profundidade máxima da agregação.'
         WHERE id = 261 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Aggregation depth',
     help = 'Aggregation depth.'
      WHERE id = 261 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Semente (seed)',
        `help` = 'Semente (seed).'
         WHERE id = 262 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Seed',
     help = 'Seed.'
      WHERE id = 262 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Atributo usado como censor (deve conter valores 0 ou 1)',
        `help` = 'Atributo usado como censor (deve conter valores 0 ou 1).'
         WHERE id = 263 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Censor',
     help = 'Censor.'
      WHERE id = 263 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Valores para probabilidade dos quantis',
        `help` = 'Valores para probabilidade dos quantis.'
         WHERE id = 264 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Quantile probabilities',
     help = 'Quantile probabilities.'
      WHERE id = 264 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Atributo com os quantis',
        `help` = 'Atributo com os quantis.'
         WHERE id = 265 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Quantiles attribute',
     help = 'Quantiles attribute.'
      WHERE id = 265 AND locale = 'pt'
     ''',
     ),
    # Citron 400
    ('''UPDATE operation_form_field_translation
        SET label = 'Iterações máximas',
        `help` = 'Iterações máximas.'
         WHERE id = 269 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Max. iterations',
     help = 'Max. iterations.'
      WHERE id = 269 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Profundidade máxima',
        `help` = 'Profundidade máxima.'
         WHERE id = 270 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Max. depth',
     help = 'Max. depth.'
      WHERE id = 270 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Instâncias mínimas',
        `help` = 'Instâncias mínimas.'
         WHERE id = 271 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Min. instance',
     help = 'Min. instance.'
      WHERE id = 271 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Ganho de informação mínimo',
        `help` = 'Ganho de informação mínimo.'
         WHERE id = 272 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Min. info gain',
     help = 'Min. info gain.'
      WHERE id = 272 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Semente (seed)',
        `help` = 'Semente (seed).'
         WHERE id = 273 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Seed',
     help = 'Seed.'
      WHERE id = 273 AND locale = 'pt'
     ''',
     ),
    # Citron 403
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(121, 'pt', 'Atributo',
            'Atributo de entrada.')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 121
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(122, 'pt', 'Nome do novo atributo (alias)',
            'Nome do novo atributo (alias).')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 122
        '''
    ),
    # Citron 404
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(111, 'pt', 'Tipo',
            'Tipo da divisão de texto.')''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 111
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(112, 'pt', 'Expressão (apenas se tipo for expressão regular)',
            'Expressão (apenas se tipo for expressão regular). Sintaxe Java.')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 112
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(113, 'pt', 'Tamanho mínimo das partes (tokens)',
        'Tamanho mínimo das partes (tokens). Parte menores serão descartadas.')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 113
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(119, 'pt', 'Atributos',
            'Atributos.')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 119
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(120, 'pt', 'Nome do novo atributo (alias)',
            'Nome do novo atributo (alias).')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 120
        '''
    ),
    # Citron 405
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(114, 'pt', 'Atributos',
            'Atributos.')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 114
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(115, 'pt', 'Nome do novo atributo (alias)',
            'Nome do novo atributo (alias).')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 115
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(116, 'pt', 'Lista de stop words',
            'Lista de stop words, separadas por vírgula.')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 116
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(117, 'pt', 'Atributo da segunda fonte de dados com as stop words',
            'Atributo da segunda fonte de dados com as stop words.')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 117
        '''
    ),
    # Citron 408
    (
        ['''
            UPDATE operation_form_field_translation SET label = 'Percentual'
            WHERE id = 74 AND locale = 'pt' ''',
         '''
        UPDATE operation_form_field_translation SET label = 'Percentage'
        WHERE id = 74 AND locale = 'en' '''
         ],
        ['''
            UPDATE operation_form_field_translation SET label = 'percentual'
            WHERE id = 74 AND locale = 'pt' ''',
         '''
        UPDATE operation_form_field_translation SET label = 'percentage'
        WHERE id = 74 AND locale = 'en' '''
         ]
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(102, 'pt', 'Tipo de amostragem ou partição',
            'Tipo de amostragem ou partição.')
        ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 102
        '''
    ),
    (
        '''
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(105, 'pt', 'Total de registros', 'Total de registros.') ''',
        '''
        DELETE FROM operation_form_field_translation WHERE locale = 'pt'
        AND id = 105
        '''
    ),
    # Citron 409
    ('''UPDATE operation_form_field_translation
        SET label = 'Pesos',
        `help` = 'Pesos usados para dividir a fonte de dados.'
         WHERE id = 16 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Weights',
     help = 'Weights used to split the data source.'
      WHERE id = 16 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Semente (seed)',
        `help` =
        'Semente (seed) usada para iniciar o gerador de números aleatórios.'
         WHERE id = 17 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Seed',
     help = 'Seed used to initialize the random number generator..'
      WHERE id = 17 AND locale = 'pt'
     ''',
     ),
    # Citron 410
    ('''UPDATE operation_form_field_translation
        SET label = 'Atributo(s) da primeira fonte de dados',
        `help` = 'Selecione um ou mais atributos da primeira fonte de dados.'
         WHERE id = 11 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Attribute(s) from first data source',
     help = 'Select one or more attributes from the first data source.'
      WHERE id = 11 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Atributo(s) da segunda fonte de dados',
        `help` = 'Selecione um ou mais atributos da segunda fonte de dados.'
         WHERE id = 12 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Attribute(s) from second data source',
     help = 'Select one or more attributes from the second data source.'
      WHERE id = 12 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Tipo de junção (join)',
        `help` = 'Tipo da junção (join) a ser realizada.'
         WHERE id = 13 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Join type',
     help = 'Type of join to be performed.'
      WHERE id = 13 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Manter chaves da segunda fonte de dados',
        `help` = concat('Chaves usads na junção podem ser ignoradas ',
        'porque elas já estão presentes na primeira fonte de dados.')
         WHERE id = 14 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Keep keys from second data source',
     help = concat('Keys columns used in the join could be ignored',
        'because they are already present in the first data source.')
      WHERE id = 14 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET
        label = 'Diferenciar maiúsculas e minúsculas quando comparar chaves',
        `help` = concat('Se marcado, irá diferenciar maiúsculas e minúsculas ',
        'quando estiver comparando as chaves.')
         WHERE id = 15 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Match case when comparing keys',
     help = concat('If checked, a case sensitive matching will ',
        'be performed when comparing keys.')
      WHERE id = 15 AND locale = 'pt'
     ''',
     ),
    # Citron 411
    ('''UPDATE operation_form_field_translation
        SET label = 'Atributo(s)',
        `help` = 'Selecione um ou mais atributos a ser(em) limpos.'
         WHERE id = 18 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Attribute(s) from first data source',
     help = 'Select one or more attributes to be cleaned.'
      WHERE id = 18 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Tipo de limpeza',
        `help` = 'Tipo de limpeza a ser realizada.'
         WHERE id = 19 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Cleaning mode',
     help = 'Type of cleaning to be performed.'
      WHERE id = 19 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Valor',
        `help` = 'Valor a ser usado para substituir os valores ausentes.'
         WHERE id = 20 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Value',
     help = 'Value used to replace missing values.'
      WHERE id = 20 AND locale = 'pt'
     ''',
     ),
    # Citron 412
    ('''UPDATE operation_form_field_translation
        SET label = 'Atributo(s)',
        `help` = concat('Selecione um ou mais atributos a serem usados como ',
            'critério de ordenação. A ordem dos atributos faz diferença.')
         WHERE id = 23 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Attribute(s)',
     help =
     'Select one or more attributes to be used as sort criteria. Order matters.'
      WHERE id = 23 AND locale = 'pt'
     ''',
     ),
    # Citron 413
    ('''UPDATE operation_form_field_translation
        SET label = 'Atributo(s)',
        `help` = concat('Escolha um ou mais atributos. Esses atributos serão ',
            'selecionados para a saída da fonte de dados.')
         WHERE id = 6 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Attribute(s)',
     help =
     concat('Choose one or more attributes. These attributes will ',
        'be selected to the output data set.')
      WHERE id = 6 AND locale = 'pt'
     ''',
     ),
    # Citron 413
    ('''UPDATE operation_form_field_translation
        SET label = 'Expressão',
        `help` = concat('Expressão a ser aplicada a um atributo para gerar ',
            'outro atributo. Veja a ajuda para saber as funções suportadas ',
            'e a sintaxe.')
         WHERE id = 88 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Expression',
     help =
     concat('Expression to apply to an attribute in order to generate another ',
        'attribute. See help for supported functions and syntax.')
      WHERE id = 88 AND locale = 'pt'
     ''',
     ),
    ('''UPDATE operation_form_field_translation
        SET label = 'Nome do atributo transformado',
        `help` = concat('Escolha um ou mais atributos. Esses atributos serão ',
            'selecionados para a saída da fonte de dados.')
         WHERE id = 89 AND locale = 'pt'
        ''',

     '''UPDATE operation_form_field_translation
     SET label = 'Name for transformed attribute',
     help = 'Name for the transformed attribute.'
      WHERE id = 89 AND locale = 'pt'
     ''',
     ),
]


# noinspection PyCallingNonCallable
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
