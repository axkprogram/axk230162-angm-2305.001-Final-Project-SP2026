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
        self.pending_result = None

        # what renderer reads
        self.ui_state = {
            "mode": "dialogue",
            "speaker": "",
            "text": "",
            "choices": []
        }
    
    #Register Scene Manager
    def register_scene_system(self, scene_system):
        self.scene_system = scene_system

    #Main update
    def update(self, input_data):

        # handle delayed dice result
        if input_data.get("advance") and self.pending_result:
            result = self.pending_result
            self.pending_result = None
            self._handle_result(result)
            input_data = {}

        if not self.scene_system:
            return
        
        while self.running:

            result = self.scene_system.update(
                input_data,
                self.game_state
            )

            if not result:
                break

            self._handle_result(result)

            # stop so player can read dialogue or make a choice
            if result.get("action") in (
                "dialogue", 
                "choice"
            ):
                break

            # prevent held key repeating
            input_data = {}


    # result handler
    def _handle_result(self, result):

        action = result.get("action")

        # dialogue
        if action == "dialogue":

            self.ui_state["mode"] = "dialogue"
            self.ui_state["speaker"] = result.get(
                "speaker", ""
            )
            self.ui_state["text"] = result.get(
                "text", ""
            )
            if "followup_result" in result:
                self.pending_result = result["followup_result"]

            self.ui_state["choices"] = []

        # Choice
        elif action == "choice":

            self.ui_state["mode"] = "choice"
            self.ui_state["choices"] = result.get(
                "choices", []
            )

            self.ui_state["speaker"] = ""
            self.ui_state["text"] = ""

        # State Change
        elif action == "state_change":

            changes = result.get(
                "changes", {}
            )

            for key, value in changes.items():
                setattr(
                    self.game_state,
                    key,
                    getattr(
                        self.game_state,
                        key,
                        0
                    ) + value
                    if isinstance(value, int)
                    else value
                )
            
            # debug
            print("Route:", self.game_state.route_state)
        
        # Scene Change
        elif action == "change_scene":
            target = result.get("target")
            print("loading scene:", target)

            #special branch handler
            if target == "route_intro":

                if self.game_state.route_state == "fighter":
                    target = "fighter_intro"

                elif self.game_state.route_state == "mage":
                    target = "mage_intro"

                elif self.game_state.route_state == "dark":
                    target = "dark_intro"

            if target in SCENE_REGISTRY:
                self.scene_system.load_scene(
                    SCENE_REGISTRY[target]
                )

                self.game_state.current_scene_id = target

        # Scene End
        elif result.get("end_scene"):
            self.ui_state["mode"] = "dialogue"
            self.ui_state["speaker"] = "System"
            self.ui_state["text"] = "End of current playable build. Pres ESC to quit"

    # Stop Engine
    def stop(self):
        self.running = False