# Dynamic Programming (DP)
# Fibonacci Sequence (DP Approach)
# Problem: Implement a dynamic programming solution to calculate the n-th Fibonacci number to avoid redundant recursive calculations.
# Objective: Practice dynamic programming by using memoization to optimize recursive solutions.


# Dynamic Programming (DP) solution for Fibonacci sequence using memoization

def fibonacci_dp(n):
    # Create a list to store Fibonacci numbers
    fib = [0] * (n + 1)
    
    # Base cases
    fib[0] = 0
    if n > 0:
        fib[1] = 1
    
    # Compute Fibonacci numbers from 2 to n
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Example usage
n = 10
print(f"The {n}-th Fibonacci number is: {fibonacci_dp(n)}")
