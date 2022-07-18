import argparse
import logging

from mesh_terms.import_definitions import import_definitions
from mesh_terms.urls import MESH_DE_2022

FORMAT = "%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


def gen_argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--url",
        default=MESH_DE_2022,
        help="URL to download the files from, default: latest version",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        default=False,
        help="Force to re-download definitions",
    )

    return parser.parse_args()


def main():
    args = gen_argparser()
    import_definitions(url=args.url, force_download=args.force)


if __name__ == "__main__":
    main()
