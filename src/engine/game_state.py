class GameState:
    def __init__(self):
        self.flags = []

        self.fighter_favor = 0
        self.mage_favor = 0

        self.player_hp = 100

        self.combat_result = None
        self.in_combat = False

    def set_flag (self, key, value=True):
        self.flags[key] = value

    def get_flag(self, key):
        return self.flags.get(key, False)

    def modify_favor(self, character, amount):
        if character == "fighter":
            self.fighter_favor += amount
        elif character == "mage":
            self.mage_favor += amount
