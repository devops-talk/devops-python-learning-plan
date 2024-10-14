# Monitor Memory Usage
# Problem: Write a Python script to check and log memory usage at regular intervals.
# Objective: Automate memory management.
# monitor_memory.py
import psutil
import time
import logging

def log_memory_usage(interval, log_file):
    """Logs memory usage at regular intervals."""
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

    try:
        while True:
            mem_info = psutil.virtual_memory()
            logging.info(f"Total Memory: {mem_info.total / (1024 ** 3):.2f} GB, "
                         f"Available Memory: {mem_info.available / (1024 ** 3):.2f} GB, "
                         f"Used Memory: {mem_info.used / (1024 ** 3):.2f} GB, "
                         f"Memory Usage: {mem_info.percent}%")
            print(f"Logged memory usage: {mem_info.percent}%")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Memory monitoring stopped.")

if __name__ == "__main__":
    log_file = "memory_usage.log"  # Log file to store memory usage data
    interval = 5  # Time interval in seconds between each log
    print(f"Monitoring memory usage every {interval} seconds...")
    log_memory_usage(interval, log_file)
