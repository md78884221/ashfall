import time
import os
import json
import random
from game import combat, inventory
actions = ["1", "2", "3", "4", "5"] #TODO: load these keys from json and create acion functions associated with it
def move_forward():
    print("you move futher down the path...")
def talk_to_npc():
    print("the figure looks up as you approach...")
def loot_npc(name,player_stats,level=0):
    try:
        with open("data/items.json", "r") as f:
            items = json.load(f)
            if 0 <= level < 5:
                print("looting npc....")
                loot = combat.lootdrops("easy","leather_armour", "rusty_dagger")
                if not loot:
                    print("no items found")
                    return []
                for item in loot:   
                    inventory.add(name,player_stats, item)
                    time.sleep(0.5)
                    print(f"+1 {items[item]['name']}")
                time.sleep(1)
                return loot
            elif level < 0 :
                print("NPC level cannot be negative")
            else:
                print("looting npc. higher than level 5 might be difficult")
                combat.lootdrops()
    except Exception as e:
        print(f"Error: {e}")
def c_stats(player_stats):
    if isinstance(player_stats, dict):
        for key, value in player_stats.items():
            if isinstance(value, dict):
                continue
            print(f"""{key} : {value}
            """)
    else:
        print("Error with parameters")
def c_inventory(player_stats):
    try:
        with open("data/items.json") as f:
            items = json.load(f)
    except Exception as e:
            print(f"error : {e}")
            return
    inv = player_stats.get("inventory", {})
    if not inv:
        print("the inventory is empty...")
        return
    inventory_list = list(inv.items())
    print("\nInventory:")
    for index, (item_id, quantity) in enumerate(inventory_list, start = 1):
        item_name = items.get(item_id, {}).get("name", item_id)
        print(f"{index}. {quantity}x {item_name}")
    while True:
        choice = input("enter an item number to inspect, or '0' to exit").strip()
        if choice == "0":
            break
        if not choice.isdigit():
            print("enter a valid number")
            continue
        choice = int(choice)
        if 1 <= choice <= len(inventory_list):
            item_id, quantity = inventory_list[choice - 1]
            item = items.get(item_id,{})
            print(f"""
Name : {item.get('name', 'unknown')}
Type: {item.get('type', 'N/A')}
Description: {item.get('description', 'no description available')}
Value: {item.get('value', 0)}
Quantity: {quantity}
                """)
            if "stats" in item:
                print(f"Stats: {item['stats']}")
            if "requirements" in item:
                print(f"Requirements : {item['requirements']}")
            if "effect" in item:
                print(f"effect: {item['effect']}")
        else:
            print("not valid")
def gameloop(name, player_stats, map="outskirts"):
    print(f"you find yourself in the edges of the {map}")
    time.sleep(0.3)
    print("the remains of an old road stretch out in front of you, broken wooden fences line the path, and abandoned houses watch you eerily from the distance.")
    time.sleep(0.3)
    print("You see someone on the other side of the road....")
    while True:
        print("""
        your next action?
        1. keep moving forward
        2. talk to the npc 
        3. attack and loot the npc 
        4. check your stats
        5. check your inventory
        6. quit
        """)
        action = input("What would you like to do?: ").strip()
        if action == "3":
            results = loot_npc(name,player_stats,2)
        elif action == "4":
            results = c_stats(player_stats)
        elif action == "5":
            results = c_inventory(player_stats)
        elif action == "6":
            print("quitting")
            return
        else:
            print("Has to be a valid number between 1-6")
