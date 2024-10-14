# Implement a Doubly Linked List
# Problem: Implement a doubly linked list with methods to insert at both ends (insert_at_head() and insert_at_tail()) and delete a node (delete_node()).
# Objective: Learn the differences between singly and doubly linked lists and how to manage prev pointers.

# Define the Node class for the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

# Define the DoublyLinkedList class to manage the DLL
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    # Method to insert a node at the head (beginning) of the list
    def insert_at_head(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty, set head to new_node
            self.head = new_node
        else:
            new_node.next = self.head  # Set new_node's next to the current head
            self.head.prev = new_node  # Update the current head's prev to new_node
            self.head = new_node  # Update the head to the new node
    
    # Method to insert a node at the tail (end) of the list
    def insert_at_tail(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty, set the new_node as the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link last node's next to new_node
            new_node.prev = current  # Link new_node's prev to the last node

    # Method to delete the first node that contains the specified data
    def delete_node(self, data):
        if not self.head:  # If the list is empty, return
            return
        
        current = self.head
        
        # If the node to be deleted is the head
        if current.data == data:
            if not current.next:  # If the head is the only node, just remove it
                self.head = None
            else:
                self.head = current.next  # Move the head to the next node
                self.head.prev = None  # Remove the link to the old head
            return
        
        # Traverse the list to find the node to delete
        while current and current.data != data:
            current = current.next
        
        if current:  # If the node was found
            if current.next:  # If it's not the last node
                current.next.prev = current.prev  # Update the next node's prev
            if current.prev:  # If it's not the first node
                current.prev.next = current.next  # Update the previous node's next

    # Method to print the list from head to tail
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")  # Use <-> to indicate double links
            current = current.next
        print("None")  # End of the list

# Example usage
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_tail(20)
dll.insert_at_tail(30)
dll.insert_at_head(5)

# Print the list
print("Doubly Linked List after insertions:")
dll.print_list()  # Output: 5 <-> 10 <-> 20 <-> 30 <-> None

# Delete a node
dll.delete_node(20)
print("Doubly Linked List after deleting 20:")
dll.print_list()  # Output: 5 <-> 10 <-> 30 <-> None
