# Count Word Frequencies

# Description: Write a function word_frequencies(s) that takes a string s and returns a dictionary with the frequency count of each word.
# Example: word_frequencies("hello world hello") should return {'hello': 2, 'world': 1}.


def word_frequencies(s):
    frequency={}
    words=s.split()
    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    return frequency

string1 = input("Enter any string: ")

every_word_freq = word_frequencies(string1)

print(f"Word frequency in this string is as follows: {every_word_freq}")


