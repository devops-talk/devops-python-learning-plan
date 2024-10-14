# Script: csv_to_json(csv_file: str, json_file: str)
# Description: Write a script that reads data from a CSV file and writes it to a JSON file, with appropriate error handling for missing files or format issues.

import csv
import json
import os

def csv_to_json(csv_file: str, json_file: str):
    try:
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"CSV file '{csv_file}' not found.")
        
        data = []
        with open(csv_file, mode='r', newline='', encoding='utf-8') as csv_f:
            reader = csv.DictReader(csv_f)
            for row in reader:
                data.append(row)

        if not data:
            raise ValueError(f"CSV file '{csv_file}' is empty or improperly formatted.")
        
        with open(json_file, mode='w', encoding='utf-8') as json_f:
            json.dump(data, json_f, indent=4)

        print(f"Data successfully written to '{json_file}'.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


csv_to_json('example.csv', 'data.json')