# IMPORTS

import subprocess
import json
from datetime import date

# FUNCTIONS PROTOTYPE

def log_message(fileName, fnName,message):
    # Log the message to a file
    with open("Webscrapper.log", "a") as log_file:
        log_file.write(f"[{fileName}][{fnName}]{date.today()}: {message}\n")

def current_usd_to_egp_exchange_rate(currency_from, currency_to):
    # Decode URL to JSON
    response = subprocess.run(["curl", f"https://wise.com/rates/history+live?source={currency_from}&target={currency_to}&length=30&resolution=hourly&unit=day"], capture_output=True, text=True)
    
    json_data = json.loads(response.stdout)
    
    values = [item['value'] for item in json_data]
    
    current_selected_curency = values[0]

    log_message("webscrapper.py", "current_usd_to_egp_exchange_rate", f"Current USD to EGP exchange rate is: {current_selected_curency}")
    
    return current_selected_curency