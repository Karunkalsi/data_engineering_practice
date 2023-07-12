import requests
import pandas as pd

# Set the base URL for the NBA API
base_url = "https://stats.nba.com/stats/"

# Set the parameters for the API request
params = {
    "LeagueID": "00",
    "PerMode": "PerGame",
    "Season": "2020-21",
    "SeasonType": "Regular Season",
    "MeasureType": "Advanced",
    "PlayerOrTeam": "Player",
    "StatCategory": "MIN_FGA",
    "MinFGA": "1000",
    "Sorter": "PER",
    "Direction": "DESC",
    "PaceAdjust": "N",
    "Rank": "Y",
}

# Make the API request
response = requests.get(base_url + "leaguedashplayerstats", params=params)
data = response.json()

# Get the column headers and the row data
headers = data["resultSets"][0]["headers"]
rows = data["resultSets"][0]["rowSet"]

# Create the DataFrame
df = pd.DataFrame(rows, columns=headers)

print(df)
