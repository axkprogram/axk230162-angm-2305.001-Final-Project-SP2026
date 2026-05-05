class GameState:
    def __init__(self):
        self.player_hp = 100
        self.fighter_hp = 120
        self.mage_hp = 80

        self.fighter_favor = 0
        self.mage_favor = 0

        self.flags = {}

        self.inventory = []

    