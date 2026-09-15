import json
import os
def add(name,player_stats,item):
    inv = player_stats.setdefault("inventory", {})
    inv[item] = inv.get(item, 0) + 1
    save_game(name,player_stats)
def save_game(name,player_stats):
    try:
        os.makedirs("save", exist_ok=True)
        with open("save/savegame.json", "w") as f:
            json.dump({"name" : name, "stats" : player_stats}, f)
    except Exception as e:
        print(f"error saving inventory: {e}")
