"""standardizing sklearn seed

Revision ID: 953911f74e49
Revises: 20f9ae94a7f3
Create Date: 2020-03-17 07:03:09.768014

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '953911f74e49'
down_revision = '20f9ae94a7f3'
branch_labels = None
depends_on = None

all_commands = [
    # removing old sklearn forms that arent used by any operation
    ("DELETE FROM operation_form_field_translation WHERE id in "
     "(4158, 4185,4199,4210,4249,4303,4309,4312,4313,4322,4323,4324,4325,"
     "4332,4333,4334,4335,4337,4338,4339,4340);", ""),
    ("DELETE FROM operation_form_field WHERE id in "
     "(4158, 4185,4199,4210,4249,4303,4309,4312,4313,4322,4323,4324,4325,"
     "4332,4333,4334,4335,4337,4338,4339,4340);", ""),
    ("DELETE FROM operation_form WHERE id = 4030", ""),

    # standardizing sklearn's seed
    ("UPDATE operation_form_field SET name = 'random_state' "
     "WHERE id IN (4003, 4010,4020,4026,4032,4038,4049,4059,4063,4069,4097, "
     "4104, 4143, 4326);",
     "UPDATE operation_form_field SET name = 'seed' "
     "WHERE id IN (4003, 4010,4020,4026,4032,4038,4049,4059,4063,4069,4097, "
     "4104, 4143, 4326);"),

    ("UPDATE operation_form_field_translation SET label='Random State', help="
     "'Seed used by the random number generator. Also used for "
     "reproducibility.' WHERE locale = 'en' AND id IN (4003, 4010,4020,4026,"
     "4032,4038,4049,4059,4063,4069,4097, 4104, 4143, 4326);",
     "UPDATE operation_form_field_translation SET label='Seed', help='Seed "
     "used by the random number generator. Also used for reproducibility.' "
     "WHERE locale = 'en' AND id IN (4003, 4010,4020,4026,4032,4038,4049,4059,"
     "4063,4069,4097,  4104, 4143, 4326);"),

    ("UPDATE operation_form_field_translation SET label='Estado Aleatório',"
     "help = 'Semente utilizada pelo gerador de números aleatórios. Também "
     "utilizada para reprodutibilidade.' "
     "WHERE locale = 'pt' AND id IN (4003, 4010,4020,4026,4032,4038,4049,4059,"
     "4063,4069,4097, 4104, 4143, 4326);",
     "UPDATE operation_form_field_translation SET label='Semente', help="
     "'Semente utilizada pelo gerador de números aleatórios. Também utilizada "
     "para reprodutibilidade.' "
     "WHERE locale = 'pt' AND id IN (4003, 4010,4020,4026,4032,4038,4049,4059,"
     "4063,4069,4097, 4104, 4143, 4326);"),

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
