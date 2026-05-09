
# Fighter path
RIO = {
    "name": "Rio",
    "hp": 100,
    "moves": [
        {"name": "Slash", "damage": 15},
        {"name": "Drawing Cut", "damage": 30, "player_skip": True},
        {"name": "Thrust", "damage":8}
    ]
}

HOUND = {
    "name": "Many-Eyed Hound",
    "hp": 80,
    "moves": [
        {"name": "Claw", "damage": 12},
        {"name": "Bite", "damage": 15},
        {"name": "Glare", "damage": 0, "player_skip": True}
    ]
}

# Mage path
YOHAN = {
    "name": "Yohan",
    "hp": 90,
    "moves": [
        {"name": "Frost Spear", "damage": 15},
        {"name": "Firebolt", "damage": 14},
        {"name": "Lightning Bolt", "damage": 8, "enemy_skip": True}
    ]
}
