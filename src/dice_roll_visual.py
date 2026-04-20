import pygame
import random
import time

pygame.init()

# screen set up
width, height = 500, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Roll for Fate")

font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)

def roll_d20():
    return random.randint(1,20)

def get_outcome(roll):
    

pygame.quit()