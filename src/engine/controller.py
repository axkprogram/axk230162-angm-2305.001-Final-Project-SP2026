import pygame

class EngineController:
    """
    Central brain of the game.
    
    Responsible for:
    - running the main loop
    - switching between systems (scene/ event/ combat)
    - holding references to GameState and systems
    """

    def __init__(self, game_state):
        self.game_state = game_state

        # Active system mode
        self.active_mode = "SCENE" # SCENE / EVENT / COMBAT
        
        # System placeholders (implementation later)
        self.scene_system = None
        self.event_system = None
        self.combat_system = None

        self.running = True
        