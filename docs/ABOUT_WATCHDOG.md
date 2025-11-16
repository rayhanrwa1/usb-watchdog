# About USB Watchdog

USB Watchdog is a security utility built to help technicians, service centers, and advanced users monitor USB activity safely.

---

## 🎯 Purpose
USB devices are one of the most common sources of:
- Autorun-based malware  
- Hidden shortcut viruses  
- Executable masquerading as image files  
- Suspicious background activities  

USB Watchdog provides protection without altering or deleting any user data.

---

## 🔍 How It Works
- Detects when a USB drive is inserted  
- Scans directory structure for:
  - Hidden files  
  - Suspicious `.lnk` shortcuts  
  - `autorun.inf` malware  
  - Fake image executables like `jpg.exe`  
- Logs findings to local files  
- Sends optional Windows notifications  
- Can run silently in the background  

---

## ⚙ Architecture
The system consists of:
- `usb_monitor.py` → detects drive insertion/removal  
- `detector.py` → scans USB for suspicious files  
- `logger.py` → writes summary & detail logs  
- `notifier.py` → Windows toast notification  
- `usb_watchdog_service.py` → main supervisor  

---

## 🛡 Safety
USB Watchdog does **not**:
- Delete files  
- Modify data  
- Upload or transmit information  
- Change system registry  

It is fully read-only.

---

## 🧑‍💻 Author
Developed by **rayhanrwa**
