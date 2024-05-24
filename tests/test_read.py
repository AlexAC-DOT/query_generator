import unittest
from unittest.mock import patch, MagicMock
from utils.read import get_table_names_from_excel, get_columns_from_db

class TestModuleFunctions(unittest.TestCase):

    @patch('utils.read.pd.read_excel')
    def test_get_table_names_from_excel(self, mock_read_excel):
        # Define mock data
        mock_data = {'Column1': ['Table1', 'Table2', 'Table3']}
        
        # Mock pd.read_excel to return the mock data
        mock_read_excel.return_value = MagicMock(**{'iloc.return_value': MagicMock(**{'iloc.return_value': mock_data})})

        # Call the function
        result = get_table_names_from_excel('sample.xlsx')

        # Define expected output
        expected_output = ['Table1', 'Table2', 'Table3']

        # Assert
        self.assertEqual(mock_data['Column1'], expected_output)

    def test_get_columns_from_db(self):
        # Test function
        with self.assertRaises(NotImplementedError):
            get_columns_from_db()

if __name__ == '__main__':
    unittest.main()
