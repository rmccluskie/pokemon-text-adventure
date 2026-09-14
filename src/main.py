# from classes.pokemonMap import PokemonMap
from enums.startersEnum import StartersEnum
import utils.text_prompts as text_prompts
from utils.utils_functions import *

print(text_prompts.welcome_text)
starter_num = int(prompt_user(text_prompts.starter_text, text_prompts.num_select_prompt))
starter_numbers = [member.value for member in StartersEnum]
if(starter_num not in starter_numbers):
    while(starter_num not in starter_numbers):
        print("\n" + text_prompts.num_select_error.format(list(StartersEnum)[0].value, list(StartersEnum)[-1].value))
        starter_num = prompt_user(text_prompts.starter_text, text_prompts.num_select_prompt)

starter = StartersEnum(starter_num).name
print("\n" + text_prompts.selection_text.format(starter))

map_num = int(prompt_user(text_prompts.map_text, text_prompts.num_select_prompt))
# chosen_map = PokemonMap(int(map_num)).name    