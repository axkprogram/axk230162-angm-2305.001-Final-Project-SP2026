import random
from roll_for_luck_dice import story_roll
from combat_roll import roll_damage

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, dmg):
        self.hp -= dmg
        print(f"{self.name} takes {dmg} damage! (HP: {self.hp})")

    def is_alive(self):
        return self.hp > 0
    
def player_turn(player, enemy):
    print("\n--- Player Turn---")

    input("Press Enter to roll for luck...")

    # Luck Roll
    roll, outcome = story_roll
    print(f"You rolled {roll} ({outcome})")

    if roll < 8:
        print ("You hesitate...")
        return
    
    print("You attack!")

    input("Press Enter to roll for damage")
