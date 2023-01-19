from pyfiglet import Figlet
from blessings import Terminal
from colorama import Fore, init, Back
from classes import Player, Game, Island
import world
import config as cfg
from utils import get_input, find_item
import random
import armory
import bestiary
import combat


f = Figlet(font='slant')
print (f.renderText('L O S T'))


def welcome_screen(current_game: Game) -> None:
    """
    welcome_screen simply shows the welcome screen of the game to the user.
    """
    print(Fore.RED + f.renderText(
        """   L O S T """))
    print(Fore.RED + 
        """      --------------------------------------""")
    print(Fore.GREEN +
        f"""
        Game Description

        A little bird told me that there are {current_game.number_monsters} monsters on this island. Proceed with caution!
        """
        )


def run_game() -> None:
    # Initialize colorama
    init()

    # Create a new Player
    player = Player()

    # Create a new Game with Player, Map X and Y location
    current_game = Game(player, cfg.MAX_X_AXIS, cfg.MAX_Y_AXIS)

    all_islands, number_monsters = world.create_world(current_game)
    current_game.number_monsters = number_monsters
    current_game.set_islands(all_islands)

    # Defining the exit point of the game randomly
    exit_point = random.choice(list(current_game.islands.keys()))
    # print(type(exit_point), exit_point)
    current_game.set_current_island(current_game.islands[exit_point])
    current_game.set_exit_point(exit_point)
    current_game.island.location = exit_point

    welcome_screen(current_game)

    player.name = input(Fore.GREEN +
        """
        Hello Adventurer!
        I can see you made a good decision!
        Would you kindly tell me your name?
        """ + Fore.LIGHTCYAN_EX + """
-> """
        ).strip()

    input(Fore.GREEN +
        f"""
        Welcome to the game, {player.name}!
        We're all set to begin.
        Would you kindly press the ENTER key to start the game?
        """
        )

    current_game.island.print_description()
    explore_island(current_game)


def explore_island(current_game: Game) -> None:
    while True:
        for i in current_game.island.items:
                print(
        f"""
        {Fore.LIGHTYELLOW_EX}You see a {i['name']} on the ground.
        """
        )

        if current_game.island.monster:
            print(
        f"""
        {Fore.LIGHTRED_EX}You see a {current_game.island.monster["name"]} nearby. """
        )
            fight_or_run = get_input(
        f"""
        Do you want to fight or run?
        Choose wisely...
        {Fore.LIGHTCYAN_EX}
-> """, ["fight", "run"])

            while True:
                if fight_or_run == "run":
                    print(Fore.LIGHTMAGENTA_EX +
        """
        You run away from the monster...
        """)
                    break
                else:
                    # Player fights the monster
                    winner = combat.fight(current_game)

                    if winner == "player":
                        current_game.island.monster = {}
                        break

                    elif winner == "monster":
                        play_again()
                        break

                    else:
                        print(Fore.LIGHTRED_EX +
        """
        You ran away from the monster...
        Maybe was a good decision...
        """)
                        break

                 

        input_player = input(Fore.LIGHTCYAN_EX + "-> ").lower().strip()

        # Get the option selected from the User
        if input_player == "exit":
            play_again()

        elif input_player == "help":
            show_help()
            continue

        elif input_player == "look":
            current_game.island.print_description()
            continue

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
                continue

        elif input_player.startswith("drop"):
            drop_item(current_game, input_player)
            continue

        elif input_player.startswith("equip"):
            equip_item(current_game.player, input_player[6:])
            continue

        elif input_player.startswith("unequip"):
            unequip_item(current_game.player, input_player[8:])
            continue

        elif input_player == "status":
            show_status(current_game)
            continue

        elif input_player == "medidate" or input_player == "md":
            meditate(current_game)
            continue

        elif input_player == "inventory" or input_player == "inv":
            show_inventory(current_game)
            continue

        elif input_player == "map":
            show_map(current_game)
            continue

        elif input_player in ["w", "s", "d", "a"]:
            direction = input_player

            if current_game.island.location == current_game.exit_point and direction == "s":
                answer_to_leave = get_input(Fore.MAGENTA +
        """
        You went to the exit point.
        That means you can leave the island.
        Do you want to leave the island? You can answer with 'yes' or 'no'.
        """
                )
                if answer_to_leave != "yes":
                    continue
                else:
                    play_again()

            if direction == "w":
                if current_game.player.y_axis < current_game.y_axis:
                    current_game.player.y_axis += 1
                else:
                    print(Fore.YELLOW +
        """
        You can't go further north...
        I think you are stuck in the island...
        Or maybe you should try going other direction...
        """
        )
                    continue

            elif direction == "s":
                if current_game.player.y_axis > (current_game.y_axis * -1):
                    current_game.player.y_axis -= 1
                else:
                    print(Fore.YELLOW +
        """
        You can't go further south...
        I think you are stuck in the island...
        Or maybe you should try going other direction...
        """
        )
                    continue

            elif direction == "d":
                if current_game.player.x_axis < current_game.x_axis:
                    current_game.player.x_axis += 1
                else:
                    print(Fore.YELLOW +
        """
        You can't go further east...
        I think you are stuck in the island...
        Or maybe you should try going other direction...
        """
        )
                    continue

            elif direction == "a":
                if current_game.player.x_axis > (current_game.x_axis * -1):
                    current_game.player.x_axis -= 1
                else:
                    print(Fore.YELLOW +
        """
        You can't go further west...
        I think you are stuck in the island...
        Or maybe you should try going other direction...
        """
        )
                    continue

            print(Fore.LIGHTMAGENTA_EX +
        """
        You go deeper into the island...
        """
        )

        else:
            print(Fore.YELLOW +
        """
        I don't think I understand what you mean...
        Maybe you could type 'help' and see what happens?
        """
        )
            continue

        # Updating player location
        new_location = f"{current_game.player.x_axis},{current_game.player.y_axis}"
        current_game.island = current_game.islands[new_location]
        current_game.island.location = new_location


        current_game.island.print_description()
        current_game.player.turns += 1
        if new_location in current_game.player.visited:
            print(Fore.YELLOW +
        """
        There's something familiar about this island...
        Maybe you have been here before...
        """
        )
        else:
            current_game.player.visited.append(new_location)


