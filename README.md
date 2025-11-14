# Python File Management and Data Processing Utility  
**Project:** Python File Management and Data Processing Utility  
**Total Marks:** 30

## NAME
BETT KIPTOO ELIAS -INTE/MG/3302/09/22— https://github.com/ELIASBETT451/INTE472-FileManagementProject-
## Project Files
- `file_manager.py` — main script (implements tasks 1–6)
- `students_report.py` — JSON/CSV data processing script (task 7)
- `students.json` — sample input for `students_report.py`
- `README.md` — this file

## Requirements
- Python 3.7+ (tested with 3.10)
- No external libraries required (uses stdlib modules: os, sys, shutil, datetime, json, csv)

## How to run
1. Open terminal in project folder (or use VS Code integrated terminal).
2. Run the main utility:

python file_manager.py

Follow the prompts to enter five student names and optionally delete files.
3. Run the report script:

python students_report.py
This will create `report.csv` in the project folder.

## Notes
- `StudentFiles` folder and `activity_log.txt` are created automatically by `file_manager.py`.
- The backup file is moved to `StudentFiles/Archive`.
- Logging format: `[YYYY-MM-DDHH:MM:SS]message`

