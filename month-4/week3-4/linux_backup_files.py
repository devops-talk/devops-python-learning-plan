# Backup Files
# Problem: Write a script to back up a directory to a specified location.
# Objective: Practice automating file backups.

# backup_files.py
import os
import shutil
import datetime

def backup_directory(src_dir, dest_dir):
    # Ensure source directory exists
    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return
    
    # Create a timestamped backup folder
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_folder_name = f"backup_{timestamp}"
    backup_path = os.path.join(dest_dir, backup_folder_name)
    
    # Copy source directory to backup location
    try:
        shutil.copytree(src_dir, backup_path)
        print(f"Backup of '{src_dir}' completed successfully at '{backup_path}'")
    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    # Define the source and destination directories
    source_directory = "/path/to/source_directory"
    destination_directory = "/path/to/destination_directory"
    
    # Run the backup
    backup_directory(source_directory, destination_directory)
