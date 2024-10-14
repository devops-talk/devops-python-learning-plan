# Extract Digits

# Function: extract_digits(s: str) -> List[int]
# Description: Implement a function to extract all the digits from a given string using regular expressions.
# Example: extract_digits("hello123") should return [1, 2, 3].


def extract_digits(s):
    # Use list comprehension to extract digits from the string
    digits = [char for char in s if char.isdigit()]
    return ''.join(digits)

string1 = input("Please enter the string to extract digits: ")

extracted_digits = extract_digits(string1)

print(f"Extracted digits: {extracted_digits}")
    
