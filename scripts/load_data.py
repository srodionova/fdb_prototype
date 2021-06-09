import pathlib

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists, drop_database

TEST_DIR = pathlib.Path(__file__).parent.parent / 'tests'


def load_pg_data():
    engine = create_engine('postgresql+psycopg2://fdb:fdb@localhost:5432/fdb')
    res = engine.execute((TEST_DIR / 'pg_schema.sql').read_text())
    print(res.fetchall())


def load_ms_schema(db_name='fdb'):
    engine = create_engine(f'mssql+pyodbc://sa:yourStrong(!)Password@localhost:1433/{db_name}?driver=ODBC Driver 17 '
                           'for SQL Server;timeout=300')

    # Create database if it does not exist.
    if not database_exists(engine.url):
        print(f'Creating a new database {db_name}')
        create_database(engine.url)
    else:
        # Connect the database if exists.
        engine.connect()

    res = engine.execute((TEST_DIR / 'sql_server_schema.sql').read_text())

    print(res.fetchall())


if __name__ == '__main__':
    load_pg_data()
    load_ms_schema()
