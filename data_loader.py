import json
import os
from models.pokemon import Pokemon

def load_pokemon(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    name = data["name"]

    # Extract stats in a dictionary
    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}

    # Extract types
    type = [t["type"]["name"] for t in data["types"]]

    return Pokemon(
        name = name,
        hp = stats["hp"],
        attack = stats["attack"],
        defense = stats["defense"],
        sp_attack = stats["special-attack"],
        sp_defense = stats["special-defense"],
        speed = stats["speed"],
        type = type,
        moves = []
    )

def load_first_151(folder_path):
    files = os.listdir(folder_path)

    # Sort by the number at the start of filename
    files.sort(key=lambda x: int(x.split(".")[0]))

    pokedex = []

    for file_name in files[:151]:
        file_path = os.path.join(folder_path, file_name)
        pokemon = load_pokemon(file_path)
        pokedex.append(pokemon)

    return pokedex

def load_moves(folder_path):
    files = os.listdir(folder_path)

    # Sort by the number at the start of filename
    files.sort(key=lambda x: int(x.split(".")[0]))

    for file_name in files[:918]:
        file_path = os.path.join(folder_path, file_name)
        moves = #Function