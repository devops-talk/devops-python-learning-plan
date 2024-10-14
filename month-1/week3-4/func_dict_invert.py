# Invert Dictionary

# Description: Write a function invert_dict(d) that takes a dictionary d and returns a new dictionary where the keys and values are swapped.
# Example: invert_dict({'a': 1, 'b': 2}) should return {1: 'a', 2: 'b'}.


import json

def invert_dict(dict1):
    dict2 = {value: key for key, value in dict1.items()}
    return dict2


# first method
# import ast
# dict_input = input("Enter dictionary (e.g., {'key1': 'value1', 'key2': 'value2'}): ")
# my_dict = ast.literal_eval(dict_input)

# second method
# dict_input = input('Enter dictionary in JSON format: ')
# my_dict = json.loads(dict_input)


# third method

file_path = 'data.json'

with open(file_path, 'r') as file:
    dict1=json.load(file)

invertdict=invert_dict(dict1)

print(f"inverted dictionary : {invertdict}")


