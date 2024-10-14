# Remove Duplicates

# Problem: Given a list of numbers, create a new list with only unique numbers (removing duplicates).
# Example: Input: [1, 2, 2, 3, 4, 4, 5] → Output: [1, 2, 3, 4, 5]


input_numbers = input("enter space separated numbers only: ")
#num_li=set(map(int, input_numbers.split()))

num_li=list(map(int, input_numbers.split()))
output_li = list(set(num_li))


print(output_li)
