# Schedule a Cron Job
# Problem: Write a Python script to schedule a cron job that runs a backup script daily.
# Objective: Automate task scheduling.

# schedule_cron_job.py
import os
import sys
import subprocess
from datetime import datetime

def create_backup_script(backup_script_path):
    """Create a backup script if it doesn't already exist."""
    if not os.path.exists(backup_script_path):
        with open(backup_script_path, 'w') as file:
            file.write("#!/bin/bash\n")
            file.write("tar -czf /path/to/backup/backup_$(date +'%Y%m%d').tar.gz /path/to/directory/to/backup\n")
        # Make the backup script executable
        os.chmod(backup_script_path, 0o755)
        print(f"Backup script created at: {backup_script_path}")
    else:
        print(f"Backup script already exists at: {backup_script_path}")

def schedule_cron_job(backup_script_path):
    """Add a cron job to run the backup script daily at 2 AM."""
    cron_time = "0 2 * * *"  # Daily at 2 AM
    cron_job = f"{cron_time} {backup_script_path}\n"

    # Get current crontab
    try:
        current_crontab = subprocess.check_output(['crontab', '-l']).decode()
    except subprocess.CalledProcessError:
        current_crontab = ""

    # Check if the job already exists
    if cron_job in current_crontab:
        print("Cron job already exists.")
    else:
        # Append the new job to the current crontab
        new_crontab = current_crontab + cron_job
        process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE)
        process.communicate(input=new_crontab.encode())
        print("Cron job scheduled successfully.")

if __name__ == "__main__":
    # Define the backup script path
    backup_script_path = "/path/to/your/backup_script.sh"  # Change this to your desired path

    # Create the backup script
    create_backup_script(backup_script_path)

    # Schedule the cron job
    schedule_cron_job(backup_script_path)
