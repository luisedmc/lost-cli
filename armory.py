# Items contains all items in the game.
items = {
    # Weapons
    "longsword": {
        "name": "longsword",
        "min_damage": 5,
        "max_damage": 25,
        "to_hit": 25,
        "type": "weapon",
    },
    "axe": {
        "name": "axe",
        "min_damage": 10,
        "max_damage": 15,
        "to_hit": 10,
        "type": "weapon",
    },
    "moonblade": {
        "name": "moonblade",
        "min_damage": 15,
        "max_damage": 25,
        "to_hit": 15,
        "type": "weapon",
    },
    "assassinsdagger": {
        "name": "assassinsdagger",
        "min_damage": 7,
        "max_damage": 20,
        "to_hit": 15,
        "type": "weapon",
    },
    "brokensword": {
        "name": "brokensword",
        "min_damage": 2,
        "max_damage": 10,
        "to_hit": 0,
        "type": "weapon",
    },
    "crossbow": {
        "name": "crossbow",
        "min_damage": 5,
        "max_damage": 15,
        "to_hit": 20,
        "type": "weapon",
    },
    "wolfsword": {
        "name": "wolfsword",
        "min_damage": 20,
        "max_damage": 40,
        "to_hit": 30,
        "type": "weapon",
    },

    # Shields
    "simpleshield": {
        "name": "simpleshield",
        "defense": 5,
        "type": "shield",
    },
    "roundshield": {
        "name": "roundshield",
        "defense": 15,
        "type": "shield",
    },
    "knightshield": {
        "name": "knightshield",
        "defense": 25,
        "type": "shield",
    },
    "wolfshield": {
        "name": "wolfshield",
        "defense": 30,
        "type": "shield",
    },

    # Armor
    "leatherarmor": {
        "name": "leatherarmor",
        "defense": 10,
        "type": "armor",
    },
    "steelarmor": {
        "name": "steelarmor",
        "defense": 20,
        "type": "armor",
    },
    "wolfarmor": {
        "name": "wolfarmor",
        "defense": 30,
        "type": "armor",
    },

    # Others
    "waterskin": {
        "name": "waterskin",
        "type": "item",
    },
    "penny": {
        "name": "penny",
        "type": "item",
    },
}

# Default contains all the items that are given to the player at the start of the game.
default = {
    "hands": {
        "name": "hands",
        "min_damage": 1,
        "max_damage": 5,
        "to_hit": 0,
        "type": "weapon",
    },
    "clothes": {
        "name": "clothes",
        "defense": 0,
        "type": "armor",
    },
    "noshield": {
        "name": "noshield",
        "defense": 0,
        "type": "shield",
    },
}
