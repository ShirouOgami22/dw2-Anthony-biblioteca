@echo off
REM Start backend (FastAPI) and open frontend in browser
cd /d %~dp0
cd backend
start "FastAPI" cmd /k "uvicorn app:app --reload"
cd ..\frontend
start "" index.html
cd ..
