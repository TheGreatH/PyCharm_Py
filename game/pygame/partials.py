import pygame
from pygame.locals import *
from functools import partial
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,400), 0, 32)
lines = partial(pygame.draw.line, screen, (0,0,0),(500, 200))

maxs = partial(max, 10)
print max(10,range(10))
print maxs(range(10))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255,0,255))
    line1 = lines((100, 100))

    pygame.display.update()

