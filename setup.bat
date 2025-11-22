@echo off
REM Setup script for Windows

echo =========================================
echo FastAPI Demo App - Setup (venv)
echo =========================================

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.11 or later from https://www.python.org/
    pause
    exit /b 1
)

echo Python version:
python --version

REM Create virtual environment
echo.
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo =========================================
echo Setup completed!
echo =========================================
echo.
echo Next steps:
echo 1. Start PostgreSQL (or use Docker for DB only):
echo    docker-compose up -d db test_db
echo.
echo 2. Activate virtual environment:
echo    venv\Scripts\activate
echo.
echo 3. Run the application:
echo    uvicorn app.main:app --reload
echo.
echo 4. Access the API documentation:
echo    http://localhost:8000/docs
echo.
pause
