# -*- coding: utf-8 -*-

"""Updating K-Means form fields (scikit_learn).

Revision ID: 2b87a7f6e8fb
Revises: c0510936c9a5
Create Date: 2020-01-22 10:23:47.784022

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
revision = '2b87a7f6e8fb'
down_revision = 'c0510936c9a5'
branch_labels = None
depends_on = None


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        #Flatten - data_format
        (4033, 41),  #appearance
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
        column('form_id', Integer),
        column('enable_conditions', String),
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')

    enable_condition = 'this.type.internalValue === "K-Means"'
    enable_condition2 = 'this.type.internalValue === "Mini-Batch K-Means"'

    data = [
        #Flatten - data_format
        (4301, 'n_init', 'INTEGER', 0, 8, 10, 'integer', None,  None, 'EXECUTION', 4013, enable_condition),
        (4302, 'n_init_mb', 'INTEGER', 0, 10, 3, 'integer', None,  None, 'EXECUTION', 4013, enable_condition2),
        (4303, 'precompute_distances', 'TEXT', 0, 9, 'auto', 'dropdown', None,
         json.dumps([
             {'key': 'auto', 'value': 'auto'},
             {'key': 'true', 'value': 'True'},
             {'key': 'false', 'value': 'False'},
         ]),
         'EXECUTION', 4013, enable_condition),
        (4304, 'verbose', 'INTEGER', 0, 7, 0, 'integer', None,  None, 'EXECUTION', 4013, None),
        (4305, 'copy_x', 'INTEGER', 0, 11, 1, 'integer', None,  None, 'EXECUTION', 4013, enable_condition),
        (4306, 'n_jobs', 'INTEGER', 0, 12, None, 'integer', None,  None, 'EXECUTION', 4013, enable_condition),
        (4307, 'algorithm', 'TEXT', 0, 13, 'auto', 'dropdown', None,
         json.dumps([
             {'key': 'auto', 'value': 'auto'},
             {'key': 'full', 'value': 'full'},
             {'key': 'elkan', 'value': 'elkan'},
         ]),
         'EXECUTION', 4013, enable_condition),
        (4308, 'batch_size', 'INTEGER', 0, 14, 100, 'integer', None,  None, 'EXECUTION', 4013, enable_condition2),
        (4309, 'compute_labels', 'INTEGER', 0, 15, 1, 'integer', None,  None, 'EXECUTION', 4013, enable_condition2),
        (4310, 'tol', 'DECIMAL', 0, 16, 0.0, 'decimal', None,  None, 'EXECUTION', 4013, enable_condition2),
        (4311, 'max_no_improvement', 'INTEGER', 0, 17, 10, 'integer', None,  None, 'EXECUTION', 4013, enable_condition2),
        (4312, 'init_size', 'INTEGER', 0, 18, None, 'integer', None,  None, 'EXECUTION', 4013, enable_condition2),
        (4313, 'reassignment_ratio', 'DECIMAL', 0, 19, 0.01, 'decimal', None,  None, 'EXECUTION', 4013,
         enable_condition2),
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
        #Flatten - data_format
        (4301, 'en', 'Number of initializations', 'Number of time the k-means algorithm will be run with different'
                                                  ' centroid seeds.'),
        (4301, 'pt', 'Número de inicializações', 'Número de vezes que o algoritmo k-means será executado com diferentes'
                                                 ' sementes de centróide.'),

        (4302, 'en', 'Number of initializations', 'Number of random initializations that are tried.'),
        (4302, 'pt', 'Número de inicializações', 'Número de inicializações aleatórias que são tentadas.'),

        (4303, 'en', 'Precompute distances', 'Precompute distances (faster but takes more memory).'),
        (4303, 'pt', 'Pré-computar distâncias', 'Distância pré-calculada (mais rápido, mas consome mais memória).'),

        (4304, 'en', 'Verbose', 'Verbosity mode.'),
        (4304, 'pt', 'Verbose', 'Modo de verbosidade.'),

        (4305, 'en', 'Center the data', 'When pre-computing distances it is more numerically accurate to center the'
                                        ' data first.'),
        (4305, 'pt', 'Centralizar os dados', 'Ao pré-calcular as distâncias, é mais preciso numericamente centralizar'
                                             ' os dados primeiro.'),

        (4306, 'en', 'Number of jobs', 'The number of jobs to use for the computation.'),
        (4306, 'pt', 'Número de jobs', 'O número de jobs a serem usados para o cálculo.'),

        (4307, 'en', 'Algorithm', 'K-means algorithm to use.'),
        (4307, 'pt', 'Algoritmo', 'Algoritmo K-means a ser usado.'),

        (4308, 'en', 'Batch size', 'Size of the mini batches.'),
        (4308, 'pt', 'Tamanho do batch', 'Tamanho dos mini batches.'),

        (4309, 'en', 'Compute labels', 'Compute label assignment and inertia for the complete dataset once the'
                                       ' minibatch optimization has converged in fit.'),
        (4309, 'pt', 'Computar atribuições', 'Calcula a atribuição e a inércia de rótulos para o conjunto de dados'
                                             ' completo assim que a otimização de minibatch convergir.'),

        (4310, 'en', 'Tolerance', 'Control early stopping based on the relative center changes as measured by a'
                                  ' smoothed, variance-normalized of the mean center squared position changes.'),
        (4310, 'pt', 'Tolerância', 'Controla a parada antecipada com base nas mudanças relativas do centro, conforme'
                                   ' medido por uma mudança suavizada, normalizada pela variação da posição média do'
                                   ' quadrado ao quadrado.'),

        (4311, 'en', 'Early stopping', 'Control early stopping based on the consecutive number of mini batches that'
                                       ' does not yield an improvement on the smoothed inertia.'),
        (4311, 'pt', 'Parada antecipada', 'Controla a parada antecipada com base no número consecutivo de mini batches'
                                          ' que não gera uma melhoria na inércia suavizada.'),

        (4312, 'en', 'Number of samples', 'Number of samples to randomly sample for speeding up the initialization'
                                          ' (sometimes at the expense of accuracy): the only algorithm is initialized'
                                          ' by running a batch KMeans on a random subset of the data.'),
        (4312, 'pt', 'Número de amostras', 'Número de amostras para amostrar aleatoriamente para acelerar a'
                                           ' inicialização (às vezes à custa da precisão): o único algoritmo é'
                                           ' inicializado executando um KMeans em lote em um subconjunto aleatório dos'
                                           ' dados.'),

        (4313, 'en', 'Reassignment ratio', 'Control the fraction of the maximum number of counts for a center to be'
                                           ' reassigned.'),
        (4313, 'pt', 'Relação de reatribuição', 'Controle a fração do número máximo de contagens para um centro a ser'
                                                ' reatribuído.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `type` = 'DECIMAL' WHERE id = 4068""",
     """UPDATE operation_form_field SET `type` = 'FLOAT' WHERE id = 4068"""),

    ("""UPDATE operation_form_field SET `default` = 1e-4 WHERE id = 4068""",
     """UPDATE operation_form_field SET `default` = 0.001 WHERE id = 4068"""),

    ("""UPDATE operation_form_field SET `default` = 100 WHERE id = 4067""",
     """UPDATE operation_form_field SET `default` = 300 WHERE id = 4067"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4301 AND 4313'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4301 AND 4313'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4033 AND operation_form_id = 41'),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if isinstance(cmd[0], str):
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