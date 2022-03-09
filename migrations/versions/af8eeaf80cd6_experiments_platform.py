"""Experiments platform

Revision ID: af8eeaf80cd6
Revises: a8642d0d1aa3
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
down_revision = 'a8642d0d1aa3'
branch_labels = None
depends_on = None

# --------------------------------------------------------------
# ATENTION: You must revise this auto-generated code.
# Please, review offsets and commands before running a migration
# and optionally, perform a database backup. If everything is
# OK, remove this comment.
# --------------------------------------------------------------
META_PLATFORM = 1000

APPEARANCE_FORM_ID=41

BASE_OP = 2100
BASE_CATEGORY = 2100
BASE_FORM = 2100
BASE_FORM_FIELD = 2100

READ_DATA = BASE_OP + 0

# Edit
CAST = BASE_OP + 1
RENAME = BASE_OP + 2
DISCARD = BASE_OP + 3
FIND_REPLACE = BASE_OP + 4
DUPLICATE = BASE_OP + 62

# Data
SELECT = BASE_OP + 63
SORT = BASE_OP + 5
FILTER = BASE_OP + 6
GROUP = BASE_OP + 7
JOIN = BASE_OP + 8
CONCAT_ROWS = BASE_OP + 9
SAMPLE = BASE_OP + 10
LIMIT = BASE_OP + 11
WINDOW_FUNCTION = BASE_OP + 12
PYTHON_CODE = BASE_OP + 13
ADD_BY_FORMULA = BASE_OP + 14
SAVE = BASE_OP + 64

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
# EXPAND_FROM_ARRAY = BASE_OP + 36
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
CLEAN_MISSING = BASE_OP + 58
REMOVE_MISSING = BASE_OP + 59
HANDLE_INVALID = BASE_OP + 60
REMOVE_INVALID = BASE_OP + 61



# Model builder
# Uses READ_DATA, SAMPLE
SPLIT = BASE_OP + 250
EVALUATOR = BASE_OP + 251
FEATURES_REDUCTION = BASE_OP + 252
GRID = BASE_OP + 253
FEATURES  = BASE_OP + 254

K_MEANS_CLUSTERING = BASE_OP + 255
GAUSSIAN_MIXTURE_CLUSTERING = BASE_OP + 256
DECISION_TREE_CLASSIFIER = BASE_OP + 257
GBT_CLASSIFIER = BASE_OP + 258
NAIVE_BAYES_CLASSIFIER = BASE_OP + 259
PERCEPTRON_CLASSIFIER = BASE_OP + 260
RANDOM_FOREST_CLASSIFIER = BASE_OP + 261
LOGISTIC_REGRESSION = BASE_OP + 262
SVM_CLASSIFICATION = BASE_OP + 263

LINEAR_REGRESSION = BASE_OP + 264
ISOTONIC_REGRESSION = BASE_OP + 265
GBT_REGRESSOR = BASE_OP + 266
RANDOM_FOREST_REGRESSOR = BASE_OP + 267
GENERALIZED_LINEAR_REGRESSOR = BASE_OP + 268
DECISION_TREE_REGRESSOR = BASE_OP + 269
# AFT_SURVIVAL_REGRESSION = BASE_OP + 269 # Not supported

VISUALIZATION = BASE_OP + 270

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
CAT_MODEL_BUILDER = BASE_CATEGORY + 13
CAT_VISUALIZATION_BUILDER = BASE_CATEGORY + 14

CAT_CLASSIFICATION = 4
CAT_REGRESSION = 45
CAT_CLUSTERING = 46

FIELD_CAST_ERROR_ATTRIBUTE = 449
FIELD_SELECT_MODE = 3
FIELD_SELECT_ALIAS = 5

ORIGINAL_CAST_FORM = 154
ORIGINAL_SELECT_FORM = 6
ORIGINAL_SAVE_FORM = 28
ORIGINAL_JOIN_FORM = 16

ALL_OPS = [
    READ_DATA,
    # Edit
    CAST, RENAME, DISCARD, FIND_REPLACE, DUPLICATE,
    # Data
    SELECT, SORT, FILTER, GROUP, JOIN, CONCAT_ROWS, SAMPLE,
    LIMIT, WINDOW_FUNCTION, PYTHON_CODE, ADD_BY_FORMULA, SAVE,
    # Transform
    INVERT_BOOLEAN, RESCALE, ROUND_NUMBER, DISCRETIZE, NORMALIZE,
    FORCE_RANGE, TS_TO_DATE, TO_UPPER, TO_LOWER, CAPITALIZE,
    REMOVE_ACCENTS, NORMALIZE_TEXT, CONCAT_ATTRIBUTE, TRIM,
    TRUNCATE_TEXT, SPLIT_INTO_WORDS, SUBSTRING, PARSE_TO_DATE,
    EXTRACT_NUMBERS, EXTRACT_WITH_REGEX, EXTRACT_FROM_ARRAY,
    #EXPAND_FROM_ARRAY, 
    FOLD_ARRAY, CHANGE_ARRAY_TYPE, SORT_ARRAY,
    FORCE_DATE_RANGE, UPDATE_HOUR, TRUNCATE_DATE_TO, DATE_DIFF,
    DATE_ADD, DATE_PART, FORMAT_DATE, DATE_TO_TS,
    # Encode / decode
    ESCAPE_XML, ESCAPE_UNICODE, STEMMING, N_GRAMS,
    OBFUSCATE, ONE_HOT_ENCODE,
    # Flag
    FLAG_IN_RANGE, FLAG_INVALID, FLAG_EMPTY, FLAG_WITH_FORMULA,
    # Fix data
    CLEAN_MISSING, HANDLE_INVALID, REMOVE_MISSING, REMOVE_INVALID,

    # Model builder
    SPLIT, EVALUATOR, FEATURES_REDUCTION, GRID, FEATURES,
    K_MEANS_CLUSTERING, GAUSSIAN_MIXTURE_CLUSTERING,
    DECISION_TREE_CLASSIFIER, GBT_CLASSIFIER, NAIVE_BAYES_CLASSIFIER,
    PERCEPTRON_CLASSIFIER, RANDOM_FOREST_CLASSIFIER, LOGISTIC_REGRESSION,
    SVM_CLASSIFICATION,
    LINEAR_REGRESSION, ISOTONIC_REGRESSION, #AFT_SURVIVAL_REGRESSION,
    GBT_REGRESSOR, RANDOM_FOREST_REGRESSOR, GENERALIZED_LINEAR_REGRESSOR,
    DECISION_TREE_REGRESSOR,

    # Visualization builder
    VISUALIZATION,
 ]

ATTRIBUTES_FORM = BASE_FORM + 2
ALIASES_FORM = BASE_FORM + 3
KEEP_ATTRIBUTE_FORM = BASE_FORM + 4
ATTRIBUTE_FORM = BASE_FORM + 5
ALIAS_FORM = BASE_FORM + 6

MAX_OP = max(ALL_OPS)

date_formats = [
    {'key': ''}
]

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
      [CAST, 'cast', 1, 'TRANSFORMATION', 'fa fa-exchange-alt', '', ''],
      [RENAME, 'rename', 1, 'TRANSFORMATION', 'fa fa-edit text-secondary', 'separator', ''],
      [DISCARD, 'discard', 1, 'TRANSFORMATION', 'fa fa-times text-danger', 'separator', ''],
      [DUPLICATE, 'duplicate', 1, 'TRANSFORMATION', 'fa fa-copy', 'separator', ''],
      [FIND_REPLACE, 'find-replace', 1, 'TRANSFORMATION', 'fa fa-search', '', ''],

      [SELECT, 'select', 1, 'TRANSFORMATION', 'fa fa-list text-secondary', 'separator', ''],
      [SORT, 'sort', 1, 'TRANSFORMATION', 'fa fa-sort text-secondary', '', ''],
      [FILTER, 'filter', 1, 'TRANSFORMATION', 'fa fa-filter text-success', '', ''],
      [GROUP, 'group', 1, 'TRANSFORMATION', '', '', ''],
      [JOIN, 'join', 1, 'TRANSFORMATION', '', '', ''],
      [CONCAT_ROWS, 'concat-rows', 1, 'TRANSFORMATION', 'fa fa-plus text-secondary', 'separator', ''],
      [SAMPLE, 'sample', 1, 'TRANSFORMATION', '', '', ''],
      [LIMIT, 'limit', 1, 'TRANSFORMATION', '', 'separator', ''],
      [WINDOW_FUNCTION, 'window-function', 1, 'TRANSFORMATION', '', '', ''],
      [PYTHON_CODE, 'python-code', 1, 'TRANSFORMATION', '', '', ''],
      [ADD_BY_FORMULA, 'add-by-formula', 1, 'TRANSFORMATION', 'fa fa-equals', '', ''],
      [SAVE, 'save', 1, 'TRANSFORMATION', 'fa fa-save', '', ''],

      [INVERT_BOOLEAN, 'invert-boolean', 1, 'TRANSFORMATION', '', 'boolean', ''],
      [RESCALE, 'rescale', 1, 'TRANSFORMATION', '', 'Number', ''],
      [ROUND_NUMBER, 'round-number', 1, 'TRANSFORMATION', '', 'Decimal', ''],
      [DISCRETIZE, 'discretize', 1, 'TRANSFORMATION', '', 'Number', ''],
      [NORMALIZE, 'normalize', 1, 'TRANSFORMATION', '', '', 'Number'],
      [FORCE_RANGE, 'force-range', 1, 'TRANSFORMATION', '', 'Number', ''],

      [TS_TO_DATE, 'ts-to-date', 1, 'TRANSFORMATION', '', 'Integer', ''],
      
      [TO_UPPER, 'to-upper', 1, 'TRANSFORMATION', '', 'Text', ''],
      [TO_LOWER, 'to-lower', 1, 'TRANSFORMATION', '', 'Text', ''],
      [CAPITALIZE, 'capitalize', 1, 'TRANSFORMATION', '', 'Text separator', ''],
      [REMOVE_ACCENTS, 'remove-accents', 1, 'TRANSFORMATION', '', 'Text', ''],
      [NORMALIZE_TEXT, 'normalize-text', 1, 'TRANSFORMATION', '', 'Text separator', ''],
      [CONCAT_ATTRIBUTE, 'concat-attribute', 1, 'TRANSFORMATION', '', 'Text', ''],
      [TRIM, 'trim', 1, 'TRANSFORMATION', '', 'Text', ''],
      [TRUNCATE_TEXT, 'truncate-text', 1, 'TRANSFORMATION', '', 'Text', ''],
      [SPLIT_INTO_WORDS, 'split-into-words', 1, 'TRANSFORMATION', '', 'Text', ''],
      [SUBSTRING, 'substring', 1, 'TRANSFORMATION', '', 'Text', ''],
      [PARSE_TO_DATE, 'parse-to-date', 1, 'TRANSFORMATION', '', 'Text separator', ''],
      [EXTRACT_NUMBERS, 'extract-numbers', 1, 'TRANSFORMATION', '', 'Text', ''],
      [EXTRACT_WITH_REGEX, 'extract-with-regex', 1, 'TRANSFORMATION', '', 'Text', ''],

      [EXTRACT_FROM_ARRAY, 'extract-from-array', 1, 'TRANSFORMATION', '', 'Array', ''],
      # [EXPAND_FROM_ARRAY, 'expand-from-array', 1, 'TRANSFORMATION', '', 'Array', ''],
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


      [CLEAN_MISSING, 'clean-missing', 1, 'TRANSFORMATION', '', '', ''],
      [REMOVE_MISSING, 'remove-empty', 1, 'TRANSFORMATION', '', 'separator', ''],
      [HANDLE_INVALID, 'handle-invalid', 1, 'TRANSFORMATION', '', '', ''],
      [REMOVE_INVALID, 'remove-invalid', 1, 'TRANSFORMATION', '', '', ''],

      [SPLIT, 'split', 1, 'TRANSFORMATION', '', '', ''],
      [EVALUATOR, 'evaluator', 1, 'TRANSFORMATION', '', '', ''],
      [FEATURES_REDUCTION, 'features-reduction', 1, 'TRANSFORMATION', '', '', ''],
      [GRID, 'grid', 1, 'TRANSFORMATION', '', '', ''],
      [FEATURES, 'features', 1, 'TRANSFORMATION', '', '', ''],

      [K_MEANS_CLUSTERING, 'k-means', 1, 'TRANSFORMATION', '', '', ''],
      [GAUSSIAN_MIXTURE_CLUSTERING, 'gaussian-mix', 1, 'TRANSFORMATION', '', '', ''],

      [DECISION_TREE_CLASSIFIER, 'decision-tree-classifier', 1, 'TRANSFORMATION', '', '', ''],
      [GBT_CLASSIFIER, 'gbt-classifier', 1, 'TRANSFORMATION', '', '', ''],
      [NAIVE_BAYES_CLASSIFIER, 'naive-bayes', 1, 'TRANSFORMATION', '', '', ''],
      [PERCEPTRON_CLASSIFIER, 'perceptron', 1, 'TRANSFORMATION', '', '', ''],
      [RANDOM_FOREST_CLASSIFIER, 'random-forest-classifier', 1, 'TRANSFORMATION', '', '', ''],
      [LOGISTIC_REGRESSION, 'logistic-regression', 1, 'TRANSFORMATION', '', '', ''],
      [SVM_CLASSIFICATION, 'svm', 1, 'TRANSFORMATION', '', '', ''],

      [LINEAR_REGRESSION, 'linear-regression', 1, 'TRANSFORMATION', '', '', ''],
      [ISOTONIC_REGRESSION, 'isotonic-regression', 1, 'TRANSFORMATION', '', '', ''],
      [GBT_REGRESSOR, 'gbt-regressor', 1, 'TRANSFORMATION', '', '', ''],
      [RANDOM_FOREST_REGRESSOR, 'random-forest-regressor', 1, 'TRANSFORMATION', '', '', ''],
      [GENERALIZED_LINEAR_REGRESSOR, 'generalized-linear-regressor', 1, 'TRANSFORMATION', '', '', ''],
      [DECISION_TREE_REGRESSOR, 'decision-tree-regressor', 1, 'TRANSFORMATION', '', '', ''],
      
      [VISUALIZATION, 'visualization', 1, 'TRANSFORMATION', '', '', ''],

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation(conn):
    conn.execute(
        'DELETE from operation WHERE id BETWEEN %s AND %s',
        BASE_OP, max(ALL_OPS))

def _insert_operation_translation(conn):
    tb = table('operation_translation',
                column('id', Integer),
                column('locale', String),
                column('name', String),
                column('description', String),
                column('label_format', String),
                )
    columns = [c.name for c in tb.columns]
    data = [
      [SELECT, 'pt', 'Selecionar atributos', 'Selecionar atributos',
          '<b>${this.mode.value == "include"?"Selecionar":(this.mode.value == "rename" ? "Renomear" : "Descartar")}</b> <i>${this.attributes.value.length > 3? '
          'this.attributes.value.length + " atributos" : this.attributes.value.map(a=>a.attribute).join(", ")}</i>'],
      [READ_DATA, 'pt', 'Ler dados', 'Ler dados', '${data_source.label}: ${data_source.labelValue}'],
      [CAST, 'pt', 'Alterar o tipo do atributo', 'Altera o tipo do atributo.',
          'Alterar o tipo de ${this?.cast_attributes?.value?.length == 1? '
          'this.cast_attributes.value[0].attribute + " para " + this.cast_attributes.value[0].type '
          ': (this?.cast_attributes?.value?.length || 0) + " atributos"}'],
      [RENAME, 'pt',  'Renomear atributo', 'Renomeia atributo.',
         '<b>Renomear</b> <i>${this.attributes.value.length > 3? this.attributes.value.length + " atributos" : this.attributes.value.map(a=>a.attribute + " para " + a.alias).join(", ")}</i>'],
      [DISCARD, 'pt',  'Descartar atributo', 'Descarta atributo do resultado.',
          '<b>Descartar</b> <i>${this.attributes.value.length > 3? this.attributes.value.length + " atributos" : this.attributes.value.join(", ")}</i>'],
      [DUPLICATE, 'pt',  'Duplicar atributo', 'Duplica o atributo.',
          '<b>Duplicar</b> <i>${this.attributes.value.length > 3? this.attributes.value.length + " atributos" : this.attributes.value.map(a=>a.attribute + " como " + a.alias).join(", ")}</i>'],
      [FIND_REPLACE, 'pt',  'Localizar e substituir', 'Localiza valores no atributo e permite a substituição.', ''],

      [SORT, 'pt', 'Ordenar', 'Permite definir as opções de ordenação.',
            '<b>Ordenar por</b> <i>${this.order_by.value.map(v => v.f+ "(" + v.attribute +")").join(", ")}</i>'],
      [FILTER, 'pt', 'Filtrar', 'Permite definir as opções de filtro.', ''],
      [GROUP, 'pt', 'Agrupar', 'Permite definir opções para agrupamento.', '<b>Agrupar</b> por <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [JOIN, 'pt', 'Juntar com outra fonte de dados', 'Permite juntar com outra fonte de dados (JOIN).', ''],
      [CONCAT_ROWS, 'pt', 'Adicionar registros ao fim', 'Permite adicionar registros ao fim dos dados a partir de outra fonte de dados.', ''],
      [SAMPLE, 'pt', 'Amostrar ou limitar', 'Permite definir a amostragem dos dados.', ''],
      [LIMIT, 'pt', 'Limitar', 'Permite limitar a quantidade de dados.', ''],
      [WINDOW_FUNCTION, 'pt', 'Transformar com função de janela', 'Permite usar uma função de janela (deslizante).', ''],
      [PYTHON_CODE, 'pt', 'Transformar com Python', 'Permite usar código Python para transformar os dados.', ''],
      [ADD_BY_FORMULA, 'pt', 'Adicionar atributos usando fórmula', 'Permite adicionar novos atributos usando uma fórmula.',
          '<b>Atributo(s)</b> <i>${this.formula.value.map(e=>e.alias).join(", ")}</i> <b>usando fórmula</b>'],

      [INVERT_BOOLEAN, 'pt', 'Inverter', 'Permite inverter um valor lógico.',
          '<b>Inverter booleano</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [RESCALE, 'pt', 'Rescalar', 'Permite rescalar um valor numérico.',
          '<b>Rescalar</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [ROUND_NUMBER, 'pt', 'Arredondar', 'Permite arredondar um número.',
          '<b>Arredondar</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [DISCRETIZE, 'pt', 'Discretizar', 'Permite discretizar um número.',
          '<b>Discretizar</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [NORMALIZE, 'pt', 'Normalizar', 'Permite normalizar um número.',
          '<b>Normalizar</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [FORCE_RANGE, 'pt', 'Forçar faixa', 'Permite forçar um número a uma faixa.',
          '<b>Forçar faixa</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [TS_TO_DATE, 'pt', 'Timestamp para data', 'Permite converter um valor timestamp para data.',
          '<b>Converter</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i> de timestamp para data'],
      [TO_UPPER, 'pt', 'Converter para maiúsculas', 'Converte um texto para maiúsculas.',
          '<b>Converter</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i> para <b>maiúsculas</b>'],
      [TO_LOWER, 'pt', 'Converter para minúsculas', 'Converte um texto para minúsculas.',
          '<b>Converter</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i> para <b>minúsculas</b>'],
      [CAPITALIZE, 'pt', 'Capitalizar iniciais', 'Capitaliza inciais das palavras.',
          '<b>Capitalizar iniciais em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [REMOVE_ACCENTS, 'pt', 'Remover acentos', 'Remove acentos das palavras.',
          '<b>Remover acentos em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [NORMALIZE_TEXT, 'pt', 'Normalizar texto', 'Normaliza o texto, retirando acentos, números e outros símbolos que não sejam letras.',
          '<b>Normalizar texto em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [CONCAT_ATTRIBUTE, 'pt', 'Concatenar', 'Permite concatenar atributos com outros atributos ou valores.',
          '<b>Concatenar</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [TRIM, 'pt', 'Remover espaços em branco', 'Permite remover espaços em branco de um texto, no início, no fim ou ambos.',
          '<b>Remover espaços em branco em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [TRUNCATE_TEXT, 'pt', 'Truncar texto', 'Trunca um texto até um limite especificado de caracteres.',
          '<b>Truncar</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i> para tamanho ${this.characters.value}'],
      [SPLIT_INTO_WORDS, 'pt', 'Dividir em palavras', 'Divite o texto em palavras, considerando um separador.',
          '<b>Dividir texto em palavras em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [SUBSTRING, 'pt', 'Extrair texto', 'Permite extrair uma parte do texto.',
          '<b>Extrair texto em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [PARSE_TO_DATE, 'pt', 'Converter para data', 'Permite converter um texto em uma data.',
          '<b>Converter</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i> <b>para data</b>'],
      [EXTRACT_NUMBERS, 'pt', 'Extrair números a partir do texto', 'Extrai números de um texto.',
          '<b>Extrair números em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [EXTRACT_WITH_REGEX, 'pt', 'Extrair com expressão regular', 'Extrai dados usando expressões regulares.',
          '<b>Extrair com expressão regular</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [EXTRACT_FROM_ARRAY, 'pt', 'Extrair elemento(s) de arranjo', 'Permite extrair um elemento de um arranjo (array) usando índice(s).',
          '<b>Extrair elemento(s)</b> <i>${this.indexes.value}</i> <b>de arranjo em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      #[EXPAND_FROM_ARRAY, 'pt', 'Expandir arranjo', 'Permite converter um arranjo (array) em uma ou mais colunas ou linhas.',
      #    '<b>Expandir arranjo em</b> <i>${this.attributes.value.map(a=>a).join(", ")} <b>em novas colunas</b></i>'],
      [FOLD_ARRAY, 'pt', 'Converter em arranjo', 'Permite converter uma ou mais colunas em um arranjo (array) de valores.',
          '<b>Converter </b> <i>${this.attributes.value.map(a=>a).join(", ")} <b>em nova coluna do tipo arranjo</b></i>'],
      [CHANGE_ARRAY_TYPE, 'pt', 'Alterar o tipo do arranjo', 'Permite alterar o tipo de dados dos elementos de um arranjo (array).',
          '<b>Alterar o tipo do item do arranjo em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [SORT_ARRAY, 'pt', 'Ordenar arranjo', 'Permite ordenar os elementos de um arranjo (array).',
          '<b>Ordenar os itens do arranjo em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [FORCE_DATE_RANGE, 'pt', 'Forçar data a uma faixa', 'Força que as datas estejam em uma faixa de valores.',
          '<b>Forçar que datas em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i> <b>estejam em uma faixa</b>'],
      [UPDATE_HOUR, 'pt', 'Atualizar hora', 'Atualiza a hora de um atributo com datas.',
          '<b>Atualizar a hora das datas em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i> com <i></i>'],
      [TRUNCATE_DATE_TO, 'pt', 'Truncar data', 'Trunca a data para algum valor inicial.',
          '<b>Truncar hora das datas em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [DATE_DIFF, 'pt', 'Diferença de datas', 'Calcula a diferença entre datas.',
          '<b>Calcular a diferença entre datas </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [DATE_ADD, 'pt', 'Adicionar datas', 'Soma uma data com um valor numérico',
          '<b>Adicionar um valor às datas em </b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [DATE_PART, 'pt', 'Extrair parte de data', 'Extrai uma parte da data.',
          '<b>Extrair partes da data em</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [FORMAT_DATE, 'pt', 'Formatar data', 'Formata uma data segundo um parâmetro.',
          '<b>Formatar a data em</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i>'],
      [DATE_TO_TS, 'pt', 'Converter para timestamp', 'Converte uma data para um valor timestamp.',
          '<b>Converter a data em</b> <i>${this.attributes.value.map(a=>a).join(", ")}</i> <b>para timestamp</b>'],

      [ESCAPE_XML, 'pt', 'Escapar caracteres (XML)', 'Escapa caracteres especiais para o formato XML.', ''],
      [ESCAPE_UNICODE, 'pt', 'Escapar Unicode', 'Escapa caracteres Unicode.', ''],
      [STEMMING, 'pt', 'Gerar radicais (stemming)', 'Gera radicais das palavras por stemming.', ''],
      [N_GRAMS, 'pt', 'Gerar N-Gramas', 'Gera combinações N-Gramas', ''],
      [OBFUSCATE, 'pt', 'Ofuscar', 'Ofusca valores de forma a torná-los mais difíceis de serem usados de forma maliciosa.', ''],
      [ONE_HOT_ENCODE, 'pt', 'Codificar usando One Hot Encoder', 'Codifica usando One Hot Encoder.', ''],

      [FLAG_IN_RANGE, 'pt', 'Sinalizar registros em faixa', 'Sinaliza registros em faixa.', ''],
      [FLAG_INVALID, 'pt', 'Sinalizar registros com dados inválidos', 'Sinaliza registros com dados inválidos.', ''],
      [FLAG_EMPTY, 'pt', 'Sinalizar registros com atributos vazios', 'Sinaliza registros que tenham valores vazios em atributos determinados.', ''],
      [FLAG_WITH_FORMULA, 'pt', 'Sinalizar registros usando fórmula', 'Sinaliza registros usando fórmula.', ''],


      [CLEAN_MISSING, 'pt', 'Tratar dados ausentes', 'Trata dados ausentes de acordo com um regra.', ''],
      [REMOVE_MISSING, 'pt', 'Remover registros com dados ausentes', 'Remove registros com dados ausentes.', ''],
      [HANDLE_INVALID, 'pt', 'Tratar dados inválidos', 'Trata dados inválidos de acordo com um regra.', ''],
      [REMOVE_INVALID, 'pt', 'Remover registros com dados inválidos', 'Remover registros com dados inválidos.', ''],
      
      [SAVE, 'pt', 'Salvar dados', 'Salva os dados considerando os passos habilitados e visíveis.', ''],


      [SPLIT, 'pt', 'Dividir dados', 'Divide os dados de entrada entre treino e teste.', ''],
      [EVALUATOR, 'pt', 'Avaliar modelo', 'Avalia um modelo segundo alguma métrica.', ''],
      [FEATURES_REDUCTION, 'pt', 'Redução de atributos preditivos', 'Permite reduzir o número de atributros preditivos.', ''],
      [GRID, 'pt', 'Grade de parâmetros', 'Permite definir uma grade de parâmetros.', ''],
      [FEATURES, 'pt', 'Atributos preditivos', 'Permite configurar os atributos preditivos', ''],
      [K_MEANS_CLUSTERING, 'pt', 'Agrupamento K-Means', 'Agrupamento K-Means', ''],
      [GAUSSIAN_MIXTURE_CLUSTERING, 'pt', 'Agrupamento Misturas Gaussianas', 'Agrupamento misturas gaussianas.', ''],
      [DECISION_TREE_CLASSIFIER, 'pt', 'Classificador Árvore de Decisão', 'Classificador árvore de decisão.', ''],
      [GBT_CLASSIFIER, 'pt', 'Classificador GBT', 'Classificador GBT (Gradient Boosted Tree)', ''],
      [NAIVE_BAYES_CLASSIFIER, 'pt', 'Classificador Naive Bayes', 'Classificador Naive Bayes.', ''],
      [PERCEPTRON_CLASSIFIER, 'pt', 'Classificador Perceptron', 'Classificador Perceptron.', ''],
      [RANDOM_FOREST_CLASSIFIER, 'pt', 'Classificador Random Forest', 'Classificador Random Forest.', ''],
      [LOGISTIC_REGRESSION, 'pt', 'Regressão Logística', 'Regressão logística.', ''],
      [SVM_CLASSIFICATION, 'pt', 'Classificador SVM', 'Classificador SVM', ''],

      [LINEAR_REGRESSION, 'pt', 'Regressão Linear', 'Regressão linear', ''],
      [ISOTONIC_REGRESSION, 'pt', 'Regressão Isotônica', 'Regressão isotônica.', ''],
      [GBT_REGRESSOR, 'pt', 'Regressão GBT', 'Regressão GBT (Gradient Boosted Tree).', ''],
      [RANDOM_FOREST_REGRESSOR, 'pt', 'Regressão Random Forest', 'Regressão Random Forest.', ''],
      [GENERALIZED_LINEAR_REGRESSOR, 'pt', 'Regressão Linear Generalizada', 'Regressão linear generalizada.', ''],
      [DECISION_TREE_REGRESSOR, 'pt', 'Regressão por Árvore de Decisão', 'Regressão por árvore de decisão.', ''],
      
      [VISUALIZATION, 'pt', 'Visualização de dados', 'Visualização de dados.', ''],

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_translation(conn):
    conn.execute(
        'DELETE from operation_translation WHERE id BETWEEN %s AND %s',
        BASE_OP, max(ALL_OPS))

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
      [CAT_ARRAY, 'data-type', 100, 100],
      [CAT_MODEL_BUILDER, 'model-builder', 1, 1],
      [CAT_VISUALIZATION_BUILDER, 'visualization-builder', 1, 1]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category(conn):
    conn.execute(
        'DELETE from operation_category WHERE id BETWEEN %s AND %s',
        BASE_CATEGORY, BASE_CATEGORY + 15)

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
      [CAT_ARRAY, 'pt', 'Arranjo'],
      [CAT_MODEL_BUILDER, 'pt', 'Construtor de modelos']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_translation(conn):
    conn.execute(
        'DELETE from operation_category_translation WHERE id BETWEEN %s AND %s',
        BASE_CATEGORY, BASE_CATEGORY + 20)

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
                column('operation_id', Integer),
                column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [READ_DATA, BASE_CATEGORY + 0],

      [CAST, CAT_EDIT],
      [RENAME, CAT_EDIT],
      [DISCARD, CAT_EDIT],
      [DUPLICATE, CAT_EDIT],
      [FIND_REPLACE, CAT_EDIT],

      [SELECT, CAT_DATA],
      [SORT, CAT_DATA],
      [FILTER, CAT_DATA],
      [GROUP, CAT_DATA],
      [JOIN, CAT_DATA],
      [CONCAT_ROWS, CAT_DATA],
      [SAMPLE, CAT_DATA],
      [LIMIT, CAT_DATA],
      [WINDOW_FUNCTION, CAT_DATA],
      [PYTHON_CODE, CAT_DATA],
      [ADD_BY_FORMULA, CAT_DATA],
      [SAVE, CAT_DATA],

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
      # [EXPAND_FROM_ARRAY, CAT_TRANSFORM],
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


      [CLEAN_MISSING, CAT_FIX],
      [HANDLE_INVALID, CAT_FIX],
      [REMOVE_MISSING, CAT_FIX],
      [REMOVE_INVALID, CAT_FIX],

      [READ_DATA, CAT_MODEL_BUILDER],
      [SAMPLE, CAT_MODEL_BUILDER],

      [SPLIT, CAT_MODEL_BUILDER],
      [EVALUATOR, CAT_MODEL_BUILDER],
      [FEATURES_REDUCTION, CAT_MODEL_BUILDER],
      [GRID, CAT_MODEL_BUILDER],
      [FEATURES , CAT_MODEL_BUILDER],
      
      [K_MEANS_CLUSTERING, CAT_MODEL_BUILDER],
      [GAUSSIAN_MIXTURE_CLUSTERING, CAT_MODEL_BUILDER],
      [DECISION_TREE_CLASSIFIER, CAT_MODEL_BUILDER],
      [GBT_CLASSIFIER, CAT_MODEL_BUILDER],
      [NAIVE_BAYES_CLASSIFIER, CAT_MODEL_BUILDER],
      [PERCEPTRON_CLASSIFIER, CAT_MODEL_BUILDER],
      [RANDOM_FOREST_CLASSIFIER, CAT_MODEL_BUILDER],
      [LOGISTIC_REGRESSION, CAT_MODEL_BUILDER],
      [SVM_CLASSIFICATION, CAT_MODEL_BUILDER],
      
      [LINEAR_REGRESSION, CAT_MODEL_BUILDER],
      [ISOTONIC_REGRESSION, CAT_MODEL_BUILDER],
      [GBT_REGRESSOR, CAT_MODEL_BUILDER],
      [RANDOM_FOREST_REGRESSOR, CAT_MODEL_BUILDER],
      [GENERALIZED_LINEAR_REGRESSOR, CAT_MODEL_BUILDER],
      [DECISION_TREE_REGRESSOR, CAT_MODEL_BUILDER],


      [READ_DATA, CAT_VISUALIZATION_BUILDER],
      [FILTER, CAT_VISUALIZATION_BUILDER],
      [GROUP, CAT_VISUALIZATION_BUILDER],
      [SAMPLE, CAT_VISUALIZATION_BUILDER],
      [VISUALIZATION, CAT_VISUALIZATION_BUILDER],

    ]
    for op_id in [
        DECISION_TREE_CLASSIFIER, GBT_CLASSIFIER, NAIVE_BAYES_CLASSIFIER,
        PERCEPTRON_CLASSIFIER, RANDOM_FOREST_CLASSIFIER, LOGISTIC_REGRESSION,
        SVM_CLASSIFICATION]:    
        data.append([op_id, CAT_CLASSIFICATION])

    for op_id in [LINEAR_REGRESSION, ISOTONIC_REGRESSION, 
        GBT_REGRESSOR, RANDOM_FOREST_REGRESSOR, GENERALIZED_LINEAR_REGRESSOR,
        DECISION_TREE_REGRESSOR]:
        data.append([op_id, CAT_REGRESSION])

    for op_id in [K_MEANS_CLUSTERING, GAUSSIAN_MIXTURE_CLUSTERING]:
        data.append([op_id, CAT_CLUSTERING])


    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_operation(conn):
    conn.execute(
        '''DELETE FROM operation_category_operation
            WHERE operation_id BETWEEN %s and %s ''',
        BASE_OP, MAX_OP)

def _insert_operation_platform(conn):
    tb = table('operation_platform',
                column('operation_id', Integer),
                column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [op_id, META_PLATFORM] for op_id in ALL_OPS
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
      [ATTRIBUTE_FORM, 1, 1, 'execution'], # Attribute (multiple = false) (common)
      [ALIAS_FORM, 1, 1, 'execution'], # Alias (common)
    ]
    exclusions = set([
        K_MEANS_CLUSTERING, GAUSSIAN_MIXTURE_CLUSTERING, DECISION_TREE_CLASSIFIER, 
        GBT_CLASSIFIER, NAIVE_BAYES_CLASSIFIER, PERCEPTRON_CLASSIFIER, 
        RANDOM_FOREST_CLASSIFIER, LOGISTIC_REGRESSION, SVM_CLASSIFICATION, 
        LINEAR_REGRESSION, ISOTONIC_REGRESSION, GBT_REGRESSOR, 
        RANDOM_FOREST_REGRESSOR, GENERALIZED_LINEAR_REGRESSOR,
        DECISION_TREE_REGRESSOR])

    for op_id in set(ALL_OPS) - exclusions: # Operations' form
        data.append([op_id + 50, 1, 1, 'execution'])

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form(conn):
    conn.execute(
        'DELETE from operation_form WHERE id BETWEEN %s AND %s',
        BASE_FORM, max(ALL_OPS) + 50)

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
      [ATTRIBUTE_FORM, 'pt', 'Execução'],
      [ALIAS_FORM, 'pt', 'Execução'],

      [BASE_FORM, 'en', 'Execution'],
      [BASE_FORM + 1, 'en', 'Execution'],
      [ATTRIBUTES_FORM, 'en', 'Execution'],
      [ALIASES_FORM, 'en', 'Execution'],
      [KEEP_ATTRIBUTE_FORM, 'en', 'Execution'],
      [ATTRIBUTE_FORM, 'en', 'Execution'],
      [ALIAS_FORM, 'en', 'Execution'],
    ]
    exclusions = set([
        K_MEANS_CLUSTERING, GAUSSIAN_MIXTURE_CLUSTERING, DECISION_TREE_CLASSIFIER, 
        GBT_CLASSIFIER, NAIVE_BAYES_CLASSIFIER, PERCEPTRON_CLASSIFIER, 
        RANDOM_FOREST_CLASSIFIER, LOGISTIC_REGRESSION, SVM_CLASSIFICATION, 
        LINEAR_REGRESSION, ISOTONIC_REGRESSION, GBT_REGRESSOR, 
        RANDOM_FOREST_REGRESSOR, GENERALIZED_LINEAR_REGRESSOR,
        DECISION_TREE_REGRESSOR])


    for op_id in set(ALL_OPS) - exclusions: # Operations' form
        data.append([op_id + 50, 'pt', 'Execução'])
        data.append([op_id + 50, 'en', 'Execution'])

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_translation(conn):
    conn.execute(
        'DELETE from operation_form_translation WHERE id BETWEEN %s AND %s',
        BASE_FORM, max(ALL_OPS) + 50)

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
    split_strategy = [
          {'key': 'split', 'pt': 'Dividir aleatoriamente entre treino e teste', 'en': 'Randomly split between training and testing'},
          {'key': 'cross_validation', 'pt': 'Realizar a validação cruzada', 'en': 'Perform cross-validation'},
    ]
    tasks_types = [
          {'key': 'clustering', 'pt': 'Agrupamento', 'en': 'Clustering'},
          {'key': 'binary-classification', 'pt': 'Classificação binária', 'en': 'Classification binária'},
          {'key': 'multiclass-classification', 'pt': 'Classificação multiclasse', 'en': 'Classification multiclasse'},
          {'key': 'regression', 'pt': 'Regressão', 'en': 'Regression'},
    ]
    bin_classification_metrics = [
	{ "key": "areaUnderROC", "value": "Area under ROC curve", "en": "Area under ROC curve", "pt": "Área sob a curva ROC"},
        { "key": "areaUnderPR", "value": "Area under precision-recall curve",
            "en": "Area under precision-recall curve", "pt": "Área sobre a curva de precisão-revocação"
        }
     ]
    multi_classification_metrics = [
        { "key": "f1", "value": "F1 score", "en": "F1 score", "pt": "Métrica F1" },
        {
            "key": "weightedPrecision", "value": "Weighted precision", "en": "Weighted precision",
            "pt": "Precisão ponderada"
        }, {
            "key": "weightedRecall", "value": "Weighted recall",
            "en": "Weighted recall", "pt": "Revocação ponderada"
        },
        { "key": "accuracy", "value": "Accuracy", "en": "Accuracy", "pt": "Acurácia" },
    ]
    regression_metrics = [
        {
            "key": "rmse", "value": "Root mean squared error", "en": "Root mean squared error",
            "pt": "Raíz do erro quadrático médio"
        },
        { "key": "mse", "value": "Mean squared error", "en": "Mean squared error", "pt": "Erro quadrático médio" },
        { "key": "mae", "value": "Mean absolute error", "en": "Mean absolute error", "pt": "Erro absoluto médio" },
        {
            "key": "mape", "value": "Mean absolute percentage error",
            "en": "Mean absolute percentage error", "pt": "Média Percentual Absoluta do Erro"
        },
        {
            "key": "r2", "value": "Coefficient of determination R2", "en": "Coefficient of determination R2",
            "pt": "Coeficiente de determinação (R2)"
        }
    ]   
    clustering_metrics = [
        {
            "key": "silhouette", "value": "Silhouette", "en": "Silhouette",
            "pt": "Silhouette"
        },
    ]
    reduction_method = [
	  {'key': 'disabled', 'pt': 'Sem redução', 'en': 'Do not reduce'},
          {'key': 'pca', 'pt': 'Principal Component Analysis - PCA', 
			'en': 'Principal Component Analysis - PCA'},
    ]  
    grid_strategy = [
	  {'key': 'grid', 'pt': 'Busca em grade', 'en': 'Grid search'},
          {'key': 'random', 'pt': 'Busca aleatória', 'en': 'Random search'},
    ]  
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM_FIELD + 0, 'comment', 'TEXT', 1, 1, None, 'textarea', None, None, 'EXECUTION', None, 1, BASE_FORM + 0],
      [BASE_FORM_FIELD + 1, 'data_source', 'TEXT', 1, 1, None, 'lookup',
        '`${LIMONERO_URL}/datasources?&simple=true&list=true&enabled=1`', None, 'EXECUTION', None, 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 2, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', None, 1, ATTRIBUTES_FORM],
      [BASE_FORM_FIELD + 3, 'overwrite', 'INTEGER', 0, 2, '1', 'checkbox', None, None, 'EXECUTION', None, 1, KEEP_ATTRIBUTE_FORM],
      [BASE_FORM_FIELD + 4, 'aliases', 'TEXT', 0, 20, None, 'tag', None, None, 'EXECUTION', None, 1, ALIASES_FORM],
      [BASE_FORM_FIELD + 5, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 1, ATTRIBUTE_FORM],#FIXME review name because UI
      [BASE_FORM_FIELD + 6, 'alias', 'TEXT', 0, 20, None, 'text', None, None, 'EXECUTION', None, 1, ALIAS_FORM],


      [BASE_FORM_FIELD + 51, 'find', 'TEXT', 1, 3, None, 'text', None, None, 'EXECUTION', None, 1, FIND_REPLACE + 50],
      [BASE_FORM_FIELD + 52, 'replace', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION', None, 1, FIND_REPLACE + 50],

      [BASE_FORM_FIELD + 53, 'other', 'TEXT', 1, 3, None, 'attribute-selector', None, None, 'EXECUTION', None, 1, CONCAT_ATTRIBUTE + 50],
      [BASE_FORM_FIELD + 54, 'separator', 'TEXT', 1, 4, None, 'attribute-selector', None, None, 'EXECUTION', None, 1, CONCAT_ATTRIBUTE + 50],

      [BASE_FORM_FIELD + 55, 'characters', 'INTEGER', 1, 3, None, 'integer', None, None, 'EXECUTION', None, 1, TRUNCATE_TEXT + 50],

      [BASE_FORM_FIELD + 56, 'delimiter', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION', None, 1, SPLIT_INTO_WORDS + 50],

      [BASE_FORM_FIELD + 57, 'format', 'TEXT', 1, 3, None, 'select2', None, None, 'EXECUTION', None, 1, PARSE_TO_DATE + 50],

      [BASE_FORM_FIELD + 58, 'regex', 'TEXT', 1, 3, None, 'text', None, None, 'EXECUTION', None, 1, EXTRACT_WITH_REGEX + 50],

      [BASE_FORM_FIELD + 59, 'start', 'FLOAT', 0, 3, None, 'decimal', None, None, 'EXECUTION', None, 1, RESCALE + 50],
      [BASE_FORM_FIELD + 60, 'end', 'FLOAT', 0, 4, None, 'decimal', None, None, 'EXECUTION', None, 1, RESCALE + 50],

      [BASE_FORM_FIELD + 61, 'bins', 'INTEGER', 1, 3, None, 'INTEGER', None, None, 'EXECUTION', None, 1, DISCRETIZE + 50],

      [BASE_FORM_FIELD + 62, 'normalizer', 'TEXT', 1, 3, None, 'dropdown', None, None, 'EXECUTION', None, 1, NORMALIZE + 50],

      [BASE_FORM_FIELD + 63, 'start', 'FLOAT', 0, 3, None, 'decimal', None, None, 'EXECUTION', None, 1, FORCE_RANGE + 50],
      [BASE_FORM_FIELD + 64, 'end', 'FLOAT', 0, 4, None, 'decimal', None, None, 'EXECUTION', None, 1, FORCE_RANGE + 50],

      [BASE_FORM_FIELD + 65, 'decimals', 'INTEGER', 1, 3, '2', 'integer', None, None, 'EXECUTION', None, 1, ROUND_NUMBER + 50],

      # [BASE_FORM_FIELD + 66, 'limit', 'INTEGER', 1, 3, '10', 'decimal', None, None, 'EXECUTION', None, 1, EXPAND_FROM_ARRAY + 50],

      [BASE_FORM_FIELD + 67, 'new_type', 'TEXT', 1, 3, None, 'dropdown', None, None, 'EXECUTION', None, 1, CHANGE_ARRAY_TYPE + 50],

      [BASE_FORM_FIELD + 68, 'direction', 'TEXT', 1, 3, 'asc', 'dropdown', None,
        json.dumps([{'key': 'asc', 'pt': 'Ascendente', 'en': 'Ascending'}, {'key': 'desc', 'pt': 'Descendente', 'en': 'Descending'}]),
        'EXECUTION', None, 1, FORCE_RANGE + 50],
      [BASE_FORM_FIELD + 69, 'format', 'TEXT', 1, 3, None, 'text', None, None, 'EXECUTION', None, 1, FORMAT_DATE + 50],

      [BASE_FORM_FIELD + 70, 'start', 'FLOAT', 0, 3, None, 'date', None, None, 'EXECUTION', None, 1, FORCE_DATE_RANGE + 50],
      [BASE_FORM_FIELD + 71, 'end', 'FLOAT', 0, 4, None, 'date', None, None, 'EXECUTION', None, 1, FORCE_DATE_RANGE + 50],

      [BASE_FORM_FIELD + 72, 'hour_column', 'TEXT', 1, 3, None, 'attribute-selector', None, None, 'EXECUTION', None, 1, UPDATE_HOUR + 50],

      [BASE_FORM_FIELD + 73, 'components', 'TEXT', 1, 3, None, 'tag', None, None, 'EXECUTION', None, 1, DATE_PART + 50],

      [BASE_FORM_FIELD + 74, 'value', 'INTEGER', 1, 3, None, 'integer', None, None, 'EXECUTION', None, 1, DATE_ADD + 50],
      [BASE_FORM_FIELD + 75, 'period', 'TEXT', 1, 4, None, 'dropdown', None,
        json.dumps([{'key': 'day', 'pt': 'Dia(s)', 'en': 'Day(s)'}, {'key': 'hour', 'pt': 'Hora(s)', 'en': 'Hour(s)'}]),
        'EXECUTION', None, 1, DATE_ADD + 50],

      [BASE_FORM_FIELD + 76, 'type', 'INTEGER', 1, 3, 'now', 'dropdown', None,
           json.dumps([{'key': 'now', 'pt': 'A data/hora atuais', 'en': 'Current date/hour'},
            {'key': 'attribute', 'pt': 'Um atributo', 'en': 'An attribute'}, {'key': 'constant', 'pt': 'Data específica', 'en': 'Specific date'}]),
        'EXECUTION', None, 1, DATE_DIFF + 50],
      [BASE_FORM_FIELD + 77, 'date_attribute', 'INTEGER', 1, 4, None, 'attribute-selector', None, None, 'EXECUTION', 'this.type.internalValue === "attribute"', 1, DATE_DIFF + 50],
      [BASE_FORM_FIELD + 78, 'value', 'TEXT', 1, 5, None, 'date', None, '{"use-datetime-local": true}', 'EXECUTION', 'this.type.internalValue === "constant"', 1, DATE_DIFF + 50],
      [BASE_FORM_FIELD + 89, 'unit', 'TEXT', 1, 6, 'days', 'dropdown', None,
              json.dumps([
                  {'key': 'seconds', 'en': 'Seconds', 'pt': 'Segundos'},
                  {'key': 'minutes', 'en': 'Minutes', 'pt': 'Minutos'},
                  {'key': 'hours', 'en': 'Hours', 'pt': 'Horas'},
                  {'key': 'days', 'en': 'Days', 'pt': 'Dias'},
                  {'key': 'weeks', 'en': 'Weeks', 'pt': 'Semanas'},
                  {'key': 'months', 'en': 'Monthis', 'pt': 'Meses'},
                  {'key': 'years', 'en': 'Years', 'pt': 'Anos'},
                  ]),
              'EXECUTION', None, 1, DATE_DIFF + 50],
      [BASE_FORM_FIELD + 90, 'invert', 'INTEGER', 1, 5, None, 'checkbox', None, None, 'EXECUTION', None, 1, DATE_DIFF + 50],

      [BASE_FORM_FIELD + 79, 'start', 'FLOAT', 0, 3, None, 'decimal', None, None, 'EXECUTION', None, 1, FLAG_IN_RANGE + 50],
      [BASE_FORM_FIELD + 80, 'end', 'FLOAT', 0, 4, None, 'decimal', None, None, 'EXECUTION', None, 1, FLAG_IN_RANGE + 50],

      [BASE_FORM_FIELD + 81, 'formula', 'TEXT', 0, 3, None, 'expression', None, None, 'EXECUTION', None, 1, FLAG_WITH_FORMULA + 50],

     [BASE_FORM_FIELD + 84, 'type', 'INTEGER', 1, 3, None, 'dropdown', None,
        json.dumps([{'key': 'null', 'pt': 'Limpar valor', 'en': 'Clean value'},
            {'key': 'average', 'pt': 'Com a média', 'en': 'With average'},
            {'key': 'constant', 'pt': 'Valor constante', 'en': 'Constant value'}]),
        'EXECUTION', None, 1, HANDLE_INVALID + 50],
     [BASE_FORM_FIELD + 85, 'value', 'TEXT', 1, 4, None, 'text', None, None, 'EXECUTION', None, 1, HANDLE_INVALID + 50],

    [BASE_FORM_FIELD + 86, 'formula', 'TEXT', 1, 3, None, 'expression', None, '{"alias": true}', 'EXECUTION', None, 1, ADD_BY_FORMULA + 50],

    [BASE_FORM_FIELD + 87, 'formula', 'TEXT', 1, 3, None, 'expression', None, '{"alias": false}', 'EXECUTION', None, 1, FILTER + 50],
    [BASE_FORM_FIELD + 88, 'order_by', 'TEXT', 1, 3, 'asc', 'attribute-function', None,
            json.dumps({"functions": [
                {"key": "asc", "value": "Ascending", "help": {"pt": "Ordena valores de forma crescente", "en": "Sort in ascending order"}},
                    {"key": "desc", "value": "Descending", "help": {"pt": "Ordena valores de forma decrescente", "en": "Sort in descending order"}}],
                    "options": {"title": "Sort operation", "description": "Sort a data source by a set of attributes",
                        "show_alias": False}}),
        'EXECUTION', None, 1, SORT + 50],

      [BASE_FORM_FIELD + 91, 'attributes', 'TEXT', 1, 1, None, 'attribute-alias-selector', None, None, 'EXECUTION', None, 1, RENAME + 50],
      [BASE_FORM_FIELD + 92, 'attributes', 'TEXT', 1, 1, None, 'attribute-alias-selector', None, None, 'EXECUTION', None, 1, DUPLICATE + 50],
      
      [BASE_FORM_FIELD + 93, 'indexes', 'TEXT', 1, 1, None, 'text', None, None, 'EXECUTION', None, 1, EXTRACT_FROM_ARRAY + 50],
      
      [BASE_FORM_FIELD + 94, 'data_source', 'INTEGER', 1, 1, None, 'lookup', '`${LIMONERO_URL}/datasources?simple=true&list=true&enabled=1`', None, 'EXECUTION', None, 1, CONCAT_ROWS + 50],
      
      [BASE_FORM_FIELD + 95, 'data_source', 'INTEGER', 1, 0, None, 'lookup', '`${LIMONERO_URL}/datasources?simple=true&list=true&enabled=1`', None, 'EXECUTION', None, 1, JOIN + 50],

      # Model builder
      [BASE_FORM_FIELD + 96, 'strategy', 'INTEGER', 1, 0, 'split', 'lookup', None, json.dumps(split_strategy), 
              'EXECUTION', None, 1, SPLIT + 50],
      [BASE_FORM_FIELD + 97, 'ratio', 'FLOAT', 1, 1, None, 'decimal', None, None, 'EXECUTION', None, 1, SPLIT + 50],
      [BASE_FORM_FIELD + 98, 'folds', 'INTEGER', 1, 1, '10', 'integer', None, None, 'EXECUTION', None, 1, SPLIT + 50],
      [BASE_FORM_FIELD + 99, 'seed', 'INTEGER', 1, 0, None, 'lookup', None, None, 'EXECUTION', None, 1, SPLIT + 50],    
      [BASE_FORM_FIELD + 100, 'task_type', 'TEXT', 1, 0, 'binary-classification', 'lookup', None, json.dumps(tasks_types), 'EXECUTION', None, 1, EVALUATOR + 50],
      [BASE_FORM_FIELD + 101, 'method', 'INTEGER', 1, 0, 'disabled', 'lookup', None, json.dumps(reduction_method), 'EXECUTION', None, 1, FEATURES_REDUCTION + 50],
      [BASE_FORM_FIELD + 102, 'strategy', 'INTEGER', 1, 0, 'grid', 'lookup', None, json.dumps(grid_strategy), 'EXECUTION', None, 1, GRID + 50],
      [BASE_FORM_FIELD + 103, 'random_grid', 'INTEGER', 1, 1, None, 'checkbox', None, None, 'EXECUTION', None, 1, GRID + 50],
      [BASE_FORM_FIELD + 104, 'seed', 'INTEGER', 1, 2, None, 'lookup', None, None, 'EXECUTION', None, 1, GRID + 50],
      [BASE_FORM_FIELD + 105, 'max_iterations', 'INTEGER', 1, 3, None, 'integer', None, None, 'EXECUTION', None, 1, GRID + 50],
      [BASE_FORM_FIELD + 106, 'max_search_time', 'INTEGER', 1, 4, None, 'integer', None, None, 'EXECUTION', None, 1, GRID + 50],
      [BASE_FORM_FIELD + 107, 'parallelism', 'INTEGER', 1, 5, None, 'integer', None, None, 'EXECUTION', None, 1, GRID + 50],
      [BASE_FORM_FIELD + 108, 'features', 'TEXT', 1, 2, None, 'features', None, None, 'EXECUTION', None, 1, FEATURES + 50],
      [BASE_FORM_FIELD + 109, 'bin_metric', 'TEXT', 1, 2, 'areaUnderROC', 'features', None, json.dumps(bin_classification_metrics), 'EXECUTION', None, 1, EVALUATOR + 50],
      [BASE_FORM_FIELD + 110, 'multi_metric', 'TEXT', 1, 2, 'accuracy', 'features', None,json.dumps(multi_classification_metrics), 'EXECUTION', None, 1, EVALUATOR + 50],
      [BASE_FORM_FIELD + 111, 'reg_metric', 'TEXT', 1, 2, 'rmse' , 'features', None, json.dumps(regression_metrics), 'EXECUTION', None, 1, EVALUATOR + 50],
      [BASE_FORM_FIELD + 112, 'clust_metric', 'TEXT', 1, 2, 'rmse' , 'features', None, json.dumps(clustering_metrics), 'EXECUTION', None, 1, EVALUATOR + 50],
      [BASE_FORM_FIELD + 113, 'k', 'INTEGER', 1, 0, None, 'integer', None, None, 'EXECUTION', 'this.method.internalValue === "pca"', 1, FEATURES_REDUCTION + 50],
      
      [BASE_FORM_FIELD + 114, 'type', 'INTEGER', 1, 0, None, 'integer', None, None, 'EXECUTION', '{"multiple": false}', 1, VISUALIZATION + 50],
      [BASE_FORM_FIELD + 115, 'x_axis', 'TEXT', 1, 1, None, 'atribute-selector', None, None, 'EXECUTION', None, 1, VISUALIZATION + 50],
      [BASE_FORM_FIELD + 116, 'y_axis', 'TEXT', 1, 1, None, 'atribute-selector', None, None, 'EXECUTION', None, 1, VISUALIZATION + 50],
      [BASE_FORM_FIELD + 117, 'display_legend', 'INTEGER', 1, 1, None, 'checkbox', None, None, 'EXECUTION', None, 1, VISUALIZATION + 50],
      [BASE_FORM_FIELD + 118, 'palette', 'TEXT', 1, 0, None, 'color-palette', None, None, 'EXECUTION', None, 1, VISUALIZATION + 50],
      [BASE_FORM_FIELD + 119, 'direction', 'TEXT', 1, 0, None, 'dropdown', None, json.dumps(
          [{'key': 'vertical', 'pt': 'Vertical', 'en': 'Vertical'}, {'key': 'horizontal', 'pt': 'Horizontal', 'en': 'Horizontal'}]), 
          'EXECUTION', None, 1, VISUALIZATION + 50],
      [BASE_FORM_FIELD + 120, 'stacked', 'INTEGER', 1, 0, None, 'checkbox', None, None, 'EXECUTION', None, 1, VISUALIZATION + 50],
      [BASE_FORM_FIELD + 121, 'hole', 'FLOAT', 1, 0, None, 'decimal', None, None, 'EXECUTION', None, 1, VISUALIZATION + 50],
      [BASE_FORM_FIELD + 122, 'line_stroke', 'INTEGER', 1, 0, None, 'integer', None, None, 'EXECUTION', None, 1, VISUALIZATION + 50],
      [BASE_FORM_FIELD + 123, 'line_type', 'TEXT', 1, 0, None, 'dropdown', None, json.dumps(
          [{'key': 'solid', 'pt': 'Sólida', 'en': 'Solid'}, {'key': 'dot', 'pt': 'Ponto', 'en': 'Dot'}, {'key': 'dashed', 'pt': 'Tracejado', 'en': 'Dashed'}]), 
          'EXECUTION', None, 1, VISUALIZATION + 50],
      [BASE_FORM_FIELD + 124, 'mode', 'TEXT', 1, 0, None, 'dropdown', None, json.dumps(
          [{'key': 'lines', 'pt': 'Linhas', 'en': 'Lines'}, {'key': 'marks', 'pt': 'Marcas', 'en': 'Marks'}, {'key': 'lines+markers', 'pt': 'Linhas e marcas', 'en': 'Lines and marks'}]), 
          'EXECUTION', None, 1, VISUALIZATION + 50],
    ]

    # Fix generalized linear regression
    # link_gaussian_gamma = [
    #         {"en": "identity", "key": "identity", "value": "identidade", "pt": "identity"}, 
    #         {"en": "log", "key": "log", "value": "log", "pt": "log"}, 
    #         {"en": "inverse", "key": "inverse", "value": "inverse", "pt": "inversa"}
    # ]
    # link_binomial = [
    #         {"en": "logit", "key": "logit", "value": "logit", "pt": "logit"}, 
    #         {"en": "probit", "key": "probit", "value": "probit", "pt": "probit"}, 
    #         {"en": "cloglog", "key": "cloglog", "value": "cloglog", "pt": "cloglog"}
    #         ]
    # link_poisson= [
    #         {"en": "identity", "key": "identity", "value": "identidade", "pt": "identity"}, 
    #         {"en": "log", "key": "log", "value": "log", "pt": "log"}, 
    #         {"en": "sqrt", "key": "sqrt", "value": "sqrt", "pt": "sqrt"}
    # ]

    # data.append([266, 'link', 'TEXT', 0, 6, 'identity', 'dropdown', None, json.dumps(link_gaussian_gamma), 'EXECUTION', 'this.family.internalValue === "gaussian"', 1, 107])
    # data.append([267, 'link', 'TEXT', 0, 6, 'logit', 'dropdown', None, json.dumps(link_binomial), 'EXECUTION', 'this.family.internalValue === "binomial"', 1, 107])
    # data.append([268, 'link', 'TEXT', 0, 6, 'log', 'dropdown', None, json.dumps(link_poisson), 'EXECUTION', 'this.family.internalValue === "poisson"', 1, 107])
    # data.append([280, 'link', 'TEXT', 0, 6, 'inverse', 'dropdown', None, json.dumps(link_gaussian_gamma), 'EXECUTION', 'this.family.internalValue === "gaussian"', 1, 107])

    # Fix linear regression
    loss = [
            {"en": "Squared error", "key": "squaredError", "pt": "Erro quadrado (squared error)"}, 
            {"en": "Huber method", "key": "huber", "pt": "Método de Huber"}, 
    ]
    data.append([240, 'loss', 'TEXT', 0, 1, 'squaredError', 'dropdown', None, json.dumps(loss), 'EXECUTION', None, 1, 8])
    data.append([241, 'reg_param', 'FLOAT', 0, 8, None, 'decimal', None, None, 'EXECUTION', None, 1, 8])
    data.append([183, 'epsilon', 'FLOAT', 0, 9, None, 'decimal', None, None, 'EXECUTION', 'this.loss.internalValue === "hubber"', 1, 8])
    data.append([184, 'tolerance', 'FLOAT', 0, 10, None, 'decimal', None, None, 'EXECUTION', None, 1, 8])
    data.append([185, 'standardization', 'INTEGER', 0, 11, '1', 'checkbox', None, None, 'EXECUTION', None, 1, 8])
    data.append([175, 'fit_intercept', 'INTEGER', 0, 12, '1', 'checkbox', None, None, 'EXECUTION', None, 1, 8])

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE (id BETWEEN %s AND %s) or id IN (183,184,185,240,241,175)',
        BASE_FORM_FIELD, BASE_FORM_FIELD + 140)

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
      [BASE_FORM_FIELD + 2, 'pt', 'Atributos', 'Lista de atributos a serem usados na ação.'],
      [BASE_FORM_FIELD + 3, 'pt', 'Sobrescrever atributo(s) original(ais)', 'Indica se o(s) atributo(s) original(ais) deve(m) ser sobrescrito(s) após a transformação ou se novos atributos serão criados.'],
      [BASE_FORM_FIELD + 4, 'pt', 'Novos nomes', 'Novos nomes para os atributos resultantes.'],
      [BASE_FORM_FIELD + 5, 'pt', 'Atributo', 'Atributo a ser usado na ação.'],
      [BASE_FORM_FIELD + 6, 'pt', 'Atributo resultante (pode ser novo)', 'Nome para o atributo resultante.'],

      [BASE_FORM_FIELD + 51, 'pt', 'Encontrar', 'Valor a ser pesquisado.'],
      [BASE_FORM_FIELD + 52, 'pt', 'Substituir', 'Valor a ser usado na substituição.'],
      [BASE_FORM_FIELD + 53, 'pt', 'Atributo(s) a ser(em) concatenado(s)', 'Atributo(s) a ser(em) concatenado(s).'],
      [BASE_FORM_FIELD + 54, 'pt', 'Separador', 'Separador para os atributos a serem concatenados.'],

      # FIXME Invalid values
      [BASE_FORM_FIELD + 55, 'pt', 'Número de caracteres', 'Números de caracteres limite.'],
      [BASE_FORM_FIELD + 56, 'pt', 'Delimitador', 'Delimitador para as palavras.'],
      [BASE_FORM_FIELD + 57, 'pt', 'Formato', 'Formato. '],
      [BASE_FORM_FIELD + 58, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 59, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 60, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 61, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 62, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 63, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 64, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 65, 'pt', 'Casas decimais', 'Número de casas decimais (dígitos após a vírgula).'],
      # [BASE_FORM_FIELD + 66, 'pt', 'Índice', 'Índice'],
      [BASE_FORM_FIELD + 67, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 68, 'pt', 'Direção', 'Direção da ordenação (ascendente ou descendente)'],
      [BASE_FORM_FIELD + 69, 'pt', 'Formato', 'Formato. Deve ser compatível com o formato da linguagem Java.'],
      [BASE_FORM_FIELD + 70, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 71, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 72, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 73, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 74, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 75, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 76, 'pt', 'Diferença para', 'Valor ou atributo usado para calcular a diferença entre datas.'],
      [BASE_FORM_FIELD + 77, 'pt', '2o. Atributo', '2o. atributo'],
      [BASE_FORM_FIELD + 78, 'pt', 'Valor (data válida)', 'Value (valid date)'],
      [BASE_FORM_FIELD + 79, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 80, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 81, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 84, 'pt', 'Value', 'Value'],
      [BASE_FORM_FIELD + 85, 'pt', 'Value', 'Value'],

      [BASE_FORM_FIELD + 86, 'pt', 'Fórmula(s)', 'Fórmula(s)'],
      [BASE_FORM_FIELD + 87, 'pt', 'Filtro(s)', 'Filtro(s)'],
      [BASE_FORM_FIELD + 88, 'pt', 'Opções de ordenação', 'Opções de ordenação'],
      [BASE_FORM_FIELD + 89, 'pt', 'Unidade de tempo', 'Unidade de tempo.'],
      [BASE_FORM_FIELD + 90, 'pt', 'Inverter o resultado (-1)', 'Calcula a diferença entre o argumento e o atributo data selecionado.'],

      [BASE_FORM_FIELD + 91, 'pt', 'Atributo(s)', 'Permite renomear um ou mais atributos.'],
      [BASE_FORM_FIELD + 92, 'pt', 'Atributo(s)', 'Permite duplicar um ou mais atributos.'],
      [BASE_FORM_FIELD + 93, 'pt', 'Índices dos elementos a extrair, separados por vírgula. 0 é o primeiro elemento e '
        'números negativos contam a partir do fim para o início (reverso).',
        'Permite duplicar um ou mais atributos. O nome dos novos atributos têm o nome original + índice como sufixo.'],

      [BASE_FORM_FIELD + 94, 'pt', 'Fonte de dados', 'Permite unir (concatenar) registros de duas fontes de dados.'],
      [BASE_FORM_FIELD + 95, 'pt', 'Fonte de dados', 'Permite juntar (join) registros de duas fontes de dados a partir de condições.'],

      [BASE_FORM_FIELD + 96, 'pt', 'Estratégia para divisão entre treino e teste', 'Estratégia para divisão entre treino e teste.'],
      [BASE_FORM_FIELD + 97, 'pt', 'Razão treino/teste', 'Razão treino/teste'],
      [BASE_FORM_FIELD + 98, 'pt', 'Número de folds', 'Número de folds.'],
      [BASE_FORM_FIELD + 99, 'pt', 'Semente aleatória', 'Semente aleatória.'],
      [BASE_FORM_FIELD + 100, 'pt', 'Métrica', 'Métrica.'],
      [BASE_FORM_FIELD + 101, 'pt', 'Método de redução', 'Método de redução.'],
      [BASE_FORM_FIELD + 102, 'pt', 'Estratégia de busca em grade', 'Estratégia de busca em grade.'],
      [BASE_FORM_FIELD + 103, 'pt', 'Usar grade aleatória', 'Usar grade aleatória.'],
      [BASE_FORM_FIELD + 104, 'pt', 'Semente aleatória', 'Semente aleatória.'],
      [BASE_FORM_FIELD + 105, 'pt', 'Número máximo de iterações', 'Número máximo de iterações.'],
      [BASE_FORM_FIELD + 106, 'pt', 'Tempo máximo de busca', 'Tempo máximo de busca.'],
      [BASE_FORM_FIELD + 107, 'pt', 'Paralelismo', 'Paralelismo'],
      [BASE_FORM_FIELD + 108, 'pt', 'Atributos preditivos', 'Atributos preditivos.'],
      [BASE_FORM_FIELD + 109, 'pt', 'Métrica', 'Métrica'],
      [BASE_FORM_FIELD + 110, 'pt', 'Métrica', 'Métrica'],
      [BASE_FORM_FIELD + 111, 'pt', 'Métrica', 'Métrica'],
      [BASE_FORM_FIELD + 112, 'pt', 'Métrica', 'Métrica'],
      [BASE_FORM_FIELD + 113, 'pt', 'Número de componentes principais (k)', 'Número de componentes principais (k).'],
      
      [BASE_FORM_FIELD + 114, 'pt', 'Tipo', 'Tipo da visualização.'],
      [BASE_FORM_FIELD + 115, 'pt', 'Eixo X', 'Atributo usado no eixo X.'],
      [BASE_FORM_FIELD + 116, 'pt', 'Eixo Y', 'Atributo usado no eixo Y.'],
      [BASE_FORM_FIELD + 117, 'pt', 'Exibir leganda', 'Indica se é para exibir a legenda do gráfico.'],
      [BASE_FORM_FIELD + 118, 'pt', 'Paleta de cores', 'Paleta de cores usada para as séries do gráfico.'],
      [BASE_FORM_FIELD + 119, 'pt', 'Direção', 'Direção do gráfico de barras.'],
      [BASE_FORM_FIELD + 120, 'pt', 'Empilhado', 'Indica se o gráfico terá suas séries empilhadas.'],
      [BASE_FORM_FIELD + 121, 'pt', 'Preenchimento', 'Preenchimento do gráfico de pizza se 100%, senão donut.'],
      [BASE_FORM_FIELD + 122, 'pt', 'Largura da linha', 'Largura da linha.'],
      [BASE_FORM_FIELD + 123, 'pt', 'Tipo da linha', 'Tipo da linha.'],
      [BASE_FORM_FIELD + 124, 'pt', 'Modo para séries', 'Modo para séries.'],
    ]
 
    # Generalized regression
    # data.append([266, 'pt', 'Ligação (Link)', 'Ligação (Link)'])
    # data.append([267, 'pt', 'Ligação (Link)', 'Ligação (Link)'])
    # data.append([268, 'pt', 'Ligação (Link)', 'Ligação (Link)'])
    # data.append([280, 'pt', 'Ligação (Link)', 'Ligação (Link)'])

    # Linear regression 
    data.append([240, 'pt', 'Função de perda', 'Função de perda a ser otimizada.'])
    data.append([241, 'pt', 'Parâmetro de regularização (λ >= 0)', 'Parâmetro de regularização (λ)'])
    data.append([183, 'pt', 'Epsilon (usado se função de perda Huber)', 'Parâmetro que controla a robustez. Deve ser maior que 1.0.'])
    data.append([184, 'pt', 'Tolerância', 'Tolerância de convergência para algoritmo iterativo. Deve ser maior ou igual a 0.0.'])
    data.append([185, 'pt', 'Padronização (standardization)', 'Indica se é para padronizar os atributos preditivos antes de realizar o treino.'])
    data.append([175, 'pt', 'Fit intercept', 'Se desligado, define y-intercept igual a 0. Se ligado, y-intercept é determinado pela lina de melhor ajuste.'])



    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute(
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s or id IN (183,184,185,240,241,175)',
        BASE_FORM_FIELD, BASE_FORM_FIELD + 192)


def _insert_operation_operation_form(conn):
    tb = table('operation_operation_form',
                column('operation_id', Integer),
                column('operation_form_id', Integer))
    columns = [c.name for c in tb.columns]
    data = []
    # for i in list(range(2, 13)):
    #    for j in list(range(2, 4)):
    #        data.append([BASE_OP + i, BASE_FORM + j])

    ops_without_attributes_field = {
        ADD_BY_FORMULA, JOIN, SAMPLE, LIMIT, WINDOW_FUNCTION, SORT, FILTER,
        DATE_DIFF, GROUP, CLEAN_MISSING, CAST, READ_DATA, SELECT, RENAME, DUPLICATE,
        EXTRACT_FROM_ARRAY,SAVE, CONCAT_ROWS,
        SPLIT, EVALUATOR, FEATURES_REDUCTION, GRID, FEATURES, 
        K_MEANS_CLUSTERING, GAUSSIAN_MIXTURE_CLUSTERING, 
        DECISION_TREE_CLASSIFIER, GBT_CLASSIFIER, NAIVE_BAYES_CLASSIFIER, 
        PERCEPTRON_CLASSIFIER, RANDOM_FOREST_CLASSIFIER, 
        LOGISTIC_REGRESSION, SVM_CLASSIFICATION, 
        LINEAR_REGRESSION, ISOTONIC_REGRESSION, GBT_REGRESSOR, 
        RANDOM_FOREST_REGRESSOR, GENERALIZED_LINEAR_REGRESSOR, 
        DECISION_TREE_REGRESSOR,
    }
    ops_with_attribute_field = {
        DATE_DIFF, EXTRACT_FROM_ARRAY
    }
    ops_with_aliases_field = {
        #CAST, DELETE, REMOVE_MISSING, SORT, FILTER, GROUP, JOIN,
        #SAMPLE, LIMIT, WINDOW_FUNCTION
    }
    ops_with_alias_field = {
        DATE_DIFF,
    }
    #ops_without_keep_attribute_field = {
    #    CAST, RENAME, DELETE, ADD_BY_FORMULA, SORT, FILTER, GROUP,
    #    JOIN, SAMPLE, LIMIT, WINDOW_FUNCTION,
    #}
    # Common forms
    exclusions = set([
        K_MEANS_CLUSTERING, GAUSSIAN_MIXTURE_CLUSTERING, DECISION_TREE_CLASSIFIER, 
        GBT_CLASSIFIER, NAIVE_BAYES_CLASSIFIER, PERCEPTRON_CLASSIFIER, 
        RANDOM_FOREST_CLASSIFIER, LOGISTIC_REGRESSION, SVM_CLASSIFICATION, 
        LINEAR_REGRESSION, ISOTONIC_REGRESSION, GBT_REGRESSOR, 
        RANDOM_FOREST_REGRESSOR, GENERALIZED_LINEAR_REGRESSOR,
        DECISION_TREE_REGRESSOR])


    for op_id in set(ALL_OPS) - exclusions:
        #if op_id == SORT:
        #    import pdb; pdb.set_trace()
        if op_id not in ops_without_attributes_field:
            data.append([op_id,  ATTRIBUTES_FORM])
        if op_id in ops_with_aliases_field:
            data.append([op_id,  ALIASES_FORM])
        if op_id in ops_with_alias_field:
            data.append([op_id,  ALIAS_FORM])
        if op_id in ops_with_attribute_field:
            data.append([op_id, ATTRIBUTE_FORM])
        #if op_id not in ops_without_keep_attribute_field:
        #    data.append([op_id,  KEEP_ATTRIBUTE_FORM])
        data.append([op_id, APPEARANCE_FORM_ID])

    # import pdb; pdb.set_trace()
    # Each op form
    for op_id in set(ALL_OPS) - exclusions:
        data.append([op_id,  op_id + 50])

    # Associate form 26 (with Sample Op fields) to the Meta operation
    data.append([SAMPLE, 26])
    # Associate form 15 (with Aggregate Op fields) to the Meta operation
    data.append([GROUP, 15])
    # Associate form 20 (with CleanMissing Op fields) to the Meta operation
    data.append([CLEAN_MISSING, 20])
    # Associate form 154 (with Cast Op fields) to the Meta operation
    data.append([CAST, ORIGINAL_CAST_FORM])
    # Associate form 6 (with Select Op fields) to the Meta operation
    data.append([SELECT, ORIGINAL_SELECT_FORM])
    # Associate form 6 (with Save Op fields) to the Meta operation
    data.append([SAVE, ORIGINAL_SAVE_FORM])
    # Associate form 6 (with Join Op fields) to the Meta operation
    data.append([JOIN, ORIGINAL_JOIN_FORM])


    # Model builder
    model_builder_items = {K_MEANS_CLUSTERING: [27], GAUSSIAN_MIXTURE_CLUSTERING: [71], 
            DECISION_TREE_CLASSIFIER: [66], GBT_CLASSIFIER: [67], NAIVE_BAYES_CLASSIFIER: [64], 
            PERCEPTRON_CLASSIFIER: [68] , RANDOM_FOREST_CLASSIFIER: [65], LOGISTIC_REGRESSION: [34], 
            SVM_CLASSIFICATION: [9], GBT_REGRESSOR: [105], RANDOM_FOREST_REGRESSOR: [106], 
            ISOTONIC_REGRESSION: [103],LINEAR_REGRESSION: [8], GENERALIZED_LINEAR_REGRESSOR: [107],
            DECISION_TREE_REGRESSOR: [29]}

    for op_id, forms in model_builder_items.items():
        for form_id in forms:
            data.append([op_id, form_id])

    rows = [dict(list(zip(columns, row))) for row in data]

    rows.append({'operation_id': BASE_OP, 'operation_form_id': BASE_FORM_FIELD + 1})
    
    # print(set([r.get('operation_form_id') for r in rows]))

    op.bulk_insert(tb, rows)

def _delete_operation_operation_form(conn):
    conn.execute(
        '''DELETE FROM operation_operation_form
            WHERE operation_id BETWEEN %s and %s''',
        BASE_OP, max(ALL_OPS))


def _fixes(conn):
    conn.execute(
           """ INSERT INTO operation_form_field(id, name, type, required, `order`,
                suggested_widget, scope, enable_conditions, editable, form_id)
                VALUES(%s, 'invalid_values', 'TEXT', 0, 3, 'text', 'EXECUTION',
                'this.errors.internalValue === "move"', 1, %s)""",
                FIELD_CAST_ERROR_ATTRIBUTE,  ORIGINAL_CAST_FORM)
    dt = [
            {"en": "Array", "value": "Array", "key": "Array", "pt": "Array"},
            {"en": "Boolean", "value": "Boolean", "key": "Boolean", "pt": "Booleano (lógico)"},
            {"en": "Date", "value": "Date", "key": "Date", "pt": "Data"},
            {"en": "Decimal", "value": "Decimal", "key": "Decimal", "pt": "Decimal"},
            {"en": "Integer", "value": "Integer", "key": "Integer", "pt": "Inteiro"},
            {"en": "Time", "value": "Time", "key": "Time", "pt": "Hora"}]

    conn.execute("""update operation_form_field
        set `order`= 1, name = 'cast_attributes', `values`= %s where id = 585""", json.dumps(dt))
    conn.execute("update operation_form_field set `order`= 2 where id = 586")
    errors_options = [
            {"en": "Fail in case of invalid value", "value": "raise", "key": "raise",
                "pt": "Falhar em caso de valores inválidos"},
            {"en": "Coerce value (invalid become null)", "value": "coerce", "key": "coerce",
                "pt": "Forçar conversão (inválidos viram nulo)"},
            {"en": "Move invalid value to (new) attribute", "value": "move",
                "key": "move", "pt": "Mover valores inválidos para um novo atributo"}]
    conn.execute('update operation_form_field set `values` = %s, `default` = %s WHERE id = 586',
            json.dumps(errors_options), 'coerce')
    conn.execute("""
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(%s, 'pt', 'Novo atributo com valores inválidos', 'Novo atributo com valores inválidos.')""",
        FIELD_CAST_ERROR_ATTRIBUTE)
    conn.execute("""
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(%s, 'en', 'New atribute with invalid data', 'New atribute with invalid data.')""", FIELD_CAST_ERROR_ATTRIBUTE)

    # Select mode
    mode = [
            {"en": "Include attributes to the selection", "value": "include", "pt": "Incluir atributos à seleção", "key": 'include'},
            {"en": "Discard attributes from the selection", "value": "exclude", "pt": "Descartar atributos da seleção", "key": 'exclude'},
            {"en": "Select all and rename some attributes", "value": "rename", "pt": "Selecionar todos e renomear alguns atributos", "key": "rename"},
            {"en": "Select all and Duplicate some attributes", "value": "rename", "pt": "Selecionar todos e duplicar alguns atributos", "key": "duplicate"},
    ]
    conn.execute(
            """ INSERT INTO operation_form_field(id, name, type, required, `order`,
                suggested_widget, scope, enable_conditions, editable, form_id, `values`, `default`)
                VALUES(%s, 'mode', 'TEXT', 0, 0, 'dropdown',
                'EXECUTION', null, 1, %s, %s, 'include')""",
                FIELD_SELECT_MODE,  ORIGINAL_SELECT_FORM, json.dumps(mode))

    # Select with alias
    #conn.execute(
    #        """ INSERT INTO operation_form_field(id, name, type, required, `order`,
    #            suggested_widget, scope, enable_conditions, editable, form_id)
    #            VALUES(%s, 'attributes', 'TEXT', 1, 0, 'attribute-alias-selector',
    #            'EXECUTION', None, 1, %s)""",
    #            FIELD_SELECT_ALIAS,  ORIGINAL_SELECT_FORM)

    # Current select attribute field
    conn.execute("""update operation_form_field set suggested_widget = 'attribute-alias-selector',
            `order` = 2 where id = 6""")

    # Translations
    conn.execute("""
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(%s, 'pt', 'Modo de seleção', 'Modo de seleção (incluir ou excluir atributos).')""",
        FIELD_SELECT_MODE)
    conn.execute("""
        INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(%s, 'en', 'Selection mode', 'Selection mode (include or exclude attributes).')""", FIELD_SELECT_MODE)
#     conn.execute("""
#         INSERT INTO operation_form_field_translation(id, locale, label, help)
#         VALUES(%s, 'pt', 'Atributo(s)', 'Atributos a serem selecionados.')""",
#         FIELD_SELECT_ALIAS)
#     conn.execute("""
#         INSERT INTO operation_form_field_translation(id, locale, label, help)
#         VALUES(%s, 'en', 'Attribute(s)', 'Attributes to be selected.')""", FIELD_SELECT_ALIAS)
    conn.execute('ALTER TABLE operation_category ADD COLUMN subtype VARCHAR(200);');
    conn.execute("""
        INSERT INTO operation_category(id, type, subtype, `order`, default_order)
        VALUES (%s, %s, %s, %s, %s)""", [45, 'algorithm', 'regression', 0, 0])

    conn.execute("""
        INSERT INTO operation_category(id, type, subtype, `order`, default_order)
        VALUES (%s, %s, %s, %s, %s)""", [46, 'algorithm', 'clustering', 0, 0])
    conn.execute("""
        INSERT INTO operation_category_translation(id, locale, name)
        VALUES (%s, %s, %s)""", [45, 'pt', 'Regressão'])

    conn.execute("""
        INSERT INTO operation_category_translation(id, locale, name)
        VALUES (%s, %s, %s)""", [46, 'pt', 'Agrupamento'])
    conn.execute("""
        INSERT INTO operation_category_translation(id, locale, name)
        VALUES (%s, %s, %s)""", [45, 'en', 'Regression'])

    conn.execute("""
        INSERT INTO operation_category_translation(id, locale, name)
        VALUES (%s, %s, %s)""", [46, 'en', 'Clustering'])
    conn.execute("UPDATE operation_category set subtype = 'classification' where id = 4")

    # Generalized linear regressio
    # family = [
    #     {"en": "Gaussian", "key": "gaussian", "value": "Gaussian", "pt": "Gaussiano"}, 
    #     {"en": "Binomial", "key": "binomial", "value": "Binomial", "pt": "Binomial"}, 
    #     {"en": "Poisson", "key": "poisson", "value": "Poisson", "pt": "Poisson"}, 
    #     {"en": "Gamma", "key": "gamma", "value": "Gamma", "pt": "Gamma"},
    #     {"en": "Tweedie ", "key": "tweedie", "value": "Tweedie", "pt": "Tweedie"}
    # ]
    # conn.execute("""
    #     UPDATE operation_form_field SET `values` = %s WHERE id = 282 """, 
    #     json.dumps(family))
    conn.execute('DELETE FROM operation_form_field_translation WHERE id = 282')
    conn.execute('DELETE FROM operation_form_field WHERE id = 282')
    conn.execute("""UPDATE operation_form_field_translation SET 
            label = 'Família/predição de link',
            help = 'Família/predição de link' 
            where id = 283 and locale = 'pt'""")
    conn.execute("""UPDATE operation_form_field_translation SET 
            label = 'Family/link prediction' ,
            help = 'Family/link prediction' 
            where id = 283 and locale = 'en'""")
    link_pred = [
            {"en": "Binomial / logit", "key": "binomial:logit", "pt": "Binomial / logit"}, 
            {"en": "Binomial / probit", "key": "binomial:probit", "pt": "Binomial / probit"}, 
            {"en": "Binomial / cloglog", "key": "binomial:cloglog", "pt": "Binomial / cloglog"}, 
            {"en": "Gamma / inverse", "key": "gamma:inverse", "pt": "Gama / inversa"}, 
            {"en": "Gamma / identity", "key": "gamma:identity", "pt": "Gama / identidade"}, 
            {"en": "Gamma / log", "key": "gamma:log", "pt": "Gama / log"},
            {"en": "Gaussian / Identity", "key": "gaussian:identity", "pt": "Gaussiana / Identidade"}, 
            {"en": "Gaussian / log", "key": "gaussian:log", "pt": "Gaussiana / log"}, 
            {"en": "Gaussian / inverse", "key": "gaussian:inverse", "pt": "Gaussiana / inversa"}, 
            {"en": "Poisson / log", "key": "poisson:log", "pt": "Poisson / log (Poisson)"}, 
            {"en": "Poisson / identity", "key": "poisson:identity", "pt": "Poisson / identidade"}, 
            {"en": "Poisson / sqrt", "key": "poisson:sqrt", "pt": "Poisson / sqrt (raiz quadrada)"}, 
    ]
    conn.execute("update operation_form_field set name='family_link', `values` = %s where id = 283",
            json.dumps(link_pred))

    solver = [{"en": "IRLS (Iteratively reweighted least squares)", "key": "irls", "pt": "Mínimos quadrados reponderados iterativamente (IRLS)"}]
    conn.execute("update operation_form_field set `values` = %s where id = 285",
            json.dumps(solver))

    # Linear regression
    conn.execute('update operation_form_field set form_id = 8 where id in (245, 248)')
    conn.execute("update operation_form_field_translation set label = 'Mix para ElasticNet (0<=α<=1)' where id = 248 and locale='pt'")
    conn.execute("update operation_form_field_translation set label = 'ElasticNet mix (0<=α<=1)' where id = 248 and locale='en'")

def _undo_fixes(conn):
    conn.execute('DELETE FROM operation_form_field WHERE id = %s',
            FIELD_CAST_ERROR_ATTRIBUTE)
    conn.execute("update operation_form_field set name = 'attributes' where id = 585")

    errors_options = [
            {"en": "Coerce value (invalid become null)", "value": "coerce", "key": "coerce",
                "pt": "Forçar conversão (inválidos viram nulo)"},
            {"en": "Fail", "value": "raise", "key": "raise", "pt": "Falhar"},
            {"en": "Ignore value (may cause errors)", "value": "ignore",
                "key": "ignore", "pt": "Ignorar valor (pode causar erros)"}]
    conn.execute('update operation_form_field set `values` = %s WHERE id = 586',
            json.dumps(errors_options))
    conn.execute('DELETE FROM operation_form_field_translation WHERE id = %s',
            FIELD_CAST_ERROR_ATTRIBUTE)
    conn.execute('DELETE FROM operation_form_field WHERE id = %s',
            FIELD_CAST_ERROR_ATTRIBUTE)


    conn.execute("""update operation_form_field
        set `order`= 0, suggested_widget = 'attribute-selector' where id = 6""")

    conn.execute('DELETE FROM operation_form_field_translation WHERE id = %s',
            FIELD_SELECT_MODE)
    conn.execute('DELETE FROM operation_form_field WHERE id = %s',
            FIELD_SELECT_MODE)
    conn.execute('ALTER TABLE operation_category DROP COLUMN subtype');

    conn.execute('DELETE FROM operation_category_translation WHERE id in (45, 46);')
    conn.execute('DELETE FROM operation_category WHERE id in (45, 46);')

    # conn.execute('DELETE FROM operation_form_field_translation WHERE id = %s',
    #         FIELD_SELECT_ALIAS)
    # conn.execute('DELETE FROM operation_form_field WHERE id = %s',
    #         FIELD_SELECT_ALIAS)
    conn.execute('update operation_form_field set form_id = 102 where id in (245, 248)')

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
        _fixes,
        _insert_platform,
        _insert_platform_translation,
        'ALTER TABLE operation_translation ADD label_format VARCHAR(800)',
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
        """update operation_form_field set `values` = 
            replace(`values`, 'os primeiro ', 'os primeiros ')
            where id = 102;""",
        """update operation_form_field set `values` = 
        replace(`values`, 'Amostrar N registros a partir', 
        'Amostrar N registros aleatórios a partir')
        where id = 102;""",
    ]
    try:
        for cmd in commands:
            _execute(conn, cmd)
    except Exception as e:
        pass
        print(e)
        import traceback
        traceback.print_exc()
        session.rollback()
        # raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    conn = session.connection()

    # Remove it if your DB doesn't support disabling FK checks
    conn.execute('SET FOREIGN_KEY_CHECKS=0;')
    commands = [
        _undo_fixes,
        _delete_platform,
        _delete_platform_translation,
        'ALTER TABLE operation_translation DROP COLUMN label_format',
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
