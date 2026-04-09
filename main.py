from models.pokemon import Pokemon
from models.moves import Move
from battle.battle import Battle
from data_loader import load_first_151
import os

script_dir = os.path.dirname(__file__)
folder_path = os.path.join(script_dir, "data", "poke_data")
pokedex = load_first_151(folder_path)

print(pokedex[24])

# # Run battle
# battle = Battle(pikachu, bulbasaur)
# battle.run()