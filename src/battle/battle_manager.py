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

    def enemy_turn(self):
        if self.enemy_skip:
            self.enemy_skip = False
            self.turn = "player"
            self.message = f"{self.enemy['name']} loses a turn!"
            return
        
        move = random.choice(self.enemy["moves"])
        self._apply_move(move, self.enemy, self.player)
        self.turn = "player"

    def _apply_move(self, move, attacker, defender):
        damage = move.get("damage", 0)

        defender["hp"] -= damage
        
        if move.get("player_skip"):
            self.player_skip = True

        if move.get("enemy_skip"):
            self.enemy_skip = True

        self.message = f"{attacker['name']} used {move['name']}!"

        if defender["hp" <= 0]:
            self.active = False
            self.message = f"{defender['name']} defeated!"