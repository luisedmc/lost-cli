from time import sleep
from classes import Game
from colorama import Fore
import random


def fight(current_game: Game) -> str:
    island = current_game.island
    player = current_game.player

    # Assume that the player attacks first
    player_turn = True

    if random.randint(1, 2) == 2:
        player_turn = False

    if player_turn:
        print(Fore.LIGHTYELLOW_EX +
        f"""
        You attack first!
        Let's if you can handle this {island.monster["name"]}!
        """
        )
    else:
        print(Fore.LIGHTYELLOW_EX +
        f"""
        {island.monster["name"]} attacks first!
        Good luck!
        """
        )

    # Defining the monster's health
    monster_hp = random.randint(island.monster["min_hp"], island.monster["max_hp"])
    monster_original_hp = monster_hp

    # Defining the winner
    winner = ""

    # Starting the fight
    while True:
        if player_turn:
            player_roll = random.randint(1, 100)

            # 50% chance to hit
            if player_roll <= 50:
                damage = random.randint(player.current_weapon["min_damage"], player.current_weapon["max_damage"])
                monster_hp -= damage
                print(Fore.LIGHTYELLOW_EX +
        f"""
        You hit the {island.monster["name"]} with your {player.weapon["name"]} and dealt {damage} damage!
        Nice hit! 
        """
                )
                sleep(1)
            else:
                print(Fore.LIGHTYELLOW_EX +
        f"""
        You missed the attack...
        That's unlucky!
        """
                )

            if monster_hp <= 0:
                print(Fore.LIGHTYELLOW_EX +
        f"""
        You killed the {island.monster["name"]}!
        You got {island.monster["xp"]} XP!
        """
                )

        else:
            # Monster's turn
            monster_roll = random.randint(1, 100)

            if monster_roll >= 50:
                damage = random.randint(island.monster["min_damage"], island.monster["max_damage"])
                player.hp -= damage
                print(Fore.LIGHTRED_EX +
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
                print(Fore.RED +
        f"""
        {island.monster["name"]} killed you!
        That's the end of your journey...

        {Fore.WHITE}"We shall find peace. We shall hear the angels, we shall see the sky sparkling with diamonds."
        - Anton Chekhov
        """
                )
                winner = "monster"

        if player.hp <= 0 or monster_hp <= 0:
            break

    return winner