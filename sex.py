import json

def load_sex_counts():
    try:
        with open("sex_counts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_sex_counts(counts):
    with open("sex_counts.json", "w") as f:
        json.dump(counts, f, indent=4)