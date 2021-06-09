import enum
from dataclasses import dataclass
from typing import Optional, List, Type

import pandas

from app.queries.select_parcel_routes import SelectParcelRoutesQuery
from app.queries.select_routes_characteristics import SelectRoutesCharacteristicsQuery
from lib.queries.query import Query, QueryParams, CompositeQuery
from lib.queries.repository import query_repository


class Operation(enum.Enum):
    SUMLEN = 'sumlen'
    MULLEN = 'mullen'


@dataclass
class MergeRoutesQueryParams(QueryParams):
    operation: Operation


@query_repository.register
class MergeRoutesQuery(CompositeQuery):
    """Composite query"""
    name = 'merge_routes'

    def __init__(self, select_checkpoints_query: SelectRoutesCharacteristicsQuery, select_parcel_routes: SelectParcelRoutesQuery):
        self.select_checkpoints_query = select_checkpoints_query
        self.select_parcel_routes = select_parcel_routes

    def execute(self, params: Optional[MergeRoutesQueryParams] = None) -> pandas.DataFrame:
        if params is None:
            params = MergeRoutesQueryParams(operation=Operation.SUMLEN)
        result1 = self.select_checkpoints_query.execute()
        result2 = self.select_parcel_routes.execute()

        res = result2.merge(result1, on=['route_uid']).head(250)

        return res[res.columns[:5]]

    @classmethod
    def get_child_query_types(cls) -> List[Type[Query]]:
        return [SelectRoutesCharacteristicsQuery, SelectParcelRoutesQuery]
