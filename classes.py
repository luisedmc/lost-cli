class Game:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.Island = None
        self.number_creatures: int = 0
        self.islands: dict = {}
        self.position_x: int = 0
        self.position_y: int = 0

    def set_islands(self, islands: dict) -> None:
        self.islands = islands

    def set_current_island(self, island: Island) -> None:
        self.island = island


class Player:
    """
    Player class holds all player data
    """
    def __init__(self) -> None:
        self.name: str = ""
        self.hp: int = 100
        self.gold: int = 0
        self.creatures_killed: int = 0
        self.xp: int = 0
        self.level: int = 1
        self.turns: int = 0


class Island:
    """
    Island class holds all island data
    """
    def __init__(self) -> None:
        self.description: str
        self.sound: str
        self.smell: str

    def print_description(self) -> None:
        print(self.description)
        print(self.sound)
        print(self.smell)