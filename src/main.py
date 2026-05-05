# main.py
import pygame
from config import *
from engine.state import GameState
from engine.dialogue import DialogueManager
from engine.choice import ChoiceManager

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

state = GameState()
dialogue = DialogueManager(font)
choices = ChoiceManager(font)

dialogue.start("Welcome to your Visual Novel")

running = True

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        result = choices.handle_event(event)
        if result:
            print("Selected:", result)

    dialogue.update()
    dialogue.draw(screen)
    choices.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)