import json
import os
from models.pokemon import Pokemon
from models.moves import Move

def find_move_by_name(name, moves):
    for move in moves:
        if move["name"] == name:
            return move
    return None

# This should take all the pokemon, which already have move names, and populate with move objects instead.
def assign_moves(pokedex, movedex):
    return None

def load_pokemon(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    name = data["name"]

    # Extract stats in a dictionary
    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}

    # Extract types
    type = [t["type"]["name"] for t in data["types"]]

    # Extract move names
    moves = [move["move"]["name"] for move in data["moves"]]

    return Pokemon(
        name = name,
        hp = stats["hp"],
        attack = stats["attack"],
        defense = stats["defense"],
        sp_attack = stats["special-attack"],
        sp_defense = stats["special-defense"],
        speed = stats["speed"],
        type = type,
        moves = moves
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

def load_move(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    
    return Move(
        name = data["name"],
        accuracy = data["accuracy"],
        power = data["power"],
        pp = data["pp"],
        type = data["type"]["name"],
        damage_class = data["damage_class"]["name"]
    )

def load_all_moves(folder_path):
    files = os.listdir(folder_path)

    # Sort by the number at the start of filename
    files.sort(key=lambda x: int(x.split(".")[0]))

    moves = []

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        move = load_move(file_path)
        moves.append(move)

    return moves