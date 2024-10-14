# Python Practice Exercises: Weeks 3-4

## Weeks 3-4: Functions, Lists, Tuples, and Dictionaries

### Functions

1. **Basic Function**
   - **Description**: Write a function `add_numbers(a, b)` that returns the sum of two numbers.
   - **Example**: `add_numbers(3, 5)` should return `8`.

2. **Factorial Function**
   - **Description**: Implement a function `factorial(n)` that returns the factorial of a number `n`.
   - **Example**: `factorial(5)` should return `120`.

3. **Palindrome Function**
   - **Description**: Write a function `is_palindrome(s)` that checks if the string `s` is a palindrome.
   - **Example**: `is_palindrome("radar")` should return `True`.

4. **Fibonacci Function**
   - **Description**: Create a function `fibonacci(n)` that returns the nth Fibonacci number.
   - **Example**: `fibonacci(6)` should return `8`.

5. **Lambda Function for Squaring**
   - **Description**: Write a lambda function `square` that takes a number and returns its square.
   - **Example**: `square(4)` should return `16`.

6. **Higher-Order Function**
   - **Description**: Write a function `apply_function(func, lst)` that takes a function `func` and a list `lst`, and applies `func` to each element in `lst`.
   - **Example**: `apply_function(lambda x: x * 2, [1, 2, 3])` should return `[2, 4, 6]`.

### Lists and Tuples

7. **List Sum**
   - **Description**: Write a function `sum_list(lst)` that returns the sum of all numbers in a list `lst`.
   - **Example**: `sum_list([1, 2, 3, 4])` should return `10`.

8. **List Even Numbers**
   - **Description**: Write a function `even_numbers(lst)` that returns a new list containing only the even numbers from `lst`.
   - **Example**: `even_numbers([1, 2, 3, 4])` should return `[2, 4]`.

9. **Tuple Operations**
   - **Description**: Write a function `double_tuple(t)` that takes a tuple `t` and returns a new tuple with each element doubled.
   - **Example**: `double_tuple((1, 2, 3))` should return `(2, 4, 6)`.

10. **List Sorting**
    - **Description**: Write a function `sort_strings(lst)` that sorts a list of strings `lst` alphabetically.
    - **Example**: `sort_strings(["banana", "apple", "cherry"])` should return `["apple", "banana", "cherry"]`.

11. **Flatten List of Lists**
    - **Description**: Write a function `flatten_list(lst)` that flattens a list of lists `lst` into a single list.
    - **Example**: `flatten_list([[1, 2], [3, 4], [5]])` should return `[1, 2, 3, 4, 5]`.

12. **Find Maximum in List**
    - **Description**: Write a function `find_max(lst)` that finds the maximum value in a list of numbers `lst`.
    - **Example**: `find_max([3, 1, 4, 1, 5])` should return `5`.

### Dictionaries and Sets

13. **Count Word Frequencies**
    - **Description**: Write a function `word_frequencies(s)` that takes a string `s` and returns a dictionary with the frequency count of each word.
    - **Example**: `word_frequencies("hello world hello")` should return `{'hello': 2, 'world': 1}`.

14. **Merge Dictionaries**
    - **Description**: Write a function `merge_dicts(d1, d2)` that merges two dictionaries `d1` and `d2`, combining their key-value pairs.
    - **Example**: `merge_dicts({'a': 1}, {'b': 2})` should return `{'a': 1, 'b': 2}`.

15. **Dictionary Comprehension**
    - **Description**: Use dictionary comprehension to create a dictionary `d` where the keys are numbers from 1 to 10 and the values are their squares.
    - **Example**: `{x: x**2 for x in range(1, 11)}` should return `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}`.

16. **Find Common Elements**
    - **Description**: Write a function `common_elements(set1, set2)` that returns the intersection of two sets `set1` and `set2`.
    - **Example**: `common_elements({1, 2, 3}, {2, 3, 4})` should return `{2, 3}`.

17. **Unique Elements**
    - **Description**: Write a function `unique_elements(lst)` that takes a list `lst` and returns a set of unique elements from that list.
    - **Example**: `unique_elements([1, 2, 2, 3, 3, 3])` should return `{1, 2, 3}`.

18. **Invert Dictionary**
    - **Description**: Write a function `invert_dict(d)` that takes a dictionary `d` and returns a new dictionary where the keys and values are swapped.
    - **Example**: `invert_dict({'a': 1, 'b': 2})` should return `{1: 'a', 2: 'b'}`.

### Mixed Topics

19. **Matrix Transposition**
    - **Description**: Write a function `transpose(matrix)` that transposes a matrix (list of lists).
    - **Example**: `transpose([[1, 2, 3], [4, 5, 6]])` should return `[[1, 4], [2, 5], [3, 6]]`.

20. **Custom Filter Function**
    - **Description**: Implement a function `custom_filter(lst, condition)` that takes a list `lst` and a condition function `condition`, and returns a list of elements that satisfy the condition.
    - **Example**: `custom_filter([1, 2, 3, 4], lambda x: x % 2 == 0)` should return `[2, 4]`.
