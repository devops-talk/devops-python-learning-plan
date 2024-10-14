# Script: search_replace(file_path: str, search_str: str, replace_str: str)
# Description: Create a script that searches for a specific string in a file and replaces it with another string, handling any file-related exceptions.



def search_replace(file_path: str, search_str: str, replace_str: str):
    with open (file_path, 'r') as file:
        data = file.read()
    
    new_data = data.replace(search_str, replace_str)
    with open(file_path, 'w') as file:
        file.write(new_data)
        print(new_data)
        






file = "user_input.txt"



str1=input("please enter string to be replace: ")
str2=input("please enter new string: ")
search_replace(file, str1, str2)