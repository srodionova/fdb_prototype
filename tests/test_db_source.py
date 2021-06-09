from lib.sources.base import DBSource


def test_db_connect():
    with DBSource(dsn='postgresql+psycopg2://fdb:fdb@localhost:5432/fdb') as source:
        print(source)


