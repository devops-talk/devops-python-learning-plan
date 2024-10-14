# Append Data to File

# Script: append_to_file(file_path: str)
# Description: Write a script that appends user input to a file until the user types 'exit'. Each new input should be on a new line.


def append_to_file(file_path: str):
    with open(file_path, 'a') as file:
        while True:
            user_input = input("Enter text to append (type 'exit' to quit): ")
            
            if user_input.lower() == 'exit':
                break
            
            file.write(user_input + '\n')

    print(f"Data has been appended to {file_path}")

append_to_file('user_input.txt')
