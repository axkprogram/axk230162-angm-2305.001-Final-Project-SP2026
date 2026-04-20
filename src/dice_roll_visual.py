import pygame
import random
import time
from roll_for_luck_dice import story_roll

pygame.init()

# screen set up
width, height = 500, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Roll for Fate")

font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)

clock = pygame.time.Clock()

# Drawing time



pygame.quit()