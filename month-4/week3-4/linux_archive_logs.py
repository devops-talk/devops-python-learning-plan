# Archive Logs
# Problem: Implement a script to compress and archive old log files.
# Objective: Automate log management.

# archive_logs.py
import os
import shutil
import time
from datetime import datetime

def archive_old_logs(logs_dir, archive_dir, days_old=7):
    # Ensure logs directory exists
    if not os.path.exists(logs_dir):
        print(f"Logs directory '{logs_dir}' does not exist.")
        return
    
    # Create archive directory if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Get current time for comparison
    now = time.time()

    # Loop through all files in the logs directory
    for filename in os.listdir(logs_dir):
        file_path = os.path.join(logs_dir, filename)
        
        # Check if it's a file and older than specified days
        if os.path.isfile(file_path):
            file_age = now - os.path.getmtime(file_path)
            if file_age > days_old * 86400:  # 86400 seconds in a day
                # Create a zip archive for the old log file
                archive_name = f"{filename}_{datetime.now().strftime('%Y%m%d')}.zip"
                archive_path = os.path.join(archive_dir, archive_name)

                # Compress and move the file
                try:
                    shutil.make_archive(archive_path.replace('.zip', ''), 'zip', logs_dir, filename)
                    os.remove(file_path)  # Remove the original log file after archiving
                    print(f"Archived and removed: {file_path}")
                except Exception as e:
                    print(f"Error archiving {file_path}: {e}")

if __name__ == "__main__":
    # Define the logs directory and archive destination
    logs_directory = "/path/to/logs"
    archive_directory = "/path/to/archive"
    
    # Specify the number of days old for log archiving
    days_threshold = 7

    # Run the archiving process
    archive_old_logs(logs_directory, archive_directory, days_old=days_threshold)
