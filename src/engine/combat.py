# engine/combat.py
import random

class Combat:
    def __init__(self, state):
        self.state = state
        self.turn = 0
        self.enemy_hp = 100
        self.used_dagger = False
        self.used_spell = False

    def player_attack(self, attack):
        self.turn += 1

        if attack == "dagger":
            self.used_dagger = True
            self.enemy_hp -= 10

        elif attack == "spell":
            self.used_spell = True
            self.enemy_hp -= 10

        elif attack == "bell":
            if not (self.used_dagger or self.used_spell):
                return "Bell locked"
            return "BELL_TRIGGER"
        
        return "continue"
    