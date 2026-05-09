import pygame

from engine.controller import EngineController
from state.game_state import GameState
from scene.scene_manager import SceneManager
from data.scenes.forest_intro import forest_intro_scene

class GameLoop:
    """
    Minimal Pygame loop for VN MVP.
    """

    def __init__(self):
        pygame.init()