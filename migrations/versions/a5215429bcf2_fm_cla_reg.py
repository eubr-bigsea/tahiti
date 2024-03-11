"""fm_cla_reg

Revision ID: a5215429bcf2 
Revises: c1bbd1bb8f85
"""
import json
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText
from tahiti.migration_utils import is_sqlite, is_mysql


# revision identifiers, used by Alembic.
revision = 'a5215429bcf2'
down_revision = 'c1bbd1bb8f85'
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

BASE_PLATFORM = 2236
BASE_OP = 2236
BASE_FORM = 2236
BASE_FORM_FIELD = 2237

# Model builder
# Uses READ_DATA, SAMPLE

FM_CLASSIFIER = BASE_OP + 9

FM_REGRESSION = BASE_OP + 10

FM_CLASSIFIER_FORM = 2236
FM_REGRESSION_FORM = 2237

CAT_CLASSIFICATION = 4
CAT_REGRESSION = 47
CAT_CLUSTERING = 46
CAT_MODEL_BUILDER = 2113

ORIGINAL_SAVE_FORM = 28

ALL_OPS = [
    # New ML algorithms
    FM_CLASSIFIER, FM_REGRESSION,
]

ATTRIBUTES_FORM = BASE_FORM + 2
ALIASES_FORM = BASE_FORM + 3
KEEP_ATTRIBUTE_FORM = BASE_FORM + 4
ATTRIBUTE_FORM = BASE_FORM + 5
ALIAS_FORM = BASE_FORM + 6

MAX_OP = max(ALL_OPS)

def execute(conn, cmd, *params):
    if is_sqlite():
        cmd2 = cmd.replace('%s', '?')
    else:
        cmd2 = cmd
    conn.execute(cmd2, *params)

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
      [FM_CLASSIFIER, 'fm-classifier', 1, 'TRANSFORMATION', '', '', ''],
      [FM_REGRESSION, 'fm-regression', 1, 'TRANSFORMATION', '', '', ''],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation(conn):
    execute(conn, 
        'DELETE from operation WHERE id BETWEEN %s AND %s',
        BASE_OP, max(ALL_OPS))

def _insert_operation_translation(conn):
    tb = table('operation_translation',
                column('id', Integer),
                column('locale', String),
                column('name', String),
                column('description', String),
                )
    columns = [c.name for c in tb.columns]
    data = [
      [FM_CLASSIFIER, 'pt', 'Classificador Factorization Machines', 'Classificador Factorization machines.',],
      [FM_REGRESSION, 'pt', 'Regressão Factorization Machines', 'Regressão Factorization machines.',],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_translation(conn):
    execute(conn, 
        'DELETE from operation_translation WHERE id BETWEEN %s AND %s',
        BASE_OP, max(ALL_OPS))

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
    ]
    exclusions = set([FM_CLASSIFIER,FM_REGRESSION])

    for op_id in set(ALL_OPS) - exclusions: # Operations' form
        data.append([op_id + 50, 1, 1, 'execution'])

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form(conn):
    execute(conn, 
        'DELETE from operation_form WHERE id BETWEEN %s AND %s',
        BASE_FORM, BASE_FORM+1)

