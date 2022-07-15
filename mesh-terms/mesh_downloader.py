import logging
import pathlib
import shutil
from zipfile import ZipFile

import requests

if __name__ == "__main__":
    from file_map import FILE_MAP
else:
    from .file_map import FILE_MAP

logger = logging.getLogger(__name__)


def download_terms(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        logger.error(f"failed to get archive: {response.text}")

    tmp_file = pathlib.Path(".") / "tmp.zip"
    if tmp_file.exists():
        tmp_file.unlink()

    tmp_file.write_bytes(response.content)

    target_dir = pathlib.Path(".") / "data"
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir()

    try:
        with ZipFile(tmp_file) as zip_ref:
            file_names = zip_ref.namelist()
            file_names = [
                entry
                for entry in file_names
                if "demo" not in entry and pathlib.Path(entry).stem in FILE_MAP
            ]
            zip_ref.extractall(target_dir, members=file_names)
    finally:
        tmp_file.unlink()


if __name__ == "__main__":
    from urls import MESH_DE_2022

    download_terms(MESH_DE_2022)
