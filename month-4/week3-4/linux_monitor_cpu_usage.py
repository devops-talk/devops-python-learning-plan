# Monitor CPU Usage
# Problem: Write a Python script to monitor and log CPU usage at regular intervals.
# Objective: Automate performance monitoring.


# monitor_cpu_usage.py
import psutil
import time

def log_cpu_usage(interval, duration):
    print(f"Monitoring CPU usage every {interval} seconds for {duration} seconds...\n")
    
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_percent = psutil.cpu_percent(interval=0)  # Get CPU percentage usage
        print(f"CPU Usage: {cpu_percent}%")
        time.sleep(interval)  # Wait for the specified interval

if __name__ == "__main__":
    log_interval = 5  # Log every 5 seconds
    monitor_duration = 60  # Monitor for 60 seconds
    log_cpu_usage(log_interval, monitor_duration)
