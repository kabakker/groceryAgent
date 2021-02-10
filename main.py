import matplotlib.pyplot as plt
import pygame
from Agent import Agent
#from movement_functions import *

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
bg_image = pygame.image.load("store.png").convert()

agent = Agent()

# Run until the user asks to quit
running = True
while running:

    screen.blit(bg_image, [0, 0])
    screen.blit(agent.image, agent.image_pos())

    keys = pygame.key.get_pressed()
    agent.move(keys)
    xy = agent.get_lines()
    pygame.draw.lines(screen, (0, 255, 0), False, xy)

    screen.blit(agent.image, agent.image_pos())

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.

pygame.quit()
