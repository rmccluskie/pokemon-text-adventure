import text_prompts
from utils import *

print(text_prompts.welcome_text)
print()
pokemon_num = prompt_user(text_prompts.starter_text, text_prompts.starter_prompt)
if(pokemon_num not in ["1", "2", "3", "4"]):
    while(pokemon_num not in ["1", "2", "3", "4"]):
        print("\n" + text_prompts.starter_error)
        pokemon_num = prompt_user(text_prompts.starter_text, text_prompts.starter_prompt)

match pokemon_num:
    case "1":
        pokemon = "Bulbasaur"
    case "2":
        pokemon = "Charmander"
    case "3":
        pokemon = "Squirtle"
    case "4":
        pokemon = "Pikachu"

print("\n" + text_prompts.selection_text.format(pokemon))
    