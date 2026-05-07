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

    # Input handling
    def get_input(self):
        """
        Collects raw input events.
        Later this will be expanded into a full input system.
        """
        event = pygame.event.get()
        input_data = {
            "quit": False,
            "keys": []
        }

        for event in events:
            if event.type == pygame.QUIT:
                input_data["quit"] = True

            if event.type == pygame.KEYDOWN:
                input_data["keys"].append(event.key)

        return input_data