# Dictionary Comprehension

# Description: Use dictionary comprehension to create a dictionary d where the keys are numbers from 1 to 10 and the values are their squares.
# Example: {x: x**2 for x in range(1, 11)} should return {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}.


d = {x: x**2 for x in range(1, 11)}

print(d)