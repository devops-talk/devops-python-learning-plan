# Kill a Process by Name
# Problem: Write a script to kill a process by its name or PID.
# Objective: Automate process management.

# kill_process.py
import psutil
import sys

def kill_process_by_name(process_name):
    """Kill all processes with the given name."""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] == process_name:
                print(f"Killing process {proc.info['name']} with PID {proc.info['pid']}")
                proc.terminate()  # or proc.kill() for force kill
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def kill_process_by_pid(pid):
    """Kill a process with the given PID."""
    try:
        proc = psutil.Process(pid)
        print(f"Killing process {proc.name()} with PID {pid}")
        proc.terminate()  # or proc.kill() for force kill
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print(f"Process with PID {pid} not found or permission denied.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("python3 kill_process.py --name <process_name>")
        print("python3 kill_process.py --pid <pid>")
        sys.exit(1)

    option = sys.argv[1]
    value = sys.argv[2]

    if option == "--name":
        kill_process_by_name(value)
    elif option == "--pid":
        kill_process_by_pid(int(value))
    else:
        print("Invalid option. Use --name or --pid.")
