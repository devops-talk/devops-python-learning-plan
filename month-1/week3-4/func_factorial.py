# Factorial Function

# Description: Implement a function factorial(n) that returns the factorial of a number n.
# Example: factorial(5) should return 120.


def factorial(n):
    result=1
    for i in range(1,n+1):
        result *= i
    return result


n=int((input("enter numer: ")).strip())
fact=factorial(n)

print(f"factorial of {n} is {fact}")