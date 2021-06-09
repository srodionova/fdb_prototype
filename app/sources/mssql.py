from abc import ABC

from lib.sources.base import DBSource

from lib.sources.repository import source_repository


@source_repository.register
class MSSQLSource(DBSource, ABC):
    """This source represents our analyst mssql db containing parcels_routes table"""
    name = 'mssql'

