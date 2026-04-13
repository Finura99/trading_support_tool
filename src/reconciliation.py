import pandas as pd
import logging

def reconcile_counts(trades_df: pd.DataFrame, positons_df: pd.DataFrame) -> dict:
    trades_count = len(trades_df)
    positions_count = len(positons_df)

    difference = trades_count - positions_count

    status = "match" if difference == 0 else "mismatch" #business logic

    if status == "match":
        logging.info(f"Reconciliation OK:{trades_count} trades vs {positions_count} positions")
    else:
        logging.error(f"Reconcilaition Failed: trades = {trades_count}, positions = {positions_count}, difference = {difference}")

    return {
        "trades_count" : trades_count,
        "positions_count" : positions_count,
        "difference": difference,
        "status": status
        } ##return back as a structured object (dictionary) for exposing it to api/dashboard/storing.


