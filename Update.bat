@echo off
setlocal

REM Set the directory where to search for the file (same directory as the batch file)
set "search_dir=%~dp0"

REM Search for the file
for /r "%search_dir%" %%i in (FortniteToolsMain.py) do (
    set "file=%%i"
)

REM Check if the file was found
if not exist "%file%" (
    echo File not found.
    pause
    exit /b
)

REM Run the file
python "%file%"

endlocal
