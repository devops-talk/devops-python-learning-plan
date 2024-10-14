# Script: read_file(file_path: str)
# Description: Create a script that tries to open a file and handles the FileNotFoundError gracefully, providing user-friendly feedback.


def read_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Error: The file was not found."
    except IsADirectoryError:
        return "Error: The provided path is a directory, not a file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

file_path = 'output.txt'
print(read_file(file_path))