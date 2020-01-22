# -*- coding: utf-8 -*-

"""Update MLP classifier (scikit_learn).

Revision ID: 1c688e5c61f3
Revises: 9307a4e438de
Create Date: 2019-12-05 08:38:34.089623

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
revision = '1c688e5c61f3'
down_revision = '9307a4e438de'
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
        (4034, 41),  #appearance
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

    enable_condition = 'this.solver.internalValue !== "lbfgs"'
    enable_condition2 = 'this.solver.internalValue === "sgd"'
    enable_condition3 = 'this.solver.internalValue === "sgd" || this.solver.internalValue === "adam"'
    enable_condition4 = 'this.solver.internalValue === "sgd" && this.momentum.internalValue > "0"'
    enable_condition5 = 'this.early_stopping.internalValue === "1"'
    enable_condition6 = 'this.solver.internalValue === "adam"'
    enable_condition7 = 'this.solver.internalValue === "lbfgs"'

    data = [
        #Flatten - data_format
        (4274, 'batch_size', 'TEXT', 0, 8, 'auto', 'text', None,  None, 'EXECUTION', 4019, enable_condition),
        (4275, 'learning_rate', 'TEXT', 0, 9, 'constant', 'dropdown', None,
         json.dumps([
             {'key': 'constant', 'value': 'constant'},
             {'key': 'invscaling', 'value': 'invscaling'},
             {'key': 'adaptive', 'value': 'adaptive'},
         ]),
         'EXECUTION', 4019, enable_condition2),
        (4276, 'learning_rate_init', 'DECIMAL', 0, 10, 0.001, 'decimal', None,  None, 'EXECUTION', 4019,
         enable_condition3),
        (4277, 'power_t', 'DECIMAL', 0, 11, 0.5, 'decimal', None,  None, 'EXECUTION', 4019, enable_condition2),
        (4278, 'shuffle', 'INTEGER', 0, 12, 1, 'checkbox', None,  None, 'EXECUTION', 4019, enable_condition3),
        (4279, 'momentum', 'DECIMAL', 0, 13, 0.9, 'decimal', None,  None, 'EXECUTION', 4019, enable_condition2),
        (4280, 'nesterovs_momentum', 'INTEGER', 0, 14, 1, 'checkbox', None,  None, 'EXECUTION', 4019,
         enable_condition4),
        (4281, 'early_stopping', 'INTEGER', 0, 15, 0, 'checkbox', None,  None, 'EXECUTION', 4019, enable_condition3),
        (4282, 'validation_fraction', 'DECIMAL', 0, 16, 0.1, 'decimal', None,  None, 'EXECUTION', 4019,
         enable_condition5),
        (4283, 'beta1', 'DECIMAL', 0, 17, 0.9, 'decimal', None,  None, 'EXECUTION', 4019, enable_condition6),
        (4284, 'beta2', 'DECIMAL', 0, 18, 0.999, 'decimal', None,  None, 'EXECUTION', 4019, enable_condition6),
        (4285, 'epsilon', 'DECIMAL', 0, 19, 1e-8, 'decimal', None,  None, 'EXECUTION', 4019, enable_condition6),
        (4286, 'n_iter_no_change', 'INTEGER', 0, 20, 10, 'integer', None,  None, 'EXECUTION', 4019, enable_condition3),
        (4287, 'max_fun', 'INTEGER', 0, 21, 15000, 'integer', None,  None, 'EXECUTION', 4019, enable_condition7),
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
        (4274, 'en', 'Batch size', 'Size of minibatches for stochastic optimizers.'),
        (4274, 'pt', 'Tamanho do batch', 'Tamanho de minibatches para otimizadores estocásticos.'),

        (4275, 'en', 'Learning rate', 'Learning rate schedule for weight updates.'),
        (4275, 'pt', 'Taxa de Aprendizagem', 'Programação da taxa de aprendizado para atualizações de peso.'),

        (4276, 'en', 'Initial learning rate', 'The initial learning rate used.'),
        (4276, 'pt', 'Taxa inicial de aprendizado', 'A taxa de aprendizado inicial usada.'),

        (4277, 'en', 'Power', 'The exponent for inverse scaling learning rate.'),
        (4277, 'pt', 'Potência', 'O expoente da taxa de aprendizado de escala inversa.'),

        (4278, 'en', 'Shuffle', 'Whether to shuffle samples in each iteration.'),
        (4278, 'pt', 'Embaralhar', 'Se as amostras devem ser embaralhadas em cada iteração.'),

        (4279, 'en', 'Momentum', 'Momentum for gradient descent update.'),
        (4279, 'pt', 'Momentum', 'Momentum para atualização do gradiente descendente.'),

        (4280, 'en', 'Nesterovs momentum', 'Whether to use Nesterov’s momentum.'),
        (4280, 'pt', 'Impulso de Nesterovs', 'Se deve usar o impulso de Nesterov.'),

        (4281, 'en', 'Early stopping', 'Whether to use early stopping to terminate training when validation score is'
                                       ' not improving.'),
        (4281, 'pt', 'Parada antecipada', 'Se a parada precoce deve ser usada para encerrar o treinamento quando a'
                                          ' pontuação de validação não está melhorando.'),

        (4282, 'en', 'Validation fraction', 'The proportion of training data to set aside as validation set for early'
                                            ' stopping.'),
        (4282, 'pt', 'Fração de validação', 'A proporção de dados de treinamento a serem retirados como validação'
                                            ' definida para a parada inicial.'),

        (4283, 'en', 'Beta1', 'Exponential decay rate for estimates of second moment vector in adam.'),
        (4283, 'pt', 'Beta1', 'Taxa de decaimento exponencial para estimativas do segundo vetor de momento em adam.'),

        (4284, 'en', 'Beta2', 'Exponential decay rate for estimates of second moment vector in adam.'),
        (4284, 'pt', 'Beta2', 'Taxa de decaimento exponencial para estimativas do segundo vetor de momento em adam.'),

        (4285, 'en', 'Epsilon', 'Value for numerical stability in adam.'),
        (4285, 'pt', 'Epsilon', 'Valor para a estabilidade numérica em adam.'),

        (4286, 'en', 'Number of iteration with no change', 'Maximum number of epochs to not meet tol improvement.'),
        (4286, 'pt', 'Número de iteração sem alteração', 'Número máximo de épocas para não atender a melhorias. '),

        (4287, 'en', 'Maximum function', 'Maximum number of loss function calls.'),
        (4287, 'pt', 'Função máxima', 'Número máximo de chamadas de função de perda.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `type` = 'DECIMAL' WHERE id = 4094 OR id = 4096""",
     """UPDATE operation_form_field SET `type` = 'FLOAT' WHERE id = 4094 OR id = 4096"""),

    ("""UPDATE operation_form_field SET `form_id` = '4030' WHERE id = 4247""",
     """UPDATE operation_form_field SET `form_id` = '4003' WHERE id = 4247"""),

    ("""UPDATE operation_form_field SET `enable_conditions` = 'this.solver.internalValue === "sgd" && 
        this.momentum.internalValue > "0"' WHERE id = 4201""",
     """UPDATE operation_form_field SET `enable_conditions` = 'this.solver.internalValue === "sgd" && 
        this.momentum.internalValue >== "0"' WHERE id = 4201"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4274 AND 4287'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4274 AND 4287'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4034 AND operation_form_id = 41'),
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
