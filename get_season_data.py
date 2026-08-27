import requests
import pandas as pd

offset = 0
limit = 100
parsed_results = []

raw_data = []

while True:
    url = f"https://api.jolpi.ca/ergast/f1/2026/results/?offset={offset}&limit={limit}"
    response = requests.get(url)
    data = response.json()

    races = data["MRData"]["RaceTable"]["Races"]
    if not races:
        break

    raw_data.extend(races)  

    for race in races:
        print(f"Round {race['round']}: {race['raceName']}")
        season = race["season"]
        round_num = race["round"]
        race_name = race["raceName"]
        
        for result in race["Results"]:
            driver = result["Driver"]
            driver_id = driver["driverId"]
            driver_name = f"{driver['givenName']} {driver['familyName']}"
            grid = result["grid"]
            position = result["position"]
            points = result["points"]

            parsed_results.append(
                {
                    "season": season,
                    "round": round_num,
                    "race_name": race_name,
                    "driver_id": driver_id,
                    "driver_name": driver_name,
                    "grid": grid,
                    "position": position,
                    "points": points
                }
            )

    offset += limit

df = pd.DataFrame(parsed_results)
df.to_csv('2026results.csv')
print(df.head())