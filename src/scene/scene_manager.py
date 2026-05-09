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
        self.dialogue_index = 0

        self.waiting_for_choice = False
        self.current_choices = []

    # Load Scene
    def load_scene(self, scene_data):
        self.scene_data = scene_data
        self.node_index = 0
        self.dialogue_index = 0
        self.waiting_for_choice = False
        self.current_choices = []

    # Main update loop
    def update(self, input_data, game_state):

        if self.scene_data is None:
            return None
        
        # waiting for player to choose
        if self.waiting_for_choice:
            return self._handle_choice(input_data, game_state)
        
        # end of scene
        if self.node_index >= len(self.scene_data):
            return {"end_scene": True}
        
        node = self.scene_data[self.node_index]
        node_type = node["type"]

        # Dialogue
        if node_type == "dialogue":
            lines = node["lines"]

            current_line = lines[self.dialogue_index]

            #only advance on click / space
            if input_data.get("advance"):
                self.dialogue_index += 1

                if self.dialogue_index >= len(lines):
                    self.dialogue_index = 0
                    self.node_index += 1
            
            return {
                "action": "dialogue",
                "speaker": current_line["speaker"],
                "text": current_line["text"]
            }
        
        # Choice
        elif node_type == "choice":
            self.waiting_for_choice = True
            self.current_choices = node["options"]

            return {
                "action": "choice",
                "choices": [
                    c["text"] for c in self.current_choices
                ]
            }
        
        # Conditional
        elif node_type == "conditional":

            if self._evaluate_condition(
                node["if"],
                game_state
            ):
                # replace current node with true branch
                self.scene_data[
                    self.node_index:self.node_index + 1
                ] = node["true"]
            else:
                self.node_index += 1

            return self.update({}, game_state)
        
        #State Change
        elif self.node_index == "state":
            changes = node.get("set", {})

            for key, value in changes.items():

                #damage/healing support
                if hasattr(game_state, key) and isinstance(value, int):
                    current = getattr(game_state, key)

                    if value < 0:
                        setattr(game_state, key, current + value)
                    else:
                        setattr(game_state, key, value)
                else:
                    setattr(game_state, key, value)

            self.node_index += 1

            return {
                "action": "state_change",
                "changes": changes
            }
        
        # transition
        elif node_type == "transition":
            return {
                "action": "change_scene",
                "target": node["target_scene"]
            }
        
        return None
    
    #Choice handler
    def _handle_choice(self, input_data, game_state):

        if "choice" not in input_data:
            return None
        
        index = input_data["choice"]
        
        if 0 <= index < len(self.current_choices):
            chosen = self.current_choices[index]

            self.waiting_for_choice = False
            self.node_index += 1

            result = chosen.get("result", {})

            if "set" in result:
                for k, v, in result["set"].items():
                    setattr(game_state, k, v)

            return result
        
        return None
    
    # Condition evaluator
    def _evaluate_condition(self, condition, game_state):

        if "has_item" in condition:
            return game_state.has_item(
                condition["has_item"]
            )
        
        if "flag" in condition:
            return game_state.get_flag(
                condition["flag"]
            )
        
        if "route" in condition:
            return (
                game_state.route_state
                == condition["route"]
            )
        
        if "party_alignment" in condition:
            return (
                game_state.party_alignment
                == condition["party_alignment"]
            )
        
        # generic key/value
        for key, value in condition.items():
            return (
                getattr(game_state, key, None)
                == value
            )
        
        return False
    
    # stop scene
    def stop(self):
        self.scene_data = None
        self.node_index = 0
        self.dialogue_index = 0
        self.waiting_for_choice = False
        self.current_choices = []
