# scene manager

class SceneManager:
    def __init__(self, state, dialogue, choice, combat):
        self.state = state
        self.dialogue = dialogue
        self.choice = choice
        self.combat = combat

        self.current_scene = "intro"

    def update(self):
        if self.current_scene == "intro":
            self.intro_scene()

        elif self.current_scene == "fork":
            self.fork_scene()

        elif self.current_scene == "fighter_path":
            self.fighter_scene()

        elif self.current_scene == "combat":
            self.combat_scene()


# Intro Scene

def intro_scene(self):
    self.dialogue([
        "You fall into a cave beneath the earth.",
        "Dust settles around you."
    ])

    self.choice.set_choices([
        ("Stand up", self.to_fork)
        ])
    
def to_fork(self):
    self.current_scene = "fork"

# Fork Scene

def fork_scene(self):
    self.dialogue.start([
        "Three paths stretch forward.",
        "One gravel. One stone. One dark."
    ])

