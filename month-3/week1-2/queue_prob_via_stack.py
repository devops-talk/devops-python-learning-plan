# Implement a Queue Using Two Stacks
# Problem: Implement a queue using two stacks. The queue should support standard queue operations like enqueue() and dequeue().
# Objective: Combine stack and queue logic to understand how data structures can simulate one another.

class QueueUsingStacks:
    def __init__(self):
        # Stack1 is for enqueue operations
        self.stack1 = []
        # Stack2 is for dequeue operations
        self.stack2 = []
    
    # Enqueue operation (push onto stack1)
    def enqueue(self, item):
        self.stack1.append(item)
    
    # Dequeue operation (pop from stack2, or transfer elements from stack1 to stack2 if stack2 is empty)
    def dequeue(self):
        if not self.stack2:
            # Transfer all elements from stack1 to stack2 if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 still has elements, pop the top one (this simulates queue dequeue)
        if self.stack2:
            return self.stack2.pop()
        else:
            return "Queue is empty!"
    
    # Peek operation to view the front element
    def peek(self):
        if not self.stack2:
            # Transfer all elements from stack1 to stack2 if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Peek the top of stack2, which is the front of the queue
        if self.stack2:
            return self.stack2[-1]
        else:
            return "Queue is empty!"
    
    # Check if the queue is empty
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

# Example usage
queue = QueueUsingStacks()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element (peek):", queue.peek())  # Output: 10
print("Dequeued element:", queue.dequeue())   # Output: 10
print("Dequeued element:", queue.dequeue())   # Output: 20
print("Front element (peek):", queue.peek())  # Output: 30
