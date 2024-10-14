# Fibonacci Sequence (Recursive)
# Problem: Write a recursive function fibonacci(n) to calculate the n-th number in the Fibonacci sequence. Implement memoization to avoid repeated calculations.
# Objective: Practice recursion and optimize it with memoization techniques.
# Fibonacci function with memoization
def fibonacci(n, memo={}):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    if n in memo:
        return memo[n]
    

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Example usage
number = 10
result = fibonacci(number)
print(f"Fibonacci number at position {number} is: {result}")
