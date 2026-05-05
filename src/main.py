# main.py
import pygame
from config import *
from engine.state import GameState
from engine.dialogue import DialogueManager
from engine.choice import ChoiceManager

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)