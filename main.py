import json
import os
from game import game_loop
# ==============================================
# 
#
#
# ==============================================
def start_game():
    name = input("Enter your character's name: ")
    print(f"Welcome, {name}!")
    print("""
    Choose your class:
    1. Warrior
    2. Mage
    3. Archer
    """)
    while True:
        class_choice = input("Enter your choice: ")
        if class_choice == "1":
            player_stats = {
                "class": "Warrior",
                "health": 150,
                "strength": 20,
                "magic": 1,
                "speed" : 20
            }
            break
        elif class_choice == "2" :
            player_stats = {
                "class": "Mage",
                "health": 100,
                "strength": 5,
                "magic": 25,
                "speed" : 10
            }
            break
        elif class_choice == "3":
            player_stats = {
                "class": "Archer",
                "health": 120,
                "strength": 15,
                "magic": 5,
                "speed" : 30
            }
            break
        else:
            print("choose a valid class (1, 2, or 3)")
    try:
        os.makedirs("save", exist_ok=True)
        with open("save/savegame.json", "w") as f:
            json.dump({"name": name, "stats" : player_stats}, f)
    except Exception as e:
        print(f"Error saving game: {e}")
    print(f"Game saved successfully!, {name} the {player_stats['class']}")
    return name, player_stats
# ==============================================
# 
#
#
# ==============================================
def load_game():
    name = input("Enter character name : ")
    try:
        with open("save/savegame.json", "r") as f:
            saved_game = json.load(f)
            if saved_game["name"] == name:
                print(f"Welcome back, {name}")
                print(f"""Your stats:
                Current Stats:
                Class: {saved_game["stats"]["class"]}
                Health: {saved_game["stats"]["health"]}
                Strength: {saved_game["stats"]["strength"]}
                Magic: {saved_game["stats"]["magic"]}
                Speed: {saved_game["stats"]["speed"]}
                """)
                return saved_game["name"], saved_game["stats"]
            else:
                print("No character found.")
                return None
    except FileNotFoundError:
        print("No saved game.")
        return None
print("welcome to ashfall")
player_name = None
player_stats = None
while True:
    choice = input("do you want to (1) start a new game or (2) load a saved game:").strip()
    if choice == "1":
        player_name, player_stats = start_game()
        break
    elif choice == "2":
        result = load_game()
        if result is not None:
            name, player_stats = result
            game_loop.gameloop(name, player_stats)
        else:
            print("please enter either 1 or 2")