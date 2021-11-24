"""Experiments platform

Revision ID: af8eeaf80cd6 
Revises: a6aa24bf8d35
"""
import json
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText

# revision identifiers, used by Alembic.
revision = 'af8eeaf80cd6'
down_revision = 'a6aa24bf8d35'
branch_labels = None
depends_on = None

# --------------------------------------------------------------
# ATENTION: You must revise this auto-generated code.
# Please, review offsets and commands before running a migration
# and optionally, perform a database backup. If everything is 
# OK, remove this comment.
# --------------------------------------------------------------
META_PLATFORM = 1000

BASE_OP = 2100
BASE_CATEGORY = 2100
BASE_FORM = 2100
BASE_FORM_FIELD = 2100

READ_DATA = BASE_OP + 0

# Edit
CHANGE_DATA_TYPE = BASE_OP + 1
RENAME = BASE_OP + 2
DELETE = BASE_OP + 3
FIND_REPLACE = BASE_OP + 4

# Data
SORT = BASE_OP + 5
FILTER = BASE_OP + 6
GROUP = BASE_OP + 7
JOIN = BASE_OP + 8
CONCATE_ROWS = BASE_OP + 9
SAMPLE = BASE_OP + 10
LIMIT = BASE_OP + 11
WINDOW_FUNCTION = BASE_OP + 12
PYTHON_CODE = BASE_OP + 13
ADD_BY_FORMULA = BASE_OP + 14

# Transform
INVERT_BOOLEAN = BASE_OP + 15
RESCALE = BASE_OP + 16
ROUND_NUMBER = BASE_OP + 17
DISCRETIZE = BASE_OP + 18
NORMALIZE = BASE_OP + 19
FORCE_RANGE = BASE_OP + 20
TS_TO_DATE = BASE_OP + 21
TO_UPPER = BASE_OP + 22
TO_LOWER = BASE_OP + 23
CAPITALIZE = BASE_OP + 24
REMOVE_ACCENTS = BASE_OP + 25
NORMALIZE_TEXT = BASE_OP + 26
CONCAT_ATTRIBUTE = BASE_OP + 27
TRIM = BASE_OP + 28
TRUNCATE_TEXT = BASE_OP + 29
SPLIT_INTO_WORDS = BASE_OP + 30
SUBSTRING = BASE_OP + 31
PARSE_TO_DATE = BASE_OP + 32
EXTRACT_NUMBERS = BASE_OP + 33
EXTRACT_WITH_REGEX = BASE_OP + 34
EXTRACT_FROM_ARRAY = BASE_OP + 35
EXPAND_FROM_ARRAY = BASE_OP + 36
FOLD_ARRAY = BASE_OP + 37
CHANGE_ARRAY_TYPE = BASE_OP + 38
SORT_ARRAY = BASE_OP + 39
FORCE_DATE_RANGE = BASE_OP + 40
UPDATE_HOUR = BASE_OP + 41
TRUNCATE_DATE_TO = BASE_OP + 42
DATE_DIFF = BASE_OP + 43
DATE_ADD = BASE_OP + 44
DATE_PART = BASE_OP + 45
FORMAT_DATE = BASE_OP + 46
DATE_TO_TS = BASE_OP + 47

# Encode / decode
ESCAPE_XML = BASE_OP + 48
ESCAPE_UNICODE = BASE_OP + 49
STEMMING = BASE_OP + 50
N_GRAMS = BASE_OP + 51
OBFUSCATE = BASE_OP + 52
ONE_HOT_ENCODE = BASE_OP + 53

# Flag
FLAG_IN_RANGE = BASE_OP + 54
FLAG_INVALID = BASE_OP + 55
FLAG_EMPTY = BASE_OP + 56
FLAG_WITH_FORMULA = BASE_OP + 57


# Fix data
FILL_MISSING = BASE_OP + 58
HANDLE_INVALID = BASE_OP + 59
REMOVE_EMPTY = BASE_OP + 60
REMOVE_INVALID = BASE_OP + 61

# Categories
CAT_INTERN = BASE_CATEGORY + 0
CAT_EDIT = BASE_CATEGORY + 1 
CAT_DATA = BASE_CATEGORY + 2
CAT_TRANSFORM = BASE_CATEGORY + 3
CAT_ENCODE = BASE_CATEGORY + 4
CAT_FLAG  = BASE_CATEGORY + 5
CAT_FIX = BASE_CATEGORY + 6
CAT_CONTEXT = BASE_CATEGORY + 7
CAT_TEXT = BASE_CATEGORY + 8
CAT_INTEGER = BASE_CATEGORY + 9
CAT_BOOL = BASE_CATEGORY + 10 
CAT_DATE = BASE_CATEGORY + 11 
CAT_ARRAY= BASE_CATEGORY + 12

MAX_OP = BASE_OP + 61

ALL_OPS = [
    # Edit
    CHANGE_DATA_TYPE, RENAME, DELETE, FIND_REPLACE, 
    # Data
    SORT, FILTER, GROUP, JOIN, CONCATE_ROWS, SAMPLE,
    LIMIT, WINDOW_FUNCTION, PYTHON_CODE, ADD_BY_FORMULA,
    # Transform
    INVERT_BOOLEAN, RESCALE, ROUND_NUMBER, DISCRETIZE, NORMALIZE,
    FORCE_RANGE, TS_TO_DATE, TO_UPPER, TO_LOWER, CAPITALIZE,
    REMOVE_ACCENTS, NORMALIZE_TEXT, CONCAT_ATTRIBUTE, TRIM,
    TRUNCATE_TEXT, SPLIT_INTO_WORDS, SUBSTRING, PARSE_TO_DATE,
    EXTRACT_NUMBERS, EXTRACT_WITH_REGEX, EXTRACT_FROM_ARRAY,
    EXPAND_FROM_ARRAY, FOLD_ARRAY, CHANGE_ARRAY_TYPE, SORT_ARRAY,
    FORCE_DATE_RANGE, UPDATE_HOUR, TRUNCATE_DATE_TO, DATE_DIFF,
    DATE_ADD, DATE_PART, FORMAT_DATE, DATE_TO_TS,
    # Encode / decode
    ESCAPE_XML, ESCAPE_UNICODE, STEMMING, N_GRAMS,
    OBFUSCATE, ONE_HOT_ENCODE,
    # Flag
    FLAG_IN_RANGE, FLAG_INVALID, FLAG_EMPTY, FLAG_WITH_FORMULA,
    # Fix data
    FILL_MISSING, HANDLE_INVALID, REMOVE_EMPTY, REMOVE_INVALID,
 ]

