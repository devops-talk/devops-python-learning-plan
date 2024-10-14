# Palindrome Function

# Description: Write a function is_palindrome(s) that checks if the string s is a palindrome.
# Example: is_palindrome("radar") should return True.


def checks_palindrom(s):
    inv_s=""
    for c in s:
        inv_s=c + inv_s
    if inv_s==s:
        return True
    
s=input("please enter a string a string to check palindrome: ")
result=checks_palindrom(s)
if result:
    print(f"{result}! its palindrome !!")
else:
    print("No!! Its not palindrome")