def _insert_operation_form_translation(conn):
    tb = table('operation_form_translation',
                column('id', Integer),
                column('locale', String),
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM, 'pt', 'Execução'], # Common form to all ops
      [BASE_FORM + 1, 'pt', 'Execução'],

      [BASE_FORM, 'en', 'Execution'],
      [BASE_FORM + 1, 'en', 'Execution'],
    ]
    exclusions = set([FM_REGRESSION, FM_CLASSIFIER])

    for op_id in set(ALL_OPS) - exclusions: # Operations' form
        data.append([op_id + 50, 'pt', 'Execução'])
        data.append([op_id + 50, 'en', 'Execution'])

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_translation(conn):
    execute(conn, 
        'DELETE from operation_form_translation WHERE id BETWEEN %s AND %s',
        BASE_FORM, BASE_FORM + 1)
    
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
	[BASE_FORM_FIELD + 1, 'factor_size', 'INTEGER', False,  0,  None, 'integer',  None,  None,  'EXECUTION',  None,  True, FM_CLASSIFIER_FORM],
        [BASE_FORM_FIELD + 2, 'fit_linear', 'INTEGER', False, 1, None, 'checkbox',  None, None, 'EXECUTION', None, True, FM_CLASSIFIER_FORM],
        [BASE_FORM_FIELD + 3, 'reg_param', 'FLOAT', False, 6, None, 'decimal', None, None, 'EXECUTION', None, True, FM_CLASSIFIER_FORM],
        [BASE_FORM_FIELD + 4, 'min_batch', 'FLOAT', False, 2, None, 'decimal', None, None, 'EXECUTION', None, True, FM_CLASSIFIER_FORM],
        [BASE_FORM_FIELD + 5, 'init_std', 'FLOAT', False, 3, None, 'decimal', None, None, 'EXECUTION', None, True, FM_CLASSIFIER_FORM],
        [BASE_FORM_FIELD + 6,'max_iter', 'INTEGER', False, 3, '10', 'integer', None, None, 'EXECUTION', None, True, FM_CLASSIFIER_FORM],
        [BASE_FORM_FIELD + 7, 'step_size', 'INTEGER', False, 5, None, 'integer', None, None, 'EXECUTION', None, True, FM_CLASSIFIER_FORM],
        [BASE_FORM_FIELD + 8, 'tolerance', 'FLOAT', False, 1, '0.0001', 'decimal', None, None, 'EXECUTION', None, True, FM_CLASSIFIER_FORM],
        [BASE_FORM_FIELD + 9, 'solver', 'TEXT', False, 4, None, 'dropdown', None, '[{"key": "adamW", "value": "adamW"}, {"key": "gd", "value": "gd"}]', 'EXECUTION', None, True, FM_CLASSIFIER_FORM],
        [BASE_FORM_FIELD + 10, 'seed', 'INTEGER', False, 0, None, 'integer', None, None, 'EXECUTION',  None, True, FM_CLASSIFIER_FORM],
        [BASE_FORM_FIELD + 11, 'threshold', 'FLOAT', False, 3, None, 'decimal', None, None, 'EXECUTION', None, True, FM_CLASSIFIER_FORM] ,

        [BASE_FORM_FIELD + 12, 'factor_size', 'INTEGER', False,  0,  None, 'integer',  None,  None,  'EXECUTION',  None,  True, FM_REGRESSION_FORM],
        [BASE_FORM_FIELD + 13, 'fit_linear', 'INTEGER', False, 1, None, 'checkbox',  None, None, 'EXECUTION', None, True, FM_REGRESSION_FORM],
        [BASE_FORM_FIELD + 14, 'reg_param', 'FLOAT', False, 6, None, 'decimal', None, None, 'EXECUTION', None, True, FM_REGRESSION_FORM],
        [BASE_FORM_FIELD + 15, 'min_batch', 'FLOAT', False, 2, None, 'decimal', None, None, 'EXECUTION', None, True, FM_REGRESSION_FORM],
        [BASE_FORM_FIELD + 16, 'init_std', 'FLOAT', False, 3, None, 'decimal', None, None, 'EXECUTION', None, True, FM_REGRESSION_FORM],
        [BASE_FORM_FIELD + 17,'max_iter', 'INTEGER', False, 3, '10', 'integer', None, None, 'EXECUTION', None, True, FM_REGRESSION_FORM],
        [BASE_FORM_FIELD + 18, 'step_size', 'INTEGER', False, 5, None, 'integer', None, None, 'EXECUTION', None, True, FM_REGRESSION_FORM],
        [BASE_FORM_FIELD + 19, 'tolerance', 'FLOAT', False, 1, '0.0001', 'decimal', None, None, 'EXECUTION', None, True, FM_REGRESSION_FORM],
        [BASE_FORM_FIELD + 20, 'solver', 'TEXT', False, 4, None, 'dropdown', None, '[{"key": "adamW", "value": "adamW"}, {"key": "gd", "value": "gd"}]', 'EXECUTION', None, True, FM_REGRESSION_FORM],
        [BASE_FORM_FIELD + 21, 'seed', 'INTEGER', False, 0, None, 'integer', None, None, 'EXECUTION', None, True, FM_REGRESSION_FORM],
        [BASE_FORM_FIELD + 22, 'threshold', 'FLOAT', False, 3, None, 'decimal', None, None, 'EXECUTION', None, True, FM_REGRESSION_FORM],

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_form_field(conn):
    execute(conn,
        'DELETE from operation_form_field WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 22)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_FORM_FIELD + 1, 'en', 'Factor Size', 'Size of the factorization'],
        [BASE_FORM_FIELD + 1, 'pt', 'Tamanho do Fator (factor size)', 'Tamanho da fatoração'],
    
        [BASE_FORM_FIELD + 2, 'en', 'Fit Linear', 'Whether to fit a linear term'],
        [BASE_FORM_FIELD + 2, 'pt', 'Ajustar Linear (fit linear)', 'Se deve ajustar um termo linear'],

        [BASE_FORM_FIELD + 3, 'en', 'Regularization Parameter', 'Regularization parameter (λ >= 0)'],
        [BASE_FORM_FIELD + 3, 'pt', 'Parâmetro de Regularização', 'Parâmetro de regularização (λ >= 0)'],

        [BASE_FORM_FIELD + 4, 'en', 'Mini-Batch Fraction', 'Fraction of data to be used for each SGD iteration'],
        [BASE_FORM_FIELD + 4, 'pt', 'Fração do Mini-Batch (mini-batch fraction)', 'Fração dos dados a ser usada para cada iteração SGD'],

        [BASE_FORM_FIELD + 5, 'en', 'Initialization Standard Deviation', 'Standard deviation for weight initialization'],
        [BASE_FORM_FIELD + 5, 'pt', 'Desvio Padrão da Inicialização', 'Desvio padrão para a inicialização dos pesos'],

        [BASE_FORM_FIELD + 6, 'en', 'Maximum Iterations', 'Maximum number of iterations'],
        [BASE_FORM_FIELD + 6, 'pt', 'Número Máximo de Iterações', 'Número máximo de iterações'],

        [BASE_FORM_FIELD + 7, 'en', 'Step Size', 'Step size for optimization'],
        [BASE_FORM_FIELD + 7, 'pt', 'Tamanho do Passo (step size)', 'Tamanho do passo para otimização'],

        [BASE_FORM_FIELD + 8, 'en', 'Tolerance', 'Convergence tolerance'],
        [BASE_FORM_FIELD + 8, 'pt', 'Tolerância (Tolerance)', 'Tolerância de convergência'],

        [BASE_FORM_FIELD + 9, 'en', 'Solver', 'Optimization solver'],
        [BASE_FORM_FIELD + 9, 'pt', 'Solver', 'Solver de otimização'],

        [BASE_FORM_FIELD + 10, 'en', 'Seed for random numbers', 'Seed for random numbers'],
        [BASE_FORM_FIELD + 10, 'pt', 'Semente para números aleatórios', 'Semente para números aleatórios'],

        [BASE_FORM_FIELD + 11, 'en', 'Threshold', 'Threshold for binary classification'],
        [BASE_FORM_FIELD + 11, 'pt', 'Limiar (threshold)', 'Limiar para classificação binária'],

        [BASE_FORM_FIELD + 12, 'en', 'Factor Size', 'Size of the factorization'],
        [BASE_FORM_FIELD + 12, 'pt', 'Tamanho do Fator (factor size)', 'Tamanho da fatoração'],
    
        [BASE_FORM_FIELD + 13, 'en', 'Fit Linear', 'Whether to fit a linear term'],
        [BASE_FORM_FIELD + 13, 'pt', 'Ajustar Linear (fit linear)', 'Se deve ajustar um termo linear'],

        [BASE_FORM_FIELD + 14, 'en', 'Regularization Parameter', 'Regularization parameter (λ >= 0)'],
        [BASE_FORM_FIELD + 14, 'pt', 'Parâmetro de Regularização', 'Parâmetro de regularização (λ >= 0)'],

        [BASE_FORM_FIELD + 15, 'en', 'Mini-Batch Fraction', 'Fraction of data to be used for each SGD iteration'],
        [BASE_FORM_FIELD + 15, 'pt', 'Fração do Mini-Batch (mini-batch fraction)', 'Fração dos dados a ser usada para cada iteração SGD'],

        [BASE_FORM_FIELD + 16, 'en', 'Initialization Standard Deviation', 'Standard deviation for weight initialization'],
        [BASE_FORM_FIELD + 16, 'pt', 'Desvio Padrão da Inicialização', 'Desvio padrão para a inicialização dos pesos'],

        [BASE_FORM_FIELD + 17, 'en', 'Maximum Iterations', 'Maximum number of iterations'],
        [BASE_FORM_FIELD + 17, 'pt', 'Número Máximo de Iterações', 'Número máximo de iterações'],

        [BASE_FORM_FIELD + 18, 'en', 'Step Size', 'Step size for optimization'],
        [BASE_FORM_FIELD + 18, 'pt', 'Tamanho do Passo (step size)', 'Tamanho do passo para otimização'],

        [BASE_FORM_FIELD + 19, 'en', 'Tolerance', 'Convergence tolerance'],
        [BASE_FORM_FIELD + 19, 'pt', 'Tolerância (Tolerance)', 'Tolerância de convergência'],

        [BASE_FORM_FIELD + 20, 'en', 'Solver', 'Optimization solver'],
        [BASE_FORM_FIELD + 20, 'pt', 'Solver', 'Solver de otimização'],

        [BASE_FORM_FIELD + 21, 'en', 'Seed for random numbers', 'Seed for random numbers'],
        [BASE_FORM_FIELD + 21, 'pt', 'Semente para números aleatórios', 'Semente para números aleatórios'],

        [BASE_FORM_FIELD + 22, 'en', 'Threshold', 'Threshold for binary classification'],
        [BASE_FORM_FIELD + 22, 'pt', 'Limiar (threshold)', 'Limiar para classificação binária']

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    execute(conn,
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 22)

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
                column('operation_id', Integer),
                column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [FM_CLASSIFIER, CAT_MODEL_BUILDER],
      [FM_CLASSIFIER, CAT_CLASSIFICATION],
      [FM_REGRESSION, CAT_MODEL_BUILDER],
      [FM_REGRESSION, CAT_REGRESSION],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_operation(conn):
    execute(conn, 
        '''DELETE FROM operation_category_operation
            WHERE operation_id BETWEEN %s and %s ''',
        BASE_OP, MAX_OP)
#corrigir
def _insert_operation_operation_form(conn):
    tb = table('operation_operation_form',
                column('operation_id', Integer),
                column('operation_form_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [FM_CLASSIFIER, BASE_FORM],
        [FM_REGRESSION, BASE_FORM + 1]
    ]
    
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _delete_operation_operation_form(conn):
    execute(conn, 
        '''DELETE FROM operation_operation_form
            WHERE operation_form_id IN (%s, %s)''',
        FM_CLASSIFIER_FORM, FM_REGRESSION_FORM)

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
    execute(conn, 
        '''DELETE FROM operation_platform
            WHERE operation_id BETWEEN %s and %s''',
        BASE_OP, MAX_OP)

# -------------------------------------------------------

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
        _insert_operation,
        _insert_operation_translation,
        _insert_operation_form,
        _insert_operation_form_translation,
        _insert_operation_form_field,
        _insert_operation_form_field_translation,
        _insert_operation_category_operation,
        _insert_operation_operation_form,
        _insert_operation_platform,
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
    if is_mysql():
        conn.execute('SET FOREIGN_KEY_CHECKS=0;')
    commands = [
        _delete_operation,
        _delete_operation_translation,
        _delete_operation_form,
        _delete_operation_form_translation,
        _delete_operation_form_field,
        _delete_operation_form_field_translation,
        _delete_operation_category_operation,
        _delete_operation_operation_form,
        _delete_operation_platform,
    ]

    try:
        for cmd in reversed(commands):
            _execute(conn, cmd)
    except:
        session.rollback()
        raise
    # Remove it if your DB doesn't support disabling FK checks
    if is_mysql():
        conn.execute('SET FOREIGN_KEY_CHECKS=1;')
    session.commit()
