import pygame

from engine.controller import EngineController
from state.game_state import GameState
from scene.scene_manager import SceneManager
from data.scenes.registry import SCENE_REGISTRY

# screen constants
WIDTH = 800
HEIGHT = 600
FPS = 60

class GameLoop:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minimum Playable Slice VN")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(None, 36)
        self.small_font = pygame.font.SysFont(None, 28)

        # systems
        self.game_state = GameState()

        self.scene_manager = SceneManager()
        self.scene_manager.load_scene(
            SCENE_REGISTRY["forest_intro"]
        )

        self.controller = EngineController(
            self.game_state
        )

        self.controller.register_scene_system(
            self.scene_manager
        )

        # load first dialogue immediately
        self.controller.update({})

    # Input
    def handle_input(self):
        input_data = {}

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self. controller.stop()

            elif event.type == pygame.KEYDOWN:

                #advance dialogue
                if event.key == pygame.K_SPACE:
                    input_data["advance"] = True

                #choices 1/2/3
                elif event.key == pygame.K_1:
                    input_data["choice_select"] = 0

                elif event.key == pygame.K_2:
                    input_data["choice_select"] = 1

                elif event.key == pygame.K_3:
                    input_data["choice_select"] = 2

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    input_data["advance"] = True

        return input_data
    
    # text wrapping
    def wrap_text(self, text, max_width):

        words = text.split()
        lines = []
        current = ""

        for word in words:
            test = current + word + " "

            if self.small_font.size(test)[0] <= max_width:
                current = test
            else:
                lines.append(current)
                current = word + " "

        lines.append(current)
        return lines
    
    #render
    def render(self):
        
        self.screen.fill((20, 20, 30))

        ui = self.controller.ui_state

        #dialogue box
        pygame.draw.rect(
            self.screen,
            (40, 40, 40),
            (20, 400, 760, 180)
        )

        # dialogue
        if ui["mode"] == "dialogue":

            speaker = self.font.render(
                ui["speaker"],
                True,
                (255, 255, 0)
            )
            self.screen.blit(speaker, (40, 420))

            wrapped = self.wrap_text(
                ui["text"],
                700
            )

            y = 470
            for line in wrapped:
                text_surface = self.small_font.render(
                    line,
                    True,
                    (255, 255, 255)
                )
                self.screen.blit(
                    text_surface,
                    (40, y)
                )
                y += 30
        
        # choice
        elif ui["mode"] == "choice":

            y = 440

            for i, choice in enumerate(ui["choices"]):
                label = f"{i+1}. {choice['text']}"

                text_surface = self.small_font.render(
                    label,
                    True,
                    (255, 255, 255)
                )

                self.screen.blit(
                    text_surface,
                    (40, y)
                )

                y += 40

        pygame.display.flip()

    # Main Loop
    def run(self):

        while self.controller.running:

            input_data = self.handle_input()

            self.controller.update(
                input_data
            )

            self.render()

            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    GameLoop().run()