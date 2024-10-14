# Python Practical Exercises (week 1-2)

This repository contains a set of practical exercises designed to strengthen your skills in string operations, file handling, exception handling, and list comprehensions in Python. Each exercise includes a brief description of the task to be performed.

## String Operations and Methods

1. **String Reversal**
   - **Function**: `reverse_string(s: str) -> str`
   - **Description**: Write a function that takes a string and returns it reversed.
   - **Example**: `reverse_string("hello")` should return `"olleh"`.

2. **Palindrome Checker**
   - **Function**: `is_palindrome(s: str) -> bool`
   - **Description**: Create a function that checks if a given string is a palindrome (reads the same forward and backward). Ignore spaces, punctuation, and capitalization.

3. **Anagram Check**
   - **Function**: `are_anagrams(s1: str, s2: str) -> bool`
   - **Description**: Develop a function that checks if two strings are anagrams of each other (contain the same characters in different order).

4. **Count Words in a String**
   - **Function**: `count_words(s: str) -> int`
   - **Description**: Write a script that counts the number of words in a given string, considering words to be sequences of characters separated by spaces.

5. **Extract Digits**
   - **Function**: `extract_digits(s: str) -> List[int]`
   - **Description**: Implement a function to extract all the digits from a given string using regular expressions.
   - **Example**: `extract_digits("hello123")` should return `[1, 2, 3]`.

## File Handling

6. **Read and Write to a File**
   - **Script**: `read_write_file(input_path: str, output_path: str)`
   - **Description**: Create a script that reads from a file and writes the content to a new file with line numbers added.

7. **CSV File Reader**
   - **Function**: `read_csv(file_path: str)`
   - **Description**: Write a function that reads data from a CSV file and prints it in a formatted manner, handling any inconsistencies in the data.

8. **JSON File Parser**
   - **Script**: `parse_json(file_path: str)`
   - **Description**: Develop a script to read a JSON file and print the data in a readable format, handling nested structures gracefully.

9. **Log File Analysis**
   - **Script**: `extract_errors(log_file: str, error_file: str)`
   - **Description**: Create a script that parses a log file, extracts error messages, and writes them to a separate file.

10. **Append Data to File**
    - **Script**: `append_to_file(file_path: str)`
    - **Description**: Write a script that appends user input to a file until the user types 'exit'. Each new input should be on a new line.

## Exception Handling

11. **Safe Division**
    - **Function**: `safe_divide(a: float, b: float) -> float`
    - **Description**: Implement a function that performs division and handles division by zero errors, returning a meaningful message.

12. **File Not Found**
    - **Script**: `read_file(file_path: str)`
    - **Description**: Create a script that tries to open a file and handles the `FileNotFoundError` gracefully, providing user-friendly feedback.

13. **Custom Exception**
    - **Class**: `InvalidInputError`
    - **Script**: `validate_input(input_value: Any)`
    - **Description**: Define a custom exception class `InvalidInputError` and use it in a script to handle specific cases (e.g., invalid user input).

14. **Retry Mechanism**
    - **Function**: `retry_read_file(file_path: str, retries: int = 3)`
    - **Description**: Write a function that retries reading a file up to three times if it encounters an `IOError`.

15. **Validate JSON**
    - **Script**: `validate_json(file_path: str)`
    - **Description**: Develop a script that reads a JSON file and handles exceptions for invalid JSON formats, providing specific error messages.

## List Comprehension Exercises

1. **Square Numbers**
   - **Problem**: Given a list of numbers, create a new list with the square of each number.
   - **Example**: Input: `[1, 2, 3, 4]` → Output: `[1, 4, 9, 16]`

2. **Filter Even Numbers**
   - **Problem**: Given a list of numbers, create a new list containing only the even numbers.
   - **Example**: Input: `[1, 2, 3, 4, 5, 6]` → Output: `[2, 4, 6]`

3. **Length of Words**
   - **Problem**: Given a list of words, create a new list with the length of each word.
   - **Example**: Input: `['apple', 'banana', 'cherry']` → Output: `[5, 6, 6]`

4. **Uppercase Words**
   - **Problem**: Given a list of words, create a new list with each word in uppercase.
   - **Example**: Input: `['hello', 'world']` → Output: `['HELLO', 'WORLD']`

5. **Extract Vowels**
   - **Problem**: Given a string, create a list of all the vowels in the string.
   - **Example**: Input: `'hello world'` → Output: `['e', 'o', 'o']`

6. **Flatten a List of Lists**
   - **Problem**: Given a list of lists, create a single flattened list with all the elements.
   - **Example**: Input: `[[1, 2], [3, 4], [5]]` → Output: `[1, 2, 3, 4, 5]`

7. **Remove Duplicates**
   - **Problem**: Given a list of numbers, create a new list with only unique numbers (removing duplicates).
   - **Example**: Input: `[1, 2, 2, 3, 4, 4, 5]` → Output: `[1, 2, 3, 4, 5]`

8. **Reverse Strings**
   - **Problem**: Given a list of strings, create a new list with each string reversed.
   - **Example**: Input: `['abc', 'def', 'ghi']` → Output: `['cba', 'fed', 'ihg']`

## Combined Exercises

16. **Search and Replace in File**
    - **Script**: `search_replace(file_path: str, search_str: str, replace_str: str)`
    - **Description**: Create a script that searches for a specific string in a file and replaces it with another string, handling any file-related exceptions.

17. **Error Logging**
    - **Script**: `perform_operations()`
    - **Description**: Implement a script that performs multiple operations (e.g., file handling, data parsing) and logs any exceptions raised to an error log file.

18. **CSV to JSON Converter**
    - **Script**: `csv_to_json(csv_file: str, json_file: str)`
    - **Description**: Write a script that reads data from a CSV file and writes it to a JSON file, with appropriate error handling for missing files or format issues.

19. **File Encryption/Decryption**
    - **Script**: `encrypt_decrypt(file_path: str, shift: int)`
    - **Description**: Develop a script to encrypt the content of a file using a simple cipher (e.g., Caesar cipher) and then decrypt it back to the original content.

20. **Config File Reader**
    - **Script**: `read_config(file_path: str)`
    - **Description**: Create a script that reads configuration values from a `.ini` or `.yaml` file and handles errors if the file is missing, malformed, or contains invalid keys.
