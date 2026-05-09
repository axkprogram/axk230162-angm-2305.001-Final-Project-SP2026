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
        self.current_choice = []

    # Load scene
    def load_scene(self, scene_data):
        self.scene_data = scene_data
        self.node_index = 0
        self. dialogue_index = 0
        self.waiting_for_choice = False
        self.current_choice = []

        
