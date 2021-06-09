from typing import Dict

from lib.queries.query import Query


class QueryRepository:
    available_queries: Dict[str, Query]

    def __init__(self):
        self.available_queries = {}

    def register(self, query_cls: Query):
        self.available_queries[query_cls.name] = query_cls
        return query_cls

    def get_available_queries(self):
        return self.available_queries


query_repository = QueryRepository()
