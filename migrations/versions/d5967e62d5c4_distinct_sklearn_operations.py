# -*- coding: utf-8 -*-

"""Adding distinct sklearn operations

Revision ID: d5967e62d5c4
Revises: c6x2kllv52os
Create Date: 2018-07-10 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column,text


# revision identifiers, used by Alembic.
revision = 'd5967e62d5c4'
down_revision = 'c6x2kllv52os'
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
    (4001, 'logistic-regression',	1,'TRANSFORMATION','fa-exchange-alt'),
    (4002, 'random-forest-classifier',	1,'TRANSFORMATION','fa-random'),
    (4003, 'gbt-classifier',	1,'TRANSFORMATION','fa-tree'),
    (4004, 'decision-tree-classifier',	1,'TRANSFORMATION','fa-arrow-right'),
    (4005, 'perceptron-classifier',	1,'TRANSFORMATION','fa-angle-double-down'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category():
    # para pertencer as operacoes do Scikit-learn
    tb = table('operation_category',
                            column("id", Integer),
                            column("type", String),
                            )
    columns = ['id', 'type']
    data = [
        (4001, 'technology'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_category_translation():

    tb = table('operation_category_translation',
                            column("id", Integer),
                            column("locale", String),
                            column('name', String),
                            )
    columns = ['id', 'locale', 'name']
    data = [
        (4001, 'en', 'Scikit-learn'),
        (4001, 'pt', 'Scikit-learn'),
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
		(4001, 4),
        (4002, 4),
		(4003, 4),
		(4004, 4),
        (4005, 4),

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
			(4001, 8),
	        (4001, 18),
			(4001, 4001),

            (4002, 8),
	        (4002, 18),
			(4002, 4001),

            (4003, 8),
	        (4003, 18),
			(4003, 4001),

            (4004, 8),
	        (4004, 18),
			(4004, 4001),

            (4005, 8),
	        (4005, 18),
			(4005, 4001),

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
        (4001, 1, 1, 'execution'),
		(4002, 1, 1, 'execution'),
		(4003, 1, 1, 'execution'),
		(4004, 1, 1, 'execution'),
		(4005, 1, 1, 'execution'),
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
        (4001, 'en', 'Execution'),
        (4001, 'pt', 'Execução'),
        (4002, 'en', 'Execution'),
        (4002, 'pt', 'Execução'),
		(4003, 'en', 'Execution'),
        (4003, 'pt', 'Execução'),
		(4004, 'en', 'Execution'),
        (4004, 'pt', 'Execução'),
		(4005, 'en', 'Execution'),
        (4005, 'pt', 'Execução'),
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
		(4001, 39),
		(4001, 40),
		(4001, 41),
		(4001, 43),
		(4001, 110),
		(4001, 4001),

		(4002, 39),
		(4002, 40),
		(4002, 41),
		(4002, 43),
		(4002, 110),
		(4002, 4002),

		(4003, 39),
		(4003, 40),
		(4003, 41),
		(4003, 43),
		(4003, 110),
		(4003, 4003),

		(4004, 39),
		(4004, 40),
		(4004, 41),
		(4004, 43),
		(4004, 110),
		(4004, 4004),

		(4005, 39),
		(4005, 40),
		(4005, 41),
		(4005, 43),
		(4005, 110),
		(4005, 4005),
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
        (4001, 'en', 'Logistic regression Classifier', 'Performs logistic regression.'), # logistic-regression
        (4001, 'pt', 'Classificador Regressão Logistica', 'Classificador por Regressão Logistica.'),

        (4002, 'en', 'Random forest classifier', 'Random forest classifier.'),  # random-forest-classifier
        (4002, 'pt', 'Classificador random forest', 'Classificador random forest.'),

		(4003, 'en', 'GBT Classifier', 'Gradient-Boosted Trees (GBTs) learning algorithm for classification. It supports binary labels, as well as both continuous and categorical features.'), # gbt-classifier
        (4003, 'pt', 'Classificador GBT', 'Algoritmo de aprendizado para classificação Gradient-Boosted Trees (GBTs). Suporta rótulos binários e features contínuas e categóricas.'),

		(4004, 'en', 'Decision tree classifier', 'Decision tree learning algorithm for classification. It supports both binary and multiclass labels, as well as both continuous and categorical features.'),  # decision-tree-classifier
        (4004, 'pt', 'Classif. Árv. Decisão', 'Classificador baseado em árvores de decisão. Suporta tanto rótulos binários quanto multiclasses e features contínuas e categóricas.'),

        (4005, 'en', 'Perceptron Classifier', 'Classifier trainer based on the Multilayer Perceptron.'),  # perceptron-classifier
        (4005, 'pt', 'Classificador Perceptron', 'Classificador baseado no Perceptron de Multicamadas.'),

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

    	(4001, 'OUTPUT', None, 4001, 1, 'MANY', 'algorithm'),
        (4002, 'OUTPUT', None, 4002, 1, 'MANY', 'algorithm'),
        (4003, 'OUTPUT', None, 4003, 1, 'MANY', 'algorithm'),
        (4004, 'OUTPUT', None, 4004, 1, 'MANY', 'algorithm'),
        (4005, 'OUTPUT', None, 4005, 1, 'MANY', 'algorithm'),

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
		(4001, 'en', 'algorithm', 'Untrained classification model'),
		(4001, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),
        (4002, 'en', 'algorithm', 'Untrained classification model'),
		(4002, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),
        (4003, 'en', 'algorithm', 'Untrained classification model'),
		(4003, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),
        (4004, 'en', 'algorithm', 'Untrained classification model'),
		(4004, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),
        (4005, 'en', 'algorithm', 'Untrained classification model'),
		(4005, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),

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

		(4001, 5),
		(4002, 5),
        (4003, 5),
        (4004, 5),
        (4005, 5),

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

		#logistic-regression
        (4001, 'tol', 'FLOAT', 	0, 1, 0.0001, 'decimal', None, None, 'EXECUTION', 4001),
        (4002, 'regularization', 'FLOAT', 0, 2, 1.0, 'decimal', None, None, 'EXECUTION', 4001),
        (4003, 'seed', 'INTEGER', 0, 3, None, 'integer', None, None, 'EXECUTION', 4001),
        (4004, 'solver', 'TEXT', 0, 4, 'liblinear', 'dropdown', None,
		'[{"key": \"newton-cg\", \"value\": \"newton-cg\"}, '
		'{\"key\": \"lbfgs\", \"value\": \"lbfgs\"}, '
        '{\"key\": \"liblinear\", \"value\": \"liblinear\"}, '
        '{\"key\": \"sag\", \"value\": \"sag\"}, '
        '{\"key\": \"saga\", \"value\": \"saga\"}]', 'EXECUTION', 4001),
        (4005, 'max_iter', 'INTEGER', 0, 5, 100, 'integer', None, None, 'EXECUTION', 4001),

        #random-forest-classifier
        (4006, 'n_estimators', 'INTEGER', 0, 1, 10, 'integer', None, None, 'EXECUTION', 4002),
        (4007, 'max_depth', 'INTEGER', 0, 2, None, 'integer', None, None, 'EXECUTION', 4002),
        (4008, 'min_samples_split', 'FLOAT', 0, 3, None, 'decimal', None, None, 'EXECUTION', 4002),
        (4009, 'min_samples_leaf', 'FLOAT', 0, 4, None, 'decimal', None, None, 'EXECUTION', 4002),
        (4010, 'seed', 'INTEGER', 0, 5, None, 'integer', None, None, 'EXECUTION', 4002),

        #gbt-classifier
        (4011, 'loss', 'TEXT', 0, 1, 'deviance', 'dropdown', None,
		'[{\"key\": \"deviance\", \"value\": \"deviance\"}, '
		'{\"key\": \"exponential\", \"value\": \"exponential\"}]', 'EXECUTION', 4003),
        (4012, 'learning_rate', 'FLOAT', 0, 2, 0.01, 'decimal', None, None, 'EXECUTION', 4003),
        (4013, 'n_estimators', 'INTEGER', 0, 3, 100, 'integer', None, None, 'EXECUTION', 4003),
        (4014, 'min_samples_split', 'FLOAT', 0, 4, None, 'decimal', None, None, 'EXECUTION', 4003),
        (4015, 'min_samples_leaf', 'FLOAT', 0, 5, None, 'decimal', None, None, 'EXECUTION', 4003),

        #decision-tree-classifier
        (4016, 'max_depth', 'INTEGER', 0, 1, None, 'integer', None, None, 'EXECUTION', 4004),
        (4017, 'min_samples_split', 'FLOAT', 0, 2, None, 'decimal', None, None, 'EXECUTION', 4004),
        (4018, 'min_samples_leaf', 'FLOAT', 0, 3, None, 'decimal', None, None, 'EXECUTION', 4004),
        (4019, 'min_weight', 'FLOAT', 0, 4, 0.0, 'decimal', None, None, 'EXECUTION', 4004),
        (4020, 'seed', 'INTEGER', 0, 5, None, 'integer', None, None, 'EXECUTION', 4004),

        #perceptron-classifier
        (4021, 'penalty', 'TEXT', 0, 1, None, 'dropdown', None,
		'[{\r\n  "key": "l2", "value": \"l2\"},  '
		'{ \"key\": \"l1\", \"value\": \"l1\"}]', 'EXECUTION', 4005),
        (4022, 'alpha', 'FLOAT', 0, 2, 0.0001, 'decimal', None, None, 'EXECUTION', 4005),
        (4023, 'max_iter', 'INTEGER', 0, 3, 1000, 'integer', None, None, 'EXECUTION', 4005),
        (4024, 'tol', 'FLOAT', 0, 4, 0.001, 'decimal', None, None, 'EXECUTION', 4005),
        (4025, 'shuffle', 'INTEGER', 0, 5,  None, 'checkbox', None, None,'EXECUTION', 4005),
        (4026, 'seed', 'INTEGER', 0, 6, None, 'integer', None, None, 'EXECUTION', 4005),

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
        #logistic-regression
        (4001,'en', 'Tolerance','Tolerance for stopping criteria.'),
        (4002,'en', 'Inverse of regularization strength','Like in support vector machines, smaller values specify stronger regularization.'),
        (4003,'en', 'Seed', 'The seed of the pseudo random number generator to use when shuffling the data.'),
        (4004,'en', 'Solver','Note that sag and saga fast convergence is only guaranteed on features with approximately the same scale.'),
        (4005,'en', 'Maximum number of iterations','Useful only for the newton-cg, sag and lbfgs solvers.'),
        (4001,'pt', 'Tolerancia','Tolerância para critérios de parada.'),
        (4002,'pt', 'força de regularização inversa','Como nas máquinas de vetores de suporte, valores menores especificam uma regularização mais forte.'),
        (4003,'pt', 'Semente', 'A semente do gerador de números pseudo-aleatórios a ser usada ao embaralhar os dados.'),
        (4004,'pt', 'Solver','A convergência rápida de sag e saga é garantida apenas em atributos com aproximadamente a mesma escala.'),
        (4005,'pt', 'Número máximo de iterações', 'Apenas para solvers: newton-cg, sag e lbfgs.'),

        #random-forest-classifier
        (4006, 'en', 'Number of trees','The number of trees in the forest.'),
        (4007, 'en', 'Maximum depth','The maximum depth of the tree.'),
        (4008, 'en', 'Minimum internal node','Percentage of the minimum number of samples required to split an internal node.'),
        (4009, 'en', 'Minimum leaf node','Percentage of the minimum number of samples required to be at a leaf node.'),
        (4010, 'en', 'Seed','The seed of the pseudo random number generator to use when shuffling the data.'),
        (4006, 'pt', 'Número de árvores','Número de árvores na floresta.'),
        (4007, 'pt', 'Profundidade máxima','Profundidade máxima na árvore.'),
        (4008, 'pt', 'Nó interno mínimo', 'Porcentagem do número mínimo de amostras necessárias para dividir um nó interno.'),
        (4009, 'pt', 'Nó de folha mínima', 'Porcentagem do número mínimo de amostras necessárias para estar em um nó folha.'),
        (4010, 'pt', 'Semente', 'A semente do gerador de números pseudo-aleatórios a ser usada ao embaralhar os dados.'),

        #gbt-classifier
        (4011, 'en', 'Loss function to be optimized',' deviance refers to deviance (= logistic regression) for classification with probabilistic outputs. For loss exponential gradient boosting recovers the AdaBoost algorithm.'),
        (4012, 'en', 'Learning rate','Learning rate shrinks the contribution of each tree by learning rate. There is a trade-off between learning rate and number of estimators.'),
        (4013, 'en', 'Number of boosting stages','Gradient boosting is fairly robust to over-fitting so a large number usually results in better performance.'),
        (4014, 'en', 'Minimum samples split','Percentage of the minimum number of samples required to split an internal node.'),
        (4015, 'en', 'Minimum samples leaf', 'Percentage of the minimum number of samples required to be at a leaf node.'),
        (4011, 'pt', 'Função de perda a ser otimizada','Desvio refere-se a desvio (= regressão logística) para classificação com saídas probabilísticas. Para aumento de gradiente exponencial de perda recupera o algoritmo AdaBoost.'),
        (4012, 'pt', 'Taxa de aprendizado','A taxa de aprendizado reduz a contribuição de cada árvore pela taxa de aprendizado. Existe um trade-off entre taxa de aprendizado e número de estimadores.'),
        (4013, 'pt', 'Número de estágios de boosting','O aumento de gradiente é bastante robusto para o ajuste excessivo, portanto, um grande número geralmente resulta em melhor desempenho.'),
        (4014, 'pt', 'Nó interno mínimo', 'Porcentagem do número mínimo de amostras necessárias para dividir um nó interno.'),
        (4015, 'pt', 'Nó de folha mínima', 'Porcentagem do número mínimo de amostras necessárias para estar em um nó folha.'),

        #decision-tree-classifier
        (4016, 'en', 'Maximum depth', 'The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.'),
        (4017, 'en', 'Minimum samples split','Percentage of the minimum number of samples required to be at a leaf node.'),
        (4018, 'en', 'Minimum samples leaf','Percentage of the minimum number of samples required to be at a leaf node.'),
        (4019, 'en', 'Sum total of weights','The minimum weighted fraction of the sum total of weights (of all the input samples) required to be at a leaf node. Samples have equal weight when sample_weight is not provided.'),
        (4020, 'en', 'Seed', 'The seed of the pseudo random number generator to use when shuffling the data.'),
        (4016, 'pt', 'Profundidade máxima','Profundidade máxima na árvore.'),
        (4017, 'pt', 'Nó interno mínimo', 'Porcentagem do número mínimo de amostras necessárias para dividir um nó interno.'),
        (4018, 'pt', 'Nó de folha mínima', 'Porcentagem do número mínimo de amostras necessárias para estar em um nó folha.'),
        (4019, 'pt', 'Soma total de pesos','A fração ponderada mínima da soma total de pesos (de todas as amostras de entrada) necessária para estar em um nó folha. As amostras têm peso igual quando não é fornecido.'),
        (4020, 'pt', 'Semente', 'A semente do gerador de números pseudo-aleatórios a ser usada ao embaralhar os dados.'),

        #perceptron-classifier
        (4021, 'en', 'Penalty', 'The penalty (aka regularization term) to be used.'),
        (4022, 'en', 'Alpha', 'Constant that multiplies the regularization term if regularization is used.'),
        (4023, 'en', 'Maximum number of iterations', 'The maximum number of passes over the training data (aka epochs).'),
        (4024, 'en', 'Tolerance', 'The stopping criterion. If it is not None, the iterations will stop when (loss > previous_loss - tol).'),
        (4025, 'en', 'Shuffle', 'Whether or not the training data should be shuffled after each epoch.'),
        (4026, 'en', 'Seed', 'The seed of the pseudo random number generator to use when shuffling the data.'),
        (4021, 'pt', 'Penalty', 'A penalidade (termo de regularização) a ser usada.'),
        (4022, 'pt', 'Alpha', 'Constante que multiplica o prazo de regularização se a regularização é usada.'),
        (4023, 'pt', 'Número máximo de iterações', 'O número máximo de passes nos dados de treinamento (também conhecidos como epochs).'),
        (4024, 'pt', 'Tolerância', 'Tolerância para critérios de parada.'),
        (4025, 'pt', 'Shuffle', 'Se os dados de treinamento devem ou não ser embaralhados após cada época.'),
        (4026, 'pt', 'Semente', 'A semente do gerador de números pseudo-aleatórios a ser usada ao embaralhar os dados.'),
	]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)



all_commands = [
	(_insert_operation_category, 'DELETE FROM operation_category WHERE id > 4000' ),
	(_insert_operation_category_translation, 'DELETE FROM operation_category_translation WHERE id > 4000' ),
	(_insert_operation, 'DELETE FROM operation WHERE id > 4000'),
	(_insert_new_operation_platform, 'DELETE FROM operation_platform WHERE operation_id > 4000' ),
	(_insert_operation_category_operation, 'DELETE FROM operation_category_operation WHERE operation_id > 4000'),
	(_insert_operation_form, 'DELETE FROM operation_form WHERE id > 4000'),
	(_insert_operation_form_translation, 'DELETE FROM operation_form_translation WHERE id > 4000'),
	(_insert_operation_operation_form, 'DELETE FROM operation_operation_form WHERE operation_id > 4000'),
	(_insert_operation_translation, 'DELETE FROM operation_translation WHERE id > 4000'),
	(_insert_operation_port, 'DELETE FROM operation_port WHERE id > 4000' ),
	(_insert_operation_port_translation, 'DELETE FROM operation_port_translation WHERE id > 4000' ),
	(_insert_operation_port_interface_operation_port, 'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id > 4000'),
	(_insert_operation_form_field, 'DELETE FROM operation_form_field WHERE id > 4000'),
	(_insert_operation_form_field_translation, 'DELETE FROM operation_form_field_translation WHERE id > 4000' ),
	]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
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
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    session.commit()
