"""new_alg_clust

Revision ID: a7c44fb9bc18 
Revises: 843451bc6ee4
"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
from sqlalchemy.sql.sqltypes import UnicodeText

# revision identifiers, used by Alembic.
revision = 'a7c44fb9bc18'
down_revision = '843451bc6ee4'
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
BASE_OP = 2252
BASE_CATEGORY = 2236
BASE_FORM_FIELD = 2259

# Model builder
# Uses READ_DATA, SAMPLE

#Power Iteration Clustering(PIC)
PIC_CLUSTERING = BASE_OP + 1
#Latent Dirichlet allocation (LDA)
LDA_CLUSTERING = BASE_OP +2 
#Bisecting k-means (BKM)
BKM_CLUSTERING = BASE_OP + 3


PIC_CLUSTERING_FORM = 2243
LDA_CLUSTERING_FORM = 2244
BKM_CLUSTERING_FORM = 2245

CAT_CLASSIFICATION = 4
CAT_REGRESSION = 47
CAT_CLUSTERING = 46
CAT_MODEL_BUILDER = 2113

ORIGINAL_SAVE_FORM = 28

ALL_OPS = [
    # New ML algorithms
    PIC_CLUSTERING, LDA_CLUSTERING,
    BKM_CLUSTERING
]

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
      [PIC_CLUSTERING, 'pic_clustering', 1, 'TRANSFORMATION', '', '', ''],
      [LDA_CLUSTERING, 'lda_clustering', 1, 'TRANSFORMATION', '', '', ''],
      [BKM_CLUSTERING, 'bkm_clustering', 1, 'TRANSFORMATION', '', '', ''],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation(conn):
    execute(conn, 
        'DELETE from operation WHERE id BETWEEN %s AND %s',
        BASE_OP + 1, max(ALL_OPS))

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
      [PIC_CLUSTERING, 'pt', 'Power Iteration Clustering', 'Agrupamento de iteração de energia.', ''],
      [LDA_CLUSTERING, 'pt', 'Latent Dirichlet allocation', 'Alocação latente de Dirichlet.', ''],
      [BKM_CLUSTERING, 'pt', 'Bisecting k-means', 'Bissecção Kmeans.', ''],

      [PIC_CLUSTERING, 'en', 'Power Iteration Clustering', 'Agrupamento de iteração de energia.', ''],
      [LDA_CLUSTERING, 'en', 'Latent Dirichlet allocation', 'Alocação latente de Dirichlet.', ''],
      [BKM_CLUSTERING, 'en', 'Bisecting k-means', 'Bissecção Kmeans.', ''],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_translation(conn):
    execute(conn, 
        'DELETE from operation_translation WHERE id BETWEEN %s AND %s',
        BASE_OP + 1, max(ALL_OPS))

def _insert_operation_form(conn):
    tb = table('operation_form',
                column('id', Integer),
                column('enabled', Boolean),
                column('order', Integer),
                column('category', String))
    columns = [c.name for c in tb.columns]
    data = [
      [PIC_CLUSTERING_FORM, 1, 1, 'execution'], 
      [LDA_CLUSTERING_FORM, 1, 1, 'execution'],
      [BKM_CLUSTERING_FORM, 1, 1, 'execution'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form(conn):
    execute(conn, 
        'DELETE from operation_form WHERE id BETWEEN %s AND %s',
        PIC_CLUSTERING_FORM, BKM_CLUSTERING_FORM)

def _insert_operation_form_translation(conn):
    tb = table('operation_form_translation',
                column('id', Integer),
                column('locale', String),
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [PIC_CLUSTERING_FORM, 'pt', 'Execução'], 
      [PIC_CLUSTERING_FORM, 'en', 'Execution'],

      [LDA_CLUSTERING_FORM, 'pt', 'Execução'],
      [LDA_CLUSTERING_FORM, 'en', 'Execution'],

      [BKM_CLUSTERING_FORM, 'pt', 'Execução'],
      [BKM_CLUSTERING_FORM, 'en', 'Execution'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_translation(conn):
    execute(conn, 
        'DELETE from operation_form_translation WHERE id BETWEEN %s AND %s',
        PIC_CLUSTERING_FORM, BKM_CLUSTERING_FORM)
    
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
    [BASE_FORM_FIELD + 1, 'number_of_clusters', 'INTEGER', True, 1, None, 'integer', None, None, 'EXECUTION', None, True, PIC_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 2, 'init_mode', 'TEXT', False, 2, None, 'dropdown', None, '[{"key": "random", "value": "random"}, {"key": "degree", "value": "degree"}]', 'EXECUTION', None, True, PIC_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 3, 'max_iterations', 'INTEGER', False, 3, None, 'integer', None, None, 'EXECUTION', None, True, PIC_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 4, 'weight_col', 'TEXT', False, 4, None, 'text', None, None, 'EXECUTION', None, True, PIC_CLUSTERING_FORM],
    
    [BASE_FORM_FIELD + 5, 'number_of_clusters', 'INTEGER', True, 1, None, 'integer', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 6, 'max_iterations', 'INTEGER', False, 2, None, 'integer', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 7, 'weight_col', 'TEXT', False, 3, None, 'text', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 8, 'features', 'TEXT', False, 4, None, 'text', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 9, 'seed', 'INTEGER', False, 5, None, 'integer', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 10, 'checkpoint_interval', 'INTEGER', False, 6, None, 'integer', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 11, 'optimizer', 'TEXT', False, 7, None, 'dropdown', None, '[{"key": "online", "value": "online"}]', 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 12, 'learning_offset', 'FLOAT', False, 8, None, 'decimal', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 13, 'learning_decay', 'FLOAT', False, 9, None, 'decimal', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 14, 'subsampling_rate', 'TEXT', False, 10, None, 'text', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 15, 'optimize_doc_concentration', 'INTEGER', False, 11, None, 'checkbox', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 16, 'doc_concentration', 'FLOAT', False, 12, None, 'decimal', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 17, 'topic_concentration', 'FLOAT', False, 13, None, 'decimal', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 18, 'topic_distribution_col', 'TEXT', False, 14, None, 'text', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 19, 'keep_last_checkpoint', 'INTEGER', False, 15, None, 'checkbox', None, None, 'EXECUTION', None, True, LDA_CLUSTERING_FORM],
    
    [BASE_FORM_FIELD + 20, 'number_of_clusters', 'INTEGER', True, 16, None, 'integer', None, None, 'EXECUTION', None, True, BKM_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 21, 'tolerance', 'FLOAT', 0, 17, None, 'decimal', None, None, 'EXECUTION', None, 1, BKM_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 22, 'max_iterations', 'INTEGER', False, 18, None, 'integer', None, None, 'EXECUTION', None, True, BKM_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 23, 'seed', 'INTEGER', False, 19, None, 'integer', None, None, 'EXECUTION', None, True, BKM_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 24, 'min_divisible_clusterSize', 'FLOAT', 0, 20, None, 'decimal', None, None, 'EXECUTION', None, True, BKM_CLUSTERING_FORM],
    [BASE_FORM_FIELD + 25, 'distance', 'TEXT', False, 21, 'euclidean', 'dropdown', None, '[{"key": "euclidean", "value": "Euclidean"},', 'EXECUTION', 27, True, BKM_CLUSTERING_FORM],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _delete_operation_form_field(conn):
    execute(conn,
        'DELETE from operation_form_field WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 25)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
    [BASE_FORM_FIELD + 1, 'en', 'Number of Clusters', 'Number of clusters in the LDA model'],
    [BASE_FORM_FIELD + 1, 'pt', 'Número de Clusters', 'Número de clusters no modelo LDA'],

    [BASE_FORM_FIELD + 2, 'en', 'Initialization Mode', 'Initialization mode for the LDA model'],
    [BASE_FORM_FIELD + 2, 'pt', 'Modo de Inicialização', 'Modo de inicialização para o modelo LDA'],

    [BASE_FORM_FIELD + 3, 'en', 'Max Iterations', 'Maximum number of iterations for the LDA model'],
    [BASE_FORM_FIELD + 3, 'pt', 'Número Máximo de Iterações', 'Número máximo de iterações para o modelo LDA'],

    [BASE_FORM_FIELD + 4, 'en', 'Weight Column', 'Column containing weights for the LDA model'],
    [BASE_FORM_FIELD + 4, 'pt', 'Coluna de Peso', 'Coluna contendo pesos para o modelo LDA'],

    [BASE_FORM_FIELD + 5, 'en', 'Number of Clusters', 'Number of clusters in the LDA clustering model'],
    [BASE_FORM_FIELD + 5, 'pt', 'Número de Clusters', 'Número de clusters no modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 6, 'en', 'Max Iterations', 'Maximum number of iterations for the LDA clustering model'],
    [BASE_FORM_FIELD + 6, 'pt', 'Número Máximo de Iterações', 'Número máximo de iterações para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 7, 'en', 'Weight Column', 'Column containing weights for the LDA clustering model'],
    [BASE_FORM_FIELD + 7, 'pt', 'Coluna de Peso', 'Coluna contendo pesos para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 8, 'en', 'Features', 'Features column for the LDA clustering model'],
    [BASE_FORM_FIELD + 8, 'pt', 'Recursos', 'Coluna de recursos para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 9, 'en', 'Seed', 'Seed for random numbers in the LDA clustering model'],
    [BASE_FORM_FIELD + 9, 'pt', 'Semente', 'Semente para números aleatórios no modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 10, 'en', 'Checkpoint Interval', 'Checkpoint interval for the LDA clustering model'],
    [BASE_FORM_FIELD + 10, 'pt', 'Intervalo de Ponto de Verificação', 'Intervalo de ponto de verificação para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 11, 'en', 'Optimizer', 'Optimizer for the LDA clustering model'],
    [BASE_FORM_FIELD + 11, 'pt', 'Otimizador', 'Otimizador para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 12, 'en', 'Learning Offset', 'Learning offset for the LDA clustering model'],
    [BASE_FORM_FIELD + 12, 'pt', 'Aprendizado Offset', 'Offset de aprendizado para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 13, 'en', 'Learning Decay', 'Learning decay for the LDA clustering model'],
    [BASE_FORM_FIELD + 13, 'pt', 'Decaimento do Aprendizado', 'Decaimento do aprendizado para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 14, 'en', 'Subsampling Rate', 'Subsampling rate for the LDA clustering model'],
    [BASE_FORM_FIELD + 14, 'pt', 'Taxa de Subamostragem', 'Taxa de subamostragem para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 15, 'en', 'Optimize Doc Concentration', 'Optimize document concentration for the LDA clustering model'],
    [BASE_FORM_FIELD + 15, 'pt', 'Otimizar Concentração do Documento', 'Otimizar concentração do documento para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 16, 'en', 'Doc Concentration', 'Document concentration for the LDA clustering model'],
    [BASE_FORM_FIELD + 16, 'pt', 'Concentração do Documento', 'Concentração do documento para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 17, 'en', 'Topic Concentration', 'Topic concentration for the LDA clustering model'],
    [BASE_FORM_FIELD + 17, 'pt', 'Concentração do Tópico', 'Concentração do tópico para o modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 18, 'en', 'Topic Distribution Column', 'Column for topic distribution in the LDA clustering model'],
    [BASE_FORM_FIELD + 18, 'pt', 'Coluna de Distribuição de Tópicos', 'Coluna para distribuição de tópicos no modelo de agrupamento LDA'],

    [BASE_FORM_FIELD + 19, 'en', 'Keep Last Checkpoint', 'Keep the last checkpoint for the LDA clustering model'],
    [BASE_FORM_FIELD + 19, 'pt', 'Manter Último Ponto de Verificação', 'Manter o último ponto de verificação para o modelo de agrupamento LDA'],


    [BASE_FORM_FIELD + 20, 'en', 'Number of Clusters', 'Number of clusters in the Bisecting k-means model'],
    [BASE_FORM_FIELD + 20, 'pt', 'Número de Clusters', 'Número de clusters no modelo Bisecting k-means '],

    [BASE_FORM_FIELD + 21, 'en', 'Tolerance', 'Convergency tolerance for the within-cluster sums of point-to-centroid distances.'],
    [BASE_FORM_FIELD + 21, 'pt', 'Tolerância', 'Tolerância de convergência para as somas das distâncias intra-cluster do ponto ao centroide.'],
    
    [BASE_FORM_FIELD + 22, 'en', 'Max Iterations', 'Max iterations'],
    [BASE_FORM_FIELD + 22, 'pt', 'Número Máximo de Iterações', 'Número máx. de iterações'],

    [BASE_FORM_FIELD + 23, 'en', 'Seed', 'Seed'],
    [BASE_FORM_FIELD + 23, 'pt', 'Semente (seed)', 'Semente (seed).'],

    [BASE_FORM_FIELD + 24, 'en', 'Min Divisible Cluster Size', 'Minimum size allowed for a cluster to be split during the hierarchical partitioning process.'],
    [BASE_FORM_FIELD + 24, 'pt', 'Tamanho mínimo do cluster divisível', 'Tamanho mínimo permitido para um cluster ser dividido durante o processo de particionamento hierárquico.'],
    
    [BASE_FORM_FIELD + 25, 'en', 'Distance Measure', 'The distance measure'],
    [BASE_FORM_FIELD + 25, 'pt', 'Medida de distância', 'A medida de distância'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    execute(conn,
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 25)

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
                column('operation_id', Integer),
                column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [PIC_CLUSTERING, CAT_MODEL_BUILDER],
      [PIC_CLUSTERING, CAT_CLUSTERING],
      [LDA_CLUSTERING, CAT_MODEL_BUILDER],
      [LDA_CLUSTERING, CAT_CLUSTERING],
      [BKM_CLUSTERING, CAT_MODEL_BUILDER],
      [BKM_CLUSTERING, CAT_CLUSTERING],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_operation(conn):
    execute(conn, 
        '''DELETE FROM operation_category_operation
            WHERE operation_id BETWEEN %s and %s ''',
        BASE_OP, MAX_OP)

def _insert_operation_operation_form(conn):
    tb = table('operation_operation_form',
                column('operation_id', Integer),
                column('operation_form_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [PIC_CLUSTERING, PIC_CLUSTERING_FORM],
        [LDA_CLUSTERING, LDA_CLUSTERING_FORM],
        [BKM_CLUSTERING, BKM_CLUSTERING_FORM]
    ]
    
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _delete_operation_operation_form(conn):
    execute(conn, 
        '''DELETE FROM operation_operation_form
            WHERE operation_form_id IN (%s, %s)''',
        PIC_CLUSTERING_FORM, LDA_CLUSTERING_FORM, BKM_CLUSTERING_FORM)

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
        PIC_CLUSTERING, BKM_CLUSTERING)

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
