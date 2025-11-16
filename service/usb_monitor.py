import time
import win32file
import win32con
from logger import log, write_summary
from detector import scan_usb
from notifier import notify

current_usb = None

def get_current_usb_drive():
    global current_usb
    return current_usb

def monitor_usb():
    global current_usb
    known = set()

    while True:
        drives = win32file.GetLogicalDrives()

        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            mask = ord(letter) - ord("A")

            if drives & (1 << mask):
                drive_path = f"{letter}:/"
                drive_type = win32file.GetDriveType(drive_path)

                if drive_type == win32file.DRIVE_REMOVABLE:
                    if letter not in known:
                        known.add(letter)
                        current_usb = drive_path

                        log(f"[INFO] USB inserted: {drive_path}")

                        suspicious = scan_usb(drive_path)
                        suspicious_count = len(suspicious)

                        if suspicious_count == 0:
                            write_summary(f"[SAFE] USB inserted: {drive_path}")
                            notify("USB Watchdog", "USB is safe.")
                        elif suspicious_count < 5:
                            write_summary(f"[WARNING] USB inserted: {drive_path} (Suspicious: {suspicious_count})")
                            notify("USB Watchdog", f"Warning: {suspicious_count} suspicious files found.")
                        else:
                            write_summary(f"[DANGER] USB inserted: {drive_path} (High-Risk: {suspicious_count})")
                            notify("USB Watchdog", "Danger: High-risk files detected!")

                else:
                    if letter in known:
                        known.remove(letter)
                        if current_usb == f"{letter}:/":
                            current_usb = None
                        log(f"[INFO] USB removed: {drive_path}")
                        write_summary(f"[INFO] USB removed: {drive_path}")

            else:
                if letter in known:
                    known.remove(letter)
                    if current_usb == f"{letter}:/":
                        current_usb = None

                    log(f"[INFO] USB removed: {letter}:/")
                    write_summary(f"[INFO] USB removed: {letter}:/")

        time.sleep(1)
