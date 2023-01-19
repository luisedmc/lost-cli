from classes import Game
import config as cfg
import game


def create_world(current_game: Game) -> (dict, int):
    islands: dict = {}
    number_monsters: int = 0

    # Creating a island for every entry on the map
    for y in (cfg.MAX_Y_AXIS, (cfg.MAX_Y_AXIS+1) * -1, -1):
        for x in range(cfg.MAX_X_AXIS * -1, cfg.MAX_X_AXIS +1):
            isl = game.create_island(f"{x},{y}")

            # If the island has a monster, add it to the number of monsters
            if isl.monster:
                number_monsters += 1

            islands[f"{x}, {y}"]

    # Returning the populated map
    return islands, number_monsters
