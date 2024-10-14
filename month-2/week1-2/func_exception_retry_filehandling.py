# Retry Mechanism

# Function: retry_read_file(file_path: str, retries: int = 3)
# Description: Write a function that retries reading a file up to three times if it encounters an IOError.


import time

def retry_read_file(file_path: str, retries: int = 3):
    attempts = 0
    while attempts < retries:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content  
        except IOError:
            attempts += 1
            print(f"Attempt {attempts} failed. Retrying...")
            time.sleep(1)  
    return "Error: Failed to read the file after multiple attempts."


file_path = 'output.txt'
print(retry_read_file(file_path))
