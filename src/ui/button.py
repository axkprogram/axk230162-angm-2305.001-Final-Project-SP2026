import pygame

class Button:
    def __init__(self, rect, text, action):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.action = action

        self.font = pygame.font.SysFont(None, 28)
        self.hovered = False

    def draw(self, screen):
        color = (80,80,80) if not self.hovered else (120,120,120)

        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)

        text_surface = self.font.render(self.text, True, (255,255,255))
        screen.blit(
            text_surface
            (self.rect.x +10, self.rect.y +10)
        )

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def click(self):
        if self.hovered:
            return self.action