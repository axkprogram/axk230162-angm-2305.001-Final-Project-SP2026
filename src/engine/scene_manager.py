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

    self.choice.set_choice([
        ("Fighter Path", self.to_fighter),
        ("Mage Path", self.to_mage),
        ("Dark Path", self.to_dark)
    ])

def to_fighter(self):
    self.current.scene = "fighter_path"

def to_mage(self):
    self.current.scene = "combat"

def to_dark(self):
    self.current_scene = "combat"

# Combat Entry

def combat_scene(self): 
    if not self.state.in_combat:
        self.state.in_combat = True
        self.combat.start_enemy("hound")

    result = self.combat.update()

    if result == "WIN":
        self.state.in_combat = False
        self.current_scene = "fighter_reward"

    elif result == "LOSE":
        self.state.in_combat = False
        self.current_scene = "game_over"

    elif result == "ANNIHILATION":
        self.state.in_combat = False
        self.current_scene = "bell_event"