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
                "trigger_event": node.get("event_id")
            }
        
        # Battle
        elif node_type == "battle":
            self.node_index += 1
            return {
                "start_combat": node.get("battle_id")
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
            
            # Inject the branch into scene flow
            self.scene_data = (
                self.scene_data[:self.node_index + 1]
                + branch
                + self.scene_data[self.node_index + 1:]
            )

            self.node_index += 1
            return None
        
        # Transition
        elif node_type == "transition":
            return {
                "action": "change_scene",
                "target": node.get("target_scene")
            }
    
        return None
    

    # Choice handling
    def _handle_choice(self, input_data, game_state):
        """
        Handles player selection from choices.
        minimum logic for now
        """

        if "choice_select" not in input_data:
            return None
        
        index = input_data["choice_select"]

        if 0 <= index < len(self.current_choices):
            chosen = self.current_choices[index]

            self.waiting_for_choice = False
            self.node_index += 1

            return chosen.get("result", {})
        
        return None
    
    # Condition Evaulator
    def _evaluate_condition(self, condition, game_state):
        """
        Simple evaluator for now
        can be expanded later into full expression system
        """

        # {"has item": "talisman"}
        if "has_item" in condition:
            return game_state.has_item(condition["has_item"])
        
        # {"flag": "bell_heard_truth"}
        if "flag" in condition:
            return game_state.get_flag(condition["flag"])
        
        # {"route": "dark"}
        if "route" in condition:
            return game_state.route_state == condition["route"]
        
        # {"party_alignment": "rio"}
        if "party_alignment" in condition:
            return (
                game_state.party_alignment
                == condition["party_alignment"]
            )
        
        return False