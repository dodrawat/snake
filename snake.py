import pygame
from pygame.locals import *

pygame.init()

width = 640
height = 480
screen = pygame.display.set_mode((width, height))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


class Snake(object):
    def __init__(self, color, length):
        self.color = color
        self.length = length
        self.body = [(width // 2, height // 2)]
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.body.append((self.body[-1][0] + 10, self.body[-1][1]))
        elif self.direction == "left":
            self.body.append((self.body[-1][0] - 10, self.body[-1][1]))
        else:
            raise ValueError("Invalid direction")

    def draw(self, screen):
        for i in range(len(self.body)):
            pygame.draw.rect(screen, self.color, (self.body[i][0], self.body[i][1], 10, 10))

class Food(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 10))


        running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elifry