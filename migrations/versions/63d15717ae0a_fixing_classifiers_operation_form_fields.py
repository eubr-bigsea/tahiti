"""fixing classifiers operation form fields

Revision ID: 63d15717ae0a
Revises: 80e8e1eab0ba
Create Date: 2020-02-06 14:06:33.474348

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
revision = '63d15717ae0a'
down_revision = '9bb45622ba10'
branch_labels = None
depends_on = None

all_commands = [
    #KNN
    ("""UPDATE operation_form_field SET required = 1 WHERE id = 4254""",
    """UPDATE operation_form_field SET required = 0 WHERE id = 4254"""),

    #Naive Bayes
    ("""UPDATE operation_form_field SET `default` = '1.0' WHERE id = 4061""",
    """UPDATE operation_form_field SET `default` = '1' WHERE id = 4061"""),
    ("""UPDATE operation_form_field SET suggested_widget = 'checkbox' WHERE id = 4264""",
    """UPDATE operation_form_field SET suggested_widget = 'integer' WHERE id = 4264"""),
    ("""UPDATE operation_form_field SET `default` = '0.0' WHERE id = 4265""",
    """UPDATE operation_form_field SET `default` = '0' WHERE id = 4265"""),

    #Perceptron
	("""UPDATE operation_form_field SET suggested_widget = 'checkbox' WHERE id = 4266""",
    """UPDATE operation_form_field SET suggested_widget = 'integer' WHERE id = 4266"""),

    #MLP
    ("""UPDATE operation_form_field 
    	SET type = 'INTEGER',
    	    `default` = NULL,
    	    suggested_widget = 'integer'
    	WHERE id = 4274""",
    """UPDATE operation_form_field 
    	SET type = 'TEXT',
    	    `default` = 'auto',
    	    suggested_widget = 'text'
    	WHERE id = 4274"""),

   	# Logistic Regression
   	("""UPDATE operation_form_field
   		SET enable_conditions = 'this.solver.internalValue === "liblinear"'
   		WHERE id = 4233""",
   	"""UPDATE operation_form_field
   		SET enable_conditions = NULL
   		WHERE id = 4233"""),
   	("""UPDATE operation_form_field
   		SET enable_conditions = 'this.solver.internalValue === "liblinear"'
   		WHERE id = 4234""",
   	"""UPDATE operation_form_field
   		SET enable_conditions = NULL
   		WHERE id = 4234"""),
   	("""UPDATE operation_form_field
   		SET enable_conditions = 'this.penalty.internalValue === "elasticnet"'
   		WHERE id = 4238""",
   	"""UPDATE operation_form_field
   		SET enable_conditions = NULL
   		WHERE id = 4238"""),

   	# Support Vector Machine
   	("""UPDATE operation_form_field
   		SET enable_conditions = 'this.kernel.internalValue != "linear"'
   		WHERE id = 4178""",
   	"""UPDATE operation_form_field
   		SET enable_conditions = NULL
   		WHERE id = 4178"""),
   	("""UPDATE operation_form_field
   		SET enable_conditions = 'this.kernel.internalValue === "sigmoid" || this.kernel.internalValue === "poly"'
   		WHERE id = 4179""",
   	"""UPDATE operation_form_field
   		SET enable_conditions = NULL
   		WHERE id = 4179""")
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