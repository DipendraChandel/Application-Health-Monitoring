import threading
import time
import signal
from monitor.cpu_monitor import monitor_cpu
from monitor.memory_monitor import monitor_memory
from monitor.disk_monitor import monitor_disk

def main():
    stop_event=threading.Event()

    cpu_thread=threading.Thread(
        target=monitor_cpu,
        args=(stop_event,)
    )

    memory_thread=threading.Thread(
        target=monitor_memory,
        args=(stop_event,)
    )

    disk_thread=threading.Thread(
        target=monitor_disk,
        args=(stop_event,)
    )

    cpu_thread.start()
    memory_thread.start()
    disk_thread.start()

    print("Robot Health Monitor running... Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("Shutting down monitors")
        stop_event.set()

        cpu_thread.join()
        memory_thread.join()
        disk_thread.join()

        print("All monitors stopped safely.")
    

if __name__=="__main__":
    main()