class SceneManager:
    """
    Full VN Script Interpreter

    Executes node-based scenes:
    dialogue, choice, event, battle, state, conditional.
    """

    def __init__(self):
        self.scene_data = None
        self.node_index = 0

        # temp runtime state
        self.waiting_for_choice = False
        self.current_choices = []

        self.active_branch = None # used for conditionals

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
            return self._handle_choice(input_data, game_state)
        
        # Get current node
        if self.node_index >= len(self.scene_data):
            return {"end_scene": True}
        
        node = self.scene_data[self.node_index]

        node_type = node.get("type")

        # Dialogue node
        if node_type == "dialogue":
            self.node_index += 1
            return {
                "action": "dialogue",
                "speaker": node.get("speaker"),
                "text": node.get("text")
            }
        
        # Choice node
        elif node_type == "choice":
            self.waiting_for_choice = True
            self.current_choices = node.get("options", [])

            return {
                "action": "choice",
                "options": self.current_choices
            }
        
        # Event Trigger node
        elif node_type == "event":
            self.node_index += 1
            return {
                "action": "event",
                "event_id": node.get("event_id")
            }
        
        # Battle
        elif node_type == "battle":
            self.node_index += 1
            return {
                "action": "battle",
                "battle_id": node.get("battle_id")
            }
        
        # State Change
        elif node_type == "state":
            self.node_index += 1

            changes = node.get("set", {})
            for key, value in changes.items():
                setattr(game_state, key, value)

            return {
                "action": "state_change",
                "changes": changes
            }
        
        # Conditional
        elif node_type == "conditional":
            condition = node.get("if", {})
            result = self._evaluate_condition(condition, game_state)

            if result:
                branch = node.get("true", [])
            else:
                branch = node.get("false", [])
            
            # Inject the branch


    # Choice handling
    def _handle_choice(self, input_data, game_state):
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