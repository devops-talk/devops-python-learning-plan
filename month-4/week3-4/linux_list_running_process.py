# List Running Processes
# Problem: Write a Python script to list all running processes.
# Objective: Automate system monitoring.

# list_running_processes.py
import psutil

def list_processes():
    print(f"{'PID':<10} {'Process Name':<25} {'Status':<10} {'Memory Usage (MB)':<20}")
    print("=" * 70)
    
    for proc in psutil.process_iter(['pid', 'name', 'status', 'memory_info']):
        try:
            # Get process information
            pid = proc.info['pid']
            name = proc.info['name']
            status = proc.info['status']
            memory = proc.info['memory_info'].rss / (1024 * 1024)  # Memory in MB
            
            print(f"{pid:<10} {name:<25} {status:<10} {memory:<20.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle processes that may no longer exist or you don't have permission to access
            pass

if __name__ == "__main__":
    list_processes()
