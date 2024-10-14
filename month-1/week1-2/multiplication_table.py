# 15. Multiplication Table
# Description: Write a program that prints the multiplication table of a given number up to 10.
# Objective: Reinforce loop structures (for loops).



n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
