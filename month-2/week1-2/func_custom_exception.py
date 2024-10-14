# Class: InvalidInputError
# Script: validate_input(input_value: Any)
# Description: Define a custom exception class InvalidInputError and use it in a script to handle specific cases (e.g., invalid user input).



class InvalidInputError(Exception):
    """Custom exception for invalid input."""
    def __init__(self, message="Invalid input provided"):
        self.message = message
        super().__init__(self.message)
def validate_input(input_value):
    try:
        if not isinstance(input_value, (int, float)):  
            raise InvalidInputError("Input must be a number.")
        if input_value < 0:  
            raise InvalidInputError("Input must be a non-negative number.")
        return f"Valid input: {input_value}"
    except InvalidInputError as e:
        return f"Error: {e}"


user_input = -10
print(validate_input(user_input))

user_input = "abc"
print(validate_input(user_input))

user_input = 5
print(validate_input(user_input))
