# 10. Reverse a String
# Description: Create a program that takes a string input and prints it in reverse order.
# Objective: Practice string manipulation and loops.

s=input("please eneter a input: ").strip()

print("we have following ways to reverse")
s=s[::-1]
print(s)

reversed_s=""

for char in s:
    reversed_s=char+reversed_s


print(reversed_s)