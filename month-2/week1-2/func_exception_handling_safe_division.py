# Function: safe_divide(a: float, b: float) -> float
# Description: Implement a function that performs division and handles division by zero errors, returning a meaningful message.

def safe_divide(a: float, b: float):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
    return result

num1=int(input("enter first number: ").strip())
num2=int(input("enter second number: ").strip())

print(f"result of division of num1/num2 is : {safe_divide(num1,num2)}")