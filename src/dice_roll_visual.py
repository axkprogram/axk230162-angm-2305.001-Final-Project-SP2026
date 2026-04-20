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

# 2 second animation
def animate_roll():
    start_time = time.time()
    duration = 2 # seconds

    temp_roll = 1

    while time.time() - start_time < duration:
        temp_roll = random.randint(1,20)
        draw(temp_roll, "")
        pygame.time.delay(50)

    return temp_roll

# main loop
running = True
current_roll = None
outcome = ""

while running:
    draw(current_roll, outcome)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # animation first
                current_roll = animate_roll()

                # final logic roll (from your system)
                current_roll, outcome = story_roll()
    
    clock.tick(60)

pygame.quit()