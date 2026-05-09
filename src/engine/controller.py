from data.scenes.registry import SCENE_REGISTRY

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
        
        # keep processing untiil visible ui
        while self.running:

            result = self.scene_system.update(
                input_data,
                self.game_state
            )

            if not result:
                break

            self._handle_result(result)

            # stop loop when player interaction needed
            if result.get("action") in ("dialogue", "choice"):
                break

            # prevent repeated inputs
            input_data = {}

    # Result Handler
    def _handle_result(self, result):

        print(result)

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

            if target in SCENE_REGISTRY:
                self.scene_system.load_scene(
                    SCENE_REGISTRY[target]
                )

                self.game_state.current_scene_id = target


        # End Scene 
        elif result.get("end_scene"):
            self.running = False

        # fix
        elif "set" in result:
            for k, v in result["set"].items():
                setattr(self.game_state, k, v)

        action = result.get("action")
        
    # Stop Engine
    def stop(self):
        self.running = False