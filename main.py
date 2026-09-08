import os
import json
def start_game():
    name = input("Enter your character's name: ")
    print(f"Welcome, {name}! Your adventure begins now.")
    print("""
    Choose your Class:
        1. Warrior
        2. Mage
        3. Archer
    """)
    while True:
        class_choice = input("Enter your choice (1, 2, or 3) --->").strip()
        if class_choice == "1":
            player_stats = {
                "class": "Warrior",
                "health": 150,
                "strength": 20,
                "magic": 1,
                "speed": 20
            }
            break
        elif class_choice == "2":
            player_stats = {
                "class": "Mage",
                "health": 100,
                "strength": 5,
                "magic": 25,
                "speed": 10
            }
            break
        elif class_choice == "3":
            player_stats = {
                "class": "Archer",
                "health": 120,
                "strength": 15,
                "magic": 10,
                "speed": 30
            }
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    try:
        os.makedirs("save", exist_ok=True)
        with open("save/savegame.json", "w") as file:
            json.dump({"name": name, "stats": player_stats}, file)
    except Exception as e:
        print(f"Error saving game: {e}")
    print(f"Character created: {name}, Class: {player_stats['class']}")
    return name, player_stats

def load_game():
    name = input("Enter your character's name:")  
    try:
        with open("save/savegame.json", "r") as file:
            saved_game = json.load(file)
            if saved_game["name"] == name:
                print(f"Welcome back, {name}! Your adventure continues.")
                print(f""""
    Current Stats:
    ----------------------------------------
    Class: {saved_game['stats']['class']}
    Health: {saved_game['stats']['health']}
    Strength: {saved_game['stats']['strength']}
    Magic: {saved_game['stats']['magic']}
    Speed: {saved_game['stats']['speed']}

    """)
                return [saved_game["name"], saved_game["stats"]]
            else: 
                print("No saved game found for that name. Please try again.")
                return None
    except FileNotFoundError:
        print("No saved game found. Please start a new game.")
        return None
print("""
==========================
 Welcome to ashfall
===========================

""")

def game_loop():
    # this is where we will implement the main game loop where the player will fight enemies, explore the world, and gather loot and allies, I'll figure out how to use my game_loop.
    pass
print("Welcome to ashfall, a text-based adventure game. In this game, you will explore a mysterious world filled with danger and excitement.")

loop = True
while loop:
    print("""
    1. Start a new game
    2. Load a saved game
    3. Quit
    """)
    choice = input("Enter your choice (1,2, or 3) --->").strip()
    if choice == "1":
        name, player_stats = start_game()
        loop = False
    elif choice == "2":
        result = load_game()
        loop = False
        if result is None:
            print("No saved game found. Please start a new game.")
            loop = True
        else:
            name, player_stats = result
            game_loop()
            print("game loaded")
            loop = False
    elif choice == "3":
        print("Thank you for playing ashfall. Goodbye!")
        loop = False
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")