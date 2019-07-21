@echo off &REM Deactivate commands prompt
pushd %~dp0 &REM Come back in the current directory
py sniffer.py &REM Start the python script
pause &REM To be able to read exceptions
popd &REM Leave the current directory