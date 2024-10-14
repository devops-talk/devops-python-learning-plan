# Search for a File
# Problem: Write a script to search for a file by name in a directory and its subdirectories.
# Objective: Automate file searching tasks.
# search_file.py
import os

def search_file(filename, search_dir):
    """Searches for a file by name in the directory and its subdirectories."""
    for root, dirs, files in os.walk(search_dir):
        if filename in files:
            print(f"File found: {os.path.join(root, filename)}")
            return os.path.join(root, filename)
    print(f"File '{filename}' not found in {search_dir}.")
    return None

if __name__ == "__main__":
    # Specify the file name to search and the directory to search in
    search_dir = "/path/to/directory"
    filename = "example.txt"
    
    print(f"Searching for '{filename}' in '{search_dir}'...")
    search_file(filename, search_dir)
