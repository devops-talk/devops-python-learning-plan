# Find Maximum in List (Recursive)
# Problem: Write a recursive function find_max(lst) that finds the maximum value in a list of integers lst.
# Objective: Use recursion to process lists and find a solution.



def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    max_of_rest = find_max(lst[1:])  
    return lst[0] if lst[0] > max_of_rest else max_of_rest

numbers = [3, 5, 1, 8, 2]
result = find_max(numbers)
print(f"The maximum value is: {result}")