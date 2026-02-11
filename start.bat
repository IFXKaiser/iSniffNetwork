@echo off
title iSniffNetwork Launcher
color 0A

echo.
echo ================================================
echo    iSniffNetwork - MAC Address Sniffer
echo ================================================
echo.

REM Prüfe ob Python installiert ist
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [FEHLER] Python ist nicht installiert oder nicht im PATH!
    echo Bitte installiere Python von https://www.python.org/
    echo.
    pause
    exit /b 1
)

REM Prüfe ob venv existiert, wenn nicht, erstelle es
if not exist "%~dp0venv\Scripts\python.exe" (
    echo [INFO] Erstelle virtuelle Umgebung...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [FEHLER] Konnte venv nicht erstellen!
        pause
        exit /b 1
    )
    echo [OK] Virtuelle Umgebung erstellt.
    echo.
)

REM Prüfe ob Dependencies installiert sind
echo Pruefe Dependencies...
"%~dp0venv\Scripts\python.exe" -c "import scapy, psutil" >nul 2>&1
if errorlevel 1 (
    echo.
    echo [INFO] Installiere Dependencies...
    echo.
    call "%~dp0venv\Scripts\pip.exe" install -r requirements.txt >nul 2>&1
    
    echo.
    echo [OK] Installation abgeschlossen.
    echo.
)

echo.
echo [INFO] Starte iSniffNetwork als Administrator...
echo [WICHTIG] Bitte erlaube die Admin-Rechte im naechsten Dialog!
echo.

REM Starte Python-Skript mit Admin-Rechten aus dem venv
powershell -Command "Start-Process '%~dp0venv\Scripts\python.exe' -ArgumentList '%~dp0isniff.py' -Verb RunAs"

if %errorlevel% neq 0 (
    echo.
    echo [FEHLER] Konnte nicht als Administrator starten!
    echo Versuche normalen Start...
    "%~dp0venv\Scripts\python.exe" "%~dp0isniff.py"
    pause
    exit /b 1
)

echo.
echo [OK] iSniffNetwork wurde gestartet!
echo Du kannst dieses Fenster jetzt schliessen.
echo.
timeout /t 3 >nul
exit
