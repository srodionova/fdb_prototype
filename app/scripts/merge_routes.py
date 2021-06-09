from app.queries.merge_routes import MergeRoutesQuery, MergeRoutesQueryParams, Operation
from app.queries.select_routes_characteristics import SelectRoutesCharacteristicsQuery
from app.queries.select_parcel_routes import SelectParcelRoutesQuery
from app.sources.mssql import MSSQLSource
from app.sources.pg import PGSource


def main():
    with PGSource('postgresql+psycopg2://fdb:fdb@localhost:5432/fdb') as pg_source:
        with MSSQLSource('mssql+pyodbc://sa:yourStrong(!)Password@localhost:1433/fdb?driver=ODBC Driver 17 for SQL Server;timeout=300') as mssql_source:
            query = MergeRoutesQuery(
                select_checkpoints_query=SelectRoutesCharacteristicsQuery(source=pg_source),
                select_parcel_routes=SelectParcelRoutesQuery(source=mssql_source),
            )
            result = query.execute(params=MergeRoutesQueryParams(operation=Operation.MULLEN))
            print(result)


if __name__ == '__main__':
    main()
