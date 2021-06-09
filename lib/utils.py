import importlib
import pathlib

from lib.sources.repository import source_repository


def recursively_import(base_path: pathlib.Path, import_path: str):
    for path_object in base_path.iterdir():
        if path_object.is_file():
            importlib.import_module(f'{import_path}.{path_object.stem}')


def build_doc(sources, queries):
    pass



if __name__ == '__main__':
    # build_doc()
    print(source_repository.get_available_sources())
