# Description: Write a lambda function square that takes a number and returns its square.
# Example: square(4) should return 16.

def square(n):
    square=lambda n: n * n
    return square(n)

n = int(input("Enter the number! you want square of: ").strip())
result=square(n)

print(f"square of {n} is {result}")