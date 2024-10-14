# 9. Fibonacci Sequence
# Description: Write a program that generates the first n numbers of the Fibonacci sequence, where n is provided by the user.
# Objective: Use loops and work with sequences.


# Get the number of terms from the user
n_terms = int(input("Enter the number of terms: ").strip())

# Initialize the first two terms
a, b = 0, 1

# Print the Fibonacci series
print("Fibonacci series:")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b  # Update the values of a and b
