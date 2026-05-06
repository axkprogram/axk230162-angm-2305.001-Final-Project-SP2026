import pygame

class Textbox:
    def __init__(self, screen_width, screen_height):
        self.rect = pygame.Ract(
            50, 
            screen_height - 180,
            screen_width - 100,
            150
        )

        self.font = pygame.font.SysFont(None, 32)

    def draw(self, screen, text):
        # back panel
        pygame.draw.rect(screen, (20,20,20), self.rect)
        pygame.draw.rect(screen, (200,200,200), self.rect, 2)

        # text rendering
        rendered = self.font.render(text, True, (255,255,255))
        screen.blit(rendered, (self.rect.x +20, self.rect.y +20))