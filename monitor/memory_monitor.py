import psutil
import time
from logger_config import setup_logger

MEMORY_THRESHOLD = 80  # percent
logger = setup_logger("MEMORY_MONITOR", "memory.log")



# def check_memory():
#     """
#     Returns memory usage percentage
#     """

#     memory=psutil.virtual_memory()
#     return memory.percent

# if __name__=="__main__":
#     while True:
#         usage=check_memory()
#         logging.info(f"Memory Usage: {usage}")

#         if usage>MEMORY_THRESHOLD:
#             logging.warning("High Memory usage detected!")

#         time.sleep(5)


def monitor_memory(stop_event):
    while not stop_event.is_set():
        memory = psutil.virtual_memory()
        usage = memory.percent
        logger.info(f"Memory usage: {usage}%")

        if usage > MEMORY_THRESHOLD:
            logger.warning("High memory usage detected!")

        time.sleep(5)