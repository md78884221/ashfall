import json
def add(player_stats,item):
    inventory = player_stats["inventory"]
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1
    with open("data/savegame.json", "w") as f:
        json.dump(player_stats,f)
        