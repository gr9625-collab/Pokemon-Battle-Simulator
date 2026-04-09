import requests
import json
import os
import time

script_dir = os.path.dirname(__file__)
save_dir = os.path.join(script_dir, "data", "move_data")

for move_id in range(1, 1001):
    url = f"https://pokeapi.co/api/v2/move/{move_id}/"
    data = requests.get(url).json()
    name = data["name"]
    file_path = os.path.join(save_dir, f"{move_id}. {name}.json")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Downloaded {move_id}. {name}")

    time.sleep(0.1)