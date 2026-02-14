@echo off
echo ===================================================
echo   CyberGuardian - Fix & Run
echo ===================================================

cd "Assignment\backend"

echo.
echo [1/4] Upgrading Google AI Library...
echo This fixes "Model Not Found" errors by getting the latest version.
pip install --upgrade -r requirements.txt

echo.
echo [2/4] Checking API Key...
if "%GOOGLE_API_KEY%"=="" (
    echo.
    echo [IMPORTANT] Google API Key not found in environment.
    set /p GOOGLE_API_KEY="Please paste your Google API Key here and press Enter: "
)

echo.
echo [3/4] Starting Server...
echo The server will now auto-detect the best available model for your key.
echo.
echo Server running on: http://127.0.0.1:8080
echo.

python server.py

pause
