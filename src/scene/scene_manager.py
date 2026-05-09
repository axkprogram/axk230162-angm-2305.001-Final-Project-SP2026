import random

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

    # Load scene
    def load_scene(self, scene_data):
        self.scene_data = scene_data
        self.node_index = 0
        self. dialogue_index = 0
        self.waiting_for_choice = False
        self.current_choices = []

    # Main Update
    def update(self, input_data, game_state):

        if self.scene_data is None:
            return None        
        
        #end of scene protection
        if self.node_index >= len(self.scene_data):
            return {"end_scene": True}

        #waiting on player choice
        if self.waiting_for_choice:
            return self._handle_choice(input_data, game_state)
        
        node = self.scene_data[self.node_index]

        node_type = node["type"]

        # Dialogue
        if node_type == "dialogue":
            lines = node["lines"]

            #finished this block
            if self.dialogue_index >= len(lines):
                self.dialogue_index = 0
                self.node_index += 1
                return self.update({}, game_state)
            
            current_line = lines[self.dialogue_index]

            #only advance when player clicks /presses space
            if input_data.get("advance"):
                self.dialogue_index += 1

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
                "choices": node ["options"]
            }
        
        # conditional
        elif node_type == "conditional":

            if self._evaluate_condition(node["if"], game_state):
                self.scene_data = (
                    self.scene_data[:self.node_index]
                    + node["true"]
                    + self.scene_data[self.node_index + 1:]
                )
            else:
                self.node_index += 1

            return self.update({}, game_state)
        
        # state change
        elif node_type == "state":
            changes = node.get("set", {})

            for key, value in changes.items():

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
            self.node_index += 1

            return{
                "action": "change_scene",
                "target": node["target_scene"]
            }
        return None
    
    # choice handler
    def _handle_choice(self, input_data, game_state):

        if "choice_select" not in input_data:
            return None
        
        index = input_data["choice_select"]

        if 0 <= index < len(self.current_choices):
            chosen = self.current_choices[index]
            result = chosen.get("result",{})

            #dice mechanic
            if result.get("dice_roll"):
                rolled = random.randint(0, 2)

                chosen = self.current_choices[rolled]
                result = chosen.get("result", {})

                path_names = {
                    0: "right path.",
                    1: "left path.",
                    2: "center path."
                }

                # move past the choice node
                self.waiting_for_choice = False
                self.node_index += 1
                
                return{
                    "action": "dialogue",
                    "speaker": "Narration",
                    "text": f"The die rolls... {rolled + 1}. Carmen decides to take the {path_names[rolled]}",
                    "followup_result": result
                }

            #other set
            if "set" in result:
                for k, v, in result["set"].items():
                    setattr(game_state, k, v)

            self.waiting_for_choice = False
            # self.current_choices = []
            self.node_index += 1

            return result
        
        return None
    
    # condition evaluator
    def _evaluate_condition(self, condition, game_state):

        for key, value in condition.items():
            return getattr(game_state, key, None) == value
        
        return False
    
    # stop scene
    def stop(self):
        self.scene_data = None
        self.node_index = 0
        self.dialogue_index = 0
        self.waiting_for_choice = False
        self.current_choices = []