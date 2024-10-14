# Merge Dictionaries

# Description: Write a function merge_dicts(d1, d2) that merges two dictionaries d1 and d2, combining their key-value pairs.
# Example: merge_dicts({'a': 1}, {'b': 2}) should return {'a': 1, 'b': 2}.


# def merge_dicts(dict1, dict2):

#     merged_dict = {**dict1, **dict2}
#     return merged_dict


def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)  
    return merged_dict

dict1_str = input("Enter first dictionary (format should be in dict format): ")
dict2_str = input("Enter second dictionary (format should be in dict format): ")


try:
    dict1 = eval(dict1_str)
    dict2 = eval(dict2_str)
    
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        merged_dicts = merge_dicts(dict1, dict2)
        print(f"Merged dictionaries: {merged_dicts}")
    else:
        print("Both inputs need to be dictionaries.")
except (SyntaxError, NameError):
    print("Invalid dictionary format. Please enter the dictionaries correctly.")
