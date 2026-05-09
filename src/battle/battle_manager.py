import random

class BattleManager:
    def __init__(self):
        self.active = False
        self.player = None
        self.enemy = None
        self.turn = "player"
        self.message = ""

        self.player_skip = False
        self.enemy_skip = False

    def start_battle(self, player, enemy):
        self.active = True
        self.player = player.copy()
        self.enemy = enemy.copy()
        self.turn = "player"
        self.message = f"{enemy['name']} appeared!"

    