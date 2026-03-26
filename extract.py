import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("FOOTBALL_API_KEY")
BASE_URL = "https://api.football-data.org/v4"
headers = {
    "X-Auth-Token": API_KEY
}

def get_standings(competition_code="PL"):
    """Get table of standings for competition. Pl = Premier League """
    url = f"{BASE_URL}/competitions/{competition_code}/standings"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Connection successful")
        return response.json()
    else:
        print(f"Network with API not working: {response.status_code}")
        return None

if __name__ == "__main__":
    data = get_standings("PL")
    print(json.dumps(data, indent=2))

