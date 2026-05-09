# state/game_state.py
class GameState:
    """
    Stores persistent game state.
    Shared across all scenes.
    """

    def __init__(self):

        # scene tracking
        self.current_scene_id = "forest_intro"
        
        # branching route
        self.route_state = None

        # Player stats
        self.player_hp = 100

        # choice flags
        self.bell_response = None
        self.creature_reaction = None
        self.fall_response = None
        self.cave_argument = None
        self.tunnel_alignment = None
        self.wall_response = None

        # Inventory
        self.inventory = []

        # Generic flags
        self.flags = {}

    # Inventory helper
    def has_item(self, item_name):
        return item_name in self.inventory
    
    def add_item(self, item_name):
        if item_name not in self.inventory:
            self.inventory.append(item_name)

    #flag helpers
    def set_flag(self, name, value=True):
        self.flags[name] = value

    def get_flag(self, name):
        return self.flags.get(name, False)