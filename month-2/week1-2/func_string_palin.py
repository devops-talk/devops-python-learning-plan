# Palindrome Checker

# Function: is_palindrome(s: str) -> bool
# Description: Create a function that checks if a given string is a palindrome (reads the same forward and backward). Ignore spaces, punctuation, and capitalization.


def is_palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
    

string1=input("please enter a string to check palindrome: ")
check_plaindrome=is_palindrome(string1)

print(f"string is palindrome: {check_plaindrome}")