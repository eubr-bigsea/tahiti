# -*- coding: utf-8 -*-

"""Fixing scikit_learn MLP regressor forms.

Revision ID: eff0acabf4fe
Revises: f2c2be48125d
Create Date: 2019-11-06 14:31:44.504773

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
revision = 'eff0acabf4fe'
down_revision = 'f2c2be48125d'
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
        (4035, 41),  #appearance
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

    enable_condition = 'this.solver.internalValue === "sgd" || this.solver.internalValue === "adam"'
    enable_condition2 = 'this.solver.internalValue === "sgd"'
    enable_condition3 = 'this.solver.internalValue === "sgd" && this.momentum.internalValue > "0"'
    enable_condition4 = 'this.early_stopping.internalValue === "1"'
    enable_condition5 = 'this.solver.internalValue === "adam"'

    data = [
        #Flatten - data_format
        (4190, 'batch_size', 'TEXT', 0, 22, 'auto', 'text', None, None, 'EXECUTION', 4020, None),
        (4191, 'learning_rate', 'TEXT', 0, 23, 'constant', 'dropdown', None,
         json.dumps([
             {'key': 'constant', 'value': 'constant'},
             {'key': 'invscaling', 'value': 'invscaling'},
             {'key': 'adaptive', 'value': 'adaptive'},
         ]),
         'EXECUTION', 4020, enable_condition2),
        (4192, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4020, None),
        (4193, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None, 'EXECUTION', 4020, None),
        (4194, 'prediction', 'TEXT', 0, 4, 'prediction', 'text', None, None, 'EXECUTION', 4020, None),
        (4195, 'learning_rate_init', 'DECIMAL', 0, 24, 0.001, 'decimal', None, None, 'EXECUTION', 4020,
         enable_condition),
        (4196, 'power_t', 'DECIMAL', 0, 11, 0.5, 'decimal', None, None, 'EXECUTION', 4020, enable_condition2),
        (4197, 'shuffle', 'INTEGER', 0, 12, 1, 'checkbox', None, None, 'EXECUTION', 4020, enable_condition),
        (4199, 'warm_start', 'INTEGER', 0, 14, 0, 'checkbox', None, None, 'EXECUTION', 4020, None),
        (4200, 'momentum', 'DECIMAL', 0, 15, 0.9, 'decimal', None, None, 'EXECUTION', 4020, enable_condition2),
        (4201, 'nesterovs_momentum', 'INTEGER', 0, 16, 1, 'checkbox', None, None, 'EXECUTION', 4020, enable_condition3),
        (4202, 'early_stopping', 'INTEGER', 0, 17, 0, 'checkbox', None, None, 'EXECUTION', 4020, enable_condition),
        (4203, 'validation_fraction', 'DECIMAL', 0, 18, 0.1, 'decimal', None, None, 'EXECUTION', 4020,
         enable_condition4),
        (4204, 'beta_1', 'DECIMAL', 0, 19, 0.9, 'decimal', None, None, 'EXECUTION', 4020, enable_condition5),
        (4205, 'beta_2', 'DECIMAL', 0, 20, 0.999, 'decimal', None, None, 'EXECUTION', 4020, enable_condition5),
        (4206, 'epsilon', 'DECIMAL', 0, 21, 1e-8, 'decimal', None, None, 'EXECUTION', 4020, enable_condition5),
        (4198, 'n_iter_no_change', 'INTEGER', 0, 13, 10, 'integer', None, None, 'EXECUTION', 4020, enable_condition),
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
        (4199, 'en', 'Warm start', 'When set to True, reuse the solution of the previous call to fit as initialization,'
                                   ' otherwise, just erase the previous solution.'),
        (4199, 'pt', 'Warm start', 'Quando definido como True, reutiliza a solução da chamada anterior para caber como'
                                   ' inicialização, caso contrário, apenas apague a solução anterior.'),

        (4192, 'en', 'Features', 'Features.'),
        (4192, 'pt', 'Atributo(s) previsor(es)', 'Atributo(s) previsor(es).'),

        (4193, 'en', 'Label attribute', 'Label attribute.'),
        (4193, 'pt', 'Atributo com o rótulo', 'Atributo com o rótulo.'),

        (4194, 'en', 'Prediction attribute (new)', 'Prediction attribute (new).'),
        (4194, 'pt', 'Atributo com a predição (novo)', 'Atributo usado para predição (novo).'),

        (4191, 'en', 'Batch size', 'Size of minibatches for stochastic optimizers. If the solver is ‘lbfgs’, the'
                                   ' classifier will not use minibatch. When set to “auto”, '
                                   'batch_size=min(200, n_samples)'),
        (4191, 'pt', 'Tamanho do batch', 'Tamanho de mini batches para otimizadores estocásticos. Se o solucionador'
                                         ' for "lbfgs", o classificador não usará minibatch. Quando definido como'
                                         ' "auto", batch_size = min (200, n_samples)'),

        (4190, 'en', 'Learning rate', 'Learning rate schedule for weight updates.'),
        (4190, 'pt', 'Taxa de aprendizado', 'Programação da taxa de aprendizado para atualizações de peso.'),

        (4195, 'en', 'Learning rate init', 'The initial learning rate used. It controls the step-size in updating the'
                                           ' weights.'),
        (4195, 'pt', 'Taxa de aprendizado inicial', 'A taxa de aprendizado inicial usada. Controla o tamanho da etapa'
                                                    ' na atualização dos pesos.'),

        (4196, 'en', 'Power', 'The exponent for inverse scaling learning rate.'),
        (4196, 'pt', 'Expoente', 'O expoente da taxa de aprendizado de escala inversa.'),

        (4197, 'en', 'Shuffle', 'Whether to shuffle samples in each iteration.'),
        (4197, 'pt', 'Shuffle', 'Se as amostras devem ser embaralhadas em cada iteração.'),

        (4200, 'en', 'Momentum', 'Momentum for gradient descent update.'),
        (4200, 'pt', 'Momentum', 'Momentum para atualização de descida de gradiente.'),

        (4201, 'en', 'Nesterov’s momentum', 'Whether to use Nesterov’s momentum.'),
        (4201, 'pt', 'Nesterovs’s momentum', 'Se deve usar o Nesterov’s momentum .'),

        (4202, 'en', 'Early stopping', 'Whether to use early stopping to terminate training when validation score is'
                                       ' not improving.'),
        (4202, 'pt', 'Parada antecipada', 'Se a parada precoce deve ser usada para encerrar o treinamento quando a'
                                          ' pontuação de validação não está melhorando.'),

        (4203, 'en', 'Validation fraction', 'The proportion of training data to set aside as validation set for early'
                                            ' stopping.'),
        (4203, 'pt', 'Fração de validação', 'A proporção de dados de treinamento a serem retirados como validação'
                                            ' definida para parada antecipada.'),

        (4204, 'en', 'Beta 1', 'Exponential decay rate for estimates of first moment vector in adam, should be in'
                               ' [0, 1).'),
        (4204, 'pt', 'Beta 1', 'A taxa de decaimento exponencial para estimativas do vetor de primeiro momento em adam,'
                               ' deve estar em [0, 1).'),

        (4205, 'en', 'Beta 2', 'Exponential decay rate for estimates of second moment vector in adam, should be in'
                               ' [0, 1).'),
        (4205, 'pt', 'Beta 2', 'A taxa de decaimento exponencial para estimativas do vetor de segundo momento em adam,'
                               ' deve estar em [0, 1).'),

        (4206, 'en', 'Epsilon', 'Value for numerical stability in adam.'),
        (4206, 'pt', 'Epsilon', 'Valor para a estabilidade numérica em adão.'),

        (4198, 'en', 'Maximum number of epochs', 'Maximum number of epochs to not meet tol improvement.'),
        (4198, 'pt', 'Número máximo de epochs', 'Número máximo de epochs para não'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `type` = 'DECIMAL' WHERE id = 4101 OR id = 4103""",
     """UPDATE operation_form_field SET `type` = 'FLOAT' WHERE id = 4101 OR id = 4103"""),

    ("""UPDATE operation_form_field SET `order` = '3' WHERE id = 4098""",
     """UPDATE operation_form_field SET `order` = '8' WHERE id = 4098"""),

    ("""UPDATE operation_form_field SET `order` = '9' WHERE id = 4099""",
     """UPDATE operation_form_field SET `order` = '2' WHERE id = 4099"""),

    ("""UPDATE operation_form_field SET `order` = '10' WHERE id = 4100""",
     """UPDATE operation_form_field SET `order` = '3' WHERE id = 4100"""),

    ("""UPDATE operation_form_field SET `order` = '25' WHERE id = 4101""",
     """UPDATE operation_form_field SET `order` = '4' WHERE id = 4101"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4190 AND 4206'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4190 AND 4206'),

    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4035 AND operation_form_id = 41'),
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