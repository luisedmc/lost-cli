from colorama import Fore


# Find an item in a list
def find_item(search: str, key: str, list_search: list) -> int:
    idx = -1
    cnt = 0
    for item in list_search:
        if item[key] == search:
            idx = cnt
        cnt += 1
    return idx


def get_input(question: str, answers: list) -> str:
    while True:
        resp = input(f"{Fore.LIGHTRED_EX}{question}").lower().strip()
        if resp not in answers:
            print(Fore.YELLOW +
        f"""
        I don't understand '{resp}'.
        Maybe you should check your spelling?
        Or you are trying to do something you can't do...
        """
        )
        else:
            return resp