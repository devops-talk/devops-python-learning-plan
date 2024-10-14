# Script: encrypt_decrypt(file_path: str, shift: int)
# Description: Develop a script to encrypt the content of a file using a simple cipher (e.g., Caesar cipher) and then decrypt it back to the original content.

import os

def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Encrypt/Decrypt only alphabetic characters
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result.append(new_char)
        else:
            result.append(char)  
    return ''.join(result)

def encrypt_file(file_path: str, shift: int):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, 'r') as file:
        content = file.read()

    encrypted_content = caesar_cipher(content, shift)

    encrypted_file_path = f"{file_path}.encrypted"
    with open(encrypted_file_path, 'w') as file:
        file.write(encrypted_content)
    
    print(f"File encrypted successfully! Encrypted file: {encrypted_file_path}")

def decrypt_file(file_path: str, shift: int):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, 'r') as file:
        encrypted_content = file.read()

    decrypted_content = caesar_cipher(encrypted_content, -shift)

    decrypted_file_path = f"{file_path}.decrypted"
    with open(decrypted_file_path, 'w') as file:
        file.write(decrypted_content)
    
    print(f"File decrypted successfully! Decrypted file: {decrypted_file_path}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    shift = int(input("Enter the shift value: "))

    action = input("Choose an action: [encrypt/decrypt]: ").lower()
    if action == "encrypt":
        encrypt_file(file_path, shift)
    elif action == "decrypt":
        decrypt_file(file_path, shift)
    else:
        print("Invalid action. Choose either 'encrypt' or 'decrypt'.")
