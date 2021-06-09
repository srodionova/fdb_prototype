import pathlib
from typing import Type

from app.utils.logging import init_logging
from lib.queries.query import Query, SQLFileQuery, CompositeQuery
from lib.queries.repository import query_repository
from lib.sources.base import Source
from lib.sources.repository import source_repository
from scripts.discover import discover

DOCS_DIR = pathlib.Path(__file__).parent.parent / 'docs'


def source_link(source_name: str) -> str:
    return f'[{source_name}](/sources/{source_name})'


def query_link(query_name: str) -> str:
    return f'[{query_name}](/queries/{query_name})'


def make_source_page(source: Source) -> str:
    source_page = f'#### {source.name}\n'
    source_page += source.__doc__
    return source_page


def make_query_page(query: Type[Query]) -> str:
    query_page = f'#### {query.name}\n'
    query_page += query.__doc__
    query_page += '\n\n'
    related_sources = '\n\n'.join([source_link(source.name) for source in query.get_related_sources()])
    query_page += '##### Related sources:\n\n'
    query_page += related_sources
    query_page += '\n\n'
    if issubclass(query, SQLFileQuery):
        query_page += '##### SQL Query body:\n\n'
        query_page += '```sql\n'
        query_page += query.get_sql_file_path().read_text()
        query_page += '```\n\n'

    if issubclass(query, CompositeQuery):
        sub_queries = query.get_child_query_types()
        related_sources = '\n\n'.join([query_link(query.name) for query in sub_queries])
        query_page += '##### Related queries:\n\n'
        query_page += related_sources
        query_page += '\n\n'
    return query_page


def main():
    sources = source_repository.get_available_sources()
    queries = query_repository.get_available_queries()

    sources_page = '### Available Sources\n'
    queries_page = '### Available Queries\n'
    for idx, value in enumerate(sorted(sources.items(), key=lambda kv: kv[0])):
        source_name, source = value
        print('Discovered source: ', source_name)

        sources_page += f'{idx + 1}. {source_link(source_name)}\n'

        source_page_path = DOCS_DIR / 'sources' / f'{source_name}.md'
        source_page_path.write_text(make_source_page(source))

    for idx, value in enumerate(sorted(queries.items(), key=lambda kv: kv[0])):
        query_name, query = value
        queries_page += f'{idx + 1}. {query_link(query_name)}\n'

        query_page_path = DOCS_DIR / 'queries' / f'{query_name}.md'
        query_page_path.write_text(make_query_page(query))

    (DOCS_DIR / 'sources.md').write_text(sources_page)
    (DOCS_DIR / 'queries.md').write_text(queries_page)


if __name__ == '__main__':
    init_logging()
    discover()
    main()
