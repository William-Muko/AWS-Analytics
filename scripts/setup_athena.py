import boto3
import yaml
import time

def load_config():
    with open('../config/config.yaml', 'r') as f:
        return yaml.safe_load(f)

def execute_query(athena, query, database, output_location):
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': database} if database else {},
        ResultConfiguration={'OutputLocation': output_location}
    )
    query_id = response['QueryExecutionId']
    
    while True:
        result = athena.get_query_execution(QueryExecutionId=query_id)
        state = result['QueryExecution']['Status']['State']
        if state in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            return state == 'SUCCEEDED'
        time.sleep(1)

def setup_athena():
    config = load_config()
    athena = boto3.client('athena', region_name=config['aws']['region'])
    
    database = config['aws']['athena_database']
    output_location = config['aws']['athena_output_location']
    
    create_db = f"CREATE DATABASE IF NOT EXISTS {database}"
    print(f"Creating database: {database}")
    execute_query(athena, create_db, None, output_location)
    print(f"✓ Database {database} ready")
    
    with open('../sql/create_tables.sql', 'r') as f:
        queries = f.read().split(';')
        for query in queries:
            if query.strip():
                print(f"Executing: {query[:50]}...")
                execute_query(athena, query, database, output_location)
    
    print("✓ All tables created")

if __name__ == '__main__':
    setup_athena()
