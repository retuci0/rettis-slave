import json

# GAMBLEING
def load_balances():
    try:
        with open("balances.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open("balances.json", "w") as f:
            f.write("{}")
        return {}

def save_balances(balances):
    with open("balances.json", "w") as f:
        json.dump(balances, f, indent=4)

def ensure_user_balance(user_id: int):
    balances = load_balances()
    if str(user_id) not in balances:
        balances[str(user_id)] = 100
        save_balances(balances)
    return balances


# SECS
def load_sex_counts():
    try:
        with open("sex_counts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open("sex_counts.json", "w") as f:
            f.write("{}")
        return {}

def save_sex_counts(counts):
    with open("sex_counts.json", "w") as f:
        json.dump(counts, f, indent=4)
        
    
# SHIPS
def load_ships():
    try:
        with open("ships.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open("ships.json", "w") as f:
            f.write("{}")
        return {}

def save_ships(data):
    with open("ships.json", "w") as f:
        json.dump(data, f, indent=4)


# INVENTORIES
def load_inventories():
    try:
        with open("inventories.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open("inventories.json", "w") as f:
            f.write("{}")
        return {}

def save_inventories(inventories):
    with open("inventories.json", "w") as f:
        json.dump(inventories, f, indent=4)