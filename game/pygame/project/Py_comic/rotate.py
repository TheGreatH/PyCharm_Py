import pygame,math
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,300),0,32)
man_pic = "name.png"
sky_pic = "sky.png"
background = pygame.image.load(sky_pic).convert()
sprit = pygame.image.load(man_pic).convert_alpha()
weight, height = background.get_size()
screen = pygame.display.set_mode((weight,height),0,32)
sprit = pygame.transform.smoothscale(sprit,(200,50))

time = pygame.time.Clock()
angle = 0

def get_angle(angle):
    return angle % 360
x,y = 0.0,0.0

screen.blit(background, (0, 0))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255, 255, 255))
    time.tick(50)
    angle = get_angle(angle + 1)

    pygame.draw.circle(screen,(255,255,255),(weight/2,height/2),10)
    old_x,old_y = x,y
    x = math.sin(math.radians(angle)) * 100
    y = math.cos(math.radians(angle)) * 100
    s = pygame.transform.rotate(sprit, angle)
    w, h = s.get_size()
    screen.blit(s, (x -w/2+ weight/2, y -h/2+ height/2))
    pygame.display.update()