# Generate a new Island
def generate_island(location: str) -> Island:
    items = []
    monsters = {}

    # 25% chance to have an item
    if random.randint(1, 100) < 25:
        item = random.choice(list(armory.items.values()))
        items.append(item)

    # 25% chance to have a monster
    if random.randint(1, 100) < 25:
        monsters = random.choice(bestiary.monsters)

    return Island(items, monsters, location)


# Show the inventory
def show_inventory(current_game: Game) -> None:
    # Checking if the inventory is empty
    if len(current_game.player.inventory) == 0:
        print(Fore.YELLOW +
        f"""
        Player: {current_game.player.name}
        Health: {current_game.player.hp}
        XP:     {current_game.player.xp}
        Gold:   {current_game.player.gold}

        Your Inventory:

        Well, looks like your inventory is empty...
        """
        )
        return

    print(Fore.YELLOW +
        f"""
        Player: {current_game.player.name}
        Health: {current_game.player.hp}
        XP:     {current_game.player.xp}
        Gold:   {current_game.player.gold}

        Your Inventory: """
        )

    for i in current_game.player.inventory:
        if i == current_game.player.current_weapon["name"]:
            print(Fore.LIGHTGREEN_EX +
            f"""
            - {i} (Equipped)\n"""
            )
        elif i == current_game.player.current_armor["name"]:
            print(Fore.LIGHTGREEN_EX +
            f"""
            - {i} (Equipped)\n"""
            )
        elif i == current_game.player.current_shield["name"]:
            print(Fore.LIGHTGREEN_EX +
            f"""
            - {i} (Equipped)\n"""
            )
        else:
            print(Fore.YELLOW +
            f"""
            - {i}
            """
            )


