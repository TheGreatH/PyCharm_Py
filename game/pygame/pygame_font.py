import pygame
import sys
from pygame.locals import *

pygame.init()
SCREEN_SIZE = (600,800)
screen = pygame.display.set_mode(SCREEN_SIZE , 0, 32)
font = pygame.font.SysFont("youyuan",12)
print font.get_linesize()
while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        sys.exit()
    screen.fill((255, 255, 255))
    pos_x = 0
    pos_y = 0
    for i in pygame.font.get_fonts():
        screen.blit(font.render(i, True, (0, 0, 0)),(pos_x, pos_y))
        pos_y += font.get_linesize()
    pygame.display.update()

