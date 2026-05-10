import random
import copy

class BattleManager:
    def __init__(self):
        self.active = False
        self.player = None
        self.enemy = None
        self.turn = "player"
        self.message = ""

        self.player_skip = False
        self.enemy_skip = False

        #Dark path special flags
        self.used_dagger = False
        self.used_spell = False
        self.dark_special_ready = False
        self.enemy_charge = 0
        self.trigger_dark_scene = False

    def start_battle(self, player, enemy):
        self.active = True
        self.player = copy.deepcopy(player)
        self.enemy = copy.deepcopy(enemy)
        self.turn = "player"
        self.message = f"{enemy['name']} appeared!"

        #reset dark flags
        self.used_dagger = False
        self.used_spell = False
        self.dark_special_ready = False
        self.enemy_charge = 0
        self.trigger_dark_scene = False

    def use_player_move(self, move):
        if not self.active:
            return
        
        if self.player_skip:
            self.player_skip = False
            self.turn = "enemy"
            self.message = f"{self.player['name']} loses a turn!"
            return
        
        # Dark path special logic
        if self.enemy["name"] == "Unnamed Monster":

            if move["name"] == "Dagger":
                self.used_dagger = True
                self.message = "Carmen's dagger does nothing. Rio looks alarmed."

            elif move["name"] == "Spell":
                self.used_spell = True
                self.message = "Carmen's spell does nothing. Yohan looks worried."

            elif move["name"] == "Unnamed":
                self.trigger_dark_scene = True
                self.active = False
                self.message = "Something answers Carmen's bell..."

            #unlock unnamged attack
            if self.used_dagger and self.used_spell:
                self.dark_special_ready = True

                #unlock unnamed
                for m in self.player["moves"]:
                    if m["name"] == "Unnamed":
                        m["locked"] = False

            self.turn = "enemy"
            return

        # Normal battles
        self._apply_move(move, self.player, self.enemy)
        
        if self.active:
            self.turn = "enemy"

    def enemy_turn(self):
        if not self.active:
            return
        
        if self.enemy_skip:
            self.enemy_skip = False
            self.turn = "player"
            self.message = f"{self.enemy['name']} loses a turn!"
            return
        
        #Dark path special enemy
        if self.enemy["name"] == "Unknown Monster":
            self.enemy_charge += 1

            if self.enemy_charge < 4:
                self.message = (
                    f"MONSTER begins charging Annihilate "
                    f"({self.enemy_charge}/4)"
                )

            else:
                self.player["hp"] = 0
                self.active = False
                self.message = "Annihilate actives. Carmen is destroyed."

            self.turn = "player"
            return
        
        # Normal enemy
        move = random.choice(self.enemy["moves"])
        self._apply_move(move, self.enemy, self.player)

        if self.active:
            self.turn = "player"

    def _apply_move(self, move, attacker, defender):
        damage = move.get("damage", 0)

        defender["hp"] = max(0, defender["hp"] - damage)
        
        if move.get("player_skip"):
            self.player_skip = True

        if move.get("enemy_skip"):
            self.enemy_skip = True

        self.message = f"{attacker['name']} used {move['name']}!"

        if defender["hp"] <= 0:
            self.active = False
            self.message = f"{defender['name']} defeated!"