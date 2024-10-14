# Unique Elements

# Description: Write a function unique_elements(lst) that takes a list lst and returns a set of unique elements from that list.
# Example: unique_elements([1, 2, 2, 3, 3, 3]) should return {1, 2, 3}.


def unique_elements(lst):
    list2 = list(set(lst))  # Convert the list to a set to remove duplicates, then back to a list
    return list2


li_str=input("please enter your element space separated: ")
li=list(li_str.split())
unique_items=unique_elements(li)
print(f"unique elements in {unique_items}")