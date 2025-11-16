import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")

SUMMARY_LOG = os.path.join(LOG_DIR, "activity.log")
DETAIL_LOG = os.path.join(LOG_DIR, "detail.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

BANNER_TEXT = """USB Watchdog Detailed Logs
--------------------------------------------------
Secure USB Activity Monitoring
Developer: rayhanrwa
--------------------------------------------------

"""

def ensure_banner_exists(path):
    """Ensure the banner exists even if logs already contain data."""
    banner_present = False

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            first_line = f.readline()
            if "USB Watchdog" in first_line:
                banner_present = True

    if not banner_present:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                old_data = f.read()
        else:
            old_data = ""

        with open(path, "w", encoding="utf-8") as f:
            f.write(BANNER_TEXT + old_data)


def log(message):
    write_detail(message)


def write_summary(message):
    ensure_banner_exists(SUMMARY_LOG)

    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(SUMMARY_LOG, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")


def write_detail(message):
    ensure_banner_exists(DETAIL_LOG)

    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(DETAIL_LOG, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")
