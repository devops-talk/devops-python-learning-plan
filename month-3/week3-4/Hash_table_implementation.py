# Basic Hash Table Implementation
# Problem: Implement a simple hash table from scratch with methods for inserting, deleting, and searching elements using a hash function.
# Objective: Learn how hash tables work under the hood and how they enable fast data access.


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Initialize the hash table with empty lists

    # Hash function to calculate the index
    def hash_function(self, key):
        return hash(key) % self.size

    # Insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if the key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key does not exist, append the new key-value pair
        self.table[index].append([key, value])

    # Search for a value by key
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value associated with the key
        return None  # Key not found

    # Delete a key-value pair from the hash table
    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]  # Delete the pair
                return True
        return False  # Key not found

    # Print the hash table (for visualization)
    def print_table(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Example usage
hash_table = HashTable()

# Insert key-value pairs
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)

# Search for a key
print("Search for 'banana':", hash_table.search("banana"))  # Output: 20

# Delete a key
hash_table.delete("banana")
print("Search for 'banana' after deletion:", hash_table.search("banana"))  # Output: None

# Print the hash table
hash_table.print_table()
