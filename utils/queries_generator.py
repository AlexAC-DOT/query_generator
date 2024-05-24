from typing import List, Optional, Union
from datetime import datetime

def validate_db_type(db_type: str) -> bool:
    if db_type not in ['sqlite', 'postgres', 'mysql']:
        raise ValueError(f"Unsupported database type: {db_type}")

def get_is_table_query(table_name: str, db_type: str) -> str:
    validate_db_type(db_type)
    if db_type == 'sqlite':
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
    elif db_type == 'postgres':
        query = f"SELECT tablename FROM pg_catalog.pg_tables WHERE tablename='{table_name}';"
    else:
        raise ValueError(f"Unsupported database type: {db_type}")
    return query

def get_count_query(table_name: str, db_type: str, daily: bool = False) -> str:
    validate_db_type(db_type)
    
    # Define date filtering clause
    if daily:
        today = datetime.now().strftime('%Y-%m-%d')
        if db_type == 'sqlite':
            date_filter_clause = f"WHERE date(timestamp_column) = '{today}'"
        elif db_type == 'postgres':
            date_filter_clause = f"WHERE DATE(timestamp_column) = '{today}'"
        else:
            raise ValueError(f"Unsupported database type: {db_type}")
    else:
        date_filter_clause = ''
    
    query = f"SELECT COUNT(*) FROM {table_name} {date_filter_clause};"
    return query

def get_schema_query(table_name:str, db_type: str) -> str:
    validate_db_type()
    if db_type == 'sqlite':
        query = f"PRAGMA table_info({table_name});"
    elif db_type == 'postgres':
        query = f"""
        SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
        FROM information_schema.columns
        WHERE table_name = '{table_name}';
        """
    elif db_type == 'mysql':
        query = f"DESCRIBE {table_name};"
    else:
        raise ValueError(f"Unsupported database type: {db_type}")
    return query

def generate_row_hash_query(
    table_name: str,
    columns: Optional[Union[List[str], str]] = None,
    db_type: str = 'sqlite',
    daily: bool = False,
    hash_algorithm: str = 'sha256'
) -> str:
    validate_db_type(db_type)
    
    # Prepare column list for inclusion in the query
    if columns:
        if isinstance(columns, str):
            columns = [columns]
        columns_clause = ', '.join(columns)
    else:
        columns_clause = '*'
    
    # Define date filtering clause
    if daily:
        today = datetime.now().strftime('%Y-%m-%d')
        if db_type == 'sqlite':
            date_filter_clause = f"WHERE date(timestamp_column) = '{today}'"
        elif db_type == 'postgres':
            date_filter_clause = f"WHERE DATE(timestamp_column) = '{today}'"
        else:
            raise ValueError(f"Unsupported database type: {db_type}")
    else:
        date_filter_clause = ''

    # Generate the query based on database type
    if db_type == 'sqlite':
        if columns:
            columns_expression = ' || '.join(columns)
            query = f"SELECT *, {hash_algorithm}({columns_expression}) AS row_hash FROM {table_name} {date_filter_clause};"
        else:
            query = f"SELECT *, {hash_algorithm}(*) AS row_hash FROM {table_name} {date_filter_clause};"
    elif db_type == 'postgres':
        if columns:
            columns_expression = " || '' || ".join(columns)
            query = f"SELECT *, ENCODE(DIGEST({columns_expression}, '{hash_algorithm}'), 'hex') AS row_hash FROM {table_name} {date_filter_clause};"
        else:
            query = f"SELECT *, ENCODE(DIGEST(*, '{hash_algorithm}'), 'hex') AS row_hash FROM {table_name} {date_filter_clause};"
    else:
        raise ValueError(f"Unsupported database type: {db_type}")
    
    return query
