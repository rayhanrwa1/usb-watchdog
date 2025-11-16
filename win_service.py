import win32serviceutil
import win32service
import win32event
import servicemanager
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_DIR = os.path.join(BASE_DIR, "service")
sys.path.append(SERVICE_DIR)

from usb_watchdog_service import start_service


class USBWatchdogService(win32serviceutil.ServiceFramework):
    _svc_name_ = "USBWatchdogService"
    _svc_display_name_ = "USB Watchdog Background Service"
    _svc_description_ = "Monitors USB activity and suspicious files in the background."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogInfoMsg("USB Watchdog Service is running...")
        start_service()


if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(USBWatchdogService)
