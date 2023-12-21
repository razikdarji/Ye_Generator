import requests

def get_kanye_quote():
    response = requests.get("https://api.kanye.rest")
    if response.status_code == 200:
        data = response.json()
        return data.get("quote", "No quote found.")
    else:
        return "Failed to retrieve quote."

# Get a quote and print it
quote = get_kanye_quote()
print(quote)
