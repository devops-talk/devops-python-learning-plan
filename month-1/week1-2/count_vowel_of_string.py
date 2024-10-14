# 13. Count Vowels in a String
# Description: Write a program to count the number of vowels in a given string.
# Objective: Practice loops, conditional statements, and string manipulation.


s=input("please eneter a sring: ")

count=0
for char in s:
    if char.lower() in ('a', 'e', 'i', 'o', 'u'):
        count+=1

print(f"string has {count} vowel")