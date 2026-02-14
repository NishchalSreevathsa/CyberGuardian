@echo off
echo ===================================================
echo   CyberGuardian Agent - Backend Launcher
echo ===================================================

cd "Assignment\backend"

echo.
echo [1/3] Checking for Python...
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    pause
    exit /b
)

echo.
echo [2/3] Installing dependencies (if needed)...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [WARNING] Dependency installation had issues.
)

echo.
echo [2.5/3] Checking API Key...
if "%GOOGLE_API_KEY%"=="" (
    echo.
    echo [IMPORTANT] Google API Key not found in environment.
    set /p GOOGLE_API_KEY="Please paste your Google API Key here and press Enter: "
)

echo.
echo [3/3] Starting Server...
echo.
echo Server is running on: http://127.0.0.1:8080
echo Keep this window OPEN while using the Chrome Extension.
echo.

python server.py

pause
