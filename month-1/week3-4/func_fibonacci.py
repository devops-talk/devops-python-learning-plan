# Fibonacci Function

# Description: Create a function fibonacci(n) that returns the nth Fibonacci number.
# Example: fibonacci(6) should return 8.


def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci series:")
    for _ in range(n):
        a, b = b, a + b
    return a


n_terms = int(input("Enter the number of terms: ").strip())

fibonacci_sequence=fibonacci(n_terms)
print(f"And the fibonacci sequence for {n_terms} term is: {fibonacci_sequence}")