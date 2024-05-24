import unittest
from unittest.mock import patch, Mock
from datetime import datetime
from utils.queries_generator import (
    validate_db_type,
    get_is_table_query,
    get_count_query,
    get_schema_query,
    generate_row_hash_query
)

class TestDatabaseFunctions(unittest.TestCase):

    def test_validate_db_type(self):
        self.assertTrue(validate_db_type('sqlite'))
        self.assertTrue(validate_db_type('postgres'))
        self.assertTrue(validate_db_type('mysql'))
        with self.assertRaises(ValueError):
            validate_db_type('unknown')

    def test_get_is_table_query(self):
        self.assertEqual(
            get_is_table_query('my_table', 'sqlite'),
            "SELECT name FROM sqlite_master WHERE type='table' AND name='my_table';"
        )
        self.assertEqual(
            get_is_table_query('my_table', 'postgres'),
            "SELECT tablename FROM pg_catalog.pg_tables WHERE tablename='my_table';"
        )
        with self.assertRaises(ValueError):
            get_is_table_query('my_table', 'mysql')

    def test_get_count_query(self):
        expected_sqlite_query = "SELECT COUNT(*) FROM my_table ;"
        expected_postgres_query = "SELECT COUNT(*) FROM my_table ;"
        self.assertEqual(get_count_query('my_table', 'sqlite'), expected_sqlite_query)
        self.assertEqual(get_count_query('my_table', 'postgres'), expected_postgres_query)

    def test_get_schema_query(self):
        expected_sqlite_query = "PRAGMA table_info(my_table);"
        expected_postgres_query = """
        SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
        FROM information_schema.columns
        WHERE table_name = 'my_table';
        """
        self.assertEqual(get_schema_query('my_table', 'sqlite'), expected_sqlite_query)
        self.assertEqual(get_schema_query('my_table', 'postgres'), expected_postgres_query)
        with self.assertRaises(ValueError):
            get_schema_query('my_table', 'duckdb')

    def test_generate_row_hash_query(self):
        expected_sqlite_query = "SELECT *, sha256(*) AS row_hash FROM my_table ;"
        expected_postgres_query = "SELECT *, ENCODE(DIGEST(*, 'sha256'), 'hex') AS row_hash FROM my_table ;"
        self.assertEqual(generate_row_hash_query('my_table', db_type='sqlite'), expected_sqlite_query)
        self.assertEqual(generate_row_hash_query('my_table', db_type='postgres'), expected_postgres_query)

if __name__ == '__main__':
    unittest.main()
