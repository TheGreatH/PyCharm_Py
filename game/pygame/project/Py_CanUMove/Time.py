#coding=UTF-8
import pygame
from sys import exit
from pygame.locals import *
import vector2
import math

def collision(r, l, h, pos1, pos2):
    x = abs(pos1.x - pos2.x)
    y = abs(pos1.y - pos2.y)
    if((r + l/2) > x):
        return "False"
    elif ((r + h/2) > x):
        return "False"
    else:
        return "Ture"

pygame.init()
SCREEN_SIZE = (640,400)
font = pygame.font.SysFont("宋体",32)
line_size = font.get_linesize()

screen = pygame.display.set_mode((640,400),0,32)
surface = pygame.Surface((90,line_size))
time = pygame.time.Clock()

tick = 0
sec = 0
min = 0
hour = 0
pos = vector2.vect()
rl = vector2.vect()
vec = vector2.vect(0,0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255, 255, 255))
    x,y = pygame.mouse.get_pos()
    tick += time.tick(50)

    aim = vector2.vect(x,y)
    pos += (aim - pos)*0.05

    if  tick >= 1000:
        tick = 0
        sec += 1
    if sec == 60:
        sec = 0
        min += 1
    if min == 60:
        min = 0
        hour += 1

    pygame.draw.rect((screen),(0,0,0),Rect((rl.x,rl.y),(50,50)),0)
    rl += vec

    if rl.x >= 590 or rl.x < 0:
        vec += vector2.vect(vec.x*-2,0)
    if rl.y >= 350 or rl.y < 0:
        vec += vector2.vect(0, vec.y*-2)

    text = ("%2d:%2d:%2d") % (hour, min, sec)
    surface.fill((255,0,255))
    surface.blit(font.render(text, True, (0, 0, 0)), (0, 0))
    screen.blit(surface,(pos.x,pos.y))
    print("%.2d:%.2d:%.2d")%(hour,min,sec)
    pygame.display.update()





