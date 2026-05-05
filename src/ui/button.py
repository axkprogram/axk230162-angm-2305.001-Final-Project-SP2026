import pygame

class Button:
    def __init__(self, rect, text, action):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.action = action

    def draw(self, screen, font):
        pygame.draw.rect(screen, (100,100,100), self.rect)
        txt = font.render(self.text, True (255,255,255))
        screen.blit(txt, (self.rect.x + 10,self.rect.y + 10))
