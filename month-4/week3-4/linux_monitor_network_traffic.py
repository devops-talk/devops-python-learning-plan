# Monitor Network Traffic
# Problem: Write a Python script to monitor network traffic and log any high-usage events.
# Objective: Automate network management.

import psutil
import time
import logging

# Set up logging
logging.basicConfig(filename='network_usage.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def log_high_usage(interface, bytes_sent, bytes_recv):
    """Log high network usage."""
    logging.info(f'High usage detected on {interface}: Sent {bytes_sent} bytes, Received {bytes_recv} bytes.')

def monitor_network_usage(threshold=1e6):
    """
    Monitor network traffic and log high usage events.

    :param threshold: Usage threshold in bytes. Default is 1,000,000 bytes (1 MB).
    """
    net_io = psutil.net_io_counters(pernic=True)  # Get network I/O statistics

    while True:
        time.sleep(5)  # Monitor every 5 seconds
        current_io = psutil.net_io_counters(pernic=True)

        for interface, io in current_io.items():
            sent = io.bytes_sent - net_io[interface].bytes_sent
            recv = io.bytes_recv - net_io[interface].bytes_recv

            if sent > threshold or recv > threshold:
                log_high_usage(interface, sent, recv)

        net_io = current_io  # Update previous values

if __name__ == "__main__":
    monitor_network_usage()
