# Installation Guide

This page explains how to install and use USB Watchdog on Windows.

---

## 📥 Requirements
- Windows 10 or later  
- Python 3.10+  
- Administrator privileges (recommended)

---

## 🔧 Step-by-Step Installation

### 1. Install Python Dependencies
Run the installer:

install.bat


Choose option:


[01] Install Dependencies


This installs:
- watchdog  
- pywin32  
- pyfiglet  
- colorama  
- win10toast  

---

## ▶ Running USB Watchdog

### **Normal Mode (Terminal Visible)**  
Allows you to see log output directly.


[02] Run USB Watchdog (Normal)


### **Background Mode (Silent / No Terminal)**  
Runs using `pythonw.exe` in background.


[03] Run USB Watchdog (Background)


To verify watchdog is running:


tasklist | findstr pythonw.exe


---

## 📄 Viewing Logs
USB Watchdog separates logs into two levels:

### Summary Logs


[04] View Summary Logs


### Detailed Logs


[05] View Detailed Logs


Logs are stored under:


logs/activity.log
logs/detail.log


---

## 🧰 Advanced Tools
Accessible under:


[07] Others / Advanced Menu


Features include:
- Restart Watchdog  
- Clean Logs  
- Test Notification  
- Show Running Status  
- Toggle Silent/Verbose  

---

## ❌ Stopping USB Watchdog


[06] Stop USB Watchdog


or manually:


taskkill /IM pythonw.exe /F


---

## 📝 Notes
- USB Watchdog does **not** modify or delete any USB files.  
- It only **reads** metadata for monitoring and security purposes.  