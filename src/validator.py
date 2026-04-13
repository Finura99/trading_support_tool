import pandas as pd



REQUIRED_COLUMNS = ["ticker", "trade_date", "price", "qty"] # hardcoded outside of func for reusability

def validate_structure(df: pd.DataFrame) -> list: # returns as a list because of missing_columns

    missing_columns = []
    for col in REQUIRED_COLUMNS: # element is a column
        if col not in df.columns: #.columns is a pandas object
            missing_columns.append(col)
        
    return missing_columns #validation to see if all the required columns are in the file


def validate_missing_values(df: pd.DataFrame) -> pd.DataFrame: #validation for missing key values
    # check key columns for missing values
    invalid_rows = df[
        (df["ticker"].isna()) |
        (df["price"].isna()) | (df["price"] <= 0) | # true if lower than 0
        (df["qty"].isna())
    ] ##if any of these are missing then returns true by isna()

    return invalid_rows




