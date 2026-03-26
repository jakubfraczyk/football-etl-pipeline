import pandas as pd

def transform_standings(raw_data):
    """Transform raw JSON into a clean DataFrame"""

    standings = raw_data["standings"][0]["table"]
    rows=[]
    for team in standings:
        rows.append({
            "position":     team["position"],
            "team":         team["team"]["name"],
            "played":       team["playedGames"],
            "won":          team["won"],
            "draw":         team["draw"],
            "lost":         team["lost"],
            "goals_for":    team["goalsFor"],
            "goals_against":team["goalsAgainst"],
            "goal_diff":    team["goalDifference"],
            "points":       team["points"]

        })
    df = pd.DataFrame(rows)
    df = df.drop_duplicates()
    print("Transformation complete")
    print(df.to_string(index=False))
    return df
if __name__ == "__main__":
    from extract import get_standings
    raw = get_standings("PL")
    df = transform_standings(raw)