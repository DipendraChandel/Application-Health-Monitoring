import psutil
import time
from logger_config import setup_logger
from auto_fix.cleanup_log import cleanup_old_logs

DISK_THRESHOLD = 85  # percent
DISK_PATH = "/"  # root filesystem
logger = setup_logger("DISK_MONITOR", "disk.log")


# def check_disk():
#     """
#     Returns disk usage percentage for root filesystem
#     """
#     disk=psutil.disk_usage(DISK_PATH)
#     return disk.percent

# if __name__=="__main__":
#     while True:
#         usage=check_disk()
#         logging.info(f"Disk Usage: {usage}%")

#         if usage > DISK_THRESHOLD:
#             logging.warning("High disk usage detected!")

#         time.sleep(10)

def monitor_disk(stop_event):
    while not stop_event.is_set():
        disk = psutil.disk_usage(DISK_PATH)
        usage = disk.percent
        logger.info(f"Disk usage: {usage}%")

        if usage > DISK_THRESHOLD:
            logger.warning("High disk usage detected!")
            cleanup_old_logs()

        time.sleep(10)