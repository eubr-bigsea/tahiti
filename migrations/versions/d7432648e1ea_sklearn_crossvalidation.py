# -*- coding: utf-8 -*-

"""Sklearn operations

Revision ID: d7432648e1ea
Revises: 5430536464c7
Create Date: 2018-09-13 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = 'd7432648e1ea'
down_revision = '5430536464c7'
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
        (4018, 'execute-sql', '1', 'TRANSFORMATION', 'fa-bolt'),
        (4019, 'mlp-classifier', 1,  'TRANSFORMATION', 'fa-code-branch'),
        (4020, 'mlp-regressor', 1, 'TRANSFORMATION', 'fa-code-branch'),
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

        (18, 4),  # spark data-reader
        (43, 4),  # cross-validation
        (82, 4),  # execute-python
        (4018, 4),  # execute-sql
        (4019, 4),
        (4020, 4),

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
        (4018, 4001),  # execute-sql
        (4018, 7),  # execute-sql

        (4019, 8),
        (4019, 18), #classifier
        (4019, 4001),

        (4020, 8),
        (4020, 21),      # regressors
        (4020, 4001),
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
        (4018, 1, 1, 'execution'),
        (4019, 1, 1, 'execution'),
        (4020, 1, 1, 'execution'),
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
        (4018, 'en', 'Execution'),
        (4018, 'pt', 'Execução'),
        (4019, 'en', 'Execution'),
        (4019, 'pt', 'Execução'),
        (4020, 'en', 'Execution'),
        (4020, 'pt', 'Execução'),
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
        (4018, 41),
        (4018, 110),
        (4018, 4018),

        (4019, 41),
        (4019, 4019),

        (4020, 41),
        (4020, 4020),
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
        (4018, 'pt', 'Executar consulta SQL',
         'Executa uma consulta usando a linguagem SQL disponível no Pandas '
         'SQL.'),
        (4018, 'en', 'Execute SQL query',
         'Executes a query using SQL language available in Pandas SQL.'),

        (4019, 'pt', 'Classificador Perceptron multicamadas',
         'Classificador Perceptron multicamadas.'),
        (4019, 'en', 'Multi-layer Perceptron classifier',
         'Multi-layer Perceptron classifier.'),

        (4020, 'pt', 'Regressor Perceptron multicamadas',
         'Regressor Perceptron multicamadas.'),
        (4020, 'en', 'Multi-layer Perceptron Regressor',
         'Multi-layer Perceptron Regressor.')
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
        (4025, 'INPUT', None, 4018, 1, 'ONE', 'input data 1 '),
        (4026, 'INPUT', None, 4018, 2, 'ONE', 'input data 2'),
        (4027, 'OUTPUT', None, 4018, 1, 'MANY', 'output data'),

        (4028, 'OUTPUT', None, 4019, 1, 'MANY', 'algorithm'),
        (4029, 'OUTPUT', None, 4020, 1, 'MANY', 'algorithm'),


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
        (4025, 'en', 'input data 1', 'Input data 1'),
        (4025, 'pt', 'dados de entrada 1', 'Input data 1'),
        (4026, 'en', 'input data 2', 'Input data 2'),
        (4026, 'pt', 'dados de entrada 2', 'Input data 2'),
        (4027, 'en', 'output data', 'Output data'),
        (4027, 'pt', 'dados de saída', 'Dados de saída'),

        (4028, 'en', 'algorithm', 'Untrained classification model'),
        (4028, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),

        (4029, 'en', 'algorithm', 'Untrained regressor model'),
        (4029, 'pt', 'algoritmo', 'Modelo de regressão não treinado'),

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
        (4025, 1),
        (4026, 1),
        (4027, 1),
        (4028, 5),  # ClassificationAlgorithm
        (4029, 17),  # IRegressionAlgorithm
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

        (4089, 'query', 'TEXT', 1, 1, None, 'code', None, None, 'EXECUTION',
         4018),
        (4090, 'names', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION',
         4018),

        # mpl-classifier
        (4091, 'layer_sizes', 'TEXT', 1, 1, '(1,100,1)', 'text', None, None,
         'EXECUTION',
         4019),
        (4092, 'activation', 'TEXT', 0, 2, 'relu', 'dropdown', None,
         '[{"key": \"identity\", \"value\": \"identity\"}, '
         '{\"key\": \"logistic\", \"value\": \"logistic\"}, '
         '{\"key\": \"tanh\", \"value\": \"tanh\"}, '
         '{\"key\": \"relu\", \"value\": \"relu\"}]', 'EXECUTION', 4019),
        (4093, 'solver', 'TEXT', 0, 3, 'adam', 'dropdown', None,
         '[{"key": \"lbfgs\", \"value\": \"lbfgs\"}, '
         '{\"key\": \"sgd\", \"value\": \"sgd\"}, '
         '{\"key\": \"adam\", \"value\": \"adam\"}]', 'EXECUTION', 4019),
        (4094, 'alpha', 'FLOAT', 0, 4, 0.0001, 'decimal', None, None, 'EXECUTION',
         4019),
        (4095, 'max_iter', 'INTEGER', 0, 5, 200, 'integer', None, None,
         'EXECUTION', 4019),
        (4096, 'tol', 'FLOAT', 0, 6, 0.0001, 'decimal', None, None, 'EXECUTION',
         4019),
        (4097, 'seed', 'INTEGER', 0, 7, None, 'integer', None, None,
         'EXECUTION', 4019),

        # mpl-regressor
        (4098, 'layer_sizes', 'TEXT', 1, 1, '(1,100,1)', 'text', None, None,
         'EXECUTION',
         4020),
        (4099, 'activation', 'TEXT', 0, 2, 'relu', 'dropdown', None,
         '[{"key": \"identity\", \"value\": \"identity\"}, '
         '{\"key\": \"logistic\", \"value\": \"logistic\"}, '
         '{\"key\": \"tanh\", \"value\": \"tanh\"}, '
         '{\"key\": \"relu\", \"value\": \"relu\"}]', 'EXECUTION', 4020),
        (4100, 'solver', 'TEXT', 0, 3, 'adam', 'dropdown', None,
         '[{"key": \"lbfgs\", \"value\": \"lbfgs\"}, '
         '{\"key\": \"sgd\", \"value\": \"sgd\"}, '
         '{\"key\": \"adam\", \"value\": \"adam\"}]', 'EXECUTION', 4020),
        (4101, 'alpha', 'FLOAT', 0, 4, 0.0001, 'decimal', None, None, 'EXECUTION',
         4020),
        (4102, 'max_iter', 'INTEGER', 0, 5, 200, 'integer', None, None,
         'EXECUTION', 4020),
        (4103, 'tol', 'FLOAT', 0, 6, 0.0001, 'decimal', None, None, 'EXECUTION',
         4020),
        (4104, 'seed', 'INTEGER', 0, 7, None, 'integer', None, None,
         'EXECUTION', 4020),


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

        (4089, 'en',
         'SQL Query, (inputs are available as tables named ds1 and ds2)',
         'SQL query compatible with SQLite sytanx. For more information, '
         'see https://www.sqlite.org/lang.html or '
         'https://github.com/yhat/pandasql.'),
        (4089, 'pt',
         'Consulta (entradas estão disponíveis como tabelas chamadas ds1 e '
         'ds2)',
         'Consulta SQL compatível com o Apache Spark. Para mais informações, '
         'veja https://www.sqlite.org/lang.html ou '
         'https://github.com/yhat/pandasql.'),
        (4090, 'en', 'Names of attributes after the query',
         'Name of the new attributes after executing the query (optional, '
         'helps attribute suggestion).'),
        (4090, 'pt', 'Nome dos novos atributos após a consulta',
         'Nome dos novos atributos após executar a consulta (opcional. auxilia '
         'na sugestão de atributos).'),

        (4091, 'en', 'Layer sizes',
         'The ith element represents the number of neurons.'),
        (4092, 'en', 'Activation', 'Activation function for the hidden layer.'),
        (4093, 'en', 'Solver', 'The solver for weight optimization.'),
        (4094, 'en', 'Alpha', 'L2 penalty (regularization term) parameter.'),
        (4095, 'en', 'Maximum number of iterations',
         'The solver iterates until convergence or this number of iterations.'),
        (4096, 'en', 'Tolerance', 'Tolerance for the optimization.'),
        (4097, 'en', 'Seed', 'Seed used by the random number generator.'),
        (4091, 'pt', 'Tamanhos das Camadas',
         'O elemento de ordem i representa o número de neurónios.'),
        (4092, 'pt', 'Ativação', 'Função de ativação para a camada oculta.'),
        (4093, 'pt', 'Solver', 'O solucionador para otimização de peso.'),
        (4094, 'pt', 'Alpha',
         'Parâmetro de penalidade L2 (termo de regularização).'),
        (4095, 'pt', 'Número máximo de iterações',
         'O solucionador itera até a convergência ou esse número de '
         'iterações.'),
        (4096, 'pt', 'Tolerância', 'Tolerância para a otimização.'),
        (4097, 'pt', 'Semente',
         'Semente usada pelo gerador de números aleatórios.'),


        (4098, 'en', 'Layer sizes',
         'The ith element represents the number of neurons.'),
        (4099, 'en', 'Activation', 'Activation function for the hidden layer.'),
        (4100, 'en', 'Solver', 'The solver for weight optimization.'),
        (4101, 'en', 'Alpha', 'L2 penalty (regularization term) parameter.'),
        (4102, 'en', 'Maximum number of iterations',
         'The solver iterates until convergence or this number of iterations.'),
        (4103, 'en', 'Tolerance', 'Tolerance for the optimization.'),
        (4104, 'en', 'Seed', 'Seed used by the random number generator.'),
        (4098, 'pt', 'Tamanhos das Camadas',
         'O elemento de ordem i representa o número de neurónios.'),
        (4099, 'pt', 'Ativação', 'Função de ativação para a camada oculta.'),
        (4100, 'pt', 'Solver', 'O solucionador para otimização de peso.'),
        (4101, 'pt', 'Alpha',
         'Parâmetro de penalidade L2 (termo de regularização).'),
        (4102, 'pt', 'Número máximo de iterações',
         'O solucionador itera até a convergência ou esse número de '
         'iterações.'),
        (4103, 'pt', 'Tolerância', 'Tolerância para a otimização.'),
        (4104, 'pt', 'Semente',
         'Semente usada pelo gerador de números aleatórios.'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN 4018 AND 4020'),
    (_insert_new_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 18 AND '
     'platform_id = 4;'
     'DELETE FROM operation_platform WHERE operation_id = 43 AND '
     'platform_id = 4;'
     'DELETE FROM operation_platform WHERE operation_id = 82 AND '
     'platform_id = 4;'
     'DELETE FROM operation_platform WHERE operation_id BETWEEN 4018 AND 4020'
     ),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN 4018 AND 4020'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 4018 AND 4020'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 4018 AND 4020'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id BETWEEN 4018 AND 4020'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 4018 AND 4020'),
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4025 AND 4029'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4025 AND 4029'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE '
     'operation_port_id BETWEEN 4025 AND 4029'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4089 AND 4104'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id BETWEEN 4089 AND 4104'),
    ("""
        DELETE FROM operation_platform WHERE operation_id = 3001 AND 
        platform_id = 4;
        
        UPDATE operation_category_operation 
        SET operation_category_id = 16
        WHERE operation_id = 3004 AND operation_category_id = 12; 
     """,
     """
        INSERT INTO operation_platform (operation_id, platform_id)
        VALUES (3001, 4);
     """),

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