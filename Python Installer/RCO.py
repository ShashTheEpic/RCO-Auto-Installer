# Modules required
import requests
import json
import os
import glob

# Obtains latest version of ClientAppSettings.json
RCO_url = "https://raw.githubusercontent.com/L8X/Roblox-Client-Optimizer/main/assets/ClientAppSettings.json" # https://roblox-client-optimizer.simulhost.com/ClientAppSettings.json is an alterative link if the following one doesn't work
RCO = requests.get(RCO_url)

try:
    RCO.raise_for_status()  # Check if the request was successful
    RCO_text = RCO.content.decode('utf-8')    
    try:
        json_data = json.loads(RCO_text)
        # Finds the directory to RCO
        user = os.getlogin()
        RobloxVersionDir = rf"C:\Users\{user}\AppData\Local\Roblox\Versions"
        LatestRobloxVersionDir = max(glob.glob(os.path.join(RobloxVersionDir, "version-*")), key=os.path.getmtime)
        RobloxClientSettingsDir = os.path.join(LatestRobloxVersionDir, "ClientSettings", "ClientAppSettings.json")

        # If RCO isn't installed, it will be installed
        if not os.path.exists(os.path.dirname(RobloxClientSettingsDir)):
            os.makedirs(os.path.dirname(RobloxClientSettingsDir))

        # Latest version of RCO writes/overwrites current ClientAppSettings.json
        with open(RobloxClientSettingsDir, "w") as f:
            json.dump(json_data, f, indent=0)

        # Informs user that RCO has been updated/installed and the directory
        print("New data has been written to", RobloxClientSettingsDir)

        # If you get errors you are informed
    except json.JSONDecodeError as error:
        print("Error occurred while parsing the JSON:", error)
except requests.exceptions.RequestException as error:
    print("Error occurred while fetching the JSON file:", error)
