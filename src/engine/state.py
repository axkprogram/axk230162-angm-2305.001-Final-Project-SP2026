class GameState:
    def __init__(self):
        self.player_hp = 100
        self.fighter_hp = 120
        self.mage_hp = 80

        self.fighter_favor = 0
        self.mage_favor = 0

        self.flags = {}

        self.inventory = []

    def modify_favor(self, character, amount):
        if character == "fighter":
            self.fighter_favor += amount
        elif character == "mage":
            self.mage_favor += amount
