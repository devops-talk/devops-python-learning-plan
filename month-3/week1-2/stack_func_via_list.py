# 3. Stack Implementation Using a List
# Problem: Implement a simple stack using Python's list data structure. The stack should support push(), pop(), and peek() operations.
# Objective: Learn stack operations and LIFO (Last In, First Out) behavior.


class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"
    
    def is_empty(self):
        return len(self.stack) == 0

# Example usage
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Top element (peek):", my_stack.peek())  # Output: 30
print("Popped element:", my_stack.pop())       # Output: 30
print("Popped element:", my_stack.pop())       # Output: 20
print("Top element (peek):", my_stack.peek())  # Output: 10
