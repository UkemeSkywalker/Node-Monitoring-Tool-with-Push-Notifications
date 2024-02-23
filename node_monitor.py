import logging
import time
import psutil  # Import psutil library for system monitoring

# Set up logging
def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

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
