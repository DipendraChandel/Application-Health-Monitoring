import psutil
import time
from logger_config import setup_logger

CPU_THRESHOLD = 80
logger=setup_logger("CPU_MONITOR", "cpu.log")

# def check_cpu():
#     return psutil.cpu_percent(interval=1)


# if __name__ == "__main__":
#     while True:
#         usage = check_cpu()
#         logging.info(f"CPU usage: {usage}%")

#         if usage > CPU_THRESHOLD:
#             logging.warning("High CPU usage detected!")

#         time.sleep(5)

def monitor_cpu(stop_event):
    while not stop_event.is_set():
        usage=psutil.cpu_percent(interval=1)
        logger.info(f"CPU USAGE: P{usage}%")

        if usage > CPU_THRESHOLD:
            logger.warning("High CPU usage detected!")

        time.sleep(5)
