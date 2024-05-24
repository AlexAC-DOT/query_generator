import pandas as pd

def get_table_names_from_excel(file_path: str) -> list:
    df = pd.read_excel(file_path)
    
    # Extract the first column
    first_column = df.iloc[:, 0].tolist()
    
    return first_column

def get_columns_from_db() -> list:
    """
    TODO: Implement function to read the tables names from the SQL database using regex
    """
    raise NotImplementedError
