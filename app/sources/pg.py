from abc import ABC

from lib.sources.base import DBSource
from lib.sources.repository import source_repository


@source_repository.register
class PGSource(DBSource):
    """This source represents our analyst postgres db containing routes and checkpoints tables"""
    name = 'pg'

