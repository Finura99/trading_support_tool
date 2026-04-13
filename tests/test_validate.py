import pandas as pd
from src.validator import validate_structure, validate_missing_values

def test_missing_column():
    data = {
        "ticker" : ["AAPL", "MSFT"],
        "trade_date" : ["2024-02-01", "2024-01-01"],
        "price" : [186.3, 130.6],
    }

    df = pd.DataFrame(data)

    result = validate_structure(df)

    assert len(result) == 1
    assert "qty" in result

def test_find_invalid_rows():
    data = {
        "ticker" : ["AAPL", None],
        "price" : [-200.4, -302.3],
        "qty" : [20,300],
    }

    df = pd.DataFrame(data)

    result = validate_missing_values(df)

    print("\nDF:")
    print(df)
    print("\nRESULT:")
    print(result)
    print("\nLEN:", len(result))

    assert len(result) == 2 ##expecting 2 rows that are incorrect
