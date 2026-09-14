from utils.utils_functions import list_num
from enums.startersEnum import StartersEnum
from enums.mapEnum import MapEnum

welcome_text = "Welcome to the Pokémon Text Adventure Game!"
starter_text = "Please select your starter:\n" + list_num([member.name for member in StartersEnum])
num_select_prompt = "Enter the number of your choice: "
num_select_error = "Invalid choice. Please enter a number {0}-{1}."
map_text = "Please select a map:\n" + list_num([member.name for member in MapEnum])

selection_text = "You have chosen {0}!"