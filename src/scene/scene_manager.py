class SceneManager:
    """
    Handles scene execution (dialogue, choices, transitions).
    
    SceneManager does NOT control game flow.
    It returns "results" to the EngineController.
    """

    def __init__(self):
        self.current_scene = None
        self.scene_data = None
        self.node_index = 0

        # temp runtime state
        self.waiting_for_choice = False
        self.current_choices = []

    # Load scene
    def load_scene(self, scene_data):
        """
        scene_data will alter come from eitehr JSON or structure format.
        """
        self.scene_data = scene_data
        self.node_index = 0
        self.waiting_for_choice = False
        self.current_choices = []

    # Main update Loop
    def update(self, input_data, game_state):
        """
        Advances the scene step-by-step.
        Returns actions for controller.
        """
        if not self.scene_data:
            return None
        
        # if waiting for player choice, do not advance
        if self.waiting_for_choice:
            return self._handle_choice_input(input_data, game_state)
        
        # Get current node
        if self.node_index >= len(self.scene_data):
            return {"end_scene": True}
        
        node = self.scene_data[self.node_index]

        node_type = node.get("type")

        # Dialogue node
        if node_type == "dialogue":
            self.node_index += 1
            return {
                "dialogue": node.get("text"),
                "speaker": node.get("speaker")
            }
        
        # Choice node
        elif node_type == "choice":
            self.waiting_for_choice = True
            self.current_choices = node.get("options", [])

            return {
                "choice": self.current_choices
            }
        
        # Event Trigger node
        elif node_type == "event":
            self.node_index += 1
            return {
                "trigger_event": node.get("event_id")
            }
        
        # Scene switch node
        elif node_type == "goto":
            return {
                "change_scene": node.get("target")
            }
        
        return None
    
    # Choice handling
    def _handle_choice_input(self, input_data, game_state):
        """
        Handles player selection from choices.
        minimum logic for now
        """

        if "choice_select" in input_data:
            choice_index = input_data["choice_select"]

            if 0 <= choice_index < len(self.current_choices):
                chosen = self.current_choices[choice_index]

                self.waiting_for_choice = False
                self.node_index += 1

                return chosen.get("result")
            
            return None