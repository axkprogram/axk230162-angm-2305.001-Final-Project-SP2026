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

    # main update loop
    def update(self, input_data):
        if not self.scene_system:
            return
        
        result = self.scene_system.update(input_data, self.game_state)

        if not result:
            return
        
        self._handle_result(result)

    # Result Handler
    def _handle_result(self, result):

        action = result.get("action")

        