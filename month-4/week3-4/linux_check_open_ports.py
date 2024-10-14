# Check for Open Ports
# Problem: Write a script to list all open ports on a Linux machine.
# Objective: Automate network monitoring.

# check_open_ports.py
import subprocess

def check_open_ports():
    try:
        # Use ss or netstat to check open ports (ss is more common in modern systems)
        cmd = "ss -tuln"  # For listing open TCP and UDP ports
        result = subprocess.run(cmd.split(), capture_output=True, text=True)

        if result.returncode == 0:
            print("Open ports:")
            print(result.stdout)
        else:
            print("Failed to run the command.")
            print(result.stderr)

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    check_open_ports()
