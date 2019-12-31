echo off
:: clear command screen
cls
:: create empty file
type nul > merged.txt
(for /r %%i in (*.txt) do more +1 %%i) >> merged.txt
echo on

:: one line command
:: cls && echo off && type nul > merged.txt && (for /r %i in (*.txt)  do more +1 %i) >> merged.txt && echo on