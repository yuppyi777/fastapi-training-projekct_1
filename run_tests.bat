@echo off
REM Run tests locally with venv (Windows)

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

REM Run tests
echo Running tests...
pytest %*
