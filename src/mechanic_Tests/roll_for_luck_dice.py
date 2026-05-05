import random

def roll_d20():
    return random.randint(1,20)

def story_roll():
    roll = roll_d20()

    if roll == 1:
        outcome = "critical fail"
    elif roll < 8:
        outcome = "fail"
    elif roll <= 12:
        outcome = "average"
    elif roll < 20:
        outcome = "success"
    else: # roll == 20
        outcome = "critical success"

    return roll, outcome

