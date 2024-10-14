# Flatten List of Lists

# Description: Write a function flatten_list(lst) that flattens a list of lists lst into a single list.
# Example: flatten_list([[1, 2], [3, 4], [5]]) should return [1, 2, 3, 4, 5].



def flatten_list(lst):
    return [item for sublist in lst for item in sublist]




nested_list_str=input("Enter a nested list (e.g., [[1, 2], [3, 4], [5]]): ")

nested_list=eval(nested_list_str)

print(nested_list)

flatten_list=flatten_list(nested_list)
print(flatten_list)