import pygame

from engine.controller import EngineController
from state.game_state import GameState


class GameLoop:
    """
    Runs the Pygame loop and connects input to controller to systems.
    """

    def __init__(self):
        pygame.init()

        # Basic window
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("VN RPG Engine")

        self.clock = pygame.time.Clock()
        self.fps = 60

        # Core game objects
        self.game_state = GameState()
        self.controller = EngineController(self.game_state)

        self.running = True

    