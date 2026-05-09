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

    def use_player_move(self, move):
        if self.player_skip:
            self.player_skip = False
            self.turn = "enemy"
            self.message = f"{self.player['name']} loses a turn!"
            return
        
        self._apply_move(move, self.player, self.enemy)
        self.turn = "enemy"

    