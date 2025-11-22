@echo off
REM Run application locally with venv (Windows)

REM Check if virtual environment exists
if not exist "venv\" (
    echo Error: Virtual environment not found. Please run setup.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Use local environment variables
if exist ".env.local" (
    for /f "tokens=*" %%a in ('type .env.local ^| findstr /v "^#"') do set %%a
)

REM Run the application
echo Starting FastAPI application...
echo API Documentation: http://localhost:8000/docs
echo.
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
