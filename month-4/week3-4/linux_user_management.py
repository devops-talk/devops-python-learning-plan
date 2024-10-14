# Create and Manage Users
# Problem: Write a script to create, delete, and list users on a Linux machine.
# Objective: Automate user management.

import subprocess
import sys

def create_user(username):
    """Create a new user."""
    try:
        subprocess.run(['sudo', 'useradd', username], check=True)
        print(f"User '{username}' created successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to create user '{username}'.")

def delete_user(username):
    """Delete a user."""
    try:
        subprocess.run(['sudo', 'userdel', username], check=True)
        print(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to delete user '{username}'.")

def list_users():
    """List all users on the system."""
    try:
        users = subprocess.run(['cut', '-d:', '-f1', '/etc/passwd'], capture_output=True, text=True, check=True)
        print("Users on the system:")
        print(users.stdout.strip())
    except subprocess.CalledProcessError:
        print("Failed to list users.")

def main():
    """Main function to manage users."""
    while True:
        print("\nUser Management Menu:")
        print("1. Create User")
        print("2. Delete User")
        print("3. List Users")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            username = input("Enter username to create: ")
            create_user(username)
        elif choice == '2':
            username = input("Enter username to delete: ")
            delete_user(username)
        elif choice == '3':
            list_users()
        elif choice == '4':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
