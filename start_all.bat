@echo off
echo Starting B2B Chat Application...
echo.

echo Starting Backend Service...
start cmd /k "start_backend.bat"

echo Starting Frontend Service...
start cmd /k "start_frontend.bat"

echo.
echo Both services have been started!
echo You can close this window, but keep the other terminal windows open to keep the services running.