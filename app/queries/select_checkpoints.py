from typing import List, Type

from app.sources.pg import PGSource
from app.utils.queries import MyDBQuery
from lib.queries.repository import query_repository
from lib.sources.base import Source


@query_repository.register
class SelectCheckpointsQuery(MyDBQuery):
    """Selects important checkpoints"""

    name = 'select_checkpoints'

    @classmethod
    def get_related_sources(cls) -> List[Type[Source]]:
        return [PGSource]
