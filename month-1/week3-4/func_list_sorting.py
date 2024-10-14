# List Sorting

# Description: Write a function sort_strings(lst) that sorts a list of strings lst alphabetically.
# Example: sort_strings(["banana", "apple", "cherry"]) should return ["apple", "banana", "cherry"].


def sort_strings(lst):
    s_list = sorted(lst)
    return s_list

    




input_list=input("please enter space serated strings: ")
list1=list(input_list.split())
sorted_string_list=sort_strings(list1)
print(sorted_string_list)