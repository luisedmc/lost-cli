from colorama import Fore
import descriptions
import random
import os


# Player holds all player data.
class Player:
    def __init__(self) -> None:
        self.name: str = ""
        self.hp: int = 100
        self.gold: int = 0
        self.creatures_killed: int = 0
        self.xp: int = 0
        self.level: int = 1
        self.turns: int = 0
        self.inventory: list = []


# Island holds all island data.
class Island:
    def __init__(self, items: list, monster: dict) -> None:
        self.description: str = descriptions.descriptions[random.randint(0, len(descriptions.descriptions)-1)]

        self.sound: str = descriptions.sounds[random.randint(0, len(descriptions.sounds)-1)]

        self.smell: str = descriptions.smells[random.randint(0, len(descriptions.smells)-1)]

        self.items: list = items

        self.monster: dict = monster

    def print_description(self) -> None:
        terminal_size = os.get_terminal_size()
        print(Fore.LIGHTCYAN_EX + "-" * terminal_size.columns)
        print(
        f"""
        {self.description}"""
        )
        print(
        f"""
        {self.sound}"""
        )
        print(
        f"""
        {self.smell}"""
        )


# Game holds all game data.
class Game:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.island = None
        self.number_creatures: int = 0
        self.islands: dict = {}
        self.position_x: int = 0
        self.position_y: int = 0

    def set_islands(self, islands: dict) -> None:
        self.islands = islands

    def set_current_island(self, island: Island) -> None:
        self.island = island
