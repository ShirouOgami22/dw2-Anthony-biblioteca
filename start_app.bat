@echo off
REM Check for Python
python3 --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python 3.10+ and try again.
    echo You can download it from the microsoft store
    echo https://apps.microsoft.com/detail/9PNRBTZXMB4Z?hl=neutral&gl=BR&ocid=pdpshare
    pause
    exit /b
)

REM Install dependencies
cd /d %~dp0
cd backend
pip install -r requirements.txt

REM Seed database if needed
python3 seed.py

REM Start backend (FastAPI) and open frontend in browser
start "FastAPI" cmd /k "uvicorn app:app --reload"
cd ..\frontend
start "" index.html
cd ..
