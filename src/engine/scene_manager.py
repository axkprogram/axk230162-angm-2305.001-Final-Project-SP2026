# scene manager

class SceneManager:
    def __init__(self, state, dialogue, choice, combat):
        self.state = state
        self.dialogue = dialogue
        self.choice = choice
        self.combat = combat

        self.scene = "intro"
        self.substate = None

# Main update Loop

def update(self):

    if self.scene == "intro":
        self.intro()

    elif self.scene == "fork":
        self.cave_fork()
    
    elif self.scene == "fighter_path":
        self.fighter_path()

    elif self.scene == "mage_path":
        self.mage_path()

    elif self.scene == "dark_path":
        self.dark_path()

    elif self.scene == "combat_hound":
        self.combat_hound()

    elif self.scene == "combat_specter":
        self.combat_specter()

    elif self.scene == "combat_strange":
        self.combat_strange()

    elif self.scene == "return_fork":
        self.return_fork()

    elif self.scene == "end":
        self.end_scene()

# Intro

def intro(self):
    self.dialogue.start([
        "Dust settles around you."
        "The cave is quiet... too quiet."
        "Ahead, faint light splits into three directions."
    ])

    self.choice.set_choices([
        ("Stand up", self.to_fork)
    ])

def to_fork(self):
    self.scene = "fork"

# Cave Fork

def cave_fork(self):
    self.dialogue.start([
        "The tunnel opens into a wide chamber.",
        "Three paths stretch forward."
    ])

    self.choice.set_choices([
        ("Follow Fighter (Gravel Path)", self.to_fighter), 
        ("Follow Mage (Stone Path)", self.to_mage),
        ("Take Dark Path", self.to_dark)
    ])

def to_fighter(self):
    self.scene = "fighter_path"

def to_mage(self):
    self.scene = "mage_path"

def to_dark(self):
    self.scene = "dark_path"

# Fighter Path
def fighter_path(self):
    self.dialogue.start([
        "The gravel path crunches underfoot.",
        "The Fighter scans ahead, alert."
    ])

    # trigger combat once
    if not self.state.get_flag("hound_fight_done"):
        self.scene + "combat_hound"
    else:
        self.scene = "return_fork"

# Mage Path
def mage_path(self):
    self.dialogue.start([
        "Stone carvings line the walls.",
        "The Mage studies them with quiet focus."
    ])

    if not self.state.get_flag("specter_fight_done"):
        self.scene = "combat_specter"
    else:
        self.scene = "return_fork"

# Dark Path
def dark_path(self):
    self.dialogue.start([
        "The air grows heavier.",
        "The path feels... aware of you."
    ])

    if not self.state.get_flag("strange_fight_done"):
        self.scene = "combat_strange"
    else:
        self.scene = "return_fork"

# Combat wrappers
def combat_hound(self):
    result = self.combat.update()

    if result == "WIN":
        self.state.set_flag("hound_fight_done", True)
        self.scene = "return_fork"
    
    elif result == "LOSE":
        self.scene = "end"

    elif result == "ANNIHILATION":
        self.scene = "end"

def combat_specter(self):
    result = self.combat.update()

    if result == "WIN":
        self.state.set_flag("specter_fight_done", True)
        self.scene = "return_fork"

    elif result == "LOSE":
        self.scene = "end"

    elif result == "ANNIHILATION":
        self.scene = "end"

def combat_strange(self):
    result = self.combat.update()

    if result == "WIN":
        self.state.set_flag("strange_fight_done", True)
        self.scene = "return_fork"

    elif result == "LOSE":
        self.scene = "end"

    elif result == "ANNIHILATION":
        self.scene = "end"

# return after paths
def return_fork(self):
    self.dialogue.start([
        "The three paths converge again deeper inside."
        "Something lingers here... changed"
    ])

    self.choice.set_choices([
        ("Continue deeper", self.to_end)
    ])

def to_end(self):
    self.scene = "end"\
    
# End
def end_scene(self):
    self.dialogue.start([
        "The chamber opens before you.",
        "The chapter ends.. but something remains unresolved."
    ])

    self.choice.set_choices([])