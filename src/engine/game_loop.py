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

        