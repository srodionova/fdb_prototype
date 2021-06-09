import abc
import logging
from abc import ABC

import pandas as pd
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)


class Source(abc.ABC):
    def __init__(self):
        self.queries = {}

    @property
    @abc.abstractmethod
    def name(self):
        pass


class FileSource(Source, ABC):
    def __init__(self, path: str):
        self.path = path
        super().__init__()


class DBSource(Source, ABC):
    def __init__(self, dsn: str):
        self.dsn = dsn
        self.engine = None
        super().__init__()

    def connect(self):
        self.engine = create_engine(self.dsn)

    def close(self):
        self.engine.dispose()
        self.engine = None

    def __enter__(self):
        if self.engine is None:
            self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def select_into_df(self, query: str) -> pd.DataFrame:
        return pd.read_sql_query(
            sql=query,
            con=self.engine,
        )
