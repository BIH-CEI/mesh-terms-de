import pathlib
from typing import List

import pandas as pd


def file_to_dataframe(file: str | pathlib.Path, columns: List[str]) -> pd.DataFrame:
    """
    Read a CSV file to a `Dataframe`

    attr
    ---
        file (str | Path):      File to read
        columns (List[str]):    Names to set for the columns

    returns
    ---
        Dataframe:  With the file's contents
    """

    df = pd.read_csv(file, header=0, quotechar="|", sep=";")

    # Remove tailoring empty column(s) as separators are used in a strange way
    df.dropna(axis=1, how="all", inplace=True)

    # Replace `NaN` with `None` for easier handling
    df.where(pd.notnull(df), None, inplace=True)

    # Set headers
    df.columns = columns

    if "Id" in columns:
        df.set_index("Id", inplace=True)

    return df
