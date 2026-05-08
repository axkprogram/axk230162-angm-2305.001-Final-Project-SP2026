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
        print("Scene Manager running")
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