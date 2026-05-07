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