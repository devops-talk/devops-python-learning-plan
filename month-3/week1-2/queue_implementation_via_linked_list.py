# Queue Implementation Using Linked List
# Problem: Implement a queue using a linked list. The queue should support enqueue(), dequeue(), and peek() operations.
# Objective: Understand how to implement a queue using a linked list and reinforce the concept of FIFO (First In, First Out) behavior.


# Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data the node holds
        self.next = None  # Reference to the next node in the list

# Queue class implemented using linked list
class Queue:
    def __init__(self):
        self.front = None  # The front of the queue (to dequeue from)
        self.rear = None   # The rear of the queue (to enqueue to)

    # Method to enqueue an element to the queue
    def enqueue(self, data):
        new_node = Node(data)  # Create a new node
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node  # Both front and rear point to the new node
        else:
            self.rear.next = new_node  # Link the current rear node to the new node
            self.rear = new_node  # Update the rear to the new node
        print(f"Enqueued {data}")

    # Method to dequeue an element from the queue
    def dequeue(self):
        if self.is_empty():  # If the queue is empty, nothing to dequeue
            print("Queue is empty. Nothing to dequeue.")
            return None
        dequeued_data = self.front.data  # Get the data from the front node
        self.front = self.front.next  # Move the front to the next node
        if self.front is None:  # If the queue becomes empty, reset rear to None
            self.rear = None
        print(f"Dequeued {dequeued_data}")
        return dequeued_data

    # Method to peek at the front element without removing it
    def peek(self):
        if self.is_empty():  # If the queue is empty, there's nothing to peek at
            print("Queue is empty. Nothing to peek.")
            return None
        print(f"Front element is {self.front.data}")
        return self.front.data

    # Method to check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Method to print the queue
    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        print("Queue elements (front to rear):")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the queue

# Example usage
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Peek at the front element
queue.peek()  # Output: Front element is 10

# Print queue elements
queue.print_queue()  # Output: Queue elements: 10 -> 20 -> 30 -> None

# Dequeue elements from the queue
queue.dequeue()  # Output: Dequeued 10
queue.dequeue()  # Output: Dequeued 20

# Print queue elements after dequeue
queue.print_queue()  # Output: Queue elements: 30 -> None

# Check if queue is empty
print(queue.is_empty())  # Output: False

# Dequeue the last element
queue.dequeue()  # Output: Dequeued 30

# Check if queue is empty after dequeueing all elements
print(queue.is_empty())  # Output: True

# Attempt to dequeue from an empty queue
queue.dequeue()  # Output: Queue is empty. Nothing to dequeue.
