# Count Words in a String

# Function: count_words(s: str) -> int
# Description: Write a script that counts the number of words in a given string, considering words to be sequences of characters separated by spaces.



def count_words(s1):
    li=list(s1.split())
    count=len(li)
    return count

string1 = input("Please enter the string to count words: ")

check_count = count_words(string1)

print(f"string count is: {check_count}")