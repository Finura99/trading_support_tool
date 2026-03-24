import pandas as pd
from pathlib import Path



def generate_summary(file_check: dict, invalid_rows: pd.DataFrame, reconciliation_result: dict) -> None:
    
    has_missing_files = len(file_check["missing"]) > 0
    has_missing_rows = not invalid_rows.empty #returns true if not empty
    reconciliation_failed = reconciliation_result["status"] != "match"

    if not has_missing_files and not has_missing_rows and not reconciliation_failed:
        final_status = "PASS"
    else:
        final_status = "REVIEW REQUIRED"

    summary = f"""
    Support Summary
    ----------------
    Present files : {file_check["present"]}
    Missing files : {file_check["missing"]}
    Invalid trade rows : {len(invalid_rows)}
    Reconciliation status : {reconciliation_result["status"]}
    Reconciliation difference : {reconciliation_result["difference"]}

    Final Status : {final_status}
    """

    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / "support_summary.txt"

    with open(file_path, "w") as f:
        f.write(summary)