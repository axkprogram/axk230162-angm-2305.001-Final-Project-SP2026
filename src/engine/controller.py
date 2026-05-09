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

        # Dialogue
        if action == "dialogue":
            self.ui_state["mode"] = "dialogue"
            self.ui_state["speaker"] = result.get("speaker", "")
            self.ui_state["text"] = result.get("text", "")
            self.ui_state["choices"] = []

        # Choice
        elif action == "choice":
            self.ui_state["mode"] = "choice"
            self.ui_state["choices"] = result.get("choices", [])

            # clear dialogue while choosing
            self.ui_state["speaker"] = ""
            self.ui_state["text"] = ""

        # State Change
        elif action == "state_change":
            changes = result.get("changes", {})

            for key, value in changes.items():
                setattr(self.game_state, key, value)

        # Scene Change
        elif action == "change_scene":
            target = result.get("target")

            if target:
                # assume scene manager handles it
                # or replace later with registry system
                pass

        # End Scene 
        elif result.get("end_scene"):
            self.running = False

        # fix
        elif "set" in result:
            for k, v in result["set"].item():
                setattr(self.game_state, k, v)

        action = result.get("action")
        
    # Stop Engine
    def stop(self):
        self.running = False