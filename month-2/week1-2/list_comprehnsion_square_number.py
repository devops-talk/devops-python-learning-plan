# Square Numbers

# Problem: Given a list of numbers, create a new list with the square of each number.
# Example: Input: [1, 2, 3, 4] → Output: [1, 4, 9, 16]

input_numbers = input("enter space separated numbers only: ")
num_li=list(map(int, input_numbers.split()))
output_numbers = [num ** 2 for num in num_li]
print(output_numbers)