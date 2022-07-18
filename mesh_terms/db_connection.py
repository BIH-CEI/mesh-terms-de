from os import environ
from typing import Dict

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from tqdm import tqdm

POSTGRES_HOST = environ.get("POSTGRES_HOST", "localhost")
POSTGRES_PORT = environ.get("POSTGRES_PORT", "5432")
POSTGRES_DB = environ.get("POSTGRES_DB", "mesh")
POSTGRES_USER = environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWD = environ.get("POSTGRES_PASSWD", "meshterms")


def write_to_db(tables: Dict[str, pd.DataFrame]):
    engine = create_engine(
        f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    for name, table in tqdm(tables.items()):
        write_table_to_db(name, table, engine)


def write_table_to_db(table_name: str, df: pd.DataFrame, engine: Engine):
    df.to_sql(table_name, con=engine, if_exists="replace")
