"""Add script to join

Revision ID: 6ce4a4ac085f
Revises: 5a2676b63d2d
Create Date: 2024-06-21 09:35:03.436291

"""
from alembic import context
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = '6ce4a4ac085f'
down_revision = '5a2676b63d2d'
branch_labels = None
depends_on = None

def _execute(conn, cmd):
    if isinstance(cmd, str):
        conn.execute(cmd)
    elif isinstance(cmd, list):
        for row in cmd:
            conn.execute(row)
    else: # it's a method
        cmd(conn)


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()
    commands = [
        '''
        INSERT INTO 
            operation_script
        VALUES 
            (null, 'JS_CLIENT', 1, 
                'task.uiPorts.inputs.push({attributes: task.uiPorts.output}); joinSuffixDuplicatedAttributes2(task);', 
                2108);
        '''
    ]
    try:
        for cmd in commands:
            _execute(conn, cmd)
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()

    commands = [
        'DELETE FROM operation_script WHERE operation_id = 2108'
    ]
    try:
        for cmd in reversed(commands):
            _execute(conn, cmd)
    except:
        session.rollback()
        raise
    session.commit()
