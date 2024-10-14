# 18. Count Occurrences of a Character
# Description: Write a program that counts the number of times a specific character appears in a given string.
# Objective: Combine loops with string manipulation.

string=input("enter any string: ").lower()
char=input("enter a character to check count in string").lower()

sum_of_char=0
for i in string:
    if char in i:
        sum_of_char+=1

print(f"sum of character count in string is {sum_of_char}")
