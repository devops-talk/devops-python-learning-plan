# Recursive Directory Search
# Problem: Write a recursive function search_file(directory, filename) that searches for a specific file in a directory and its subdirectories.
# Objective: Use recursion to traverse directories, a relevant task for file management in DevOps.


import os


def search_file(directory, filename):
  
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)  
        
       
        if os.path.isdir(item_path):
            result = search_file(item_path, filename)
            if result:  
                return result
        
  
        elif os.path.isfile(item_path) and item == filename:
            return item_path

    return None

directory_to_search = '/Users/shobhit.srivastava/Documents/aws/project/python-master/python mastering exercise 16 week plan/month-2/week3-4'  
file_to_find = 'example.txt'

result = search_file(directory_to_search, file_to_find)
if result:
    print(f"File found: {result}")
else:
    print("File not found.")
