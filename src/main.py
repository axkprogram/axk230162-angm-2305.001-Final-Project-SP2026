# main.py
import pygame

from engine.game_state import GameState
from engine.scene_manager import SceneManager
from engine.dialogue import DialogueManager
from engine.choice import ChoiceManager
from engine.combat import CombatSystem

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

state = GameState()
dialogue = DialogueManager()
choice = ChoiceManager()
combat = CombatSystem(state)

scene = SceneManager(state, dialogue, choice, combat)

running = True

while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dialogue.advance()

            if event.key == pygame.K_1:
                choice.pick(0)
            if event.key == pygame.K_2:
                choice.pick(1)
            if event.key == pygame.K_3:
                choice.pick(2)

    # Core loop
    scene.update()

    font = pygame.font.SysFont(None, 32)

    text = font.render(dialogue.get_current(), True, (255,255,255))
    screen.blit(text, (50, 600))

    pygame.display.flip()
    clock.tick(60)