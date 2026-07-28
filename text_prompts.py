from utils import *
from pokemon import Pokemon
welcome_text = "Welcome to the Pokémon Text Adventure Game!"
starter_text = "Please select your starter:\n" + list_num([member.name for member in Pokemon])
starter_prompt = "Enter the number of your choice: "
starter_error = "Invalid choice. Please enter a number 1-4."

selection_text = "You have chosen {0}!"