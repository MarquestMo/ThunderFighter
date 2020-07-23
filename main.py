#coding=utf-8

import sys
import pygame
#-------------------------------------------
pygame.init()
size = width, height = 480, 960
screen = pygame.display.set_mode(size)
color = (255, 255, 255)

plane = pygame.image.load("plane.png")
plane_rect = plane.get_rect()

#-------------------------------------------
while True:
    #检查关闭点击
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.show()
#-------------------------------------------
