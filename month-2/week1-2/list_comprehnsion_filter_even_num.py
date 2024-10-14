# Filter Even Numbers

# Problem: Given a list of numbers, create a new list containing only the even numbers.
# Example: Input: [1, 2, 3, 4, 5, 6] → Output: [2, 4, 6]


input_numbers = input("enter space separated numbers only: ")
num_li=list(map(int, input_numbers.split()))

output_numbers = [num for num in num_li if num % 2 == 0]

print(output_numbers)