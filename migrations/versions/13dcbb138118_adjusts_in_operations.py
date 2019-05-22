# coding=utf-8
"""adjusts_in_operations

Revision ID: 13dcbb138118
Revises: 2232f498d42e
Create Date: 2019-02-25 09:32:51.420862

"""
import json

from alembic import context
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = '13dcbb138118'
down_revision = '2232f498d42e'
branch_labels = None
depends_on = None

values = {
    'pt': ['1a parte', '2a parte'],
    'en': ['1st part', '2nd part'],
}

all_commands = [
    ('''UPDATE operation_form_field_translation SET label = 'Percentual',
     HELP = 'Percentual usado para dividir os dados' WHERE
        id = 16 AND locale = 'pt';''',
     '''UPDATE operation_form_field_translation SET label = 'Pesos',
     HELP = 'Pesos usados para dividir os dados' WHERE
        id = 16 AND locale = 'pt';'''),
    ('''UPDATE operation_form_field_translation SET label = 'Percentage',
     HELP = 'Percentage used to split the data' WHERE
        id = 16 AND locale = 'en';''',
     '''UPDATE operation_form_field_translation SET label = 'Weights',
     HELP = 'Weights used to split the data source' WHERE
        id = 16 AND locale = 'en';'''),

    ('''UPDATE operation_port_translation SET name = '1a. parte',
     description = 'Primeira parte dos dados divididos' WHERE
        id = 27 AND locale = 'pt';''',
     '''UPDATE operation_port_translation SET name = 'parte 1 dos dados',
     description = 'Dados de saída 1' WHERE
        id = 27 AND locale = 'pt';'''),

    ('''UPDATE operation_port_translation SET name = '1st part',
     description = 'First part of split data' WHERE
        id = 27 AND locale = 'en';''',
     '''UPDATE operation_port_translation SET name = 'splitted data 1',
     description = 'Output data 1' WHERE
        id = 27 AND locale = 'en';'''),

    ('''UPDATE operation_port_translation SET name = '2a. parte',
     description = 'Segunda parte dos dados divididos' WHERE
        id = 28 AND locale = 'pt';''',
     '''UPDATE operation_port_translation SET name = 'parte 2 dos dados',
     description = 'Dados de saída 2' WHERE
        id = 28 AND locale = 'pt';'''),

    ('''UPDATE operation_port_translation SET name = '2nd part',
     description = 'Second part of split data' WHERE
        id = 28 AND locale = 'en';''',
     '''UPDATE operation_port_translation SET name = 'splitted data 2',
     description = 'Output data 2' WHERE
        id = 28 AND locale = 'en';'''),

    ('''UPDATE operation_port SET `order` = 2, slug = 'split 1'
        WHERE id = 27''',
     '''UPDATE operation_port SET `order` = 1, slug = 'splitted data 1'
         WHERE id = 27'''
     ),
    ('''UPDATE operation_port SET `order` = 1, slug = 'split 2'
        WHERE id = 28''',
     '''UPDATE operation_port SET `order` = 2, slug = 'splitted data 2'
         WHERE id = 28'''
     ),

    # FIX translations, it is not necessary to undo
    ('''INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(107, 'pt', 'Avaliador', 'Avaliador')''',
     '''DELETE FROM operation_form_field_translation
        WHERE id = 107 and locale = 'pt' '''),

    ('''INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(108, 'pt', 'Partições', 'Partições')''',
     '''DELETE FROM operation_form_field_translation
        WHERE id = 108 and locale = 'pt' '''),

    ('''INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(109, 'pt', 'Semente', 'Semente')''',
     '''DELETE FROM operation_form_field_translation
        WHERE id = 109 and locale = 'pt' '''),

    ('''INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(110, 'pt', 'Otimizador', 'Otimizador')''',
     '''DELETE FROM operation_form_field_translation
        WHERE id = 110 and locale = 'pt' '''),

    ('''UPDATE operation_form_field_translation SET help =
        'Frequência mínima de documentos (DF)' WHERE id = 125 and locale = 'pt'
         ''', ''),

    ('''INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(126, 'pt', 'Número de tópicos (K)', 'Número de tópicos (K)')'''
     , '''DELETE FROM operation_form_field_translation
        WHERE id = 126 and locale = 'pt' '''),

    ('''INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(132, 'pt', 'Atributo(s) com as features',
        'Atributo(s) com as features')''',
     '''DELETE FROM operation_form_field_translation
        WHERE id = 132 and locale = 'pt' '''),

    ('''INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(133, 'pt', 'Arquivo shapefile', 'Arquivo shapefile')''',
     '''DELETE FROM operation_form_field_translation
        WHERE id = 133 and locale = 'pt' '''),

    ('''INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(152, 'pt', 'Termos por tópico(máx)',
        'Termos por tópico(máx)')''',
     '''DELETE FROM operation_form_field_translation
        WHERE id = 152 and locale = 'pt' '''),

    ('''INSERT INTO operation_form_field_translation(id, locale, label, help)
        VALUES(161, 'pt', 'Número de agrupamentos (K)',
        'Número de agrupamentos (K)')''',
     '''DELETE FROM operation_form_field_translation
        WHERE id = 161 and locale = 'pt' '''),

    ('''
        UPDATE operation_translation SET description =
        'Splits dataset into 2 different data sets using percentage. Uses an approximate algorithm to split data, so the percentages may be slightly different in results'
        WHERE id = 17 and locale = 'en'
    ''', '''
    UPDATE operation_translation SET description =
        'Splits dataset into 2 different data sets using weights'
        WHERE id = 17 and locale = 'en'
    '''),
    ('''
        UPDATE operation_translation SET description =
        'Divide os dados em 2 conjutos diferentes, distribuindo de acordo com o percentual. Usa um algoritmo aproximado, portanto os percentuais podem ser um pouco diferentes no resultado'
        WHERE id = 17 and locale = 'pt'
    ''', '''
    UPDATE operation_translation SET description =
        'Divide uma fonte de dados em 2 conjutos diferentes, distribuindo de acordo com pesos'
        WHERE id = 17 and locale = 'pt'
    '''),
    ('''
        UPDATE operation_form_field SET `default` = 50, `values` = '{values}'
        WHERE id = 16
    '''.format(values=json.dumps(values)), '''
        UPDATE operation_form_field SET `default` = null, `values` = '50'
            WHERE id = 16
    '''),
    ('UPDATE operation_form_field SET required = 0 WHERE id = 279',
     'UPDATE operation_form_field SET required = 1 WHERE id = 279')


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
            if cmd[1]:
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
