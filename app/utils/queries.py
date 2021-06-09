import pathlib
from abc import ABC

from lib.queries.query import SQLFileQuery

SQL = pathlib.Path(__file__).parent.parent / 'queries' / 'sql'


class MyDBQuery(SQLFileQuery, ABC):
    @classmethod
    def get_sql_file_path(cls) -> pathlib.Path:
        return SQL / f"{cls.name}.sql"

