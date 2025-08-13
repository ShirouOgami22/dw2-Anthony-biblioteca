@echo off
REM Try to use 'python' or 'py' to start the backend
cd backend
python app.py || py app.py
pause