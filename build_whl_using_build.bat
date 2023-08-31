@echo off
REM Assumes you have the build package installed

if exist danstring.egg-info (
    rmdir /s /q danstring.egg-info
)
if exist dist (
    rmdir /s /q dist
)

echo "Old directories removed, building anew"
python -m build
pause