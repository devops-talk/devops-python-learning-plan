# Check Disk Usage
# Problem: Write a Python script to check and display disk usage on a Linux machine.
# Objective: Automate system monitoring.

# check_disk_usage.py
import subprocess

def check_disk_usage():
    try:
        # Run the 'df' command to check disk usage
        result = subprocess.run(['df', '-h'], capture_output=True, text=True)

        if result.returncode == 0:
            print("Disk Usage Information:\n")
            print(result.stdout)
        else:
            print(f"Error checking disk usage: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_disk_usage()
