# Problem: Given a list of lists, create a single flattened list with all the elements.
# Example: Input: [[1, 2], [3, 4], [5]] → Output: [1, 2, 3, 4, 5]


# Input: List of lists
input_list = input("please eneter in input like [[1, 2], [3, 4], [5]]: ")
list_of_lists=eval(input_list)

# Flatten the list of lists
flattened_list = [item for sublist in list_of_lists for item in sublist]

print(flattened_list)