def show_map(current_game: Game) -> None:
    for i in range(1, cfg.MAX_X_AXIS * 6 +3):
        print(Fore.YELLOW + ">", end="")
    print()

    for y in range(cfg.MAX_Y_AXIS, (cfg.MAX_Y_AXIS+1) * -1, -1):
        for x in range(cfg.MAX_X_AXIS * -1, cfg.MAX_X_AXIS +1):
            content = ""

            # Current location
            if f"{x},{y}" == current_game.island.location:
                content = Fore.BLUE + Back.WHITE + " X " + Fore.YELLOW + Back.RESET

            # Exit point
            elif f"{x},{y}" == current_game.exit_point:
                content = Fore.BLUE + Back.WHITE + " E " + Fore.YELLOW + Back.RESET

            # Island visited
            elif f"{x},{y}" in current_game.player.visited:
                test_island = current_game.islands[f"{x},{y}"]

                # Checking if there is a monster or an item and marking the map
                if test_island.monster:
                    content = Fore.RED + " M " + Fore.YELLOW
                
                elif test_island.items:
                    content = Fore.MAGENTA + " I " + Fore.YELLOW

                else:
                    ...

                # Items + Monsters
                if test_island.monster and test_island.items:
                    content = Fore.RED + " S " + Fore.YELLOW
        
            # Island not visited
            else:
                content = " ? "
        
            print(Fore.YELLOW + f"{content.center(3)}", end="")

        print()

    for i in range(1, cfg.MAX_X_AXIS * 6 +3):
        print(Fore.YELLOW + "<", end="")
    print("\n")

    # Legend
    print(Fore.BLUE + Back.WHITE + " X " + Back.RESET + ": Current location     ", end="")
    print(Fore.RED + " M " + Back.RESET + ": Monster     ", end="")
    print(Fore.MAGENTA + " I " + Back.RESET + ": Item     ", end="")
    print(Fore.RED + " S " + Back.RESET + ": Item + Monster     ", end="")
    print(Fore.BLUE + " E " + Back.RESET + ": Exit point     ", end="")
    print(Fore.YELLOW + " ? " + Back.RESET + ": Unknown", end="\n\n")


