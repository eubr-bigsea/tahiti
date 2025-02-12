from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

import argparse
# import pprint 
import sys

def connect_to_database(db_url):
    """
    Conecta ao banco de dados usando a URL fornecida e retorna uma sessão e metadados.
    
    Args:
        db_url (str): URL de conexão do banco de dados.
    
    Returns:
        session: Sessão para executar operações no banco de dados.
        metadata: Objeto MetaData contendo informações sobre as tabelas.
    """
    try:
        if "/tahiti" not in db_url:
            db_url += "/tahiti"

        engine = create_engine(db_url, echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()

        metadata = MetaData()
        metadata.reflect(bind=engine)  # Carrega as informações do esquema do banco de dados
        
        print(f"Conexão bem-sucedida ao banco de dados `{db_url}`!")
        return session, metadata
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None, None

def execute_custom_query(session, query, single_row=False):
    """
    Executa uma query SQL personalizada e retorna os resultados.

    Args:
        session (Session): Sessão ativa do SQLAlchemy.
        query (str): Query SQL a ser executada.
        single (boolean): Se o retorno será uma única linha ou várias.

    Returns:
        list: Lista de resultados como dicionários.
    """
    try:
        results = session.execute(text(query))
        if single_row:
            data = results.fetchone()
        else:
            data = results.fetchall()
        return data
    except Exception as e:
        print(f"Erro ao executar a query: {e}")
        return []
    

def get_current_id(session, full_table_name):
    """
    Recupera qual é o maior `id` de uma tabela.
    
    Args:
        session (Session): Sessão ativa do SQLAlchemy.
        full_table_name (str): Nome da tabela alvo no formato `database.table`.
    
    Returns:
        current_id (int): O id mais atual da tabela.
    """
    query = f"SELECT MAX(id) FROM {full_table_name};"
    current_id = execute_custom_query(session, query, single_row=True)[0]
    if not current_id:
        current_id = 0
    return current_id 


def get_user_info(session, user_login):
    """
    Recupera informações do usuário no banco de dados alvo baseado no seu login.
    
    Args:
        session (Session): Sessão ativa do SQLAlchemy.
        user_login (str): Login salvo no Thorn.
        
    Returns:
        dict: Um dicionário contendo informações do user_id, user_name e user_login
    
    """
    query = f"SELECT id, first_name FROM thorn.user WHERE login = '{user_login}';"
    r = execute_custom_query(session, query, single_row=True)
    if r:
        return {'user_id': r[0], "user_name": r[1], "user_login": user_login}
    else:
        raise Exception(f"User with login `{user_login}` not found in target!")

        
def get_all_ids(session, full_table_name):
    """
    Recupera a lista de ids de uma tabela.
    
    Args:
        session (Session): Sessão ativa do SQLAlchemy.
        full_table_name (str): Nome da tabela alvo no formato `database.table`.
    
    Returns:
        list: Lista de ids da tabela.
    """
    query = f"SELECT id FROM {full_table_name};"
    ids_list = execute_custom_query(session, query)
    return [i[0] for i in ids_list]
    
    
def migrate_tahiti_workflow(source_session, source_workflow_id, target_session, target_metadata, target_workflow_id, user=None):
    """
    Recupera as informações da tabela tahiti.workflow, atualizando os ids e o user para evitar conflito no alvo.
    
    Args:
        source_session (Session): Sessão ativa do SQLAlchemy no db de origem.
        source_workflow_id (int): Id do workflow original.
        target_session (Session): Sessão ativa do SQLAlchemy no db de destino.
        target_metadata (Metadata): Metadados do SQLAlchemy sobre o db de destino.
        target_workflow_id (int): Id do workflow de destino.
        user (dict): Dicionário contendo as informações do novo owner do workflow.
    
    Returns:
        list: dados a serem inseridos na tabela alvo.
    """

    table = target_metadata.tables['workflow']
    columns = [c.name for c in table.columns]

    query = f"SELECT * FROM tahiti.workflow WHERE id = {source_workflow_id};"
    
    move_data = [dict(zip(columns, row)) 
                 for row in execute_custom_query(source_session, query)]
    for row in move_data:
        row['id'] = target_workflow_id
        if user:
            row['user_id'] = user['user_id']
            row['user_login'] = user['user_login']
            row['user_name'] = user['user_name']
            
    if len(move_data) > 0:
        # pprint.pprint(move_data)
        return table.insert(), move_data
    

def migrate_tahiti_task(source_session, source_workflow_id, target_session, target_metadata, target_workflow_id):
    """
    Recupera as informações da tabela tahiti.task, atualizando os workflow_id para evitar conflito no alvo.
    
    Args:
        source_session (Session): Sessão ativa do SQLAlchemy no db de origem.
        source_workflow_id (int): Id do workflow original.
        target_session (Session): Sessão ativa do SQLAlchemy no db de destino.
        target_metadata (Metadata): Metadados do SQLAlchemy sobre o db de destino.
        target_workflow_id (int): Id do workflow de destino.
    
    Returns:
        list: dados a serem inseridos na tabela alvo.
    """

    table = target_metadata.tables['task']
    columns = [c.name for c in table.columns]

    query = f"SELECT * FROM tahiti.task WHERE workflow_id = {source_workflow_id};"
    move_data = [dict(zip(columns, row)) 
                 for row in execute_custom_query(source_session, query)]

    for row in move_data:
        row['workflow_id'] = target_workflow_id

    if len(move_data) > 0:
        # pprint.pprint(move_data)
        return table.insert(), move_data

def migrate_tahiti_flow(source_session, source_workflow_id, target_session, target_metadata, target_workflow_id):
    """
    Recupera as informações da tabela tahiti.flow, atualizando os ids e o workflow_id para evitar conflito no alvo.
    
    Args:
        source_session (Session): Sessão ativa do SQLAlchemy no db de origem.
        source_workflow_id (int): Id do workflow original.
        target_session (Session): Sessão ativa do SQLAlchemy no db de destino.
        target_metadata (Metadata): Metadados do SQLAlchemy sobre o db de destino.
        target_workflow_id (int): Id do workflow de destino.
    
    Returns:
        list: dados a serem inseridos na tabela alvo.
    """

    table = target_metadata.tables['flow']
    columns = [c.name for c in table.columns]
    
    current_flow_id = get_current_id(target_session, "tahiti.flow")    
    print(f"Current flow id:", current_flow_id)
    
    query = f"SELECT * FROM tahiti.flow WHERE workflow_id = {source_workflow_id};"
    move_data = [dict(zip(columns, row)) 
                 for row in execute_custom_query(source_session, query)]

    for row in move_data:
        current_flow_id += 1
        row['workflow_id'] = target_workflow_id
        row['id'] = current_flow_id

    if len(move_data) > 0:
        # pprint.pprint(move_data)
        return table.insert(), move_data
    

def migrate_tahiti_workflow_variable(source_session, source_workflow_id, target_session, target_metadata, target_workflow_id):
    """
    Recupera as informações da tabela tahiti.flow, atualizando os ids e o workflow_id para evitar conflito no alvo.
    
    Args:
        source_session (Session): Sessão ativa do SQLAlchemy no db de origem.
        source_workflow_id (int): Id do workflow original.
        target_session (Session): Sessão ativa do SQLAlchemy no db de destino.
        target_metadata (Metadata): Metadados do SQLAlchemy sobre o db de destino.
        target_workflow_id (int): Id do workflow de destino.
    
    Returns:
        list: dados a serem inseridos na tabela alvo.
    """
    
    table = target_metadata.tables['workflow_variable']
    columns = [c.name for c in table.columns]

    current_flow_id = get_current_id(target_session, "tahiti.workflow_variable")    
    print(f"Current workflow_variable id:", current_flow_id)
    
    
    query = f"SELECT * FROM tahiti.workflow_variable WHERE workflow_id = {source_workflow_id};"
    move_data = [dict(zip(columns, row)) 
                 for row in execute_custom_query(source_session, query)]

    for row in move_data:
        row['id'] = current_flow_id + 1
        row['workflow_id'] = target_workflow_id

    if len(move_data) > 0:
        # pprint.pprint(move_data)
        return table.insert(), move_data


def migrate_tahiti_pipeline(source_session, source_pipeline_id, target_session, target_metadata, target_pipeline_id, user=None):
    """
    Recupera as informações da tabela tahiti.flow, atualizando-as os ids, o workflow_id e o user para evitar conflito no alvo.
    
    Args:
        source_session (Session): Sessão ativa do SQLAlchemy no db de origem.
        source_workflow_id (int): Id do workflow original.
        target_session (Session): Sessão ativa do SQLAlchemy no db de destino.
        target_metadata (Metadata): Metadados do SQLAlchemy sobre o db de destino.
        target_workflow_id (int): Id do workflow de destino.
        user (dict): Dicionário contendo as informações do novo owner do workflow.
    
    Returns:
        list: dados a serem inseridos na tabela alvo.
    """

    table = target_metadata.tables['pipeline']
    columns = [c.name for c in table.columns]

    query = f"SELECT * FROM tahiti.pipeline WHERE id = {source_pipeline_id};"
    
    move_data = [dict(zip(columns, row)) 
                 for row in execute_custom_query(source_session, query)]
    
    for row in move_data:
        row['id'] = target_pipeline_id
        if user:
            row['user_id'] = user['user_id']
            row['user_login'] = user['user_login']
            row['user_name'] = user['user_name']
           
    if len(move_data) > 0:
        # pprint.pprint(move_data)
        return table.insert(), move_data
    
def get_workflow_ids_from_pipeline_step(session, pipeline_id):
    """
    Recupera a lista de workflow_id vinculado a um pipeline_step.
    
    Args:
        session (Session): Sessão ativa do SQLAlchemy.
        pipeline_id (int): Id do pipeline_step alvo.
    
    Returns:
        list: Lista de workflow_id.
    """
    
    query = f"SELECT workflow_id FROM tahiti.pipeline_step WHERE pipeline_id = {pipeline_id};"
    workflow_ids = [v[0] for v in execute_custom_query(session, query)]
    return workflow_ids 


def migrate_tahiti_pipeline_step(source_session, source_pipeline_id, target_session, target_metadata, target_pipeline_id, target_workflow_id, user=None):
    """
    Recupera as informações da tabela tahiti.flow, atualizando-as os ids e o workflow_id que no alvo.
    
    Args:
        source_session (Session): Sessão ativa do SQLAlchemy no db de origem.
        source_workflow_id (int): Id do workflow original.
        target_session (Session): Sessão ativa do SQLAlchemy no db de destino.
        target_metadata (Metadata): Metadados do SQLAlchemy sobre o db de destino.
        target_workflow_id: Id do workflow de destino.
    
    Returns:
        list: dados a serem inseridos na tabela alvo.
    """
    

    table = target_metadata.tables['pipeline_step']
    columns = [c.name for c in table.columns]
    
    current_pipeline_step_id = get_current_id(target_session, "tahiti.pipeline_step")    
    print(f"Current pipeline_step id:", current_pipeline_step_id)

    query = f"SELECT * FROM tahiti.pipeline_step WHERE pipeline_id = {source_pipeline_id};"
    move_data = [dict(zip(columns, row)) 
                 for row in execute_custom_query(source_session, query)]
    
    for row in move_data:
        current_pipeline_step_id += 1
        row['id'] = current_pipeline_step_id
        row['pipeline_id'] = target_pipeline_id
        row['workflow_id'] = target_workflow_id
            
    if len(move_data) > 0:
        # pprint.pprint(move_data)
        return table.insert(), move_data


def migrate_tahiti_source_code(source_session, source_source_code_id, target_session, target_metadata, target_source_code_id):
    """
    Recupera as informações da tabela tahiti.source_code, atualizando os ids para evitar conflito no alvo.
    
    Args:
        source_session (Session): Sessão ativa do SQLAlchemy no db de origem.
        source_source_code_id (int): Id do source_code original.
        target_session (Session): Sessão ativa do SQLAlchemy no db de destino.
        target_metadata (Metadata): Metadados do SQLAlchemy sobre o db de destino.
        target_source_code_id (int): Id do source_code de destino.
    
    Returns:
        list: dados a serem inseridos na tabela alvo.
    """
    
    table = target_metadata.tables['source_code']
    columns = [c.name for c in table.columns]  
    
    query = f"SELECT * FROM tahiti.source_code WHERE id = {source_source_code_id};"
    move_data = [dict(zip(columns, row)) 
                 for row in execute_custom_query(source_session, query)]

    for row in move_data:
        row['id'] = target_source_code_id


    if len(move_data) > 0:
        # pprint.pprint(move_data)
        return table.insert(), move_data
    

def main():
    parser = argparse.ArgumentParser(
        description="Script to migrate Lemonade's workflows and pipelines from one database to another."
    )

    parser.add_argument(
        "--source-db",
        required=True,
        help="Connection string for the source database (e.g., 'mysql://user:pass@host:port')."
    )

    parser.add_argument(
        "--target-db",
        required=True,
        help="Connection string for the target database (e.g., 'mysql://user:pass@host:port')."
    )
    
    parser.add_argument(
        "--type",
        type=str,
        required=True,
        choices=['pipeline', 'workflow', 'source_code'],
        help="Copy `pipeline`, `workflow` or `source_code`."
    )
    
    parser.add_argument(
        "--id",
        type=str,
        required=True,
        help="ID of the pipeline or workflow to migrate. Supported options are: a specific id (e.g., `1`), a list of ids (e.g., `1,2,3`), or `all` to migrate all pipelines/workflows/source_code."
    )
    
    parser.add_argument(
        "--user-login",
        type=str,
        required=False,
        help="When set, it will change the current user owner of the workflow."
    )
    
    args = parser.parse_args()

    print("Migration Configuration:")
    print(f"  Source Database: {args.source_db}")
    print(f"  Target Database: {args.target_db}")
    print(f"  Pipeline/Workflow/Source Code ID: {args.id}")
    print(f"  Type: {args.type}")
    print(f"  User login: {args.user_login}")
    
    source_session, source_metadata = connect_to_database(args.source_db)
    target_session, target_metadata = connect_to_database(args.target_db)    
    
    if args.user_login:
        user_info = get_user_info(target_session, args.user_login)
    else:
        user_info = None
        
    if args.id == "all":
        ids_list = get_all_ids(source_session, f'tahiti.{args.type}')
    elif "," in args.id:
        ids_list = [int(p.strip()) for p in args.id.split(",")]
    else:
        ids_list = [int(args.id)]
    print(f"{args.type.capitalize()}'s ids to copy: {ids_list}")
    
    values_to_copy = []
    if args.type == "source_code":
        current_source_code_id = get_current_id(target_session, "tahiti.source_code")
        for source_source_code_id in ids_list:
            current_source_code_id += 1
            print(f"Cloning source_code from source {source_source_code_id} to {current_source_code_id} on target.")
            result = migrate_tahiti_source_code(source_session, source_source_code_id, target_session, target_metadata, current_source_code_id)
            values_to_copy.append(result)
    elif args.type == "pipeline":
        for source_pipeline_id in ids_list:

            target_pipeline_id = get_current_id(target_session, "tahiti.pipeline") + 1   
            print(f"Cloning pipeline_id from source {source_pipeline_id} to {target_pipeline_id} on target.")

            result = migrate_tahiti_pipeline(source_session=source_session, source_pipeline_id=source_pipeline_id, target_session=target_session, 
                                             target_metadata=target_metadata, target_pipeline_id=target_pipeline_id, user=user_info)
            values_to_copy.append(result)
            
            workflow_ids = get_workflow_ids_from_pipeline_step(session=source_session, pipeline_id=source_pipeline_id) # ids on source
            current_workflow_id = get_current_id(target_session, "tahiti.workflow") # last id on target
            for source_workflow_id in workflow_ids:
                current_workflow_id += 1
                print(f"Cloning workflow_id from source {source_workflow_id} to {current_workflow_id} on target.")
                print("Cloning workflow ...")
                result = migrate_tahiti_workflow(source_session=source_session, source_workflow_id=source_workflow_id, target_session=target_session, 
                                                 target_metadata=target_metadata, target_workflow_id=current_workflow_id, user=user_info)
                values_to_copy.append(result)
                print("Cloning workflow's task ...")
                result = migrate_tahiti_task(source_session=source_session, source_workflow_id=source_workflow_id, target_session=target_session, 
                                             target_metadata=target_metadata, target_workflow_id=current_workflow_id)
                values_to_copy.append(result)
                print("Cloning workflow's flow ...")
                result = migrate_tahiti_flow(source_session=source_session, source_workflow_id=source_workflow_id, target_session=target_session, 
                                             target_metadata=target_metadata, target_workflow_id=current_workflow_id)
                values_to_copy.append(result)
                print("Cloning workflow's variable (if exists) ...")
                result = migrate_tahiti_workflow_variable(source_session=source_session, source_workflow_id=source_workflow_id, 
                                                          target_session=target_session, target_metadata=target_metadata, 
                                                          target_workflow_id=current_workflow_id)
                values_to_copy.append(result)
                print("Cloning pipeline step ...")
                result = migrate_tahiti_pipeline_step(source_session=source_session, source_pipeline_id=source_pipeline_id, target_session=target_session, 
                                                      target_metadata=target_metadata, target_pipeline_id=target_pipeline_id, 
                                                      target_workflow_id=current_workflow_id)
                values_to_copy.append(result)
                
    else:
        current_workflow_id = get_current_id(target_session, "tahiti.workflow")
        
        for source_workflow_id in ids_list:
            current_workflow_id += 1
            print(f"Cloning workflow_id from source {source_workflow_id} to {current_workflow_id} on target.")
            print("Cloning workflow ...")
            result = migrate_tahiti_workflow(source_session=source_session, source_workflow_id=source_workflow_id, target_session=target_session, 
                                             target_metadata=target_metadata, target_workflow_id=current_workflow_id, user=user_info)
            values_to_copy.append(result)
            print("Cloning workflow's task ...")
            result = migrate_tahiti_task(source_session=source_session, source_workflow_id=source_workflow_id, target_session=target_session, 
                                         target_metadata=target_metadata, target_workflow_id=current_workflow_id)
            values_to_copy.append(result)
            print("Cloning workflow's flow ...")
            result = migrate_tahiti_flow(source_session=source_session, source_workflow_id=source_workflow_id, target_session=target_session, 
                                         target_metadata=target_metadata, target_workflow_id=current_workflow_id)
            values_to_copy.append(result)
            print("Cloning workflow's variable (if exists) ...")
            result = migrate_tahiti_workflow_variable(source_session=source_session, source_workflow_id=source_workflow_id, target_session=target_session, 
                                                      target_metadata=target_metadata, target_workflow_id=current_workflow_id)
            values_to_copy.append(result)
            print("Cloning pipeline step ...")

    
    print("Starting migration process...")

    try:
        for migration in values_to_copy:
            if migration:
                table_ob, data = migration
                target_session.execute(table_ob, data)
                target_session.flush()
    except:
        target_session.rollback()
        source_session.close()
        target_session.close()
        raise

    target_session.commit()
    source_session.close()
    target_session.close()
    print("Migration completed successfully!")

if __name__ == "__main__":
    main()
