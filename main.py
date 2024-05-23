from utils.read import get_column_names_from_excel
from utils import queries_generator as qg
import pandas as pd

def main():
    # Excel path with the name of the tables
    file_path = 'tables.xlsx'
    column_list = get_column_names_from_excel(file_path)
    column_names = ['table_name', 'exists_in_db', 'counts_match', 'schemas_match', 'hash_match']

    # Create an empty DataFrame with the specified column names
    df = pd.DataFrame(columns=column_names)
    db_type = "sqlite"
    for column in column_list:
        is_table_query = qg.get_is_table_query(column, db_type)
        print(is_table_query)
        
        

if __name__ == "__main__":
    main()