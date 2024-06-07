"""Add missing visualization operation

Revision ID: 5a2676b63d2d
Revises: 32eebe6744e5
Create Date: 2024-06-07 09:02:46.129660

"""
from alembic import op, context
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a2676b63d2d'
down_revision = '32eebe6744e5'
branch_labels = None
depends_on = None


def upgrade():
    commands = [
    "insert into operation values(145, 'visualization', 1, 'VISUALIZATION', 'fa-chart-line', null, null);",
    "insert into operation_platform values(145, 1);",
    "insert into operation_platform values(145, 4);",
    "insert into operation_port values(354, 'visualization', 'OUTPUT', null, 1, 'MANY', 145);",
    "insert into operation_port values(355, 'input data', 'INPUT', null, 1, 'ONE', 145);",
    "insert into operation_port_translation values(354, 'en', 'visualization', 'Visualization');",
    "insert into operation_port_translation values(354, 'pt', 'visualização', 'Visualização');",
    "insert into operation_port_translation values(355, 'en', 'input data', 'Input data');",
    "insert into operation_port_translation values(355, 'pt', 'dados de entrada', 'Dados de entrada');",
    ]
    _execute(commands)

def _execute(commands):
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    conn = session.connection()
    try:
        for cmd in commands:
            conn.execute(cmd)
    except:
        session.rollback()
        raise
    session.commit()

def downgrade():
    commands = [
        'delete from operation_port_translation where id in (354,355)',
        'delete from operation_port where id in (354, 355)',
        'delete from operation_platform where operation_id = 145',
        'delete from operation where id = 145'
    ]
    _execute(commands)
    
