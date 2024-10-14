# String Reversal

# Function: reverse_string(s: str) -> str
# Description: Write a function that takes a string and returns it reversed.
# Example: reverse_string("hello") should return "olleh".

def reverse_string(s):
    re_str=s[::-1]
    return re_str


string1=input("please enter a string to get reverse of it: ")

rev_str=reverse_string(string1)

print(f"reverse of this string is: {rev_str}")


