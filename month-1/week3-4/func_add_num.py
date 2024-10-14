# Functions
# Basic Function

# Description: Write a function add_numbers(a, b) that returns the sum of two numbers.
# Example: add_numbers(3, 5) should return 8.


def add_numbers(a,b):
    return a+b



a= int(input("Enter the first num: ").strip())
b= int(input("Enter the second num: ").strip())

total=add_numbers(a, b)
print(f"total of two number is {total}")
