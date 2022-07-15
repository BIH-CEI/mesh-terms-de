from typing import Dict

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from tqdm import tqdm


def write_to_db(tables: Dict[str, pd.DataFrame]):
    engine = create_engine(
        "postgresql+psycopg2://postgres:meshterms@localhost:5432/mesh"
    )

    for name, table in tqdm(tables.items()):
        write_table_to_db(name, table, engine)


def write_table_to_db(table_name: str, df: pd.DataFrame, engine: Engine):
    df.to_sql(table_name, con=engine, if_exists="replace")
