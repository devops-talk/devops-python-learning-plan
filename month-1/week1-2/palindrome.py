# 11. Palindrome Check
# Description: Write a program to check if a given string is a palindrome (reads the same forward and backward).
# Objective: Combine string manipulation with if-else conditions.


s=input("please eneter a input: ").strip()

reversed_s=""

for char in s:
    reversed_s= char + reversed_s

if reversed_s==s:
    print("input string is palindrome")

else:
    print("it's not a palindrome string")