# 7. Largest of Three Numbers
# Description: Write a program that takes three numbers as input and prints the largest of the three.
# Objective: Practice nested if-else statements.

a=int((input("enter first numer: ")).strip())
b=int((input("enter second numer: ")).strip())
c=int((input("enter third numer: ")).strip())


if a==b==c:
    print("all input numbers are equal")
elif a>=b and a>=c:
    print("a is largest number")
elif b>=a and b>=c:
    print("b is largest number")
else:
    print("c is largest number")