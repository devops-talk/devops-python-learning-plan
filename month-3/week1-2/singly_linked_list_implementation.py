# Implement a Singly Linked List
# Problem: Create a basic implementation of a singly linked list with methods to insert_at_head(), insert_at_tail(), delete_node(), and print_list().
# Objective: Understand the structure and operations of singly linked lists.


# Define the Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Initialize the next pointer to None

# Define the LinkedList class to manage the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None
    
    # Method to insert a node at the head (beginning) of the list
    def insert_at_head(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Update the head to the new node
    
    # Method to insert a node at the tail (end) of the list
    def insert_at_tail(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the last node to the new node
    
    # Method to delete the first node with the specified data
    def delete_node(self, data):
        if not self.head:  # If the list is empty, do nothing
            return
        
        # If the node to be deleted is the head
        if self.head.data == data:
            self.head = self.head.next  # Move the head to the next node
            return
        
        # Otherwise, find the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        # If the node was found, unlink it from the list
        if current.next:
            current.next = current.next.next
    
    # Method to print all elements in the linked list
    def print_list(self):
        current = self.head
        while current:  # Traverse the list
            print(current.data, end=" -> ")  # Print each node's data
            current = current.next
        print("None")  # End of the list

# Example usage
linked_list = LinkedList()
linked_list.insert_at_head(30)
linked_list.insert_at_head(20)
linked_list.insert_at_tail(40)
linked_list.insert_at_tail(50)

# Print the linked list
print("Linked List after insertions:")
linked_list.print_list()  # Output: 20 -> 30 -> 40 -> 50 -> None

# Delete a node
linked_list.delete_node(30)
print("Linked List after deleting 30:")
linked_list.print_list()  # Output: 20 -> 40 -> 50 -> None

