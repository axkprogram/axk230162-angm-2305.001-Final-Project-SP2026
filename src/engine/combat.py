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
        