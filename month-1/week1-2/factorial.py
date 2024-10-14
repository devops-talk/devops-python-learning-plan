# 8. Factorial Calculation
# Description: Implement a program to calculate the factorial of a given number using a loop.
# Objective: Practice using loops (for, while).

n=int((input("enter numer: ")).strip())
result = 1
for i in range(1,n+1):
    result *= i

print(f"The factorial of {n} is {result}")
    

