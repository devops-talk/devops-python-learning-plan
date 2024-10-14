# Stack Implementation Using Linked List
# Problem: Implement a stack using a linked list instead of a Python list. The stack should support push(), pop(), and peek() operations.
# Objective: Learn how to use a linked list for stack operations and reinforce the concept of LIFO (Last In, First Out) behavior.

# Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data the node holds
        self.next = None  # Reference to the next node in the list

# Stack class implemented using linked list
class Stack:
    def __init__(self):
        self.top = None  # Initialize the top of the stack as None (empty stack)

    # Method to push an element onto the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.top  # Link the new node to the current top
        self.top = new_node  # Update the top to the new node
        print(f"Pushed {data} onto the stack")

    # Method to pop an element from the stack
    def pop(self):
        if self.is_empty():  # If the stack is empty, nothing to pop
            print("Stack is empty. Nothing to pop.")
            return None
        popped_data = self.top.data  # Get the data from the top node
        self.top = self.top.next  # Move the top to the next node
        print(f"Popped {popped_data} from the stack")
        return popped_data

    # Method to peek at the top element without removing it
    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        print(f"Top element is {self.top.data}")
        return self.top.data

    # Method to check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Method to print the stack
    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
            return
        current = self.top
        print("Stack elements (top to bottom):")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the stack

# Example usage
stack = Stack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Peek at the top element
stack.peek()  # Output: Top element is 30

# Print stack elements
stack.print_stack()  # Output: Stack elements: 30 -> 20 -> 10 -> None

# Pop elements from the stack
stack.pop()  # Output: Popped 30 from the stack
stack.pop()  # Output: Popped 20 from the stack

# Print stack elements after popping
stack.print_stack()  # Output: Stack elements: 10 -> None

# Check if stack is empty
print(stack.is_empty())  # Output: False

# Pop the last element
stack.pop()  # Output: Popped 10 from the stack

# Check if stack is empty after popping all elements
print(stack.is_empty())  # Output: True

# Attempt to pop from an empty stack
stack.pop()  # Output: Stack is empty. Nothing to pop.
