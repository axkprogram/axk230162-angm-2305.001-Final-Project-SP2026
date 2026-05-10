
# Fighter path
RIO = {
    "name": "Rio",
    "hp": 100,
    "moves": [
        {"name": "Slash", "damage": 15}, # basic damage
        {"name": "Drawing Cut", "damage": 30, "player_skip": True}, # skip the player turn
        {"name": "Thrust", "damage":8} # lower damage, temporary 2 turns defense buff
    ]
}

HOUND = {
    "name": "Many-Eyed Hound",
    "hp": 80,
    "moves": [
        {"name": "Claw", "damage": 12},
        {"name": "Bite", "damage": 15}, # chance to cause extra damage
        {"name": "Glare", "damage": 0, "player_skip": True} # chance to cause player to skip turn
    ]
}

# Mage path
YOHAN = {
    "name": "Yohan",
    "hp": 90,
    "moves": [
        {"name": "Frost Spear", "damage": 15}, # basic damage
        {"name": "Firebolt", "damage": 14}, # change to cause extra enemy damage next turn
        {"name": "Lightning Bolt", "damage": 8, "enemy_skip": True} # chance to stun the enemy causing to skip turn
    ]
}

SPECTER = {
    "name": "Specter",
    "hp": 75,
    "moves": [
        {"name": "Banish", "damage": 0}, # only one spell can get banished at a time
        {"name": "Pellet", "damage": 10}, #less attack, but can attack multiple times in one turn 2-4 times
        {"name": "Screech", "damage": 12, "player_skip": True} # chance to cause player to lose a turn
    ]
}


# Dark path
CARMEN = {
    "name": "Carmen",
    "hp": 100,
    "moves": [
        {"name": "Dagger", "damage": 0},
        {"name": "Spell", "damage": 0},
        {"name": "Unnamed", "damage": 999}
    ]
}

MONSTER = {
    "name": "Unknown Monster",
    "hp": 999,
    "moves": [
        {"name": "Annihilate", "damage": 999} # takes four turns to charge
    ]
}


# Special casing later