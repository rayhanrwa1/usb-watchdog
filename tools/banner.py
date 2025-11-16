from pyfiglet import figlet_format
from colorama import Fore, Style

def show_banner():
    print(Fore.CYAN + figlet_format("USB WATCHDOG", font="slant"))

    subtitle = f"""
{Fore.MAGENTA}───────────────────────────────────────────────
    {Fore.YELLOW}Secure USB Activity Monitoring System
    {Fore.GREEN}Real-time Protection • Silent Background Mode
    {Fore.CYAN}Developed by: {Fore.WHITE}rayhanrwa
{Fore.MAGENTA}───────────────────────────────────────────────
"""
    print(subtitle)

    info = f"""
{Fore.BLUE} • Monitoring USB devices in real-time
 • Detecting suspicious & hidden files
 • Autorun malware detection system
 • Logging activity & background alerts
 • Designed for technicians & forensic tools
{Style.RESET_ALL}
"""
    print(info)

if __name__ == "__main__":
    show_banner()
