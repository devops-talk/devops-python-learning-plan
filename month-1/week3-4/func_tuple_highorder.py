# Tuple Operations

# Description: Write a function double_tuple(t) that takes a tuple t and returns a new tuple with each element doubled.
# Example: double_tuple((1, 2, 3)) should return (2, 4, 6).



def apply_function(func, tpl):
    return [func(x) for x in tpl]







input_list=input("please enter space serated integer: ")
tuple1 = tuple(map(int, input_list.split()))
result = apply_function(lambda x: x * 2, tuple1)
print(result) 