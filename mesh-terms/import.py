import logging
import pathlib

if __package__ == "":
    from convert import file_to_dataframe
    from db_connection import write_to_db
    from file_map import FILE_MAP
    from mesh_download import download_terms
else:
    from .convert import file_to_dataframe
    from .db_connection import write_to_db
    from .file_map import FILE_MAP
    from .mesh_download import download_terms

logger = logging.getLogger(__name__)


def import_definitions(url: str, force_download: bool = False):
    data_dir = pathlib.Path(".") / "data"

    if not data_dir.exists() or force_download:
        download_terms(url)

    tables = {}
    for file in data_dir.glob("**/*.txt"):
        mapped = FILE_MAP[file.stem]
        try:
            tables[mapped.name] = file_to_dataframe(file, columns=mapped.columns)
        except KeyError as e:
            logger.error(f"unknown file name {file.stem}: {e}")
            continue

    write_to_db(tables)


if __name__ == "__main__":
    from urls import MESH_DE_2022

    import_definitions(url=MESH_DE_2022)
