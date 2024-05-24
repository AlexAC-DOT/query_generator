# Database Reconciliation Tool

## Overview

The Database Reconciliation Tool is a Python project designed to generate SQL queries that ensure two databases have the same tables and data. This tool helps in identifying discrepancies between two databases and generates the necessary SQL statements to reconcile them.

## Features

- **SQL Query Generation**: Generate SQL queries to reconcile differences in table structures and data.
- **Report Generation**: Produce a report detailing the differences and the generated SQL queries.

## Requirements

- Python 3.8 or higher

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/db-reconciliation-tool.git
   cd db-reconciliation-tool
   ```

2. Install Poetry:
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install the dependencies:
   ```sh
   poetry install
   ```

## Usage

Run the main script to start the reconciliation process:
```sh
poetry run python main.py
```

The tool will:
1. Read a list of the tables to be consiliated.
2. For each table it will generate a query to check if the table exists (The query generator function will have an optional boolean parameter (date_to_compare) to generate a query with only this data.)
 - If the table does not exist it will check the next table.
 - If the table exists in the target db it will generate queries to:
      - Get count of rows on the table.
      - Get schema for table.
      - Get hash for each row.
 3. Use this queries on the source and target dbs and do a comparisson.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on GitHub or contact the project maintainer:

- **GitHub**: [yourusername](https://github.com/yourusername)
- **Email**: your.email@example.com

---

Thank you for using the Database Reconciliation Tool! We hope it helps streamline your database management processes.