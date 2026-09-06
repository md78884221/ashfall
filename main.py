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

    print(f"Character created: {name}, Class: {player_stats['class']}")
def load_game():
    print("Loading a saved game...")
print("""
==========================
 Welcome to ashfall
===========================

""")

print("Welcome to ashfall, a text-based adventure game. In this game, you will explore a mysterious world filled with danger and excitement.")

while True:
    print("""
    1. Start a new game
    2. Load a saved game
    3. Quit
    """)
    choice = input("Enter your choice (1,2, or 3) --->").strip()
    if choice == "1":
        start_game()
        break
    elif choice == "2":
        load_game()
        break
    elif choice == "3":
        print("Thank you for playing ashfall. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")