def take_item(current_game: Game, input_player: str) -> None:
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
        You took {input_player[5:]} from the ground.
        """
        )
        else:
            print(Fore.YELLOW +
        f"""
        I can't find {input_player[5:]} in the ground.
        Maybe you should check your spelling?
        Or the item is not in the ground...
        """
        )
            

    else:
        print(Fore.YELLOW +
        f"""
        You already have {input_player[5:]} in your inventory.
        I don't think you need another one...
        """
        )


def drop_item(current_game: Game, input_player: str) -> None:
    if input_player[5:] == current_game.player.current_weapon["name"]:
        print(Fore.YELLOW +
        f"""
        You can't drop your equipped weapon.
        You need it to kill things...
        """
        )
    elif input_player[5:] == current_game.player.current_armor["name"]:
        print(Fore.YELLOW +
        f"""
        You can't drop your equipped armor.
        You need protection against these monsters out there...
        """
        )
    elif input_player[5:] == current_game.player.current_shield["name"]:
        print(Fore.YELLOW +
        f"""
        You can't drop your equipped shield.
        You need it to defend yourself...
        """
        )

    else:
        try:
            current_game.player.inventory.remove(input_player[5:])
            print(Fore.YELLOW +
        f"""
        You dropped {input_player[5:]} from your inventory.
        Hope you don't need it...
        """
        )

            # If the player decides to drop the item, it will be added to the ground
            current_game.island.items.append(armory.items[input_player[5:]])
        except Exception:
            print(Fore.YELLOW +
        f"""
        I can't find '{input_player[5:]}' in your inventory.
        Maybe you should check your spelling?
        Or the item is not in your inventory...
        """
        )


def equip_item(player: Player, item: str):
    if item in player.inventory:
        old_weapon = player.current_weapon
        old_armor = player.current_armor
        old_shield = player.current_shield

        # Equipping weapons
        if armory.items[item]["type"] == "weapon":
            player.current_weapon = armory.items[item]
            print(Fore.YELLOW +
        f"""
        You equipped {item} instead of {old_weapon["name"]}.
        Make a good use of it!
        """
        )

            # Can't use bows and shields at the same time
            if item == "crossbow" and player.current_shield["name"] != "noshield":
                player.current_shield = armory.default["noshield"]
                print(Fore.YELLOW +
        f"""
        You can't use a shield and a bow at the same time.
        I mean, you need both hands to shoot a bow...
        But don't worry, the shield is still in your inventory.
        """
        )

        # Equipping armor
        elif armory.items[item]["type"] == "armor":
            print(Fore.YELLOW +
        f"""
        You equipped {item} instead of {old_armor["name"]}.
        Hope you are more protected now!
        """
        )
            player.current_armor = armory.items[item]

        # Equipping shield
        elif armory.items[item]["type"] == "shield":
            if player.current_weapon["name"] == "crossbow":
                print(Fore.YELLOW +
        f"""
        You can't use a shield and a bow at the same time.
        I mean, you need both hands to shoot a bow...
        """
        )
            else:
                player.current_shield = armory.items[item]
                print(Fore.YELLOW +
        f"""
        You equipped {item} instead of {old_shield["name"]}.
        Hope you are more protected now!
        """
        )

        else:
            print(Fore.YELLOW +
        f"""
        I don't think you can equip {item}.
        Probably it's not a weapon, armor or shield...
        """
        )

        
    else:
        print(Fore.YELLOW +
        f"""
        I can't find '{item}' in your inventory.
        Maybe you should check your spelling?
        Or the item is not in your inventory...
        """
        )


def unequip_item(player: Player, item: str) -> None:
    if item in player.inventory:
        if player.current_weapon["name"] == item:
            player.current_weapon = armory.default["hands"]
            print(Fore.YELLOW +
        f"""
        You unequipped {item}.
        Now you are using your hands again.
        """
        )

        elif player.current_armor["name"] == item:
            player.current_armor = armory.default["clothes"]
            print(Fore.YELLOW +
        f"""
        You unequipped {item}.
        Back using your clothes again.
        """
        )

        elif player.current_shield["name"] == item:
            player.current_shield = armory.default["noshield"]
            print(Fore.YELLOW +
        f"""
        You unequipped {item}.
        Back using no shield at all again.
        """
        )

        else:
            print(Fore.YELLOW +
        f"""
        I don't think you can unequip {item}.
        Probably it's not equipped at the moment...
        """
        )

    else:
        print(Fore.YELLOW +
        f"""
        I can't find '{item}' in your inventory.
        Maybe you should check your spelling?
        Or the item is not in your inventory...
        """
        )


def show_status(current_game: Game) -> None:
    print(Fore.LIGHTYELLOW_EX + 
        f"""
        You have played the game for {current_game.player.turns} turns,
        defeated {current_game.player.monsters_killed} monsters,
        and found {current_game.player.gold} gold.

        Player {current_game.player.name}
        - XP:     {current_game.player.xp}
        - Level:  {current_game.player.level}
        - Health: {current_game.player.hp}
        - Weapon: {current_game.player.current_weapon["name"]}
        - Armor:  {current_game.player.current_armor["name"]}
        - Shield: {current_game.player.current_shield["name"]}
        """
        )


def meditate(current_game: Game) -> None:
    if current_game.player.hp == cfg.PLAYER_HP:
        print(Fore.GREEN + 
        f"""
        You meditated for a while and now you are full health!
        You now have {current_game.player.hp}/{cfg.PLAYER_HP} HP.
        """
        )

    
    else:
        current_game.player.hp += random.randint(1, 10)
        if current_game.player.hp > cfg.PLAYER_HP:
            current_game.player.hp = cfg.PLAYER_HP
        print(Fore.GREEN +
        f"""
        You meditated for a while and recovered some Health!
        You now have {current_game.player.hp}/{cfg.PLAYER_HP} HP.
        """
        )


# Show the help message
def show_help() -> None:
    print(Fore.YELLOW +
        """
        If you need help, you have a few options:

        Player Options:
        - 'w/s/d/a' to move Up/Down/Right/Left
        - 'map' to show the map
        - 'look' to look around your current position
        - 'medidate' or 'md' to recover some health
        - 'status' to show your current status
        - 'inventory' to show your inventory and your current equipment
        - 'equip' <item> to equip an item from your inventory
        - 'unequip' <item> to unequip an item from your inventory
        - 'examine' <item> to examine an item from your inventory
        - 'use' <item> to use an item from your inventory
        - 'take' <item> to take an item from the ground
        - 'drop' <item> to drop an item from your inventory

        Game Options:
        - 'exit' to leave the game
        - 'help' to show this message
        
        """
        )


# Ask the user if he wants to play again
def play_again() -> None:
    answer = get_input(Fore.YELLOW +
        f"""
        So...
        You want to play again?
        Just answer with a simple 'yes' or 'no' and I will know what to do... {Fore.LIGHTCYAN_EX}
-> """, ["yes", "no"])


    if answer == "yes":
        term = Terminal()
        print(term.clear())
        run_game()
        
    elif answer == "no":
        print(Fore.RED +
        """
        So you choose to leave...
        Another soul lost in the island.
        """
        )
        exit(0)
