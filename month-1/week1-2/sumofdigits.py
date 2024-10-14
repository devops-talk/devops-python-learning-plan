# 12. Sum of Digits
# Description: Develop a program that calculates the sum of the digits of a given integer.
# Objective: Practice loops and basic arithmetic.

s=input("please eneter a number: ").strip()

try:
    number = int(s)
    print("The entered string is an integer.")

except ValueError:
    print("The entered string is not an integer.")

sum=0
for i in s:
    sum=int(i)+sum

print(f"sum of digit in given input number is {sum}")
