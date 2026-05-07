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
    route_state: str = "netural" # can become fighter / mage / dark / neutral

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
    part_state: dict = field(default_factory=lambda: { 
        "carmen": {"hp": 100},
        "rio": {"hp": 150},
        "yohan": {"hp": 125}
    })