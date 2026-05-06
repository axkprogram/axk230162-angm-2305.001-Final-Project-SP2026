from ui.button import Button

class ChoiceManager:
    def __init__(self):
        self.choices = []

    def set_choices(self, choices):
        self.choices = choices

    def pick(self, index):
        if 0 <= index < len(self.choices):
            self.choices[index][1]()
            self.choices = []