import pygame

class EngineController:
    """
    Central brain of the game.
    
    Responsible for:
    - running the main loop
    - switching between systems (scene/ event/ combat)
    - holding references to GameState and systems
    """
    