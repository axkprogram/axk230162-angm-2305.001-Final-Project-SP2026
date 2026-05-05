class StoryNode:
    def __init__(self, text, choices=None):
        self.text = text
        self.choices = choices or []
        
