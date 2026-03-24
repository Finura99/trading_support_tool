# Trading Support Automation Tool

## Overview 
This project simulates a real yet simple automation of the trading support workflow. It checks whether the expected daily files are present before the the day starts, validates the file structure/s and key fields and runs a reconciliation to verify whether the fiels are in harmony of each other or not, and finally, produces a logging trace and support summary.

## Features
- required file checks
- file structure validation
- missing value / invalid value checks
- reconciliation between files
- support summary output
- logging 
- print for debugging
- basic testing

## Project Structure
- "src/file_checker.py" - checks for expected files 
- "src/validator.py" - validates file structure and missing/invalid values
- "src/reconciliation.py" - compares counts across fields
- "src/reporter.py" - creates a report summary
- "src/main.py" - orchestrates the overall control flow

## How to Run
```bash
python src/main.py