import pandas as pd

def read_first_column_as_list(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Extract the first column
    first_column = df.iloc[:, 0].tolist()
    
    return first_column

# Example usage
if __name__ == "__main__":
    file_path = 'path_to_your_excel_file.xlsx'
    first_column_list = read_first_column_as_list(file_path)
    print(first_column_list)
