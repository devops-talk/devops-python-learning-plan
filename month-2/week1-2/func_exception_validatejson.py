# Validate JSON

# Script: validate_json(file_path: str)
# Description: Develop a script that reads a JSON file and handles exceptions for invalid JSON formats, providing specific error messages.

import json

def validate_json(file_path: str):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return "Valid JSON file."
    except FileNotFoundError:
        return "Error: The file was not found."
    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON format. {e}"
    except IsADirectoryError:
        return "Error: The provided path is a directory, not a file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


file_path = 'example.json'
print(validate_json(file_path))
