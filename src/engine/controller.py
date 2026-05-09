import pygame
from scene.scene_manager import SceneManager

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

        # UI
        self.ui_state = {
            "mode": None,
            "speaker": "",
            "text": "",
            "choices": []
        }

    # System registration
    def register_scene_system(self, scene_system):
         self.scene_system = scene_system

    def register_event_system(self, event_system):
        self.event_system = event_system

    def register_combat_system(self, combat_system):
        self.combat_system = combat_system

    # Main update loop
    def update(self, input_data):
        """
        Called every frame by the game loop.
        Routes control to the active system.
        """

        if self.active_mode == "SCENE":
            self._update_scene(input_data)

        elif self.active_mode == "EVENT":
            self._update_event(input_data)

        elif self.active_mode == "COMBAT":
            self._update_combat(input_data)

    # Scene mode
    def _update_scene(self, input_data):
        if not self.scene_system:
            return
        
        result = self.scene_system.update(input_data, self.game_state)
        self._handle_result(result)

    # Event mode
    def _update_event(self, input_data):
        if  not self.event_system:
            return
        
        result = self.event_system.update(input_data, self.game_state)
        self._handle_result(result)

    # Combat Mode
    def _update_combat(self, input_data):
        if not self.combat_system:
            return
        
        result = self.combat_system.update(input_data, self.game_state)
        self._handle_result(result)

    # Result handler
    def _handle_result(self, result):
        """
        Systems do NOT control the flow directly.
        They return results and the controller then decides the next step.
        """

        if not result:
            return
        
        action = result.get("action")

        # Dialogue output
        if action == "dialogue":
            self.ui_state["mode"] = "dialogue"
            self.ui_state["speaker"] = result.get("speaker", "")
            self.ui_state["text"] = result.get("text", "")
            self.ui_state["choices"] = []

        # Choice output
        elif action == "choice":
            self.game_state_.active_event_id = result.get("event_id")
            self.game_state.in_event = True
            self.active_mode = "EVENT"

        # Combat trigger
        elif action == "battle":
            self.game_state.active_battle_id = result.get("battle_id")
            self.game_state.in_combat = True
            self.active_mode = "COMBAT"

        # Scene transition
        elif action == "change_scene":
            self.game_state.current_scene_id = result.get("target")
            self.active_mode = "SCENE"

        # Scene finished
        elif result.get("end_scene"):
            # for now in scene mode
            self.active_mode = "SCENE"

        # Stop the Engine
    def stop(self):
        self.running = False