from pokemon import Pokemon
import text_prompts
from utils import *

print(text_prompts.welcome_text)
starter_num = int(prompt_user(text_prompts.starter_text, text_prompts.starter_prompt))
starter_numbers = [member.value for member in Pokemon]
print(starter_numbers)
if(starter_num not in starter_numbers):
    while(starter_num not in starter_numbers):
        print("\n" + text_prompts.starter_error)
        starter_num = prompt_user(text_prompts.starter_text, text_prompts.starter_prompt)

starter = Pokemon(int(starter_num)).name
print("\n" + text_prompts.selection_text.format(starter))
    