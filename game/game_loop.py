import time
import os
import json
import random
from game import combat 
actions = ["1", "2", "3", "4", "5"] #TODO: load these keys from json and create acion functions associated with it
def move_forward():
    pass
def talk_to_npc():
    pass
def loot_npc(level=0):
    if 0 <= level < 5:
        print("looting npc....")
        loot = combat.lootdrops("easy","leather_armour", "rusty_dagger")
        for item in loot:
            time.sleep(1)
            print(f"+1 {item}")
        time.sleep(1)
        return loot
    elif level < 0 :
        print("NPC level cannot be negative")
    else:
        print("looting npc. higher than level 5 might be difficult")
        combat.lootdrops()
def c_stats(player_stats):
    if isinstance(player_stats, dict):
        for key, value in player_stats.items():
            print(f"""{key} : {value}
            """)
    else:
        print("Error with parameters")
def c_inventory():
    # placeholder for checking inventory
    print("Still in development")
    pass
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
            results = loot_npc(2)
        elif action == "4":
            results = c_stats(player_stats)
        elif action == "6":
            print("quitting")
        else:
            print("Has to be a valid number between 1-6")
