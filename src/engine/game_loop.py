import pygame

from engine.controller import EngineController
from state.game_state import GameState
from scene.scene_manager import SceneManager

# Temp scene import
from data.scenes.forest_intro import forest_intro_scene


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

        # System set up
        scene_system = SceneManager()

        #register system
        self.controller.register_scene_system(scene_system)

        # Load first scene
        self.controller.scene_system.load_scene(forest_intro_scene)

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
            "keys": [],
            "choice_select": None
        }

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                input_data["quit"] = True

            elif event.type == pygame.KEYDOWN:

                # quit short cut
                if event.key == pygame.K_ESCAPE:
                    input_data["quit"] = True

                # Choice selection
                if pygame.K_1 <= event.key <= pygame.K_9:
                    input_data["choice_select"] = event.key - pygame.K_1

                # Advance dialogue (Space)
                if event.key == pygame.K_SPACE:
                    input_data["advance"] = True

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

            # Update engine
            self.controller.update(input_data)

            # render (debug only)
            self.render()

            self.clock.tick(self.fps)

        pygame.quit()

    # Temp rendering layer

    def render(self):
        self.screen.fill((20,20,20))

        ui = self.controller.ui_state
        font = pygame.font.SysFont("Arial", 20)

        y = 50

        # Dialogue mode
        if ui["mode"] == "dialogue":
            speaker = font.render(f"{ui['speaker']}:", True, (255, 220, 120))
            self.screen.blit(speaker, (50, y))
            y += 30

            for line in ui["text"].splite("\n"):
                text = font.render(line, True, (230, 230, 230))
                self.screen.blit(text, (50, y))
                y += 25

        # Choice Mode
        elif ui ["mode"] == "choice":
            title = font.render("Choose:", True, (200, 200, 255))
            self.screen.blit(title, (50, y))
            y += 40

            for i, choice in enumerate(ui["choices"]):
                text = font.render(
                    f"{i+1}. {choice['text']}",
                    True,
                    (220, 220, 220)
                )
                self.screen.blit(text, (50,y))
                y += 25
        
        pygame.display.flip()