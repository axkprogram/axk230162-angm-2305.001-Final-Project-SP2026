import pygame

from engine.controller import EngineController
from state.game_state import GameState


class GameLoop:
    """
    Runs the Pygame loop and connects input to controller to systems.
    """

    