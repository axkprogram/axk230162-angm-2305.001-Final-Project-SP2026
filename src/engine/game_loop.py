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
    
    # Main loop
    def run(self):
        while self.running and self.controller.running:

            # Input
            input_data = self.get_input()

            if input_data["quit"]:
                self.running = False
                self.controller.stop()
                break

            # Engine update (Core link)
            self.controller.update(input_data)

            # TEMP Visual debug (no assets yet)
            self.screen.fill((20,20,20))
            pygame.display.flip()

            self.clock.tick(self.fps)

            
