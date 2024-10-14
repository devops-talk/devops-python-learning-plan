# Generate System Report
# Problem: Write a Python script to generate a system report including CPU, memory, disk usage, and running processes.
# Objective: Automate system diagnostics.

# system_report.py
import psutil
import platform
import datetime

def get_cpu_info():
    """Returns CPU usage percentage and core information."""
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_cores = psutil.cpu_count(logical=False)
    return cpu_usage, cpu_cores

def get_memory_info():
    """Returns memory usage information."""
    memory = psutil.virtual_memory()
    return memory.total, memory.used, memory.percent

def get_disk_info():
    """Returns disk usage information."""
    disk = psutil.disk_usage('/')
    return disk.total, disk.used, disk.percent

def get_running_processes():
    """Returns a list of running processes."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        processes.append(proc.info)
    return processes

def generate_system_report():
    """Generates and prints the system report."""
    print("=== System Report ===")
    print(f"Report Generated On: {datetime.datetime.now()}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.architecture()[0]}")
    
    # CPU Info
    cpu_usage, cpu_cores = get_cpu_info()
    print(f"CPU Usage: {cpu_usage}%")
    print(f"CPU Cores: {cpu_cores}")

    # Memory Info
    total_memory, used_memory, memory_percent = get_memory_info()
    print(f"Total Memory: {total_memory / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {used_memory / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {memory_percent}%")

    # Disk Info
    total_disk, used_disk, disk_percent = get_disk_info()
    print(f"Total Disk Space: {total_disk / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {used_disk / (1024 ** 3):.2f} GB")
    print(f"Disk Usage: {disk_percent}%")

    # Running Processes
    print("\nRunning Processes:")
    processes = get_running_processes()
    for process in processes[:10]:  # Limiting to 10 processes for readability
        print(f"PID: {process['pid']}, Name: {process['name']}")
    print("...")  # Indicating that there are more processes

if __name__ == "__main__":
    generate_system_report()
