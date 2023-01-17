import config as cfg
import os
import utils
from time import sleep
from classes import Game
from colorama import Fore
import random


# Fight function will return the winner - 'Player' or 'Monster'
def fight(current_game: Game) -> str:
    island = current_game.island
    player = current_game.player

    # Assume that the player attacks first
    player_turn = True

    # 50% chance
    if random.randint(1, 2) == 2:
        player_turn = False

    if player_turn:
        print(Fore.LIGHTYELLOW_EX +
        f"""
        You attack first!
        Let's if you can handle this {island.monster["name"]}!
        """
        )
        sleep(2)
    else:
        print(Fore.LIGHTYELLOW_EX +
        f"""
        {island.monster["name"]} attacks first!
        Good luck!
        """
        )
        sleep(2)

    # Defining the monster's health
    monster_hp = random.randint(island.monster["min_hp"], island.monster["max_hp"])
    monster_original_hp = monster_hp

    # Defining the winner, empty by default
    winner = ""

    # Starting the fight
    while True:
        if player_turn:
            player_roll = random.randint(1, 100)
            modified_player_roll = player_roll + player.current_weapon["to_hit"] - island.monster["armor_modifier"]

            # 50% chance to hit
            if modified_player_roll > 50:
                damage = random.randint(player.current_weapon["min_damage"], player.current_weapon["max_damage"])
                monster_hp -= damage
                print(
        f""" {Fore.LIGHTYELLOW_EX}
        You hit the {island.monster["name"]} with your {player.current_weapon["name"]} and dealt {Fore.BLUE} {damage} damage! {Fore.LIGHTYELLOW_EX}
        Nice hit!
        """
                )

            else:
                print(Fore.LIGHTYELLOW_EX +
        f"""
        You missed the attack...
        That's unlucky!
        """
                )

            if monster_hp <= 0:
                print(Fore.LIGHTGREEN_EX +
        f"""
        You killed the {island.monster["name"]} and he dropped {island.monster["gold"]} gold!
        You better catch it! (Relax, it's already in your inventory)
        Good job!

        You received {island.monster["xp"]} XP!
        """)
                current_game.player.gold += current_game.island.monster["gold"]
                current_game.player.xp += current_game.island.monster["xp"]
                current_game.player.monsters_killed += 1
                winner = "player"

        # Monster's turn
        else:
            monster_roll = random.randint(1, 100)
            modified_monster_roll = monster_roll - player.current_shield["defense"] + player.current_armor["defense"]

            if modified_monster_roll > 50:
                damage = random.randint(island.monster["min_damage"], island.monster["max_damage"])
                player.hp -= damage
                print(Fore.RED +
        f"""
        The {island.monster["name"]} hit you and dealt {damage} damage!
        You have {player.hp} HP left! Be careful!
        """
                )
            else:
                print(Fore.LIGHTYELLOW_EX +
        f"""
        The {island.monster["name"]} missed the attack...
        That's lucky!
        """
                )

            if player.hp <= 0:
                print(Fore.LIGHTRED_EX +
        f"""
        You fought bravely, but {island.monster["name"]} was too strong for you...
        That's the end of your journey...


        {Fore.WHITE}"We shall find peace. We shall hear the angels, we shall see the sky sparkling with diamonds."
        - Anton Chekhov
        """
                )
                winner = "monster"

        if player.hp <= 0 or monster_hp <= 0:
            break

        if player.hp <= int(0.2 * cfg.PLAYER_HP):
            answer = utils.get_input(Fore.LIGHTRED_EX +
        f"""
        You are low on health! Do you want to continue this fight against the {island.monster["name"]}?
        You can answer with 'y' or 'n'. {Fore.LIGHTCYAN_EX}
-> """, ["y", "n"])
            if answer == "n":
                return "run"

        elif player.hp <= int(0.3 * cfg.PLAYER_HP):
            answer = utils.get_input(Fore.LIGHTRED_EX +
        f"""
        You are not doing great {player.name}. Do you want to continue this fight against the {island.monster["name"]}?
        You can answer with 'y' or 'n'. {Fore.LIGHTCYAN_EX}
-> """, ["y", "n"])
            if answer == "n":
                return "run"

        elif player.hp <= int(0.5 * cfg.PLAYER_HP):
            answer = utils.get_input(Fore.LIGHTRED_EX +
        f"""
        You are a little hurt, but nothing serious. Do you want to continue this fight against the {island.monster["name"]}?
        You can answer with 'y' or 'n'. {Fore.LIGHTCYAN_EX}
-> """, ["y", "n"])
            if answer == "n":
                return "run"

        else:
            print(Fore.LIGHTYELLOW_EX +
        f"""
        {island.monster["name"]} HP: {monster_hp}/{monster_original_hp}
        """
                )

        sleep(1.5)

        terminal_size = os.get_terminal_size()
        print(Fore.LIGHTCYAN_EX + "-" * terminal_size.columns)

        player_turn = not player_turn

    return winner