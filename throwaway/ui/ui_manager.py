class UIManager:
    def __init__(self, textbox, choice_system):
        self.textbox = textbox
        self.choice_system = choice_system

    def draw(self, screen, dialogue_text, buttons):
        self.textbox.draw(screen, dialogue_text)

        for b in buttons:
            b.draw(screen)

    def update(self, mouse_pos, buttons):
        for b in buttons:
            b.update(mouse_pos)