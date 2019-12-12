"""classifier logistic regression add fields

Revision ID: 40705a398028
Revises: 529bd5bd009e
Create Date: 2019-11-25 10:38:52.414039

"""
from alembic import op
import sqlalchemy as sa
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json

# revision identifiers, used by Alembic.
revision = '40705a398028'
down_revision = '326dfd633ba8'

branch_labels = None
depends_on = None

SCIKIT_LEARN_PLATAFORM_ID = 4
ID_OPERATION = 4021

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

    data = [
        (4231, 'penalty', 'TEXT', 0, 6, 'l2', 'dropdown', None, 
         json.dumps([
             {'key': 'l1', 'value': 'l1'},
             {'key': 'l2', 'value': 'l2'},
             {'key': 'elasticnet', 'value': 'elasticnet'},
             {'key': 'none', 'value': 'none'}
         ]),
        'EXECUTION', 4001, None),
        (4232, 'dual', 'INTEGER', 0, 7, 0, 'checkbox', None, None, 'EXECUTION', 4001, None),
        (4233, 'fit_intercept', 'INTEGER', 0, 8, 1, 'checkbox', None, None, 'EXECUTION', 4001, None),
        (4234, 'intercept_scaling', 'DECIMAL', 0, 9, 1.0, 'decimal', None, None, 'EXECUTION', 4001, None),
        (4236, 'multi_class', 'TEXT', 0, 11, 'ovr', 'dropdown', None,
         json.dumps([
             {'key': 'ovr', 'value': 'ovr'},
             {'key': 'multinomial', 'value': 'multinomial'},
             {'key': 'auto', 'value': 'auto'}
         ]),
         'EXECUTION', 4001, None),
        (4237, 'n_jobs', 'INTEGER', 0, 12, None, 'integer', None, None, 'EXECUTION', 4001, None),
        (4238, 'l1_ratio', 'DECIMAL', 0, 13, None, 'decimal', None, None, 'EXECUTION', 4001, None),
        (4239, 'verbose', 'INTEGER', 0, 14, 0, 'integer', None, None, 'EXECUTION', 4001, None)
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
        (4231, 'en', 'Penalty', 'Used to specify the norm used in the penalization.'),
        (4231, 'pt', 'Penalidade', 'Usado para especificar a norma da penalização.'),

        (4232, 'en', 'Dual', 'Dual or primal formulation.'),
        (4232, 'pt', 'Dual', 'Formulação dual ou primal.'),

        (4233, 'en', 'Fit intercept', 'Specifies if a constant (a.k.a. bias or intercept) should be added to the decision function.'),
        (4233, 'pt', 'Considerar intercepto', 'Especificar se uma constante (intecerpto ou viés) deve ser adicionada na função de decisão.'),

        (4234, 'en', 'Intercept scaling', 'Useful only when the solver "liblinear" is used and "Fit intercept" is set to True.'),
        (4234, 'pt', 'Escala do intercepto', 'Usado apenas se o Solver "liblinear" for utilizado com o atributo "Considerar intercepto" habilitado.' ),

        (4236, 'en', 'Multi class', 'If the option chosen is "ovr", then a binary problem is fit for each label. For "multinomial" the loss minimised is the multinomial loss fit across the entire probability distribution, even when the data is binary.'),
        (4236, 'pt', 'Mutiplas classes' , 'Se a opção selecionada é "ovr", então um problema binário é moldado para cada label. Para o atributo "multinomial" a minização de perda é o ajuste de perda multinomial das funções de probabilidade, mesmo com atributos binários.'),
        
        (4237, 'en', 'Number of CPU cores', 'Number of CPU cores used when parallelizing over classes if multi_class="ovr".'),
        (4237, 'pt', 'Numero de núcleos do CPU' , 'Quantidade de núcleos do CPU utilizados para paralelização quando o atributo multi_class="ovr".'),

        (4238, 'en', 'L1 Ratio', 'The Elastic-Net mixing parameter, with l1_ratio between 0 and 1.'),
        (4238, 'pt', 'L1 Ratio', 'Parâmetro do Elastic-Net, o valor deve estar entre 0 e 1.'),

		(4239, 'en', 'Verbose', 'For the "liblinear" and "lbfgs" solvers set verbose to any positive number for verbosity.'),
        (4239, 'pt', 'Verboso' , 'Para os solvers "liblinear" e "lbfgs" insira qualquer inteiro positivo como numéro de verbosidade.')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4231 AND 4239'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4231 AND 4239')
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
