from utils.read import get_table_names_from_excel
from utils import queries_generator as qg
from utils import db_connector as db
import pandas as pd


TABLES_NAMES_FILE_PATH = 'tables.xlsx'
OUTPUT_FILE_PATH = 'queries.txt'
COLUMN_NAMES = ['table_name', 'exists_in_db', 'counts_match', 'schemas_match', 'hash_match']
DB_TYPE = "sqlite"

def main():
    # Excel path with the name of the tables
    table_list = get_table_names_from_excel(TABLES_NAMES_FILE_PATH)
    query_list = []
    # conn = db.connect_to_sqlite()
    
    # Create an empty DataFrame with the specified column names
    df = pd.DataFrame(columns=COLUMN_NAMES)

    for table in table_list:
        # Generates all the queries and append them to a list. At the end of the program it will write them into a txt file
        is_table_query = qg.get_is_table_query(table_name=table, db_type=DB_TYPE)
        schema_query = qg.get_schema_query(table_name=table, db_type=DB_TYPE)
        count_query = qg.get_count_query(table_name=table, db_type=DB_TYPE, daily=False)
        row_hash_query = qg.generate_row_hash_query(table_name=table,columns=None, db_type=DB_TYPE, daily=False)
        query_list.extend([is_table_query, schema_query, count_query, row_hash_query])
        # results = db.execute_query(conn, is_table_query)
        # if results:
        #     pass
    with open(OUTPUT_FILE_PATH, 'w') as file:
        for query in query_list:
            file.write(query + '\n')

if __name__ == "__main__":
    main()