# engine/combat.py
import random

class CombatSystem:
    def __init__(self, state):
        self.state = state
        self.turn = 0
        self.enemy_hp = 80

        self.used_dagger = False
        self.used_spell = False
    
    def start_enemy(self, enemy):
        self.enemy_hp = 80
        self.turn = 0

    def player_action(self, action):
        self.turn += 1

        if action == "dagger":
            self.used_dagger = True
            self.enemy_hp -= 10

        elif action == "spell":
            self.used_spell = True
            self.enemy_hp -= 10

        elif action == "bell":
            if not (self.used_dagger or self.used_spell):
                return "Locked"
            return "BELL_TRIGGER"
        
        return "ok"
    
    def enemy_action(self):
        self.state.player_hp -= random.randint(5,10)
        self.trun += 1

    def update(self):
        if self.enemy_hp <= 0:
            return "WIN"
        
        if self.state.player_hp <= 0:
            return "LOSE"
        
        if self.turn >= 4:
            return "ANNIHILATION"
        
        self.enemy_action()
        return "CONTINUE"
