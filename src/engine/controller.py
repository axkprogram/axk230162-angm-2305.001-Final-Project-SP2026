class EngineController:
    """
    Minimal game controller for VN MVP.
    
    Responsibilities:
    - Receive SceneManager output
    - Update UI state
    - Maintain game state flags
    - Switch modes cleanly
    """

    def __init__(self, game_state):
        self.game_state = game_state

        self.scene_system = None

        self.running = True

        # UI state (only what renderer needs)
        self.ui_state = {
            "mode": "dialogue",
            "speaker": "",
            "text": "",
            "choices": []
        }

    # System registration
    def register_scene_system(self, scene_system):
        self.scene_system = scene_system

    