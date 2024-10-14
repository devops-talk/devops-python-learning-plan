# List Even Numbers

# Description: Write a function even_numbers(lst) that returns a new list containing only the even numbers from lst.
# Example: even_numbers([1, 2, 3, 4]) should return [2, 4].

def even_numbers(lst):
    evn_list=[]
    for i in lst:
        if i%2==0:
            evn_list.append(i)
    return evn_list





str=input("enter space separated integer: ")
list1=list(map(int,str.split()))
even_num=even_numbers(list1)
print(f"list of even numbers is {even_num}")