from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from logger import log
from usb_monitor import get_current_usb_drive, monitor_usb
import threading
import time
import os

class Watcher(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            log(f"[FILE] Created: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            log(f"[FILE] Modified: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            log(f"[FILE] Deleted: {event.src_path}")


def run_file_watch():
    observer = Observer()
    event_handler = Watcher()

    log("[INFO] Waiting for active USB drive...")

    current_drive = None

    while True:
        usb_drive = get_current_usb_drive()

        if usb_drive != current_drive:
            if current_drive:
                log(f"[INFO] Stopped monitoring: {current_drive}")
                observer.stop()
                observer.join()
            if usb_drive:
                log(f"[INFO] Monitoring files on: {usb_drive}")
                observer = Observer()
                observer.schedule(event_handler, usb_drive, recursive=True)
                observer.start()
            current_drive = usb_drive

        time.sleep(1)


def start_service():
    """Runs USB monitoring and file monitoring in parallel threads."""
    t1 = threading.Thread(target=monitor_usb, daemon=True)
    t2 = threading.Thread(target=run_file_watch, daemon=True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    start_service()
