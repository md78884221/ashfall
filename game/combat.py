import random
import json
import os
def lootdrops(difficulty="easy",*p_drops):
    if os.path.exists("data/items.json") :
        try:
            with open("data/items.json", "r") as f:
                items = json.load(f)
                whitelisted_items = [item for item in items if item in p_drops]
                if not whitelisted_items:
                    return []
                if difficulty == "easy":
                    loot = random.choices(whitelisted_items, k=random.randint(1,3))
                else:
                    loot = random.choices(items, k=random.randint(1,3))
                return loot
        except Exception as e:
            print(f"Error: {e}")
    return 