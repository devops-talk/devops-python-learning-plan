# Trie (Prefix Tree) Implementation
# Simple Trie (Prefix Tree)
# Problem: Implement a Trie data structure to store a set of words and check if a word or prefix exists.
# Objective: Practice using Tries for efficient word storage and searching.

class TrieNode:
    def __init__(self):
        # Each node contains a dictionary of children and a boolean indicating the end of a word
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the Trie with the root node
        self.root = TrieNode()

    def insert(self, word):
        # Start from the root node
        current_node = self.root
        for char in word:
            # For each character in the word, create a new node if it doesn't exist
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        # Mark the end of the word
        current_node.is_end_of_word = True

    def search(self, word):
        # Start from the root node
        current_node = self.root
        for char in word:
            # Traverse through the Trie for each character
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # Check if we've reached the end of the word
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        # Start from the root node
        current_node = self.root
        for char in prefix:
            # Traverse through the Trie for each character in the prefix
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

    def print_trie(self, node=None, word=''):
        # Helper function to print the Trie
        if node is None:
            node = self.root
        if node.is_end_of_word:
            print(word)
        for char, next_node in node.children.items():
            self.print_trie(next_node, word + char)

# Example usage:
trie = Trie()
words = ["apple", "app", "bat", "ball"]
for word in words:
    trie.insert(word)

print("Searching for 'apple':", trie.search("apple"))  # True
print("Searching for 'app':", trie.search("app"))      # True
print("Searching for 'bat':", trie.search("bat"))      # True
print("Searching for 'cat':", trie.search("cat"))      # False
print("Prefix 'ba' exists:", trie.starts_with("ba"))   # True
print("Prefix 'ap' exists:", trie.starts_with("ap"))   # True
print("Prefix 'ca' exists:", trie.starts_with("ca"))   # False

print("\nTrie contents:")
trie.print_trie()
