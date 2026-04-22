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