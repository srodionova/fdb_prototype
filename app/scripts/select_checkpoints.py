
from app.queries.select_checkpoints import SelectCheckpointsQuery
from app.sources.pg import PGSource
from app.utils.logging import init_logging


def main():
    # maybe dependency injection for query/source
    with PGSource('postgresql+psycopg2://fdb:fdb@localhost:5432/fdb') as source:
        query = SelectCheckpointsQuery(source=source)
        result = query.execute_tracked()
        print(result)


if __name__ == '__main__':
    init_logging()
    main()
