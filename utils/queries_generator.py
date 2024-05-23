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
    
    query = f"SELECT COUNT(*) FROM {table_name};"
    return query

def get_schema_query(table_name, db_type) -> str:
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

def get_row_hash_query(table_name, db_type, hash_algorithm='sha256'):
    validate_db_type()
    if db_type == 'sqlite':
        query = f"SELECT *, HASH('{hash_algorithm}', * || '') AS row_hash FROM {table_name};"
    elif db_type == 'postgres':
        query = f"SELECT *, ENCODE(DIGEST(CONCAT_WS('', *, ''), '{hash_algorithm}'), 'hex') AS row_hash FROM {table_name};"
    else:
        raise ValueError(f"Unsupported database type: {db_type}")
    return query
