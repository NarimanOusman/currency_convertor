import csv
import json
import urllib.request

def fetch_and_save_csv():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    print(f"Fetching data from {url}...")
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        
        rates = data.get('rates', {})
        if not rates:
            print("No rates found in response.")
            return

        filename = 'exchange_rates.csv'
        print(f"Saving to {filename}...")
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Currency', 'Rate'])
            for currency, rate in sorted(rates.items()):
                writer.writerow([currency, rate])
                
        print(f"Successfully saved {len(rates)} currencies to {filename}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_and_save_csv()
