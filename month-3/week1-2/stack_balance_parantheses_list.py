# Check for Balanced Parentheses (Stack Problem)
# Problem: Write a function to check if the parentheses in a given string are balanced. You should use a stack to solve this problem.
# Objective: Practice using a stack to solve a common problem involving matching parentheses.


def is_balanced(expression):
    stack = []
    
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        
        elif char in ')}]':

            if stack and stack[-1] == matching_parentheses[char]:
                stack.pop()  
            else:
                return False 
            
    return len(stack) == 0


expression1 = "{[()()]}"
expression2 = "{[(])}"
expression3 = "((()))"

print(f"Expression 1 is balanced: {is_balanced(expression1)}")  # Output: True
print(f"Expression 2 is balanced: {is_balanced(expression2)}")  # Output: False
print(f"Expression 3 is balanced: {is_balanced(expression3)}")  # Output: True
