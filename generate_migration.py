import os
import sys
import uuid
import argparse
import sqlalchemy
from tahiti.models import *
from sqlalchemy.orm import class_mapper
from jinja2 import Environment, BaseLoader
from textwrap import dedent
from alembic.config import Config
from alembic import command


TEMPLATE='''    
    """{{args.message}}

    Revision ID: {{new_revision}} 
    Revises: {{args.revision}}
    """
    from alembic import context
    from alembic import op
    from sqlalchemy import Integer, String, Text, Boolean
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.sql import table, column

    # revision identifiers, used by Alembic.
    revision = '{{new_revision}}'
    down_revision = '{{args.revision}}'
    branch_labels = None
    depends_on = None

    # --------------------------------------------------------------
    # ATENTION: You must revise this auto-generated code.
    # Please, review offsets and commands before running a migration
    # and optionally, perform a database backup. If everything is 
    # OK, remove this comment.
    # --------------------------------------------------------------
    {# extra line #}

    {%- for offset in offsets %}
    BASE_{{offset}} = {{args.id}}
    {%- endfor %} 
    {%- for entity in entities %}
    {%- set mapper = class_mapper(entity) %}
    {# extra line #}
    def _insert_{{entity.__table__}}(conn):
        tb = table('{{entity.__table__}}',
            {%- for c in mapper|get_properties%}
                    column('{{c.expression.name}}', {{c.expression.type|get_type}})
            {%- if not loop.last %}, {% endif -%}
            {%- endfor %})
        columns = [c.name for c in tb.columns]
        data = [
          {%- for i in range(entity|get_totals(args))%}
            {%- set outer_loop = loop %}
          [
        {%- for c in mapper|get_properties -%}
            {{c|get_placeholder(outer_loop, entity)}}
            {%- if not loop.last %}, {% endif -%}
        {%- endfor %}]
        {%- if not loop.last %}, {% endif -%}
        {%- endfor %}
        ]
        rows = [dict(zip(columns, row)) for row in data]
        op.bulk_insert(tb, rows)
    
    def _delete_{{entity.__table__}}(conn):
        conn.execute(
            'DELETE from {{entity.__table__}} WHERE id BETWEEN %s AND %s', 
            BASE_{{entity.__table__.name|get_base_name}} + 1, {# -#}
            BASE_{{entity.__table__.name|get_base_name}} + {{entity|get_totals(args)}})
    {%- endfor %}
    {# extra line #}
    {%- for assoc, tables in associations.items() %}
    def _insert_{{assoc}}(conn):
        tb = table('{{assoc}}',
            {%- for c in tables %}
                    column('{{c}}_id', Integer)
            {%- if not loop.last%}, {%endif%}
            {%- endfor %})
        columns = [c.name for c in tb.columns]
        data = [
        ]
        rows = [dict(list(zip(columns, row))) for row in data]
        op.bulk_insert(tb, rows)
    
    def _delete_{{assoc}}(conn):
        return 'SQL'
    {# extra line #}
    {%- endfor %}

    def _execute(conn, cmd):
        if isinstance(cmd, str):
            conn.execute(cmd)
        elif isinstance(cmd, list):
            for row in cmd:
                conn.execute(row)
        else: # it's a method
            cmd(conn)

    # -------------------------------------------------------

    def upgrade():
        ctx = context.get_context()
        session = sessionmaker(bind=ctx.bind)() 
        conn = session.connection()
        commands = [
        {%- for entity in entities %}
            _insert_{{entity.__table__}},
        {%- endfor %}
        {%- for assoc, tables in associations.items() %}
            _insert_{{assoc}},
        {%- endfor %}
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
    
        # Remove it if your DB doesn't support disabling FK checks
        conn.execute('SET FOREIGN_KEY_CHECKS=0;')
        commands = [
        {%- for entity in entities %}
            _delete_{{entity.__table__}},
        {%- endfor %}
        {%- for assoc, tables in associations.items() %}
            _delete_{{assoc}},
        {%- endfor %}
        ]
 
        try:
            for cmd in reversed(commands):
                _execute(conn, cmd)
        except:
            session.rollback()
            raise
        # Remove it if your DB doesn't support disabling FK checks
        conn.execute('SET FOREIGN_KEY_CHECKS=1;')
        session.commit()
    
    '''
def get_properties(mapper):
     return [c for c in mapper.iterate_properties
             if hasattr(c, 'expression') and 
             (not c.expression.nullable or 
                hasattr(c.expression, 'table'))]

def get_type(value):
    v = value.__class__.__name__
    return v if v not in ['Unicode', 'Enum', 'LONGTEXT'] else 'String'

def get_base_name(name):
    if name in ['platform', 'platform_translation']:
        name = 'PLATFORM'
    elif name in ['operation', 'operation_translation', 'operation_script']:
        name = 'OP'
    elif name in ['operation_form', 'operation_form_translation']:
        name ='FORM'
    elif name in ['operation_port_interface', 'operation_port_interface_translation']:
        name = 'INTERFACE'
    elif name in ['operation_category', 'operation_category_translation']:
        name = 'CATEGORY'
    elif name in ['operation_form_field', 'operation_form_field_translation']:
        name = 'FORM_FIELD'
    else:
        raise ValueError(f'Invalid entity: {name}')
    return name
 
