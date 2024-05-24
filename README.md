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
2. For each table it will generate a queries to run a do table comparisons. Some query_generator functions will have an optional boolean parameter (daily) to generate a query with only most recent data.
3. The Queries generated will answer this questions:
   - If the table exists.
   - How many rows are on a table
   - What is the schema of the table
   - What is the result of hashing every row.
 3. Use this queries to do comparissons between the 2 tables.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.
