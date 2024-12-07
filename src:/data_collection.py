import requests
import pandas as pd

# Function to collect data from a fleet data API (example)
def collect_fleet_data(api_url):
    try:
        response = requests.get(api_url)
        data = response.json()
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Error collecting data: {e}")
        return None

# Example usage
api_url = 'https://api.fleetdata.com/vehicles'
fleet_df = collect_fleet_data(api_url)

if fleet_df is not None:
    fleet_df.to_csv('data/fleet_data.csv', index=False)
    print("Data collection successful!")
