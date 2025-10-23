@echo off
ECHO Setting up and running the Link Programmer...

:: Get the directory where the batch file is located
SET "SCRIPT_DIR=%~dp0"

:: Create a virtual environment in the same directory
ECHO Creating virtual environment...
python -m venv "%SCRIPT_DIR%venv"
IF %ERRORLEVEL% NEQ 0 (
    ECHO Failed to create virtual environment. Ensure Python is installed and try again.
    PAUSE
    EXIT /B 1
)

:: Activate the virtual environment
ECHO Activating virtual environment...
CALL "%SCRIPT_DIR%venv\Scripts\activate.bat"
IF %ERRORLEVEL% NEQ 0 (
    ECHO Failed to activate virtual environment.
    PAUSE
    EXIT /B 1
)

:: Upgrade pip in the virtual environment
ECHO Upgrading pip...
python -m pip install --upgrade pip
IF %ERRORLEVEL% NEQ 0 (
    ECHO Failed to upgrade pip.
    PAUSE
    EXIT /B 1
)

:: Install Gradio
ECHO Installing Gradio...
pip install gradio
IF %ERRORLEVEL% NEQ 0 (
    ECHO Failed to install Gradio.
    PAUSE
    EXIT /B 1
)

:: Run the Python program
ECHO Running link_programmer.py...
python "%SCRIPT_DIR%link_programmer.py"
IF %ERRORLEVEL% NEQ 0 (
    ECHO Failed to run link_programmer.py.
    PAUSE
    EXIT /B 1
)

:: Deactivate the virtual environment
ECHO Deactivating virtual environment...
CALL "%SCRIPT_DIR%venv\Scripts\deactivate.bat"

ECHO Done! Press any key to exit.
PAUSE
EXIT /B 0