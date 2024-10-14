#  Reverse a List
# Problem: Write a function that takes a list and returns the list in reverse order without using built-in methods like reverse().
# Objective: Practice list manipulation and understand list traversal.


def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

numbers = [1, 2, 3, 4, 5]
result = reverse_list(numbers)
print(result) 