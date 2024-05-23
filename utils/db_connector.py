import sqlite3
import psycopg2
import yaml

def load_config(config_file='config.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def connect_to_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def connect_to_postgresql(connection_string):
    conn = psycopg2.connect(connection_string)
    return conn

def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

# if __name__ == "__main__":
#     # Load database configuration
#     config = load_config()

#     # Connect to the database
#     if config['database_type'] == 'sqlite':
#         conn = connect_to_sqlite(config['sqlite']['db_path'])
#     elif config['database_type'] == 'postgresql':
#         conn = connect_to_postgresql(config['postgresql']['connection_string'])
#     else:
#         raise ValueError(f"Unsupported database type: {config['database_type']}")

#     # Example query
#     query = "SELECT * FROM my_table;"

#     # Execute the query
#     results = execute_query(conn, query)
#     print("Query Results:")
#     for row in results:
#         print(row)

#     # Close the connection
#     conn.close()
