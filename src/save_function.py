import json

SAVE_FILE = "save.json"

def save_game(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None