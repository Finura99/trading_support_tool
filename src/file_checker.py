from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent # constructs path to root of dir
INPUT_DIR = BASE_DIR / "data" / "input" 


def check_required_files(expected_files: list[str]) -> dict:
    present = [] 
    missing = [] #our cabinets to store our expected and missing files

    for file_name in expected_files:
        file_path = INPUT_DIR / file_name #checks if there is a file name from expected_files

        if file_path.exists(): #does the file exist on disk ?
            present.append(file_name) #if true, adds it to the list
        else:
            missing.append(file_name)

    return {
        "present": present,
        "missing": missing
    }