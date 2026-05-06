import pygame
class CombatUI:
    def __init__(self, state, combat):
        self.state = state
        self.combat = combat

        self.font = pygame.font.SysFont(None, 28)
        self.big_font = pygame.font.SysFont(None, 36)

        self.buttons = []
        self.create_buttons()

    # Button setup
    def create_button(self):
        self.buttons = [
            {"label": "Slash", "rect": pygame.Rect(100, 550, 150, 50), "action": "dagger"},
            {"label": "Spell"}
        ]