def get_placeholder(value, loop, entity):
    counter = loop.index
    v = value.expression.type.__class__.__name__
    if value.expression.name == 'id':
        name = get_base_name(entity.__table__.name)
        return f'BASE_{name} + {counter}'
    elif v in ['Enum']:
        return f"'{value.expression.type.enums[0]}'"
    elif v in ['String', 'Unicode', 'LONGTEXT', 'UnicodeText']:
        return f"'{value.expression.name}'" 
    elif v in ['Integer']:
        return 0
    elif v in ['Boolean']:
        return 0
    else:
        raise ValueError(f'Unknown type: {v}')

def rev_id():
    return 'a' + uuid.uuid4().hex[-11:]

def get_totals(entity, args):
    name = entity.__table__.name
    if name in ['platform', 'platform_translation']:
        return args.platforms
    elif name in ['operation', 'operation_translation', 'operation_script']:
        return args.operations
    elif name in ['operation_form', 'operation_form_translation']:
        return args.forms
    elif name in ['operation_port_interface', 'operation_port_interface_translation']:
        return args.interfaces
    elif name in ['operation_category', 'operation_category_translation']:
        return args.categories
    elif name in ['operation_form_field', 'operation_form_field_translation']:
        return args.fields
    else:
        raise ValueError(f'Invalid entity: {name}')

def main(args):
    entities = []
    associations = {}
    offsets = []
    totals = []

    if args.platforms > 0:
        entities += [Platform, PlatformTranslation]
        offsets.append('PLATFORM')
    if args.operations > 0:
        entities += [Operation, OperationTranslation, 
            OperationScript,
        ]
        associations.update({
            'operation_category_operation': ['operation', 'category'], 
            'operation_operation_form': ['operation', 'form'], 
            'operation_subset_operation': ['operation', 'operation_subset'], 
        })
        offsets.append('OP')
    if args.categories > 0:
        entities += [OperationCategory, OperationCategoryTranslation]
        offsets.append('CATEGORY')
    if args.forms > 0:
        entities += [OperationForm, OperationFormTranslation]
        offsets.append('FORM')
    if args.fields > 0:
        entities += [OperationFormField, OperationFormFieldTranslation]
        offsets.append('FORM_FIELD')
    if args.ports > 0:
        entities += [OperationPort, OperationPortTranslation]
        associations.update({
           'operation_port_interface_operation_port ': 
            ['operation_port_interface', 'operation_port']
        })
        offsets.append('PORT')
    if args.interfaces > 0:
        entities += [OperationPortInterface, OperationPortInterfaceTranslation]
        offsets.append('INTERFACE')
    #for e in entities:
    template = dedent(TEMPLATE).strip()
    #mapper = class_mapper(e)
    #for c in mapper.iterate_properties:
    #    if isinstance(c, sqlalchemy.orm.ColumnProperty):
    #        import pdb; pdb.set_trace()
    #        print(c)
    env = Environment(loader=BaseLoader)
    env.filters['get_type'] = get_type
    env.filters['get_base_name'] = get_base_name
    env.filters['get_properties'] = get_properties
    env.filters['get_totals'] = get_totals
    env.filters['get_placeholder'] = get_placeholder
    revision_id = rev_id()
    
    jinja_template = env.from_string(template)
    data = {
        'offsets': offsets,
        'entities': entities,
        'associations': associations, 
        'class_mapper': class_mapper, 
        'args': args, 
        'new_revision': revision_id,
        'totals': totals
    }
    data = jinja_template.render(**data)
    comment = args.message

    out_name = os.path.join('migrations', 'versions', 
        revision_id + '_' + comment.lower().replace(' ', '_') + '.py')
    with open(out_name, 'w') as f:
        print(dedent(data), file=f)
    print(f'Generated {out_name}.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--categories", type=int, 
        help="Number of categories", default=0)
    parser.add_argument("-f", "--forms", type=int, 
        help="Number of forms", default=0)
    parser.add_argument("-d", "--fields", type=int, 
        help="Number of forms fields", default=0)
    parser.add_argument("-i", "--interfaces", type=int, 
        help="Number of port interfaces", default=0)
    parser.add_argument("--id", type=int, 
        help="Id offset", required=True)
    parser.add_argument("-o", "--operations", type=int, 
        help="Number of operations", default=0)
    parser.add_argument("-p", "--platforms", type=int, 
        help="Number of platforms", default=0)
    parser.add_argument("-t", "--ports", type=int, 
        help="Number of ports", default=0)
    parser.add_argument("-r", "--revision", type=str, 
        help="Current revision id (obtained from flask db current)",
        required=True)
    parser.add_argument("-m", "--message", type=str, 
        help="Message used to document the migration and define output filename",
        required=True)
    args = parser.parse_args()
    main(args)

