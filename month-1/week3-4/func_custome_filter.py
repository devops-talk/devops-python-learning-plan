# Custom Filter Function

# Description: Implement a function custom_filter(lst, condition) that takes a list lst and a condition function condition, and returns a list of elements that satisfy the condition.
# Example: custom_filter([1, 2, 3, 4], lambda x: x % 2 == 0) should return [2, 4].


def custom_filter(lst, condition):
    filtered_list = []
    for item in lst:
        if condition(item):
            filtered_list.append(item)
    
    return filtered_list

li_str=input("enter list of integer e,g [[1, 2, 3]: ")
li=eval(li_str)


result = custom_filter(li, lambda x: x % 2 == 0)
print(result) 
