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
def draw(roll, outcome):
    screen.fill((30,30,30))

    # Outcome text
    if outcome:
        text = small_font.render(outcome.upper(), True, (255,255,255))
        screen.blit(text, (width//2 - text.get_width()//2,50))
    
    # Dice box
    pygame.draw.rect(screen, (220, 220, 220), (200,150,100,100))

    # Number
    if roll:
        num = font.render(str(roll), True, (0,0,0))
        screen.blit(num, (250 - num.get_width()//2, 200 - num.get_height()//2))
    
    pygame.display.flip()



pygame.quit()