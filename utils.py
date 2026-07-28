def prompt_user(text, prompt):
    print(text)
    return input(prompt)

def list_num(items):
    out = ""
    for i, item in enumerate(items, start=1):
        out += f"{i}. {item}\n"
    return out
