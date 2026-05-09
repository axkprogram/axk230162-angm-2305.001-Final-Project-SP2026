import pygame

from engine.controller import EngineController
from state.game_state import GameState
from scene.scene_manager import SceneManager
from data.scenes.forest_intro import forest_intro_scene

WIDTH = 800
HEIGHT = 600
FPS = 60

class GameLoop:
    """
    Minimal Pygame loop for VN MVP.
    """
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("VN MVP")

        FPS = 60

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("arial", 28)
        self.small_font = pygame.font.SysFont("arial", 22)

        # core systems
        self.game_state = GameState()

        self.scene_manager = SceneManager()
        self.scene_manager.load_scene(forest_intro_scene)

        self.controller = EngineController(self.game_state)
        self.controller.register_scene_system(self.scene_manager)

        # boot first line
        self.controller.update({})
    
    # Input
    def handle_input(self):
        input_data = {}

        for event in pygame.event.get():

            # close window
            if event.type == pygame.QUIT:
                self.controller.stop()

            # advance dialogue
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    input_data["advance"] = True

                # choice selection: 1, 2, 3 keys
                elif event.key == pygame.K_1:
                    input_data["choice"] = 0
                elif event.key == pygame.K_2:
                    input_data["choice"] = 1
                elif event.key == pygame.K_3:
                    input_data["choice"] = 2

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    input_data["advance"] = True

        return input_data
        
    
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

    # Render
    def render(self):
        self.screen.fill((0, 0, 0))

        ui = self.controller.ui_state

        # dialogue
        if ui["mode"] == "dialogue":
            speaker = self.font.render(
                ui["speaker"], True, (255,255,255)
            )
            self.screen.blit(speaker, (50, 400))

            wrapped = self.wrap_text(ui["text"], 700)

        # dialogue box
        pygame.draw.rect(
            self.screen,
            (40, 40, 60),
            (50, 400, 700, 170)
        )

        if ui["mode"] == "dialogue":
            speaker = self.font.render(
                ui["speaker"],
                True,
                (255, 220, 100)
            )
            text = self.small_font.render(
                ui["text"],
                True,
                (255, 255, 255)
            )

            self.screen.blit(speaker, (70, 420))
            self.screen.blit(text, (70, 470))

        elif ui["mode"] == "choice":
            y = 350

            for i, choice in enumerate(ui["choices"]):
                label = f"{i+1}, {choice['text']}"

                text_surface = self.small_font.render(
                    label,
                    True,
                    (255, 255, 255)
                )

                self.screen.blit(text, (50, y))
                y += 40
        
        hp_text = self.small_font.render(
            f"HP: {self.game_state.player_hp}",
            True,
            (255,255,255)
        )

        self.screen.blit(hp_text, (20, 20))

        wrapped = self.wrap_text(
            ui["text"],
            self.small_font,
            700
        ) or []

        y = 450
        for line in wrapped:
            text_surface = self.small_font.render(line, True, (255,255,255))
            self.screen.blit(text_surface, (20, y))
            y += 30

        pygame.display.flip()

    # Main Loop
    def run(self):

        while self.controller.running:
            input_data = self.handle_input()

            self.controller.update(input_data)

            self.render()

            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    GameLoop().run()