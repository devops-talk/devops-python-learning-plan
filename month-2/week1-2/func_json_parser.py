# JSON File Parser

# Script: parse_json(file_path: str)
# Description: Develop a script to read a JSON file and print the data in a readable format, handling nested structures gracefully.


import json

def parse_json(file_path: str):
    def pretty_print(data, indent=0):
        if isinstance(data, dict):
            for key, value in data.items():
                print('  ' * indent + str(key) + ":")
                pretty_print(value, indent + 1)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                print('  ' * indent + f"[{i}]:")
                pretty_print(item, indent + 1)
        else:
            print('  ' * indent + str(data))

    with open(file_path, 'r') as file:
        data = json.load(file)
        print(data)
        pretty_print(data)


parse_json('example.json')
