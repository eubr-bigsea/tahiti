"""removing low level sklearn parameters

Revision ID: 20f9ae94a7f3
Revises: 54147db30380
Create Date: 2020-03-11 18:17:32.345486

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '20f9ae94a7f3'
down_revision = '54147db30380'
branch_labels = None
depends_on = None


def _undo_operation_form_field():
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
        column('enable_conditions', String))

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
    data = [

        (4120, "n_jobs", "INTEGER", "0", "10", None, "integer", None, None,
         "EXECUTION", "4024", None),
        (4126, "n_jobs", "INTEGER", "0", "4", None, "integer", None, None,
         "EXECUTION", "4025", None),
        (4155, "n_jobs", "INTEGER", "0", "9", "0", "integer", None, None,
         "EXECUTION", "4022", None),
        (4237, "n_jobs", "INTEGER", "0", "12", None, "integer", None, None,
         "EXECUTION", "4001", None),
        (4261, "n_jobs", "INTEGER", "0", "8", None, "integer", None, None,
         "EXECUTION", "4029", None),
        (4269, "n_jobs", "INTEGER", "0", "10", None, "integer", None, None,
         "EXECUTION", "4005", None),
        (4297, "n_jobs", "INTEGER", "0", "14", None, "integer", None, None,
         "EXECUTION", "4002", None),
        (4306, "n_jobs", "INTEGER", "0", "12", None, "integer", None, None,
         "EXECUTION", "4013", "this.type.internalValue === \"K-Means\""),
        (4336, "n_jobs", "INTEGER", "0", "10", None, "integer", None, None,
         "EXECUTION", "4030", None),

        (4157, "verbose", "INTEGER", "0", "11", "0", "integer", None, None,
         "EXECUTION", "4022", None),
        (4218, "verbose", "INTEGER", "0", "18", "0", "integer", None, None,
         "EXECUTION", "4009", None),
        (4239, "verbose", "INTEGER", "0", "14", "0", "integer", None, None,
         "EXECUTION", "4001", None),
        (4247, "verbose", "INTEGER", "0", "14", "0", "integer", None, None,
         "EXECUTION", "4030", None),
        (4267, "verbose", "INTEGER", "0", "8", "0", "integer", None, None,
         "EXECUTION", "4005", None),
        (4298, "verbose", "INTEGER", "0", "15", "0", "integer", None, None,
         "EXECUTION", "4002", None),
        (4304, "verbose", "INTEGER", "0", "7", "0", "integer", None, None,
         "EXECUTION", "4030", None),

        (4230, "presort", "INTEGER", "0", "12", "0", "checkbox", None, None,
         "EXECUTION", "4004", None),
        (4250, "presort", "TEXT", "0", "17", None, "auto", None, None,
         "EXECUTION",
         "4003", None),

        (4182, "cache_size", "DECIMAL", "0", "11", "200", "decimal", None, None,
         "EXECUTION", "4011", None),

        (4125, "copy_X", "INTEGER", "0", "7", "1", "checkbox", None, None,
         "EXECUTION", "4025", None),
        (4305, "copy_x", "INTEGER", "0", "11", "1", "integer", None, None,
         "EXECUTION", "4030", "this.type.internalValue === \"K-Means\""),

        (4221, "features", "TEXT", "1", "1", None, "attribute-selector", None,
         None, "EXECUTION", 4009, None),
        (4222, "label", "TEXT", "1", "2", None, "attribute-selector", None,
         None, "EXECUTION", 4009, None),
        (4223, "prediction", "TEXT", "0", "3", "prediction", "text", None, None,
         "EXECUTION", 4009, None),
        (4192, "features", "TEXT", "1", "1", None, "attribute-selector", None,
         None, "EXECUTION", "4020", None),
        (4193, "label", "TEXT", "1", "2", None, "attribute-selector", None,
         None, "EXECUTION", "4020", None),
        (4194, "prediction", "TEXT", "0", "4", "prediction", "text", None, None,
         "EXECUTION", "4020", None),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _undo_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = ('id', 'locale', 'label', 'help')
    data = [
        (4120, "en", "Parallel jobs",
         "The number of parallel jobs to run for neighbors search."),
        (4120, "pt", "Jobs paralelos",
         "Número de tarefas paralelas a serem executadas na pesquisa de "
         "vizinhos."),
        (4125, "en", "Copy",
         "If True, X will be copied; else, it may be overwritten."),
        (4125, "pt", "Copiar",
         "Se verdadeiro, X vai ser copiado; senão, pode ser sobrescrito."),
        (4126, "en", "Number of jobs",
         "The number of jobs to use for the computation."),
        (4126, "pt", "Número de jobs",
         "O número de jobs usados para a computação."),
        (4155, "en", "Number of jobs",
         "The number of jobs to run in parallel for both fit and predict."),
        (4155, "pt", "Números de jobs",
         "O número de jobs a serem executados em paralelo para o fit e o "
         "predict"),
        (4157, "en", "Verbose",
         "Controls the verbosity when fitting and predicting."),
        (4157, "pt", "Verbose", "Controla a verbosidade ao ajustar e prever."),
        (4182, "en", "Size of the kernel cache (in MB).",
         "Specify the size of the kernel cache (in MB)."),
        (4182, "pt", "Tamanho do cache em MB.",
         "Especificação do tamanho do cache em MB."),
        (4218, "en", "Verbose", "The verbosity level."),
        (4218, "pt", "Verbosidade", "O nível de verbosidade."),
        (4230, "en", "Presort",
         "Whether to presort the data to speed up the finding of best splits "
         "in fitting."),
        (4230, "pt", "Pré-classificação",
         "Se os dados devem ser pré-classificados para acelerar a localização "
         "das melhores divisões no ajuste."),
        (4237, "en", "Number of CPU cores",
         "Number of CPU cores used when parallelizing over classes if "
         "multi_class=""ovr""."),
        (4237, "pt", "Numero de núcleos do CPU",
         "Quantidade de núcleos do CPU utilizados para paralelização quando o "
         "atributo multi_class=""ovr""."),
        (4239, "en", "Verbose",
         "For the ""liblinear"" and ""lbfgs"" solvers set verbose to any "
         "positive number for verbosity."),
        (4239, "pt", "Verboso",
         "Para os solvers ""liblinear"" e ""lbfgs"" insira qualquer inteiro "
         "positivo como numéro de verbosidade."),
        (4247, "en", "Verbose",
         "Enable verbose output. If 1 then it prints progress and performance "
         "once in a while (the more trees the lower the frequency). If "
         "greater than 1 then it prints progress and performance for every "
         "tree."),
        (4247, "pt", "Saída detalhada",
         "Ativar saída detalhada. Se 1, ele imprime progresso e desempenho de "
         "vez em quando (quanto mais árvores, menor a frequência). Se maior "
         "que 1, imprime o progresso e o desempenho de todas as árvores."),
        (4250, "en", "Presort",
         "Whether to presort the data to speed up the finding of best splits "
         "in fitting."),
        (4250, "pt", "Pré-classificação",
         "Se os dados devem ser pré-classificados para acelerar a localização "
         "das melhores divisões no ajuste."),
        (4261, "en", "Number of jobs",
         "The number of parallel jobs to run for neighbors search."),
        (4261, "pt", "Número de tarefas",
         "O número de tarefas paralelas a serem executadas na pesquisa de "
         "vizinhos."),
        (4267, "en", "Verbose", "The verbosity level."),
        (4267, "pt", "Verbosidade", "O nível de verbosidade."),
        (4269, "en", "Number of jobs",
         "The number of CPUs to use to do the OVA (One Versus All, "
         "for multi-class problems) computation."),
        (4269, "pt", "Número de jobs",
         "O número de CPUs a serem usadas para calcular o OVA (One Versus "
         "All, para problemas de várias classes)."),
        (4297, "en", "Number of CPU cores",
         "Number of CPU cores used when parallelizing over classes if "
         "multi_class=""ovr""."),
        (4297, "pt", "Numero de núcleos do CPU",
         "Quantidade de núcleos do CPU utilizados para paralelização quando o "
         "atributo multi_class=""ovr""."),
        (4298, "en", "Verbose",
         "Controls the verbosity when fitting and predicting."),
        (4298, "pt", "Verboso",
         "Controle da verbosidade ao executar o treinamento e a predição."),
        (4304, "en", "Verbose", "Verbosity mode."),
        (4304, "pt", "Verbose", "Modo de verbosidade."),
        (4305, "en", "Center the data",
         "When pre-computing distances it is more numerically accurate to "
         "center the data first."),
        (4305, "pt", "Centralizar os dados",
         "Ao pré-calcular as distâncias, é mais preciso numericamente "
         "centralizar os dados primeiro."),
        (4306, "en", "Number of jobs",
         "The number of jobs to use for the computation."),
        (4306, "pt", "Número de jobs",
         "O número de jobs a serem usados para o cálculo."),
        (4336, "en", "Number of jobs", "The number of parallel jobs to run."),
        (4336, "pt", "Número de tarefas",
         "O número de tarefas paralelas a serem executadas."),
        (4221, "en", "Features", "Features."),
        (4221, "pt", "Atributo(s) previsor(es)", "Atributo(s) previsor(es)."),
        (4222, "en", "Label attribute", "Label attribute."),
        (4222, "pt", "Atributo com o rótulo", "Atributo com o rótulo."),
        (4223, "en", "Prediction attribute (new)",
         "Prediction attribute (new)."),
        (4223, "pt", "Atributo com a predição (novo)",
         "Atributo usado para predição (novo)."),
        (4192, "en", "Features", "Features."),
        (4192, "pt", "Atributo(s) previsor(es)", "Atributo(s) previsor(es)."),
        (4193, "en", "Label attribute", "Label attribute."),
        (4193, "pt", "Atributo com o rótulo", "Atributo com o rótulo."),
        (4194, "en", "Prediction attribute (new)",
         "Prediction attribute (new)."),
        (4194, "pt", "Atributo com a predição (novo)",
         "Atributo usado para predição (novo)."),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    # removing presort parameter from gbt-classifier e decision-tree-classifier
    # Removing n_jobs parameters form logistic-regression-model,
    # random-forest-classifier-model, perceptron-classifier-model,
    # sgd-regressor-model, gbt-regressor-model, random-forest-regressor-model,
    # huber-regressor-model, mlp-regressor-model
    # Removing verbose parameter from logistic-regression-model,
    # random-forest-classifier-model, perceptron-classifier-model,
    # sgd-regressor-model, gbt-regressor-model,
    # random-forest-regressor-model, huber-regressor-model, mlp-regressor-model
    # Removing cache_size from svm-classifier-model

    ("DELETE FROM operation_form_field_translation WHERE id IN (4120, 4126, "
     "4155, 4237, 4261, 4269,4297,4306,4336, 4230, 4250, 4157, 4218, 4239, "
     "4247, 4267, 4298, 4304, 4182, 4125, 4305, 4221, 4222, 4223, 4192, 4193, "
     "4194);",
     _undo_operation_form_field_translation),
    ("DELETE FROM operation_form_field WHERE id IN (4120, 4126, 4155, 4237, "
     "4261, 4269,4297,4306,4336, 4230, 4250, 4157, 4218, 4239, 4247, "
     "4267, 4298, 4304, 4182, 4125, 4305, 4221, 4222, 4223, 4192, 4193, 4194);",
     _undo_operation_form_field),

    # fixing dbscan as a transformation
    ("UPDATE operation SET type = 'TRANSFORMATION' WHERE id = 4032;",
     "UPDATE operation SET type = 'ACTION' WHERE id = 4032;"),

    # removing compss's dbscan and spark gaussian mixture
    ("DELETE FROM operation_platform WHERE platform_id = 4 AND "
     "operation_id IN (3020, 120);",
     "INSERT INTO operation_platform (operation_id, platform_id) "
     "VALUES (3020, 4), (120, 4);"),

    # changing kmeans "algorithm" translation
    ("UPDATE operation_form_field_translation SET label='Type' "
     "WHERE id = 4065 AND locale = 'en'",
     "UPDATE operation_form_field_translation SET label='Algorithm' "
     "WHERE id = 4065 AND locale = 'en'"
     ),

    ("UPDATE operation_operation_form SET operation_form_id = 4021 "
     "WHERE operation_form_id = 4022 AND operation_id IN (4026, 4029, 4030,"
     " 4035)",
     "UPDATE operation_operation_form SET operation_form_id = 4022 "
     "WHERE operation_form_id = 4021 AND operation_id IN (4026, 4029, 4030,"
     " 4035)"
     )

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


