# Problem: Given a list of words, create a new list with each word in uppercase.
# Example: Input: ['hello', 'world'] → Output: ['HELLO', 'WORLD']

input_strs = input("enter space separated strings: ")
li_str=list(map(str,input_strs.split()))

output_li_str=[string.upper() for string in li_str]
print(output_li_str)