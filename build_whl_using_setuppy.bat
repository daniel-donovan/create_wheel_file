@echo off
REM Assumes you have the wheel package installed

if exist build (
    rmdir /s /q build
)
if exist danstring.egg-info (
    rmdir /s /q danstring.egg-info
)
if exist dist (
    rmdir /s /q dist
)

echo "Old directories removed, building anew"
python setup.py bdist_wheel
pause