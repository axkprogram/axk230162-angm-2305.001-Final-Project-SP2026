# main.py
import pygame

from engine.game_state import GameState
from engine.scene_manager import SceneManager
from engine.dialogue import DialogueManager
from engine.choice import ChoiceManager
from engine.combat import CombatSystem
from ui.textbox import Textbox
from ui.ui_manager import UIManager

# init

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visual Novel Engine")

clock = pygame.time.Clock()

# Core systems

state = GameState
dialogue = DialogueManager
choices = ChoiceManager
combat = CombatSystem

scene = SceneManager(state, dialogue, choices, combat)

# UI System

textbox = Textbox(WIDTH, HEIGHT)
ui = UIManager(textbox, choices)

# Game Loop
running = True

while running:
    screen.fill((0,0,0))

    mouse_pos = pygame.mouse.get_pos()

    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Dialogue advance
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dialogue.advance()

        # Choice selection
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in choices.choices:
                if button in choices.choices:
                    if button.rect.collidepoint(event.pos):
                        result = button.action()

                        # optional debug
                        if result == "BELL TRIGGER":
                            print("Bell event triggered")

# Game logic update

scene.update()

# Ui update

ui.update(mouse_pos, choices.choices)

# Draw UI

current_text = dialogue.get_current()

ui.draw (
    screen, 
    current_text,
    choices.choices
)

# Flip screen

pygame.display.flip()
clock.tick(60)