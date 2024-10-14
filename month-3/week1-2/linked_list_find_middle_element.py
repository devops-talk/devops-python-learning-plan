# Find the Middle of a Linked List
# Problem: Implement a function that finds the middle element of a singly linked list. If the list has an even number of elements, return the second of the two middle elements.
# Objective: Understand how to traverse a linked list and find the middle.
# Define a Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Initialize the next pointer to None

# Define a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None
    
    # Method to add elements to the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:
            self.head = new_node  # If the list is empty, set the head to the new node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the last node to the new node
    
    # Method to find the middle element of the linked list
    def find_middle(self):
        slow = self.head  # Slow pointer
        fast = self.head  # Fast pointer
        
        # Traverse the list with two pointers
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
        
        # Slow will now point to the middle node
        if slow:
            return slow.data
        return None

# Example usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

middle = linked_list.find_middle()
print(f"The middle element is: {middle}")
