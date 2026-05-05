import pygame

class Portrait:
    def __init__(self, image_path, pos):
        self.image = pygame.image.load(image_path)
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.image, self.pos)