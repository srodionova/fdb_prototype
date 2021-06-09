import abc
import pathlib
import typing
from dataclasses import dataclass
from typing import List, Type
from typing import Optional

import pandas

from lib.queries.stat import LogStatCollector

if typing.TYPE_CHECKING:
    from lib.sources.base import DBSource, Source


@dataclass
class QueryParams(abc.ABC):
    pass


class Query(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    def get_stat_collector(self):
        return LogStatCollector()

    @abc.abstractmethod
    def execute(self, params: Optional[QueryParams] = None) -> pandas.DataFrame:
        pass

    def execute_tracked(self, params: Optional[QueryParams] = None) -> pandas.DataFrame:
        collector = self.get_stat_collector()
        with collector.track(self):
            result = self.execute(params=params)
            return result

    @classmethod
    def get_query_params_type(cls) -> Type[QueryParams]:
        return QueryParams

    @classmethod
    @abc.abstractmethod
    def get_related_sources(cls) -> List[Type['Source']]:
        return []


class SQLFileQuery(Query, abc.ABC):
    def __init__(self, source: 'DBSource'):
        self.source = source

    @classmethod
    @abc.abstractmethod
    def get_sql_file_path(cls) -> pathlib.Path:
        pass

    def execute(self, params: Optional[QueryParams] = None) -> pandas.DataFrame:
        return self.source.select_into_df(self.get_sql_file_path().read_text())


class CompositeQuery(Query, abc.ABC):
    @classmethod
    @abc.abstractmethod
    def get_child_query_types(cls) -> List[Type[Query]]:
        pass

    @classmethod
    def get_related_sources(cls) -> List[Type['Source']]:
        res = []
        for qt in cls.get_child_query_types():
            res.extend(qt.get_related_sources())
        return res
