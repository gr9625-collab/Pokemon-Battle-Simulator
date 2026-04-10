from models.pokemon import Pokemon
from models.moves import Move
from battle.battle import Battle
from data_loader import load_first_151
from data_loader import load_all_moves
import os

script_dir = os.path.dirname(__file__)
pokemon_folder_path = os.path.join(script_dir, "data", "poke_data")
move_folder_path = os.path.join(script_dir, "data", "move_data")

# Should load moves first then load pokemon with their respective moves (as objects from the class Move)

pokedex = load_first_151(pokemon_folder_path)
movedex = load_all_moves(move_folder_path)