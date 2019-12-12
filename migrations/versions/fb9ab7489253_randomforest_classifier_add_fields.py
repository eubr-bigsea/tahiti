"""RandomForest classifier add fields

Revision ID: fb9ab7489253
Revises: 1c688e5c61f3
Create Date: 2019-12-05 11:58:31.426187

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
revision = 'fb9ab7489253'
down_revision = 'cebc00c49ab8'

branch_labels = None
depends_on = None

SCIKIT_LEARN_PLATAFORM_ID = 4
ID_OPERATION = 4022

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
		(4290, 'criterion', 'TEXT', 0, 6, 'gini', 'dropdown', None, 
			json.dumps([
             {'key': 'gini', 'value': 'gini'},
             {'key': 'entropy', 'value': 'entropy'}
         ]),
         'EXECUTION', 4002, None),
        (4291, 'min_weight_fraction_leaf', 'DECIMAL', 0, 8, 0.0, 'decimal', None, None, 'EXECUTION', 4002, None),
        (4292, 'max_features', 'INTEGER', 0, 9, None, 'integer', None, None, 'EXECUTION', 4002, None),
        (4293, 'max_leaf_nodes', 'INTEGER', 0, 10, None, 'integer', None, None, 'EXECUTION', 4002, None),
        (4294, 'min_impurity_decrease', 'DECIMAL', 0, 11, 0.0, 'decimal', None, None, 'EXECUTION', 4002, None),
        (4295, 'bootstrap', 'INTEGER', 0, 12, 1, 'checkbox', None, None, 'EXECUTION', 4001, None),
        (4296, 'oob_score', 'INTEGER', 0, 13, 1, 'checkbox', None, None, 'EXECUTION', 4001, None),
        (4297, 'n_jobs', 'INTEGER', 0, 14, None, 'integer', None, None, 'EXECUTION', 4002, None),
        (4298, 'verbose', 'INTEGER', 0, 15, 0, 'integer', None, None, 'EXECUTION', 4002, None),
        (4299, 'ccp_alpha', 'DECIMAL', 0, 16, 0, 'decimal', None, None, 'EXECUTION', 4002, None),
        (4300, 'max_samples', 'DECIMAL', 0, 17, None, 'decimal', None, None, 'EXECUTION', 4002, None)
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
        (4290, 'en', 'Criterion', 'The function to measure the quality of a split.'),
        (4290, 'pt', 'Critério', 'Função utilizada na medição da qualidade do particionamento.'),

        (4291, 'en', 'Minimum weighted fraction leaf', 'The minimum weighted fraction of the sum total of weights (of all the input samples) required to be at a leaf node.'),
        (4291, 'pt', 'Fração ponderada mínima de folhas', 'A fração ponderada mínima da soma total de pesos (de todas as amostras de entrada) necessária para estar em um nó folha.'),

        (4292, 'en', 'Max Features', 'The number of features to consider when looking for the best split.'),
        (4292, 'pt', 'Quantidade máxima de atributos', 'Quantidade máxima de atributos a se considerar no particionamento.'),

        (4293, 'en', 'Max leaf nodes', 'Trees growth control.'),
        (4293, 'pt', 'Quantidade máxima de nós folha', 'Controle de crescimento da árvore.'),

        (4294, 'en', 'Min impurity decrease', 'A node will be split if this split induces a decrease of the impurity greater than or equal to this value.'),
        (4294, 'pt', 'Diminuição mínima de impureza', 'Um nó será particionado caso isso resulte na diminuição da impureza maior ou igual o valor do atributo.' ),

        (4295, 'en', 'Bootstrap', 'Whether bootstrap samples are used when building trees.'),
        (4295, 'pt', 'Bootstrap', 'Utilizar amostras de um bootstrap para gerar as árvores.'),

        (4296, 'en', 'Out of bag', 'Whether to use out-of-bag samples to estimate the generalization accuracy'),
        (4296, 'pt', 'Out of bag' , 'Usar amostras "out-of-bag" para estimar a acurácia do generalizador'),
        
        (4297, 'en', 'Number of CPU cores', 'Number of CPU cores used when parallelizing over classes if multi_class="ovr".'),
        (4297, 'pt', 'Numero de núcleos do CPU' , 'Quantidade de núcleos do CPU utilizados para paralelização quando o atributo multi_class="ovr".'),

        (4298, 'en', 'Verbose', 'Controls the verbosity when fitting and predicting.'),
        (4298, 'pt', 'Verboso', 'Controle da verbosidade ao executar o treinamento e a predição.'),

		(4299, 'en', 'Alpha complexity parameter', 'Complexity parameter used for Minimal Cost-Complexity Pruning.'),
        (4299, 'pt', 'Parâmetro de complexidade alpha' , 'Parâmetro de complexidade usado para a poda mínima de complexidade de custo.'),

        (4300, 'en', 'Percuntal of max samples', 'If bootstrap is True, the number of samples to draw from X to train each base estimator.'),
        (4300, 'pt', 'Percentual máximo de amostras' , 'Quando o parâmetro "Bootstrap" estiver habilitado, utilize esse número para obter um conjunto X de treinamento para cada base.')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4290 AND 4300'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4290 AND 4300'),
    ('UPDATE operation_translation \
    	SET name="Random Forest Classifier", \
    	description="Random Forest Classifier." \
    	WHERE id=4002 AND locale="en"',
    'UPDATE operation_translation \
    	SET name="Random forest classifier", \
    		description="Random forest classifier." \
    	WHERE id=4002 AND locale="en"'),
    ('UPDATE operation_translation \
    	SET name="Classificador Random Forest", \
    		description="Classificador Random Forest."\
    	WHERE id=4002 AND locale="pt"',
    'UPDATE operation_translation \
    	SET name="Classificador random forest", \
			description="Classificador random forest." \
    	WHERE id=4002 AND locale="pt"')
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