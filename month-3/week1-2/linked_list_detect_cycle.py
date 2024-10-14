# Problem: Write a function to detect if a linked list contains a cycle. Use Floyd's cycle detection algorithm (two-pointer technique).
#  Objective: Practice implementing a common algorithm for cycle detection in linked lists.


# Define the Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Initialize the next pointer to None

# Define the LinkedList class
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
    
    # Method to detect if there is a cycle in the linked list
    def detect_cycle(self):
        slow = self.head  # Initialize the slow pointer
        fast = self.head  # Initialize the fast pointer
        
        # Traverse the list with the two pointers
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
            
            # If slow and fast pointers meet, there is a cycle
            if slow == fast:
                return True
        
        # If fast pointer reaches the end, there is no cycle
        return False

# Example usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

# Create a cycle manually by linking the last node to the second node
linked_list.head.next.next.next.next = linked_list.head.next

# Check if the linked list contains a cycle
has_cycle = linked_list.detect_cycle()
print(f"Cycle detected: {has_cycle}")
