@echo off
title USB Watchdog Installer
cls

REM 
if "%silent%"=="" set silent=0

:menu
cls
python tools\banner.py

echo ============================================
echo [01] Install Dependencies
echo [02] Run USB Watchdog (Normal)
echo [03] Run USB Watchdog (Background)
echo [04] View Summary Logs
echo [05] View Detailed Logs
echo [06] Stop USB Watchdog
echo [07] Others / Advanced Menu
echo [08] Exit
echo ============================================
echo.

set /p choice="Select option: "

if "%choice%"=="1" goto deps
if "%choice%"=="2" goto run_normal
if "%choice%"=="3" goto run_background
if "%choice%"=="4" goto summary_logs
if "%choice%"=="5" goto detail_logs
if "%choice%"=="6" goto stop
if "%choice%"=="7" goto others
if "%choice%"=="8" goto exit_program

echo Invalid option. Try again.
pause
goto menu

:deps
cls
echo Installing dependencies...
pip install watchdog pywin32 pyfiglet colorama win10toast
echo Installation finished.
pause
goto menu

:run_normal
cls
echo Starting USB Watchdog (Normal Mode)...
python service\usb_watchdog_service.py
pause
goto menu

:run_background
cls
echo Starting USB Watchdog in background...
start "" /B pythonw "%~dp0service\usb_watchdog_service.py"
echo Running silently in background.
pause
goto menu

:summary_logs
cls
python tools\banner.py

echo -------- USB Watchdog Summary Logs --------
if not exist logs\activity.log (
    echo Log file not found. Creating...
    mkdir logs
    echo. > logs\activity.log
)
type logs\activity.log

echo.
pause
goto menu

:detail_logs
cls
python tools\banner.py

echo -------- USB Watchdog Detailed Logs --------
if not exist logs\detail.log (
    echo Log file not found. Creating...
    mkdir logs
    echo. > logs\detail.log
)
type logs\detail.log

echo.
pause
goto menu


:stop
cls
echo Stopping USB Watchdog...
taskkill /IM pythonw.exe /F >nul 2>&1
taskkill /IM python.exe /F >nul 2>&1
echo USB Watchdog stopped.
pause
goto menu

:others
cls
python tools\banner.py

echo =============== ADVANCED MENU ===============
echo [01] Restart USB Watchdog
echo [02] Clean Logs
echo [03] Test Notification
echo [04] Show Running Status
echo [05] Toggle Silent / Verbose Mode
echo [06] Back to Main Menu
echo =============================================
echo.


set /p other="Choose option: "

if "%other%"=="1" goto restart
if "%other%"=="2" goto clean_logs
if "%other%"=="3" goto test_notify
if "%other%"=="4" goto status
if "%other%"=="5" goto toggle
if "%other%"=="6" goto menu

echo Invalid option.
pause
goto others

:restart
call :stop
call :run_background
goto others

:clean_logs
cls
del /Q logs\*.log >nul 2>&1
echo Logs cleaned.
pause
goto others

:test_notify
cls
python -c "from win10toast import ToastNotifier; ToastNotifier().show_toast('USB Watchdog','Notification Test Successful', duration=3)"
echo.
echo Notification sent.
pause
goto others


:status
cls
echo Checking running watchdog processes...
tasklist | findstr /I "pythonw.exe python.exe"
echo.
pause
goto others

:toggle
cls
if "%silent%"=="0" (
    set silent=1
    echo Silent Mode ENABLED.
) else (
    set silent=0
    echo Verbose Mode ENABLED.
)
pause
goto others

:exit_program
echo Exiting...
timeout /t 1 >nul
exit
