#!/usr/bin/python3
"""Convert CSV data to JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON file named data.json"""
    try:
        with open(csv_filename, mode="r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

        with open("data.json", mode="w", encoding="utf-8") as out:
            json.dump(data, out)

        return True
    except Exception:
        return False
