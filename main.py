#coding=utf-8

import sys
import pygame
#-------------------------------------------
pygame.init()
size = width, height = 480, 960
screen = pygame.display.set_mode(size)
color = (255, 255, 255)
clock = pygame.time.Clock()

plane = pygame.image.load("plane.png")
plane_rect = plane.get_rect()

plane_d = [0, 930]
plane_rect = plane_rect.move(plane_d)
#-------------------------------------------
while True:
    clock.tick(60)
    temp = plane_d #改变前坐标
    pressed = pygame.key.get_pressed() #获得所有键盘按钮的状态
    #print(pressed[pygame.K_RIGHT])  #DEBUG
    if pygame.key.get_focused():  #判断按键操作
        if pressed[pygame.K_RIGHT]:
            plane_d[0] +=4
            plane_rect = plane_rect.move(4,0)
        elif pressed[pygame.K_LEFT]:
            plane_d[0] -=4
            plane_rect = plane_rect.move(-4,0)
        print(plane_d)
    #检查关闭点击
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    screen.fill(color)
    screen.blit(plane, plane_rect)
    pygame.display.flip()
#-------------------------------------------
