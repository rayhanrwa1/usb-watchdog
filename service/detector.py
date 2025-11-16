import os
from logger import log
import win32con
import win32file

SAFE_HIDDEN_PREFIXES = [
    "._",                
    ".DS_Store",        
    ".Spotlight-V100",
    ".Trashes",
    ".fseventsd",
]

SAFE_WINDOWS_HIDDEN = [
    "System Volume Information",
    "$RECYCLE.BIN",
]

def is_hidden(filepath):
    """Returns True if a file has the hidden attribute."""
    try:
        attrs = win32file.GetFileAttributesW(filepath)
        return bool(attrs & win32con.FILE_ATTRIBUTE_HIDDEN)
    except:
        return False


def is_safe_hidden(full_path):
    """Returns True if hidden file is known safe (macOS / Windows metadata)."""
    filename = os.path.basename(full_path)

    if filename.startswith(tuple(SAFE_HIDDEN_PREFIXES)):
        return True

    if filename in SAFE_WINDOWS_HIDDEN:
        return True

    return False


def scan_usb(drive):
    suspicious = []

    for root, dirs, files in os.walk(drive):
        for f in files:
            full = os.path.join(root, f)
            lower = f.lower()

            if is_hidden(full):
                if is_safe_hidden(full):
                    log(f"[INFO] Ignoring safe hidden file: {full}")
                else:
                    suspicious.append(full)
                    log(f"[WARNING] Hidden file detected: {full}")
                continue

            if lower.endswith(".lnk"):
                suspicious.append(full)
                log(f"[WARNING] Suspicious shortcut detected: {full}")

            if lower == "autorun.inf":
                suspicious.append(full)
                log("[WARNING] autorun.inf found (possible USB malware)")

            if lower.endswith(".jpg.exe") or lower.endswith(".png.exe"):
                suspicious.append(full)
                log(f"[WARNING] Executable disguised as image: {full}")

    return suspicious
