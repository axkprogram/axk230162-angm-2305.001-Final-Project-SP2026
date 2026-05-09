# state/game_state.py
from dataclasses import dataclass, field

@dataclass
class GameState:
    """
    Central truth container for the entire VN/RPG engine.
    
    This object is shared across:
    - Scene System
    - Event System
    - Combat System
    - Engine Controller
    - Save System
    """

    # Narrative/ Flow State
    current_scene_id: str = "forest_intro"
    route_state: str = "neutral" # can become fighter / mage / dark / neutral

    party_alignment: str | None = None

    flags: dict = field(default_factory=dict)
    """
    Example flags:
    - "heard_bell_context": True
    - "met_rio": True
    - "cave_fallen": True
    """

    # Inventory State
    inventory: dict = field(default_factory=dict)
    """
    Example:
    {
        "mysterious_object": True,
        "talisman_of_sight": False
    }
    """

    # Player State
    player_hp: int = 100
    player_max_hp: int = 100

    # Party Context
    party_state: dict = field(default_factory=lambda: { 
        "carmen": {"hp": 100},
        "rio": {"hp": 150},
        "yohan": {"hp": 125}
    })

    # Combat State
    active_battle_id: str | None = None
    in_combat: bool = False
    battle_result: str | None = None # "win", "loss", None

    # Event State
    active_event_id: str | None = None
    in_event: bool = False

    # Core Utility methods
    def set_flag(self, key: str, value=True):
        self.flags[key] = value

    def get_flag(self, key: str, default=None):
        return self.flags.get(key, default)
    
    def add_item(self, item_name: str, value=True):
        self.inventory[item_name] = value

    def has_item(self, item_name: str) -> bool:
        return self.inventory.get(item_name, False)
    
    def reset_battle_state(self):
        self.active_battle_id = None
        self.in_combat = False
        self.battle_result = None

    def reset_event_state(self):
        self.active_event_id = None
        self.in_event = False