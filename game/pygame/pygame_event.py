#coding= utf-8
import pygame
import sys
from pygame.locals import *

SCREEN_SIZE = (640, 800)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
font = pygame.font.SysFont("宋体", 16)
font_linesize = font.get_linesize()
event_get = []
while True:

    event = pygame.event.wait()
    event_get.append(str(event))
    event_get = event_get[-SCREEN_SIZE[1]/font_linesize:]

    if event.type == QUIT:
        sys.exit()
    screen.fill((255, 255, 255))
    pan_posY = 0
    pan_posX = 0
    for event in event_get[::-1]:
        screen.blit(font.render(event, True, (0, 0, 0)),(pan_posY, pan_posY))
        pan_posY += font_linesize
        pan_posX += 1
    pygame.display.update()