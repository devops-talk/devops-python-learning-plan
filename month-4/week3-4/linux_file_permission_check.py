# File Permission Check
# Problem: Write a script to check the permissions of all files in a directory and log any files with improper permissions.
# Objective: Automate security checks.

import os
import stat
import logging

# Configure logging
logging.basicConfig(
    filename='improper_permissions.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_file_permissions(directory):
    """Check file permissions in the specified directory."""
    # Define improper permission criteria
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                # Get file permissions
                permissions = stat.S_IMODE(os.lstat(file_path).st_mode)

                # Check for improper permissions
                if permissions & stat.S_IWOTH:  # Check if world-writable
                    logging.warning(f'Improper permission found: {file_path} - World-writable')

                if not (permissions & stat.S_IRUSR):  # Check if owner cannot read
                    logging.warning(f'Improper permission found: {file_path} - Owner not readable')

            except Exception as e:
                logging.error(f'Error checking {file_path}: {e}')

if __name__ == "__main__":
    # Set the directory you want to check
    directory_to_check = '/path/to/directory'  # Change this to your desired directory

    # Check file permissions
    check_file_permissions(directory_to_check)

    print("File permission check complete. Check 'improper_permissions.log' for details.")
