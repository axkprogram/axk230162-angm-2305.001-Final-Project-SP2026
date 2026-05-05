class StoryNode:
    def __init__(self, text, choices=None):
        self.text = text
        self.choices = choices or []

class Choice:
    def __init__(self, text, next_node):
        self.text = text
        self.next_node = next_node

# Ending nodes
ending_good = StoryNode("You saved the village. The end.")
ending_bad = StoryNode("The village was destroyed. The end.")

# Branches
fight = StoryNode("You chose to fight!", [Choice ("keep fighting", ending_good), Choice("Run away", ending_bad)])

run = StoryNode("You ran away safely. The end.")

# Start Node
start = StoryNode("A dragon attacks your vilalge!", [
    Choice("fight the dragon", fight), Choice("Run away", run)
])
