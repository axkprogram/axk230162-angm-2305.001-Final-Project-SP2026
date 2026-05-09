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
            if event.type == pygame.QUIT:
                self.controller.stop()

            if event.type == pygame.KEYDOWN:

               # advance dialogue
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                   input_data["advance"] = True
                # choices 1-9
                if pygame.K_1 <= event.key <= pygame.K_9:
                   index = event.key - pygame.K_1
                   input_data["choice_select"] = index

        return input_data
    
    # Render
    def render(self):
        self.screen.fill((20, 20, 30))

        ui = self.controller.ui_state

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
            text = self.small_font.rander(
                ui["text"],
                True,
                (255, 255, 255)
            )

            self.screen.blit(speaker, (70, 420))
            self.screen.blit(text, (70, 470))

        elif ui["mode"] == "choice":
            y = 40

            for i, choice in enumerate(ui["choices"]):
                label = f"{i+1}, {choice['text']}"

                text = self.small_font.render(
                    label,
                    True,
                    (200, 255, 200)
                )

                self.screen.blit(text, (70, y))
                y += 40
        
        hp_text = self.small_font.render(
            f"HP: {self.game_state.player_hp}",
            True,
            (255,255,255)
        )

        self.screen.blit(hp_text, (20, 20))

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