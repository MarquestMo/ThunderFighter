#coding=utf-8

import sys
import pygame
from random import randint
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
class enemy:
    def __init__(self):
        """初始化单个敌人"""
        self.d = [randint(0,464),randint(0,800)]
        #self.d = [89,520]
        self.enemy = pygame.image.load("enemy.png") #加载图片
        #self.enemy_rect = self.enemy.get_rect() #获取矩形区域
        #self.enemy_rect.move(self.d)
        #screen.blit(self.enemy, self.enemy_rect)
        
    def move(self, d):
        self.d = d
        
    def up(self):
        temp = [randint(-50,50),randint(-50,50)]
        self.d = [self.d[0]+temp[0],self.d[1]+temp[1]]
        if self.d[0]<0:
            self.d[0] = 0
        elif self.d[0]>464:
            self.d[0] = 464
        if self.d[1]<0:
            self.d[1] = 0
        elif self.d[1]>800:
            self.d[1] = 800
#-------------------------------------------
enemies = []
for i in range(10):   #敌人数量
    enemies.append(enemy()) #初始化实例
    print(enemies[i].d)
del_list = [-1]    #已删除对象的序号

while True:
    clock.tick(120)
    screen.fill(color)
    
    temp = plane_d #改变前坐标
    pressed = pygame.key.get_pressed() #获得所有键盘按钮的状态
    #print(pressed[pygame.K_RIGHT])  #DEBUG
    if pygame.key.get_focused():  #判断按键操作
        if pressed[pygame.K_RIGHT] and plane_d[0]+4<=448:
            plane_d[0] +=4
            plane_rect = plane_rect.move(4,0)
        if pressed[pygame.K_LEFT] and plane_d[0]-4>=0:
            plane_d[0] -=4
            plane_rect = plane_rect.move(-4,0)
        if pressed[pygame.K_UP] and plane_d[1]-4>=0:
            plane_d[1] -=4
            plane_rect = plane_rect.move(0,-4)
        if pressed[pygame.K_DOWN] and plane_d[1]+4<=930:
            plane_d[1] +=4
            plane_rect = plane_rect.move(0,4)
        if pressed[pygame.K_SPACE]:
            #print(plane_d[0]+15,0,plane_d[0],plane_d[1])  #DEBUG
            pygame.draw.line(screen, (204,51,17), (plane_d[0]+16,0),(plane_d[0]+16,plane_d[1]), 2)
            
            for i in range(len(enemies)):
                if enemies[i].d[0]>=plane_d[0]-6 or enemies[i].d[0]<=plane_d[0]+6:
                     del_list.append(i)
        print(len(plane_d)) #DEBUG
    #检查关闭点击
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #print(del_list) #DEBUG
    for i in range(len(enemies)):
        if del_list.count(i)!=1:
            #enemies[i].up()
            screen.blit(enemies[i].enemy, enemies[i].d)
    screen.blit(plane, plane_rect)
    pygame.display.flip()
#-------------------------------------------
