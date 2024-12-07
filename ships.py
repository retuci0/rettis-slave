import json
import os

def load_ships():
    if os.path.exists("ships.json"):
        with open("ships.json", "r") as f:
            return json.load(f)
    return {}

def save_ships(data):
    with open("ships.json", "w") as f:
        json.dump(data, f, indent=4)