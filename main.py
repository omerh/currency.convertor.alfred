import json
import requests
import sys

# Get your API Key from https://www.exchangerate-api.com/
api_key = ""

# Wanted currency symbol
symbols = ["ILS", "USD", "EUR", "CAD", "GBP"]
query = (sys.argv[1:])
args = str.split(query[0], " ")

# amount
number = args[0]
number = number.replace("\\", "", -1)
amount = float(number)

if len(args) >= 2:
    symbol = str.upper(args[1]).strip()
else:
    # Default to USD
    symbol = "USD"

# Remove the symbol you asked
symbols.remove(symbol)

# Exchange rate API
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{symbol}"
response = requests.get(url).json()
# Get conversion rates dict from response
conversion_rates = response["conversion_rates"]

alfred_results = []

for item in conversion_rates:
    currency = item
    if currency in symbols:
        currency_rate = float(conversion_rates[item])
        converted_amount = currency_rate * amount
        result = {
            "title": f"{currency} {converted_amount}",
            "icon": {
                "path": f"./{currency}.png"  # Downloaded from "https://www.countryflagicons.com/FLAT/64/DE.png"
            }
        }
        alfred_results.append(result)

response = json.dumps({
    "items": alfred_results
})

sys.stdout.write(response)
