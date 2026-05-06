# scene manager

class SceneManager:
    def __init__(self, state, dialogue, choice, combat):
        self.state = state
        self.dialogue = dialogue
        self.choice = choice
        self.combat = combat

        self.current_scene = "intro"