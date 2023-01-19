from colorama import Fore
import armory
import descriptions
import random
import os


# Player holds all player data.
class Player:
    def __init__(self) -> None:
        self.name: str = ""
        self.hp: int = 100
        self.gold: int = 0
        self.monsters_killed: int = 0
        self.xp: int = 0
        self.level: int = 0
        self.turns: int = 0
        self.inventory: list = []
        self.current_weapon: dict = armory.default["hands"]
        self.current_armor: dict = armory.default["clothes"]
        self.current_shield: dict = armory.default["noshield"]
        self.x_axis: int = 0
        self.y_axis: int = 0
        self.visited: list = []

# Island holds all island data.
class Island:
    def __init__(self, items: list, monster: dict, location: str) -> None:
        self.description: str = descriptions.descriptions[random.randint(0, len(descriptions.descriptions)-1)]

        self.sound: str = descriptions.sounds[random.randint(0, len(descriptions.sounds)-1)]

        self.smell: str = descriptions.smells[random.randint(0, len(descriptions.smells)-1)]

        self.items: list = items
        self.monster: dict = monster
        self.location: str = location

    def print_description(self) -> None:
        terminal_size = os.get_terminal_size()
        print(Fore.LIGHTCYAN_EX + "-" * terminal_size.columns)
        print(
        f"""
        {self.description} """)
        print(
        f"""
        {self.sound} """)
        print(
        f"""
        {self.smell}
        """
        )


# Game holds all game data.
class Game:
    def __init__(self, player: Player, x: int, y: int) -> None:
        self.player = player
        self.island = None
        self.number_monsters: int = 0
        self.islands: dict = {}
        self.x_axis: int = x
        self.y_axis: int = y
        self.start_point: str = ""

    def set_islands(self, islands: dict) -> None:
        self.islands = islands

    def set_current_island(self, island: Island) -> None:
        self.island = island

    def set_start_point(self, start_point: str) -> None:
        self.start_point = start_point
