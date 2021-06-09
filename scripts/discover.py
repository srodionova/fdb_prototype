import logging
import pathlib

from lib.utils import recursively_import
from lib.sources.repository import source_repository

def discover():
    recursively_import(
        base_path=pathlib.Path(__file__).parent.parent / 'app' / 'sources',
        import_path='app.sources',
    )
    recursively_import(
        base_path=pathlib.Path(__file__).parent.parent / 'app' / 'queries',
        import_path='app.queries',
    )

if __name__ == '__main__':
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    discover()
    srcs = source_repository.get_available_sources()
    for source_name, source in srcs.items():
        print('Discovered source: ', source_name)
        print('Queries:')
        for query_name, query in source.get_queries().items():
            print('\t', query_name, query.__doc__)
