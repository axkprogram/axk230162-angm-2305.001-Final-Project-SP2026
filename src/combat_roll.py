import random

def roll_damage():
    roll = random.randint(1,20)

    if roll == 1:
        multiplier = 0.0
    elif roll <= 8:
        multiplier = 0.5
    elif roll <= 15:
        multiplier = 1.0
    elif roll < 20:
        multiplier = 1.5
    else:
        multiplier = 2.0

    base_damage = random.randint(5,10)
    final_damage = int(base_damage * multiplier)
    
    return roll, final_damage