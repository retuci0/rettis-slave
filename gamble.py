import json

def load_balances():
    try:
        with open("balances.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_balances(balances):
    with open("balances.json", "w") as f:
        json.dump(balances, f, indent=4)

def ensure_user_balance(user_id):
    balances = load_balances()
    if str(user_id) not in balances:
        balances[str(user_id)] = 100
        save_balances(balances)
    return balances