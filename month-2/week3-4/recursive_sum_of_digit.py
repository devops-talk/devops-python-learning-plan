# Sum of Digits (Recursive)
# Problem: Implement a recursive function sum_of_digits(n) to compute the sum of digits of a given integer n.
# Objective: Solve a simple problem using recursion.


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage
n = sum_of_digits(123)
print(n)