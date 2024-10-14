# Length of Words

# Problem: Given a list of words, create a new list with the length of each word.
# Example: Input: ['apple', 'banana', 'cherry'] → Output: [5, 6, 6]


input_strs = input("enter space separated strings: ")
li_str=list(map(str,input_strs.split()))

output_li_str=[len(string) for string in li_str]
print(output_li_str)