ATTRIBUTES_FORM = BASE_FORM + 2
ALIASES_FORM = BASE_FORM + 3
KEEP_ATTRIBUTE_FORM = BASE_FORM + 4

def _insert_platform(conn):
    conn.execute(
        ''' INSERT INTO platform(id, slug, enabled, icon, version, plugin)
            VALUES(%s, %s, %s, %s, %s, %s)''', 
        META_PLATFORM, 'meta', 1, ' ', None, 0)

def _delete_platform(conn):
    conn.execute(
        'DELETE from platform WHERE id BETWEEN %s AND %s', 
        META_PLATFORM, META_PLATFORM)

def _insert_platform_translation(conn):
    tb = table('platform_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
      [META_PLATFORM, 'pt', 'Platforma Meta', 'Plataforma que gera código para outras plataformas'],
      [META_PLATFORM, 'en', 'Meta Platform', 'Generates code to other platforms'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_platform_translation(conn):
    conn.execute(
        'DELETE from platform_translation WHERE id BETWEEN %s AND %s', 
        META_PLATFORM, META_PLATFORM)


def _insert_operation(conn):
    tb = table('operation',
                column('id', Integer), 
                column('slug', String), 
                column('enabled', Boolean), 
                column('type', String), 
                column('icon', String), 
                column('css_class', String), 
                column('doc_link', String))
    columns = [c.name for c in tb.columns]
    data = [
      [READ_DATA, 'read-data', 1, 'TRANSFORMATION', 'fa fa-edit', '', ''], 
      [CHANGE_DATA_TYPE, 'change-data-type', 1, 'TRANSFORMATION', 'fa fa-exchange-alt', '', ''], 
      [RENAME, 'rename', 1, 'TRANSFORMATION', 'fa fa-edit text-secondary', 'separator', ''], 
      [DELETE, 'delete', 1, 'TRANSFORMATION', 'fa fa-times text-danger', 'separator', ''], 
      [FIND_REPLACE, 'find-replace', 1, 'TRANSFORMATION', 'fa fa-search', '', ''], 

      [SORT, 'sort', 1, 'TRANSFORMATION', 'fa fa-sort text-secondary', '', ''], 
      [FILTER, 'filter', 1, 'TRANSFORMATION', 'fa fa-filter text-success', '', ''], 
      [GROUP, 'group', 1, 'TRANSFORMATION', 'fa fa-sort text-secondary', '', ''], 
      [JOIN, 'join', 1, 'TRANSFORMATION', 'fa fa-sort text-secondary', '', ''], 
      [CONCATE_ROWS, 'concat-rows', 1, 'TRANSFORMATION', 'fa fa-sort text-secondary', '', ''], 
      [SAMPLE, 'sample', 1, 'TRANSFORMATION', 'fa fa-sort text-secondary', '', ''], 
      [LIMIT, 'limit', 1, 'TRANSFORMATION', 'fa fa-sort text-secondary', '', ''], 
      [WINDOW_FUNCTION, 'window-function', 1, 'TRANSFORMATION', 'fa fa-sort text-secondary', '', ''], 
      [PYTHON_CODE, 'python-code', 1, 'TRANSFORMATION', 'fa fa-sort text-secondary', '', ''], 
      [ADD_BY_FORMULA, 'add-by-formula', 1, 'TRANSFORMATION', '', '', ''], 

      [INVERT_BOOLEAN, 'invert-boolean', 1, 'TRANSFORMATION', '', 'boolean', ''], 
      [RESCALE, 'rescale', 1, 'TRANSFORMATION', '', 'Number', ''], 
      [ROUND_NUMBER, 'round-number', 1, 'TRANSFORMATION', '', 'Decimal', ''], 
      [DISCRETIZE, 'discretize', 1, 'TRANSFORMATION', '', 'Number', ''], 
      [NORMALIZE, 'normalize', 1, 'TRANSFORMATION', '', '', 'Number'], 
      [FORCE_RANGE, 'force-range', 1, 'TRANSFORMATION', '', 'Number', ''], 
      [TS_TO_DATE, 'ts-to-date', 1, 'TRANSFORMATION', '', 'Integer', ''], 
      [TO_UPPER, 'to-upper', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [TO_LOWER, 'to-lower', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [CAPITALIZE, 'capitalize', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [REMOVE_ACCENTS, 'remove-accents', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [NORMALIZE_TEXT, 'normalize-text', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [CONCAT_ATTRIBUTE, 'concat-attribute', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [TRIM, 'trim', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [TRUNCATE_TEXT, 'truncate-text', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [SPLIT_INTO_WORDS, 'split-into-words', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [SUBSTRING, 'substring', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [PARSE_TO_DATE, 'parse-to-date', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [EXTRACT_NUMBERS, 'extract-numbers', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [EXTRACT_WITH_REGEX, 'extract-with-regex', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [EXTRACT_FROM_ARRAY, 'extract-from-array', 1, 'TRANSFORMATION', '', 'Array', ''], 
      [EXPAND_FROM_ARRAY, 'expand-from-array', 1, 'TRANSFORMATION', '', 'Array', ''], 
      [FOLD_ARRAY, 'fold-array', 1, 'TRANSFORMATION', '', 'Array', ''], 
      [CHANGE_ARRAY_TYPE, 'change-array-type', 1, 'TRANSFORMATION', '', 'Array', ''], 
      [SORT_ARRAY, 'sort-array', 1, 'TRANSFORMATION', '', 'Array', ''], 
      [FORCE_DATE_RANGE, 'force-date-range', 1, 'TRANSFORMATION', '', 'Datetime', ''], 
      [UPDATE_HOUR, 'update-hour', 1, 'TRANSFORMATION', '', 'Datetime', ''], 
      [TRUNCATE_DATE_TO, 'truncate-date-to', 1, 'TRANSFORMATION', '', 'Datetime', ''], 
      [DATE_DIFF, 'date-diff', 1, 'TRANSFORMATION', '', 'Datetime', ''], 
      [DATE_ADD, 'date-add', 1, 'TRANSFORMATION', '', 'Datetime', ''], 
      [DATE_PART, 'date-part', 1, 'TRANSFORMATION', '', 'Datetime', ''], 
      [FORMAT_DATE, 'format-date', 1, 'TRANSFORMATION', '', 'Datetime', ''], 
      [DATE_TO_TS, 'date-to-ts', 1, 'TRANSFORMATION', '', 'Datetime', ''], 
      
      [ESCAPE_XML, 'escape-xml', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [ESCAPE_UNICODE, 'escape-unicode', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [STEMMING, 'stemming', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [N_GRAMS, 'n-grams', 1, 'TRANSFORMATION', '', 'Text', ''], 
      [OBFUSCATE, 'obfuscate', 1, 'TRANSFORMATION', '', '', ''], 
      [ONE_HOT_ENCODE, 'one-hot-encoding', 1, 'TRANSFORMATION', '', '', ''], 

      [FLAG_IN_RANGE, 'flag-in-range', 1, 'TRANSFORMATION', '', '', ''], 
      [FLAG_INVALID, 'flag-invalid', 1, 'TRANSFORMATION', '', '', ''], 
      [FLAG_EMPTY, 'flag-invalid', 1, 'TRANSFORMATION', '', '', ''], 
      [FLAG_WITH_FORMULA, 'flag-with-formula', 1, 'TRANSFORMATION', '', '', ''], 
      
      
      [FILL_MISSING, 'fill-missing', 1, 'TRANSFORMATION', '', '', ''], 
      [HANDLE_INVALID, 'handle-invalid', 1, 'TRANSFORMATION', '', '', ''], 
      [REMOVE_EMPTY, 'remove-empty', 1, 'TRANSFORMATION', '', '', ''], 
      [REMOVE_INVALID, 'remove-invalid', 1, 'TRANSFORMATION', '', '', ''], 
   
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation(conn):
    conn.execute(
        'DELETE from operation WHERE id BETWEEN %s AND %s', 
        BASE_OP, MAX_OP)

def _insert_operation_translation(conn):
    tb = table('operation_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
      [READ_DATA, 'pt', 'Ler dados', 'Ler dados'], 
      [CHANGE_DATA_TYPE, 'pt', 'Alterar o tipo do atributo', 'Altera o tipo do atributo.'], 
      [RENAME, 'pt',  'Renomear atributo', 'Renomeia atributo.'], 
      [DELETE, 'pt',  'Excluir atributo', 'Exclui atributo.'], 
      [FIND_REPLACE, 'pt',  'Localizar e substituir', 'Localiza valores no atributo e permite a substituição.'], 

      [SORT, 'pt', 'Ordenar', 'Permite definir as opções de ordenação.'], 
      [FILTER, 'pt', 'Filtrar', 'Permite definir as opções de filtro.'], 
      [GROUP, 'pt', 'Agrupar', 'Permite definir opções para agrupamento.'], 
      [JOIN, 'pt', 'Juntar com outra fonte de dados', 'Permite juntar com outra fonte de dados (JOIN).'], 
      [CONCATE_ROWS, 'pt', 'Adicionar registros ao fim', 'Permite adicionar registros ao fim dos dados a partir de outra fonte de dados.'], 
      [SAMPLE, 'pt', 'Amostrar', 'Permite definir amostragem dos dados.'], 
      [LIMIT, 'pt', 'Limitar', 'Permite limitar a quantidade de dados.'], 
      [WINDOW_FUNCTION, 'pt', 'Transformar com função de janela', 'Permite usar uma função de janela (deslizante).'], 
      [PYTHON_CODE, 'pt', 'Transformar com Python', 'Permite usar código Python para transformar os dados.'],
      [ADD_BY_FORMULA, 'pt', 'Adicionar atributo via fórmula', 'Permite adicionar um novo atributo usando uma fórmula.'],

      [INVERT_BOOLEAN, 'pt', 'Inverter', 'Permite inverter um valor lógico.'],
      [RESCALE, 'pt', 'Rescalar', 'Permite rescalar um valor numérico.'],
      [ROUND_NUMBER, 'pt', 'Arredondar', 'Permite arredondar um número.'],
      [DISCRETIZE, 'pt', 'Discretizar', 'Permite discretizar um número.'],
      [NORMALIZE, 'pt', 'Normalizar', 'Permite normalizar um número.'],
      [FORCE_RANGE, 'pt', 'Forçar faixa', 'Permite forçar um número a uma faixa.'],
      [TS_TO_DATE, 'pt', 'Timestamp para data', 'Permite converter um valor timestamp para data.'],
      [TO_UPPER, 'pt', 'Converter para maiúsculas', 'Converte um texto para maiúsculas.'],
      [TO_LOWER, 'pt', 'Converter para minúsculas', 'Converte um texto para minúsculas.'],
      [CAPITALIZE, 'pt', 'Capitalizar iniciais', 'Capitaliza inciais das palavras.'],
      [REMOVE_ACCENTS, 'pt', 'Remover acentos', 'Remove acentos das palavras.'],
      [NORMALIZE_TEXT, 'pt', 'Normalizar texto', 'Normaliza o texto, retirando acentos, números e outros símbolos que não sejam letras.'],
      [CONCAT_ATTRIBUTE, 'pt', 'Concatenar', 'Permite concatenar atributos com outros atributos ou valores.'],
      [TRIM, 'pt', 'Remover espaços em branco', 'Permite remover espaços em branco de um texto, no início, no fim ou ambos.'],
      [TRUNCATE_TEXT, 'pt', 'Truncar texto', 'Trunca um texto até um limite especificado de caracteres.'],
      [SPLIT_INTO_WORDS, 'pt', 'Dividir em palavras', 'Divite o texto em palavras, considerando um separador.'],
      [SUBSTRING, 'pt', 'Extrair texto', 'Permite extrair uma parte do texto.'],
      [PARSE_TO_DATE, 'pt', 'Converter para data', 'Permite converter um texto em uma data.'],
      [EXTRACT_NUMBERS, 'pt', 'Extrair números a partir do texto', 'Extrai números de um texto.'],
      [EXTRACT_WITH_REGEX, 'pt', 'Extrair com expressão regular', 'Extrai dados usando expressões regulares.'],
      [EXTRACT_FROM_ARRAY, 'pt', 'Extrair elemento de arranjo', 'Permite extrair um elemento de um arranjo (array) por um índice.'],
      [EXPAND_FROM_ARRAY, 'pt', 'Expandir arranjo', 'Permite converter um arranjo (array) em uma ou mais colunas ou linhas.'],
      [FOLD_ARRAY, 'pt', 'Converter em arranjo', 'Permite converter uma ou mais colunas em um arranjo (array) de valores.'],
      [CHANGE_ARRAY_TYPE, 'pt', 'Alterar o tipo do arranjo', 'Permite alterar o tipo de dados dos elementos de um arranjo (array).'],
      [SORT_ARRAY, 'pt', 'Ordenar arranjo', 'Permite ordenar os elementos de um arranjo (array).'],
      [FORCE_DATE_RANGE, 'pt', 'Forçar data a uma faixa', 'Força que as datas estejam em uma faixa de valores.'],
      [UPDATE_HOUR, 'pt', 'Atualizar hora', 'Atualiza a hora de um atributo com datas.'],
      [TRUNCATE_DATE_TO, 'pt', 'Truncar data', 'Trunca a data para algum valor inicial.'],
      [DATE_DIFF, 'pt', 'Diferença de datas', 'Calcula a diferença entre datas.'],
      [DATE_ADD, 'pt', 'Adicionar datas', 'Soma uma data com um valor numérico'],
      [DATE_PART, 'pt', 'Extrair parte de data', 'Extrai uma parte da data.'],
      [FORMAT_DATE, 'pt', 'Formatar data', 'Formata uma data segundo um parâmetro.'],
      [DATE_TO_TS, 'pt', 'Converter para timestamp', 'Converte uma data para um valor timestamp.'],
      
      [ESCAPE_XML, 'pt', 'Escapar caracteres (XML)', 'Escapa caracteres especiais para o formato XML.'],
      [ESCAPE_UNICODE, 'pt', 'Escapar Unicode', 'Escapa caracteres Unicode.'],
      [STEMMING, 'pt', 'Gerar radicais (stemming)', 'Gera radicais das palavras por stemming.'],
      [N_GRAMS, 'pt', 'Gerar N-Gramas', 'Gera combinações N-Gramas'],
      [OBFUSCATE, 'pt', 'Ofuscar', 'Ofusca valores de forma a torná-los mais difíceis de serem usados de forma maliciosa.'],
      [ONE_HOT_ENCODE, 'pt', 'Codificar usando One Hot Encoder', 'Codifica usando One Hot Encoder.'],

      [FLAG_IN_RANGE, 'pt', 'Sinalizar registros em faixa', 'Sinaliza registros em faixa.'],
      [FLAG_INVALID, 'pt', 'Sinalizar registros com dados inválidos', 'Sinaliza registros com dados inválidos.'],
      [FLAG_EMPTY, 'pt', 'Sinalizar registros com atributos vazios', 'Sinaliza registros que tenham valores vazios em atributos determinados.'],
      [FLAG_WITH_FORMULA, 'pt', 'Sinalizar registros usando fórmula', 'Sinaliza registros usando fórmula.'],
      
      
      [FILL_MISSING, 'pt', 'Preencher dados ausentes', 'Preenche dados ausentes de acordo com um regra.'],
      [HANDLE_INVALID, 'pt', 'Tratar dados inválidos', 'Trata dados inválidos de acordo com um regra.'],
      [REMOVE_EMPTY, 'pt', 'Remover registros com dados ausentes', 'Remove registros com dados ausentes.'],
      [REMOVE_INVALID, 'pt', 'Remover registros com dados inválidos', 'Remover registros com dados inválidos.'],

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_translation(conn):
    conn.execute(
        'DELETE from operation_translation WHERE id BETWEEN %s AND %s', 
        BASE_OP, MAX_OP)

def _insert_operation_category(conn):
    tb = table('operation_category',
                column('id', Integer), 
                column('type', String), 
                column('order', Integer), 
                column('default_order', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [CAT_INTERN, 'internal', 1, 1], 
      [CAT_EDIT, 'menu/selected/fa fa-edit', 1, 1], 
      [CAT_DATA, 'menu/always/fa fa-database', 2, 2], 
      [CAT_TRANSFORM, 'menu/selected/fa fa-magic', 3, 3], 
      [CAT_ENCODE, 'menu/selected/fa fa-code', 4, 4], 
      [CAT_FLAG, 'menu/selected/fa fa-flag', 5, 5], 
      [CAT_FIX, 'menu/selected/fa fa-eraser', 6, 6], 
      [CAT_CONTEXT, 'context', 7, 7], 
      [CAT_TEXT, 'data-type', 100, 100], 
      [CAT_INTEGER, 'data-type', 100, 100], 
      [CAT_BOOL, 'data-type', 100, 100], 
      [CAT_DATE, 'data-type', 100, 100], 
      [CAT_ARRAY, 'data-type', 100, 100]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category(conn):
    conn.execute(
        'DELETE from operation_category WHERE id BETWEEN %s AND %s', 
        BASE_CATEGORY, BASE_CATEGORY + 12)

def _insert_operation_category_translation(conn):
    tb = table('operation_category_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [CAT_INTERN, 'pt', 'Interna'], 
      [CAT_EDIT, 'pt', 'Editar'], 
      [CAT_DATA, 'pt', 'Dados'], 
      [CAT_TRANSFORM, 'pt', 'Transformar'], 
      [CAT_ENCODE, 'pt', '(De)codificar'], 
      [CAT_FLAG, 'pt', 'Sinalizar'], 
      [CAT_FIX, 'pt', 'Corrigir'], 
      [CAT_CONTEXT, 'pt', 'Contexto'], 
      [CAT_TEXT, 'pt', 'Texto'], 
      [CAT_INTEGER, 'pt', 'Inteiro'], 
      [CAT_BOOL, 'pt', 'Booleano'], 
      [CAT_DATE, 'pt', 'Data'], 
      [CAT_ARRAY, 'pt', 'Arrajo']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_translation(conn):
    conn.execute(
        'DELETE from operation_category_translation WHERE id BETWEEN %s AND %s', 
        BASE_CATEGORY, BASE_CATEGORY + 12)

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
                column('operation_id', Integer), 
                column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [READ_DATA, BASE_CATEGORY + 0],

      [CHANGE_DATA_TYPE, CAT_EDIT],
      [RENAME, CAT_EDIT],
      [DELETE, CAT_EDIT],
      [FIND_REPLACE, CAT_EDIT],

      [SORT, CAT_DATA],
      [FILTER, CAT_DATA],
      [GROUP, CAT_DATA],
      [JOIN, CAT_DATA],
      [CONCATE_ROWS, CAT_DATA],
      [SAMPLE, CAT_DATA],
      [LIMIT, CAT_DATA],
      [WINDOW_FUNCTION, CAT_DATA],
      [PYTHON_CODE, CAT_DATA],
      [ADD_BY_FORMULA, CAT_DATA],

      [INVERT_BOOLEAN, CAT_TRANSFORM],
      [RESCALE, CAT_TRANSFORM],
      [ROUND_NUMBER, CAT_TRANSFORM],
      [DISCRETIZE, CAT_TRANSFORM],
      [NORMALIZE, CAT_TRANSFORM],
      [FORCE_RANGE, CAT_TRANSFORM],
      [TS_TO_DATE, CAT_TRANSFORM],
      [TO_UPPER, CAT_TRANSFORM],
      [TO_LOWER, CAT_TRANSFORM],
      [CAPITALIZE, CAT_TRANSFORM],
      [REMOVE_ACCENTS, CAT_TRANSFORM],
      [NORMALIZE_TEXT, CAT_TRANSFORM],
      [CONCAT_ATTRIBUTE, CAT_TRANSFORM],
      [TRIM, CAT_TRANSFORM],
      [TRUNCATE_TEXT, CAT_TRANSFORM],
      [SPLIT_INTO_WORDS, CAT_TRANSFORM],
      [SUBSTRING, CAT_TRANSFORM],
      [PARSE_TO_DATE, CAT_TRANSFORM],
      [EXTRACT_NUMBERS, CAT_TRANSFORM],
      [EXTRACT_WITH_REGEX, CAT_TRANSFORM],
      [EXTRACT_FROM_ARRAY, CAT_TRANSFORM],
      [EXPAND_FROM_ARRAY, CAT_TRANSFORM],
      [FOLD_ARRAY, CAT_TRANSFORM],
      [CHANGE_ARRAY_TYPE, CAT_TRANSFORM],
      [SORT_ARRAY, CAT_TRANSFORM],
      [FORCE_DATE_RANGE, CAT_TRANSFORM],
      [UPDATE_HOUR, CAT_TRANSFORM],
      [TRUNCATE_DATE_TO, CAT_TRANSFORM],
      [DATE_DIFF, CAT_TRANSFORM],
      [DATE_ADD, CAT_TRANSFORM],
      [DATE_PART, CAT_TRANSFORM],
      [FORMAT_DATE, CAT_TRANSFORM],
      [DATE_TO_TS, CAT_TRANSFORM],
      
      [ESCAPE_XML, CAT_ENCODE],
      [ESCAPE_UNICODE, CAT_ENCODE],
      [STEMMING, CAT_ENCODE],
      [N_GRAMS, CAT_ENCODE],
      [OBFUSCATE, CAT_ENCODE],
      [ONE_HOT_ENCODE, CAT_ENCODE],

      [FLAG_IN_RANGE, CAT_FLAG],
      [FLAG_INVALID, CAT_FLAG],
      [FLAG_EMPTY, CAT_FLAG],
      [FLAG_WITH_FORMULA, CAT_FLAG],
      
      
      [FILL_MISSING, CAT_FIX],
      [HANDLE_INVALID, CAT_FIX],
      [REMOVE_EMPTY, CAT_FIX],
      [REMOVE_INVALID, CAT_FIX],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_operation(conn):
    conn.execute(
        '''DELETE FROM operation_category_operation
            WHERE operation_category_id BETWEEN %s and %s''',
        BASE_CATEGORY, BASE_CATEGORY + 12)

def _insert_operation_platform(conn):
    tb = table('operation_platform',
                column('operation_id', Integer), 
                column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [op_id, META_PLATFORM] for op_id in list(range(BASE_OP, MAX_OP + 1))
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_platform(conn):
    conn.execute(
        '''DELETE FROM operation_platform
            WHERE operation_id BETWEEN %s and %s''',
        BASE_OP, MAX_OP)

def _insert_operation_form(conn):
    tb = table('operation_form',
                column('id', Integer), 
                column('enabled', Boolean), 
                column('order', Integer), 
                column('category', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM + 0, 1, 1, 'execution'], # Comment
      [BASE_FORM + 1, 1, 1, 'execution'], # ReadData
      [ATTRIBUTES_FORM, 1, 1, 'execution'], # Attributes (common)
      [ALIASES_FORM, 1, 1, 'execution'], # Aliases (common)
      [KEEP_ATTRIBUTE_FORM, 1, 1, 'execution'], # Keep attribute (common)
    ]
    for op_id in ALL_OPS: # Operations' form
        data.append([op_id + 50, 1, 1, 'execution'])

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form(conn):
    conn.execute(
        'DELETE from operation_form WHERE id BETWEEN %s AND %s', 
        BASE_FORM, ALL_OPS[-1] + 50)

def _insert_operation_form_translation(conn):
    tb = table('operation_form_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM, 'pt', 'Execução'], # Common form to all ops
      [BASE_FORM + 1, 'pt', 'Execução'],
      [ATTRIBUTES_FORM, 'pt', 'Execução'],
      [ALIASES_FORM, 'pt', 'Execução'],
      [KEEP_ATTRIBUTE_FORM, 'pt', 'Execução'],

      [BASE_FORM, 'en', 'Execution'], 
      [BASE_FORM + 1, 'en', 'Execution'],
      [ATTRIBUTES_FORM, 'en', 'Execution'],
      [ALIASES_FORM, 'en', 'Execution'],
      [KEEP_ATTRIBUTE_FORM, 'en', 'Execution'],
    ]
    for op_id in ALL_OPS: # Operations' form
        data.append([op_id + 50, 'pt', 'Execução'])
        data.append([op_id + 50, 'en', 'Execution'])

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_translation(conn):
    conn.execute(
        'DELETE from operation_form_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM, ALL_OPS[-1] + 50)

def _insert_operation_form_field(conn):
    tb = table('operation_form_field',
                column('id', Integer), 
                column('name', String), 
                column('type', String), 
                column('required', Boolean), 
                column('order', Integer), 
                column('default', String), 
                column('suggested_widget', String), 
                column('values_url', String), 
                column('values', String), 
                column('scope', String), 
                column('enable_conditions', String), 
                column('editable', Boolean), 
                column('form_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM_FIELD + 0, 'comment', 'TEXT', 1, 1, None, 'textarea', None, None, 'DESIGN', None, 1, BASE_FORM + 0], 
      [BASE_FORM_FIELD + 1, 'data_source', 'TEXT', 1, 1, None, 'lookup', 
        '`${LIMONERO_URL}/datasources?&simple=true&list=true&enabled=1`', None, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 2, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'DESIGN', None, 1, ATTRIBUTES_FORM], 
      [BASE_FORM_FIELD + 3, 'overwrite', 'INTEGER', 0, 2, '1', 'checkbox', None, None, 'DESIGN', None, 1, KEEP_ATTRIBUTE_FORM], 
      [BASE_FORM_FIELD + 4, 'aliases', 'TEXT', 0, 3, None, 'text', None, None, 'DESIGN', 'this.overwrite.internalValue !== "1" ', 1, ALIASES_FORM], 
      
      [BASE_FORM_FIELD + 50, 'new_type', 'TEXT', 1, 3, None, 'dropdown', None, None, 'DESIGN', None, 1, CHANGE_DATA_TYPE + 50], 
      
      [BASE_FORM_FIELD + 51, 'find', 'TEXT', 1, 3, None, 'text', None, None, 'DESIGN', None, 1, FIND_REPLACE + 50], 
      [BASE_FORM_FIELD + 52, 'replace', 'TEXT', 0, 4, None, 'text', None, None, 'DESIGN', None, 1, FIND_REPLACE + 50], 

      [BASE_FORM_FIELD + 53, 'other', 'TEXT', 1, 3, None, 'attribute-selector', None, None, 'DESIGN', None, 1, CONCAT_ATTRIBUTE + 50], 
      [BASE_FORM_FIELD + 54, 'separator', 'TEXT', 1, 4, None, 'attribute-selector', None, None, 'DESIGN', None, 1, CONCAT_ATTRIBUTE + 50], 

      [BASE_FORM_FIELD + 55, 'characters', 'INTEGER', 1, 3, None, 'integer', None, None, 'DESIGN', None, 1, TRUNCATE_TEXT + 50], 
      
      [BASE_FORM_FIELD + 56, 'delimiter', 'INTEGER', 0, 3, None, 'integer', None, None, 'DESIGN', None, 1, SPLIT_INTO_WORDS + 50], 
      
      [BASE_FORM_FIELD + 57, 'format', 'TEXT', 1, 3, None, 'select2', None, None, 'DESIGN', None, 1, PARSE_TO_DATE + 50], 

      [BASE_FORM_FIELD + 58, 'regex', 'TEXT', 1, 3, None, 'text', None, None, 'DESIGN', None, 1, EXTRACT_WITH_REGEX + 50], 

      [BASE_FORM_FIELD + 59, 'start', 'FLOAT', 0, 3, None, 'decimal', None, None, 'DESIGN', None, 1, RESCALE + 50], 
      [BASE_FORM_FIELD + 60, 'end', 'FLOAT', 0, 4, None, 'decimal', None, None, 'DESIGN', None, 1, RESCALE + 50], 

      [BASE_FORM_FIELD + 61, 'bins', 'INTEGER', 1, 3, None, 'INTEGER', None, None, 'DESIGN', None, 1, DISCRETIZE + 50], 

      [BASE_FORM_FIELD + 62, 'normalizer', 'TEXT', 1, 3, None, 'dropdown', None, None, 'DESIGN', None, 1, NORMALIZE + 50], 

      [BASE_FORM_FIELD + 63, 'start', 'FLOAT', 0, 3, None, 'decimal', None, None, 'DESIGN', None, 1, FORCE_RANGE + 50], 
      [BASE_FORM_FIELD + 64, 'end', 'FLOAT', 0, 4, None, 'decimal', None, None, 'DESIGN', None, 1, FORCE_RANGE + 50], 

      [BASE_FORM_FIELD + 65, 'decimals', 'INTEGER', 1, 3, '2', 'integer', None, None, 'DESIGN', None, 1, ROUND_NUMBER + 50], 

      [BASE_FORM_FIELD + 66, 'limit', 'INTEGER', 1, 3, '10', 'decimal', None, None, 'DESIGN', None, 1, EXPAND_FROM_ARRAY + 50],   

      [BASE_FORM_FIELD + 67, 'new_type', 'TEXT', 1, 3, None, 'dropdown', None, None, 'DESIGN', None, 1, CHANGE_ARRAY_TYPE + 50], 

      [BASE_FORM_FIELD + 68, 'direction', 'TEXT', 1, 3, 'asc', 'dropdown', None, 
        json.dumps([{'key': 'asc', 'pt': 'Ascendente', 'en': 'Ascending'}, {'key': 'desc', 'pt': 'Descendente', 'en': 'Descending'}]), 
        'DESIGN', None, 1, FORCE_RANGE + 50], 
      [BASE_FORM_FIELD + 69, 'formato', 'TEXT', 1, 3, None, 'select2', None, None, 'DESIGN', None, 1, FORMAT_DATE + 50], 

      [BASE_FORM_FIELD + 70, 'start', 'FLOAT', 0, 3, None, 'date', None, None, 'DESIGN', None, 1, FORCE_DATE_RANGE + 50], 
      [BASE_FORM_FIELD + 71, 'end', 'FLOAT', 0, 4, None, 'date', None, None, 'DESIGN', None, 1, FORCE_DATE_RANGE + 50], 

      [BASE_FORM_FIELD + 72, 'hour_column', 'TEXT', 1, 3, None, 'attribute-selector', None, None, 'DESIGN', None, 1, UPDATE_HOUR + 50], 

      [BASE_FORM_FIELD + 73, 'components', 'TEXT', 1, 3, None, 'tag', None, None, 'DESIGN', None, 1, DATE_PART + 50], 

      [BASE_FORM_FIELD + 74, 'value', 'INTEGER', 1, 3, None, 'integer', None, None, 'DESIGN', None, 1, DATE_ADD + 50], 
      [BASE_FORM_FIELD + 75, 'period', 'TEXT', 1, 4, None, 'dropdown', None, 
        json.dumps([{'key': 'day', 'pt': 'Dia(s)', 'en': 'Day(s)'}, {'key': 'hour', 'pt': 'Hora(s)', 'en': 'Hour(s)'}]), 
        'DESIGN', None, 1, DATE_ADD + 50], 

      [BASE_FORM_FIELD + 76, 'type', 'INTEGER', 1, 3, None, 'dropdown', None, 
        json.dumps([{'key': 'column', 'pt': 'De uma coluna', 'en': 'From column'}, {'key': 'constant', 'pt': 'Valor constante', 'en': 'Constant value'}]), 
        'DESIGN', None, 1, DATE_DIFF + 50],  
      [BASE_FORM_FIELD + 77, 'column', 'INTEGER', 1, 4, None, 'attribute-selector', None, None, 'DESIGN', None, 1, DATE_DIFF + 50], 
      [BASE_FORM_FIELD + 78, 'value', 'TEXT', 1, 5, None, 'text', None, None, 'DESIGN', None, 1, DATE_DIFF + 50], 

      [BASE_FORM_FIELD + 79, 'start', 'FLOAT', 0, 3, None, 'decimal', None, None, 'DESIGN', None, 1, FLAG_IN_RANGE + 50], 
      [BASE_FORM_FIELD + 80, 'end', 'FLOAT', 0, 4, None, 'decimal', None, None, 'DESIGN', None, 1, FLAG_IN_RANGE + 50], 

      [BASE_FORM_FIELD + 81, 'formula', 'TEXT', 0, 3, None, 'expression', None, None, 'DESIGN', None, 1, FLAG_WITH_FORMULA + 50], 

     [BASE_FORM_FIELD + 82, 'type', 'INTEGER', 1, 3, None, 'dropdown', None, 
        json.dumps([{'key': 'average', 'pt': 'Com a média', 'en': 'With average'}, {'key': 'constant', 'pt': 'Valor constante', 'en': 'Constant value'}]), 
        'DESIGN', None, 1, FILL_MISSING + 50], 
     [BASE_FORM_FIELD + 83, 'value', 'TEXT', 1, 4, None, 'text', None, None, 'DESIGN', None, 1, FILL_MISSING + 50], 

     [BASE_FORM_FIELD + 84, 'type', 'INTEGER', 1, 3, None, 'dropdown', None, 
        json.dumps([{'key': 'null', 'pt': 'Limpar valor', 'en': 'Clean value'}, 
            {'key': 'average', 'pt': 'Com a média', 'en': 'With average'}, 
            {'key': 'constant', 'pt': 'Valor constante', 'en': 'Constant value'}]), 
        'DESIGN', None, 1, HANDLE_INVALID + 50], 
     [BASE_FORM_FIELD + 85, 'value', 'TEXT', 1, 4, None, 'text', None, None, 'DESIGN', None, 1, HANDLE_INVALID + 50], 

    [BASE_FORM_FIELD + 86, 'formula', 'TEXT', 1, 3, None, 'expression', None, None, 'DESIGN', None, 1, ADD_BY_FORMULA + 50], 

    [BASE_FORM_FIELD + 87, 'formula', 'TEXT', 1, 3, None, 'expression', None, None, 'DESIGN', None, 1, FILTER + 50], 

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD, BASE_FORM_FIELD + 87)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM_FIELD + 0, 'pt', 'Comentário', 'Comentário sobre a tarefa.'], 
      [BASE_FORM_FIELD + 1, 'pt', 'Fonte de dados', 'Fonte de dados a ser utilizada como entrada para os dados.'], 
      [BASE_FORM_FIELD + 2, 'pt', 'Atributos', 'Lista de atributos a ser usado na ação.'], 
      [BASE_FORM_FIELD + 3, 'pt', 'Sobrescrever atributo(s) original(ais)', 'Indica se o(s) atributo(s) original(ais) deve(m) ser sobrescrito(s) após a transformação ou se novos atributos serão criados.'], 
      [BASE_FORM_FIELD + 4, 'pt', 'Novos nomes', 'Novos nomes para os atributos resultantes.'], 

      [BASE_FORM_FIELD + 50, 'pt', 'Novo tipo', 'Novo tipo para o atributo.'], 
      [BASE_FORM_FIELD + 51, 'pt', 'Encontrar', 'Valor a ser pesquisado.'], 
      [BASE_FORM_FIELD + 52, 'pt', 'Substituir', 'Valor a ser usado na substituição.'], 
      [BASE_FORM_FIELD + 53, 'pt', 'Atributo(s) a ser(em) concatenado(s)', 'Atributo(s) a ser(em) concatenado(s).'], 
      [BASE_FORM_FIELD + 54, 'pt', 'Separador', 'Separador para os atributos a serem concatenados.'], 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute(
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD, BASE_FORM_FIELD + 87)


def _insert_operation_operation_form(conn):
    tb = table('operation_operation_form',
                column('operation_id', Integer), 
                column('operation_form_id', Integer))
    columns = [c.name for c in tb.columns]
    data = []
    # for i in list(range(2, 13)):
    #    for j in list(range(2, 4)):
    #        data.append([BASE_OP + i, BASE_FORM + j])

    ops_without_attribute_field = {
        ADD_BY_FORMULA, JOIN, SAMPLE, LIMIT, WINDOW_FUNCTION,
    }
    ops_without_aliases_field = {
        CHANGE_DATA_TYPE, DELETE, REMOVE_EMPTY, SORT, FILTER, GROUP, JOIN, 
        SAMPLE, LIMIT, WINDOW_FUNCTION
    }
    ops_without_keep_attribute_field = {
        CHANGE_DATA_TYPE, RENAME, DELETE, ADD_BY_FORMULA, SORT, FILTER, GROUP,
        JOIN, SAMPLE, LIMIT, WINDOW_FUNCTION,
    }
    # Common forms
    for op_id in ALL_OPS:
        #if op_id == SORT: 
        #    import pdb; pdb.set_trace()
        if op_id not in ops_without_attribute_field:
            data.append([op_id,  ATTRIBUTES_FORM])
        if op_id not in ops_without_aliases_field:
            data.append([op_id,  ALIASES_FORM])
        if op_id not in ops_without_keep_attribute_field:
            data.append([op_id,  KEEP_ATTRIBUTE_FORM])

    # import pdb; pdb.set_trace()
    # Each op form
    for op_id in ALL_OPS: 
        data.append([op_id,  op_id + 50])

    rows = [dict(list(zip(columns, row))) for row in data]

    rows.append({'operation_id': BASE_OP, 'operation_form_id': BASE_FORM_FIELD + 1})
    op.bulk_insert(tb, rows)

def _delete_operation_operation_form(conn):
    conn.execute(
        '''DELETE FROM operation_operation_form
            WHERE operation_id BETWEEN %s and %s''',
        BASE_OP, ALL_OPS[-1] + 50)


# -----------------------
def _execute(conn, cmd):
    if isinstance(cmd, str):
        conn.execute(cmd)
    elif isinstance(cmd, list):
        for row in cmd:
            conn.execute(row)
    else: # it's a method
        cmd(conn)

# -------------------------------------------------------

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()
    commands = [
        _insert_platform,
        _insert_platform_translation,
        _insert_operation,
        _insert_operation_translation,
        _insert_operation_category,
        _insert_operation_category_translation,
        _insert_operation_category_operation,
        _insert_operation_platform,
        _insert_operation_form,
        _insert_operation_form_translation,
        _insert_operation_form_field,
        _insert_operation_form_field_translation,
        _insert_operation_operation_form,
    ]
    try:
        for cmd in commands:
            _execute(conn, cmd)
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()

    # Remove it if your DB doesn't support disabling FK checks
    conn.execute('SET FOREIGN_KEY_CHECKS=0;')
    commands = [
        _delete_platform,
        _delete_platform_translation,
        _delete_operation,
        _delete_operation_translation,
        _delete_operation_category,
        _delete_operation_category_translation,
        _delete_operation_category_operation,
        _delete_operation_platform,
        _delete_operation_form,
        _delete_operation_form_translation,
        _delete_operation_form_field,
        _delete_operation_form_field_translation,
        _delete_operation_operation_form,
    ]

    try:
        for cmd in reversed(commands):
            _execute(conn, cmd)
    except:
        session.rollback()
        raise
    # Remove it if your DB doesn't support disabling FK checks
    conn.execute('SET FOREIGN_KEY_CHECKS=1;')
    session.commit()
