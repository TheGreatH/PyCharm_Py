import sys
import pygame
import random
from pygame.locals import *

SCREEN_SIZE = (640,800)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

print type(screen)

rect1 = Rect(0, 0, 100, 100)
rect2 = (100, 0, 100, 100)
print type(rect1),type(rect2)
while True:
    event = pygame.event.poll()
    if event.type == QUIT:
        print tuple(screen.get_clip())
        print type(rect1), type(rect2)
        sys.exit()
    elif event.type == MOUSEBUTTONDOWN:
        while event.type != MOUSEBUTTONUP:
            event = pygame.event.poll()
            pos = pygame.mouse.get_pos()
            screen.set_at(pos, (255, 255, 255))
            pygame.display.update()
            for i in range(10):
                screen.set_at(tuple((random.randint(0 ,600)) for x in range(2)), tuple((random.randint(0 ,255)) for x in range(3)))

    # pygame.draw.rect(screen, (255, 255, 255), rect1, 1)
    # pygame.draw.rect(screen, (255, 255, 255), rect2, 1)
    screen.blit(screen,rect2)
    pygame.display.update()