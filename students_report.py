#!/usr/bin/env python3
"""
students_report.py
Reads students.json, computes averages, writes report.csv
"""

import json
import csv
import os
from statistics import mean

INPUT_JSON = "students.json"
OUTPUT_CSV = "report.csv"

def load_students(json_path=INPUT_JSON):
    """Load students JSON, return list of dicts. If missing, notify and exit gracefully."""
    if not os.path.exists(json_path):
        print(f"Input file '{json_path}' not found. Please ensure it exists in the project folder.")
        return None
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error reading {json_path}: {e}")
        return None

def compute_averages(students):
    """Compute average for each student, rounded to two decimals."""
    results = []
    for s in students:
        scores = s.get("scores", [])
        avg = round(mean(scores), 2) if scores else 0.00
        results.append({
            "id": s.get("id", ""),
            "name": s.get("name", ""),
            "average": avg
        })
    return results

def write_csv(reports, csv_path=OUTPUT_CSV):
    """Write list of dicts into CSV sorted by average descending."""
    # Sort descending by 'average'
    sorted_reports = sorted(reports, key=lambda x: x["average"], reverse=True)
    try:
        with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "name", "average"])
            writer.writeheader()
            for row in sorted_reports:
                writer.writerow(row)
        print(f"Report written to {csv_path}")
    except Exception as e:
        print(f"Failed to write {csv_path}: {e}")

def main():
    students = load_students()
    if students is None:
        # Informative message already printed in load_students
        return
    reports = compute_averages(students)
    write_csv(reports)

if __name__ == "__main__":
    main()
