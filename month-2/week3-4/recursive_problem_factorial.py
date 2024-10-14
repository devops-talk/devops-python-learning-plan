# Factorial Calculation (Recursive)
# Problem: Write a recursive function factorial(n) that computes the factorial of a given number n.
# Objective: Practice recursion with a classic mathematical problem.



def factorial(n):
   
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"Factorial of {number} is: {result}")
