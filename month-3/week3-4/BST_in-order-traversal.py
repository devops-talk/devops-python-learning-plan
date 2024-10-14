class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # Left child
        self.right = None  # Right child

class BST:
    def __init__(self):
        self.root = None

    # Method to insert a value into the BST
    def insert(self, value):
        # If the tree is empty, create the root node
        if self.root is None:
            self.root = Node(value)
        else:
            # Insert the value starting from the root
            self._insert_recursive(self.root, value)

    # Helper method for recursive insertion
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            # Go to the left subtree
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            # Go to the right subtree
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    # Method to perform in-order traversal
    def in_order_traversal(self):
        elements = []
        self._in_order_recursive(self.root, elements)
        return elements

    # Helper method for recursive in-order traversal
    def _in_order_recursive(self, current_node, elements):
        if current_node:
            # Traverse the left subtree
            self._in_order_recursive(current_node.left, elements)
            # Visit the root
            elements.append(current_node.value)
            # Traverse the right subtree
            self._in_order_recursive(current_node.right, elements)

# Example Usage
tree = BST()

# Insert values into the tree
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

# Perform in-order traversal
print("In-Order Traversal of the BST:", tree.in_order_traversal())
