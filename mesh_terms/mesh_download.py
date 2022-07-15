import logging
import pathlib
import shutil
from zipfile import ZipFile

import requests

if __package__ == "":
    from file_map import FILE_MAP
else:
    from .file_map import FILE_MAP

logger = logging.getLogger(__name__)


def download_terms(url: str) -> None:
    response = requests.get(url)
    if response.status_code != 200:
        logger.error(f"failed to get archive: {response.text}")

    tmp_file = pathlib.Path("tmp.zip")
    if tmp_file.exists():
        tmp_file.unlink()

    tmp_file.write_bytes(response.content)

    target_dir = pathlib.Path("data")
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

    # Fix irregular file encoding and file extensions
    for file in target_dir.glob("**/*"):
        if not file.is_file():
            continue

        # Read with western european encoding
        try:
            content = file.read_text(encoding="cp1252")
            file.write_text(content)
        except UnicodeDecodeError:
            logger.info(f"ignore file '{str(file)}', may already be UTF-8?")

        # Fix suffix
        file.rename(file.with_suffix(".txt"))


if __name__ == "__main__":
    from urls import MESH_DE_2022

    download_terms(MESH_DE_2022)
