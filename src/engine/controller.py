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

        self.scene_system = SceneManager()

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
        if self.scene_system:
            result = self.scene_system.update(input_data, self.game_state)
            self._handle_result(result)

    # Event mode
    def _update_event(self, input_data):
        if self.event_system:
            result = self.event_system.update(input_data, self.game_state)
            self._handle_result(result)

    # Combat Mode
    def _update_combat(self, input_data):
        if self.combat_system:
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
            
        # Scene requests combat start
        if result.get("start_combat"):
            self.active_mode = "COMBAT"

        # Scene requests event
        elif result.get("trigger_event"):
            self.active_mode = "EVENT"

        # Combat ends return to scene
        elif result.get("end_combat"):
            self.game_state.reset_event_state()
            self.active_mode = "SCENE"

        # Scene transition
        elif result.get("change_scene"):
            self.game_state.current_scene_id = result["change_scene"]
            self.active_mode = "SCENE"

        # Stop the Engine
    def stop(self):
        self.running = False