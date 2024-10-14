# Problem: Given a string, create a list of all the vowels in the string.
# Example: Input: 'hello world' → Output: ['e', 'o', 'o']


input_strs = input("Enter a string: ")

# List comprehension to extract vowels from the input string
output_li_str = [char for char in input_strs if char.lower() in ("a", "e", "i", "o", "u")]

print(output_li_str)
