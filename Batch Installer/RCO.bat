@echo off

REM Obtains latest version of ClientAppSettings.json 
set RCO_url=https://raw.githubusercontent.com/L8X/Roblox-Client-Optimizer/main/assets/ClientAppSettings.json 
REM https://roblox-client-optimizer.simulhost.com/ClientAppSettings.json is an alternative link to use
set RobloxVersionDir=C:\Users\%username%\AppData\Local\Roblox\Versions

REM Writes ClientAppSettings.json to RCO.json in temporary folder
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%RCO_url%', 'RCO.json')"

REM Finds the latest Roblox folder
for /f "delims=" %%I in ('dir /b /ad /o-d "%RobloxVersionDir%\version-*"') do (
    set LatestRobloxVersionDir=%RobloxVersionDir%\%%I
    goto :WriteRCO
)

REM If RCO isn't installed yet, it will be installed
:WriteRCO
if not exist "%LatestRobloxVersionDir%\ClientSettings" (
    mkdir "%LatestRobloxVersionDir%\ClientSettings"
)

REM RCO.json is copied to the ClientSettings folder
copy /y "RCO.json" "%LatestRobloxVersionDir%\ClientSettings\ClientAppSettings.json" >nul

REM RCO.json which was downloaded to the temporary folder is deleted
del "RCO.json"

REM Informs user that RCO has been updated/installed and the directory
echo New data has been written to %LatestRobloxVersionDir%\ClientSettings\ClientAppSettings.json
pause