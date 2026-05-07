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