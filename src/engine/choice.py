from ui.button import Button

class ChoiceManager:
    def __init__(self, font):
        self.buttons = []
        self.font = font

    def set_choices(self, choices):
        self.buttons = []
        y = 400
        for text, action, in choices :
            self. buttons.append(Button((100, y, 400, 50), text, action))
            y += 70

    def draw(self, screen):
        for b in self.buttons:
            b.draw(screen, self.font)