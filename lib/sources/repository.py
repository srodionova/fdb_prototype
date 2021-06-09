from typing import Dict

from lib.sources.base import Source


class SourceRepository:
    # available_sources: Dict[str, Source]

    def __init__(self):
        self.available_sources = {}

    def register(self, source_cls: Source):
        self.available_sources[source_cls.name] = source_cls
        return source_cls

    def get_available_sources(self) -> Dict[str, Source]:
        return self.available_sources


source_repository = SourceRepository()
