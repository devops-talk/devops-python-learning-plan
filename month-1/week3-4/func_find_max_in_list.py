# Find Maximum in List

# Description: Write a function find_max(lst) that finds the maximum value in a list of numbers lst.
# Example: find_max([3, 1, 4, 1, 5]) should return 5.



# def find_max(lst):
#     highest_element=max(lst)
#     return highest_element



# list_str=input("enter integer space separated: ")
# list1=list(map(int,list_str.split()))

# find_max_element=find_max(list1)
# print(f"highest element is {find_max_element}")

def find_max(lst):
    highest_element=lst[0]
    for i in range(1,len(lst)):
        if lst[i] >= highest_element:
            highest_element=lst[i]
    return highest_element





list_str=input("enter integer space separated: ")
list1=list(map(int,list_str.split()))

find_max_element=find_max(list1)
print(f"highest element is {find_max_element}")