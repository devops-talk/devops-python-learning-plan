# List Sum

# Description: Write a function sum_list(lst) that returns the sum of all numbers in a list lst.
# Example: sum_list([1, 2, 3, 4]) should return 10.



def sum_list(lst):
    total=0
    for i in lst:
        total=total+i
    return total

input_list=input("please enter space serated integer: ")
list1 = list(map(int, input_list.split()))
total_of_list=sum_list(list1)
print(f"total of entered num is {total_of_list}")


