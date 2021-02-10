import pygame
import math
from ImageGrid import ImageGrid


class Agent:

    def __init__(self):
        self.pos = [450, 450]
        self.orientation = 0
        self.image = pygame.image.load("agent.png").convert_alpha()
        self.circle = pygame.draw.circle(self.image, (255, 0, 0), [8, 2], 3)
        self.sensors = ImageGrid()

    def image_pos(self):
        return [self.pos[0] - 8, self.pos[1]-8]

    def move(self, keys):
        step = 0.1
        if keys[pygame.K_LEFT]:
            self.orientation += step
            self.draw_circle()
        if keys[pygame.K_RIGHT]:
            self.orientation += -step
            self.draw_circle()
        if keys[pygame.K_UP]:
            self.move_forward(True)
        if keys[pygame.K_DOWN]:
            self.move_forward(False)

    def move_forward(self, forward):
        step = 0.1
        if forward:
            self.pos[0] -= step * math.sin(self.orientation * math.pi / 180)
            self.pos[1] -= step * math.cos(self.orientation * math.pi / 180)
        else:
            self.pos[0] += step * math.sin(self.orientation * math.pi / 180)
            self.pos[1] += step * math.cos(self.orientation * math.pi / 180)

    def draw_circle(self):
        rad = 3
        x = -rad * math.sin(self.orientation * math.pi / 180)
        y = -rad * math.cos(self.orientation * math.pi / 180)
        self.image = pygame.image.load("agent.png").convert_alpha()
        self.circle = pygame.draw.circle(self.image, (255, 0, 0), [8 + x, 8 + y], 3)

    def get_lines(self):
        X, Y = self.sensors.create_sensor_lines(self.pos, 20, self.orientation)
        return [(x, y) for x,y in zip(X,Y)]