# testing

import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("VN RPG Test Window")

    clock = pygame.time.Clock()
    running = True
    
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        # BG color
        screen.fill((20,20,20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()