from classes import Player, Game, Island
from colorama import Fore, init
import random
import armory
import bestiary


def welcome_screen() -> None:
    """
    welcome_screen simply shows the welcome screen of the game to the user.
    """
    print(Fore.RED +
        "                                   D U N G E O N"
        )

    print(Fore.GREEN +
        """
        Game Description
        """
        )


def run_game() -> None:
    # Initialize colorama
    init()

    welcome_screen()

    # Create a new Player
    player = Player()

    player.name = input(Fore.GREEN +
        """
        Hello Adventurer!
        I can see you made a good decision!
        Would you kindly tell me your name?
        """ + Fore.LIGHTCYAN_EX + """
-> """
        ).strip()

    # Create a new Game
    new_game = Game(player)

    input(Fore.GREEN +
        f"""
        Welcome to the game, {player.name}!
        We're all set to begin.
        Would you kindly press the ENTER key to start the game?
        """
        )
    explore_island(new_game)


def explore_island(current_game: Game) -> None:
    while True:
        island = generate_island()
        current_game.island = island
            

        current_game.island.print_description()

        for i in current_game.island.items:
                print(
        f"""
        {Fore.LIGHTYELLOW_EX}You see a {i['name']} on the ground.
        """
        )

        if current_game.island.monster:
                print(
        f"""
        {Fore.LIGHTRED_EX}You see a {current_game.island.monster['name']} nearby.
        """
        )

        input_player = input(Fore.LIGHTCYAN_EX + "-> ").lower().strip()

        # Get the option selected from the User
        if input_player == "exit":
            play_again()

        elif input_player == "help":
            show_help()

        elif input_player.startswith("take"):
            if not current_game.island.items:
                print(Fore.YELLOW +
        """
        There's nothing to take here...
        """
        )
                continue
            else:
                take_item(current_game, input_player)

        elif input_player in ["w", "s", "d", "a"]:
            print(Fore.LIGHTMAGENTA_EX +
        """
        You go deeper into the island...
        """
        )
            continue


        else:
            print(Fore.YELLOW +
        """
        I don't think I understand what you mean...
        Maybe you could type 'help' and see what happens?
        """
        )

# Generate a new Island
def generate_island() -> Island:
    items = []
    monsters = {}

    # 25% chance to have an item
    if random.randint(1, 100) < 25:
        item = random.choice(list(armory.items.values()))
        items.append(item)

    # 25% chance to have a monster
    if random.randint(1, 100) < 25:
        monsters = random.choice(bestiary.monsters)

    return Island(items, monsters)


def take_item(current_game, input_player) -> None:
    # Checking if the the user is using the command 'take'
    if len(current_game.island.items) > 0 and input_player[5:] == "":
        input_player = input_player + " " + current_game.island.items[0]["name"]

    # Checking if the item is not in the inventory
    if input_player[5:] not in current_game.player.inventory:
        idx = find_item(input_player[5:], "name", current_game.island.items)

        # Adding the item to the inventory
        if idx > -1:
            current_item = current_game.island.items[idx]
            current_game.player.inventory.append(current_item["name"])
            current_game.island.items.remove(current_item)
            print(Fore.YELLOW +
        f"""
        You took '{input_player[5:]}' from the ground.
        """
        )
        else:
            print(Fore.YELLOW +
        f"""
        I can't find '{input_player[5:]}' in the ground.
        Maybe you should check your spelling?
        Or the item is not in the ground...
        """
        )
            

    else:
        print(Fore.YELLOW +
        f"""
        You already have '{input_player[5:]}' in your inventory.
        I don't think you need another one...
        """
        )


def find_item(search: str, key: str, list_search: list) -> int:
    idx = -1
    cnt = 0
    for item in list_search:
        if item[key] == search:
            idx = cnt
        cnt += 1
    return idx

# Show the help message
def show_help() -> None:
    print(Fore.YELLOW +
        """
        If you need help, you have a few options:

        Player Options:
        - w/s/d/a to move Up/Down/Right/Left
        - map to show the map
        - look to look around your current position
        - inventory to show your inventory
        - equip <item> to equip an item from your inventory
        - unequip <item> to unequip an item from your inventory
        - examine <item> to examine an item from your inventory
        - use <item> to use an item from your inventory
        - take <item> to take an item from the ground
        - drop <item> to drop an item from your inventory

        Game Options:
        - 'exit' to leave the game
        - 'help' to show this message
        
        """
        )


# Ask the user if he wants to play again
def play_again() -> None:
    answer = input(Fore.YELLOW +
        """
        So...
        You want to play again?
        Just answer with a simple 'yes' or 'no' and I will know what to do...
-> """
        ).lower().strip()

    while answer not in ["yes", "no"]:
        answer = input(Fore.YELLOW +
        """
        I don't think I understand what you mean...
        Maybe you could type 'yes' or 'no'?
-> """
        )

    if answer == "yes":
        run_game()
        
    elif answer == "no":
        print(Fore.RED +
        """
        So you choose to leave...
        Another soul lost in the labyrinth.
        """
        )
        exit(0)
