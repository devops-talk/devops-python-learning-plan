# Problem: Given a list of strings, create a new list with each string reversed.
# Example: Input: ['abc', 'def', 'ghi'] → Output: ['cba', 'fed', 'ihg']



input_strs = input("enter space separated strings: ")
li_str=list(map(str,input_strs.split()))

output_li_str=[item[::-1] for item in li_str  ]
print(output_li_str)