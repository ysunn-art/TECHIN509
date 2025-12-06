import pandas as pd

def store_game_data(filename: str, first_player: str, winner: str):
    """
    Store game data into a CSV file using Pandas.

    Args:
        filename (str): The name of the CSV file.
        first_player (str): Name of the first player (e.g., "Human (X)").
        winner (str): Name of the winner (e.g., "Human", "Robot") or "Draw".
    """
    # Create a new DataFrame for the current game's data
    game_data = pd.DataFrame([{
        "First Player": first_player,
        "Winner": winner
    }])
    
    try:
        # Load existing data if the file exists and append the new game
        existing_data = pd.read_csv(filename)
        updated_data = pd.concat([existing_data, game_data], ignore_index=True)
    except FileNotFoundError:
        # If the file doesn't exist, use the current game's data as the starting data
        updated_data = game_data

    # Save the updated DataFrame back to the CSV file
    updated_data.to_csv(filename, index=False)
