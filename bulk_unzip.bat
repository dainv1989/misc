@echo off
set WinRAR="C:\Program Files\WinRAR\WinRAR.exe"

:: %%~dpa get folder path from file path given by variable %a
:: in batch script use %%~dp prefix
:: run below line in command prompt to see result
:: for /r . %a in (*.zip) do echo %~dpa

for /r . %%a in (*.zip) do (echo %%a && %WinRAR% x -iblk -y %%a *.* %%~dpa)

@echo on