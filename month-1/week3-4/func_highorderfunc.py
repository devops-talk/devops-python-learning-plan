# Higher-Order Function

# Description: Write a function apply_function(func, lst) that takes a function func and a list lst, and applies func to each element in lst.
# Example: apply_function(lambda x: x * 2, [1, 2, 3]) should return [2, 4, 6].


# def apply_function(lst):
#     list1=[]
#     for i in lst:
#         list1.append(i*2)
#     return list1

# result=apply_function([1,2,3])
# print(result)
def apply_function(func, lst):
    return [func(x) for x in lst]

input_list=input("please enter space serated integer: ")
list1 = list(map(int, input_list.split()))
result = apply_function(lambda x: x * 2, list1)
print(result) 