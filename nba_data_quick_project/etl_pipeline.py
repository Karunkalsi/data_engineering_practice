import requests
import pandas as pd
import matplotlib.pyplot as plt

# Cache for player IDs
player_cache = {}

# Function to retrieve shot attempts for a player in a specific year
def get_shot_attempts(player_name, year):
    # Check if player ID is already cached
    if player_name in player_cache:
        player_id = player_cache[player_name]
    else:
        # Set the base URL for the NBA API
        base_url = "https://stats.nba.com/stats/"

        # Set the parameters for the API request
        params = {
            "LeagueID": "00",
            "PerMode": "Totals",
            "PlayerOrTeam": "P",
            "StatCategory": "PTS",
            "Season": "2020-21",
            "SeasonType": "Regular Season",
            "PlayerOrTeam": "Player",
            "Sorter": "PTS",
            "Direction": "DESC",
            "PlayerID": "",
            "SeasonSegment": "",
            "DateFrom": "",
            "DateTo": "",
            "OpponentTeamID": "0",
            "VsConference": "",
            "VsDivision": "",
            "GameSegment": "",
            "Period": "0",
            "LastNGames": "0",
        }

        # Make the API request to search for the player
        response = requests.get(base_url + "commonallplayers", params=params)
        data = response.json()

        # Find the player ID from the API response
        player_id = ""
        for player in data["resultSets"][0]["rowSet"]:
            if player[3] == player_name:
                player_id = player[0]
                break

        # Cache the player ID
        player_cache[player_name] = player_id

    # Set the base URL for the NBA API
    base_url = "https://stats.nba.com/stats/"

    # Set the parameters for the API request
    params = {
        "PlayerID": player_id,
        "Season": year,
        "ContextMeasure": "FGA",
    }

    # Make the API request to retrieve shot attempts
    response = requests.get(base_url + "shotchartdetail", params=params)
    data = response.json()

    # Get the column headers and the row data
    headers = data["resultSets"][0]["headers"]
    rows = data["resultSets"][0]["rowSet"]

    # Create the DataFrame
    df = pd.DataFrame(rows, columns=headers)

    return df

# Function to plot shot attempts on a half-court visualization
def plot_shot_attempts(df):
    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_xlim(-250, 250)
    ax.set_ylim(-47.5, 422.5)
    ax.set_aspect('equal')

    # Draw half-court lines
    court = plt.Rectangle((-250, -47.5), 500, 470, linewidth=2, color='black', fill=False)
    hoop = plt.Circle((0, 0), radius=7.5, linewidth=2, color='black', fill=False)
    ax.add_patch(court)
    ax.add_patch(hoop)

    # Plot shot attempts
    x = df["LOC_X"]
    y = df["LOC_Y"]
    ax.scatter(x, y, color='blue', alpha=0.6)

    # Set axis labels and title
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('Shot Attempts')

    # Show the plot
    plt.show()

# Main function
def main():
    # Get user input for player name and year
    player_name = input("Enter player name: ")
    year = input("Enter year: ")

    # Get shot attempts
    df = get_shot_attempts(player_name, year)

    if df.empty:
        print("Player not found or no shot attempts available.")
        return

    # Plot shot attempts
    plot_shot_attempts(df)

# Run the main function
if __name__ == "__main__":
    main()
