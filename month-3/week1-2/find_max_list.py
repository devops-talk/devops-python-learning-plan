# Find Maximum in a List
# Problem: Implement a function to find the maximum element in a list without using the built-in max() function.
# Objective: Gain practice in iterating through a list and comparing elements.


def find_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
    
    return max_value

numbers = [3, 5, 1, 8, 2]
result = find_max(numbers)
print(f"The maximum value is: {result}")