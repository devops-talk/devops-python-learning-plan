# Anagram Check

# Function: are_anagrams(s1: str, s2: str) -> bool
# Description: Develop a function that checks if two strings are anagrams of each other (contain the same characters in different order).

def are_anagrams(s1, s2):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Sort the characters in both strings and compare
    return sorted(s1) == sorted(s2)

string1 = input("Please enter the first string to check for anagrams: ")
string2 = input("Please enter the second string to check for anagrams: ")
check_anagrams = are_anagrams(string1, string2)

print(f"Strings are anagrams: {check_anagrams}")