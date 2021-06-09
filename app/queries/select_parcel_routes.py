from typing import Type, List

from app.sources.mssql import MSSQLSource
from app.utils.queries import MyDBQuery
from lib.queries.repository import query_repository
from lib.sources.base import Source


@query_repository.register
class SelectParcelRoutesQuery(MyDBQuery):
    """Selects important checkpoints"""
    name = 'select_parcel_routes'

    @classmethod
    def get_related_sources(cls) -> List[Type[Source]]:
        return [MSSQLSource]
