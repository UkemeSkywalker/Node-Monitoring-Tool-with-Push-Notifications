import os
import logging
import time
import psutil  # Import psutil library for system monitoring


# Global Variables
CPU_Threshold = 75
Disk_Threshold = 80
Mem_Threshold = 90

# Set up logging
def setup_logging():

    # Create a "logs" directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create file handler and set level to debug
    log_file = os.path.join("logs", "monitoring.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)


    # Create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Function to monitor system resources
def monitor_system(logger):
    while True:
        # Get system information using psutil
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        network_stats = psutil.net_io_counters()

        # Log system information
        logger.info(f"CPU Usage: {cpu_percent}%")
        logger.info(f"Memory Usage: {mem_percent}%")
        logger.info(f"Disk Usage: {disk_percent}%")
        logger.info(f"Network Stats: {network_stats}")

        # Check threshold and trigger alert
        if cpu_percent > CPU_Threshold :
            logger.warning(f"CPU Usage has passed its threshold: {cpu_percent}%")
        if mem_percent > Mem_Threshold :
            logger.warning(f"Memory Usage has passed its threshold: {mem_percent}%")
        if disk_percent > Disk_Threshold :
            logger.warning(f"Disk Usage has passed its threshold: {disk_percent}%")
        

        # Sleep for some time before checking again
        time.sleep(5)

def main():
    # Setup logging
    logger = setup_logging()

    # Start monitoring system
    logger.info("System monitoring started...")
    monitor_system(logger)

if __name__ == "__main__":
    main()
