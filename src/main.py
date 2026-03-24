from pathlib import Path
from validator import validate_structure, validate_missing_values
from reconciliation import reconcile_counts
from file_checker import check_required_files
from reporter import generate_summary

import pandas as pd
import logging

BASE_DIR = Path(__file__).resolve().parent.parent #root dir
INPUT_DIR = BASE_DIR / "data" / "input"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def main():
    logging.info("Starting trading support automation check")

    expected_files = [
        "trades_20260102.csv",
        "positions_20260102.csv",
        "pnl_20260102.csv"
    ]

    file_check = check_required_files(expected_files)
    logging.info(f"Present files: {file_check["present"]}")
    logging.info(f"Missing files: {file_check["missing"]}") #returns a dict i assume...

    if file_check["missing"]:
        logging.error("Required files are missing, Stopping flow...")
        return
    
    trades_path = INPUT_DIR / "trades_20260102.csv"
    positions_path = INPUT_DIR / "positions_20260102.csv"

    trades_df = pd.read_csv(trades_path)
    positions_df = pd.read_csv(positions_path)

    logging.info(f"Loaded trade rows: {len(trades_df)}")
    logging.info(f"Positions rows: {len(positions_df)}")

    missing_cols = validate_structure(trades_df)

    if missing_cols:
        logging.error(f"Trades file missing column: {missing_cols}")
        return
    
    invalid_rows = validate_missing_values(trades_df) #returns missing values from trades

    if not invalid_rows.empty:
        logging.error(f"Invalid trades flow found: {len(invalid_rows)}")

    reconciliation_result = reconcile_counts(trades_df, positions_df)
    logging.info(f"Reconciliation Results: {reconciliation_result}")

    generate_summary(file_check, invalid_rows, reconciliation_result)
    
    print("\nSupport Summary")
    print("------------------")
    print("Present files:", file_check["present"])
    print("Missing files:", file_check["missing"])
    print("Invalid trade rows:", len(invalid_rows))
    print("Reconciliation:", reconciliation_result)

    print("invalid_rows length:", len(invalid_rows))
    print("invalid_rows.empty,", invalid_rows.empty)

    logging.info("Trading support automation check complete...")




if __name__ == "__main__":
    main()