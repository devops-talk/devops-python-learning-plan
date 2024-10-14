# 16. Sum of First N Natural Numbers
# Description: Write a program to calculate the sum of the first n natural numbers, where n is provided by the user.
# Objective: Practice loops and arithmetic operations.

num=int((input("enter numer: ")).strip())

sum=0

for i in range(1,num+1):
    sum=sum+i


print(f"sum of all natural numbers till {num} is {sum}")