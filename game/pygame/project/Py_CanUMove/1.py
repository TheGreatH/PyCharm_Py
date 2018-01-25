import pygame
from sys import *
import random
from pygame.locals import *
import math

LENGTH = 600
WIDTH = 480
screen = pygame.display.set_mode((LENGTH,WIDTH),0,32)
time = pygame.time.Clock()

class rect(object):
    def __init__(self, pos, leight, width, color, vect):
        self.pos = pos
        self.leight = leight
        self.width = width
        self.color = color
        self.vect = vect
        self.centerx = pos[0] + leight/2
        self.centery = pos[1] + width/2

    def move(self):
        self.pos[0] = self.pos[0] + self.vect[0]
        self.pos[1] = self.pos[1] + self.vect[1]

        if self.pos[0] > LENGTH - self.leight or self.pos[0] < 0:
            self.vect[0] *= -1
        if self.pos[1] > WIDTH - self.width or self.pos[1] < 0:
            self.vect[1] *= -1

        pygame.draw.rect(screen, self.color, Rect((self.pos[0], self.pos[1]),(self.leight, self.width)))

def collision(r, l, h, pos1, pos2):
    x = abs(pos1[0] - pos2[0])
    y = abs(pos1[1] - pos2[1])
    if(((r + l/2) < x) or ((r + h/2) < y)) and (math.sqrt(x**2 + y**2)<(r+math.sqrt((l/2)**2 + (h/2)**2))):
        return "False"
    else:
        return "Ture"
pygame.init()
rect1 = rect([0,0],100,150,(0,0,0),[3,3])
rect2 = rect([360,0],120,140,(0,0,0),[-2,3])
rect3 = rect([0,280],60,100,(0,0,0),[3,-1])
rect4 = rect([450,400],150,80,(0,0,0),[-3,-3])
x,y = 0,0
color = (0,0,0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    time.tick(50)
    screen.fill((255,255,255))
    posx,posy = pygame.mouse.get_pos()
    x += int((posx - x) * 0.05)
    y += int((posy - y) * 0.05)
    rect1.move()
    rect2.move()
    rect3.move()
    rect4.move()
    if collision(20,rect1.width,rect1.leight,(rect1.centerx,rect1.centery),(x,y)):
        color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    pygame.draw.circle(screen,color,(x,y),20)

    pygame.display.update()
