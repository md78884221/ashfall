import os
import json

def open_location(current_world,current_zone,current_location):
    path = f"data/worlds/{current_world}/zones/{current_zone}/locations/{current_location}.json"
    try: 
        with open(path, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"error loading location! : {e}")
        print(path)
        print("Path doesn't exist?")