# Queue Implementation Using a List
# Problem: Create a queue using a Python list. The queue should support enqueue(), dequeue(), and peek() operations.
# Objective: Understand FIFO (First In, First Out) operations using a list data structure.

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) 
        else:
            return "Queue is empty!"
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]  
        else:
            return "Queue is empty!"
    
    def is_empty(self):
        return len(self.queue) == 0

# Example usage
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print("Front element (peek):", my_queue.peek())  
print("Dequeued element:", my_queue.dequeue())  
print("Dequeued element:", my_queue.dequeue())   
