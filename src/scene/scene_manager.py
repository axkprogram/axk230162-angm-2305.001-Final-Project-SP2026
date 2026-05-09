class SceneManager:
    """
    Minimal VN scene runner.
    
    Responsibilities:
    - Step through scene nodes
    - Evaluate conditions
    - Return simple actions to controller
    """

    def __init__(self):
        self.scene_data = None
        self.node_index = 0

        self.waiting_for_choice = False
        self.current_choices = []

    # Load Scene
    def load_scene(self, scene_data):
        self.scene_data = scene_data
        self.node_index = 0
        self.waiting_for_choice = False
        self.current_choices = []

    # Main update loop
    def update(self, input_data, game_state):

        if not self.scene_data:
            return None
        
        # Handle choice input first
        if self.waiting_for_choice:
            return self._handle_choice(input_data, game_state)
        
        # End of Scene
        if self.node_index >= len(self.scene_data):
            return {"end_scene": True}
        
        node = self.scene_data[self.node_index]
        node_type = node.get("type")

        # Dialogue
        if node_type == "dialogue":
            self.node_index += 1

            #MVP: Flatten lines to show one at a time
            lines = node.get("lines",[])

            if not lines:
                return None
            
            line = lines[0]

            # If multiple lines, reinsert rest
            if len(lines) > 1:
                extra = []
                for 1 in lines [1:]:
                    extra.append({
                        "type": "dialogue",
                        "lines": [1]
                    })

                self.scene_data = (
                    self.scene_data[:self.node_index]
                    + extra
                    + self.scene_data[self.node_index]
                )

            return {
                "action": "dialogue",
                "speaker": line.get("speaker", "Narration"),
                "text": line.get("text", "")
            }
        
        # Choice
        elif node_type == "choice":
            self.waiting_for_choice = True
            self.current_choices = node.get("options", [])

            return {
                "action": "choice",
                "choices": self.current_choices
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
            condition = node.get("if",{})

            result = self._evaluate_condition(condition, game_state)

            branch = node.get("true", []) if result else node.get("false", [])

            # Inject Branch into scene
            self.scene_data = (
                self.scene_data[:self.node_index]
                + branch
                +self.scene_data[self.node_index + 1:]
            )

            return None
        
        # Transition
        elif node_type == "transition":
            target = node.get("target_scene")

            return {
                "action": "change scene",
                "target": target
            }
        
        # unknown node
        self.node_index += 1
        return None
    
    # Choice Handling
    def _handle_choice(self, input_data, game_state):

        if "choice_select" not in input_data:
            return None
        
        index = input_data["choice_select"]

        if 0 <= index < len(self.current_choices):
            chosen = self.current_choices[index]

            self.waiting_for_choice = False
            self.node_index += 1

            return chosen.get("result", {})
        
        return None
    
    # Condition
    def _evaluate_condition(self, condition, game_state):

        # has_item check
        if "has_item" in condition:
            return game_state.has_item(condition["has_item"])
        
        # flag check
        if "flag" in condition:
            return game_state.get_flag(condition["flag"])
        
        # route check
        if "route" in condition:
            return game_state.route_state == condition["route"]
        
        # party alignment
        if "party_alignment" in condition:
            return game_state.party_alignment == condition["party_alignment"]
        
        