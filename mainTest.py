#-*-coding:utf8;-*-

import sys
import pygame
import math as m
import matplotlib.pyplot as plt
import time as t
#--------------------------------------------------
def Length2XY(r,a):
    '''
    弧长转平面直角坐标，r为半径，a为弧长/π
    '''
    r=r #旋转半径
    x=0 #起始坐标
    y=0 #起始坐标
    a=a*m.pi #路程（弧长）
    lengths=2*r*0.25*m.pi #1/4圆弧长
    #time=1000 #前进时间（秒）
    #speed=lengths/time #前进速度（单位长度/秒）
    #a=speed*(i+1)
    x=r*m.cos(m.radians((180*a)/(m.pi*r)))
    y=r*m.sin(m.radians((180*a)/(m.pi*r)))
    return (x,y)
#--------------------------------------------------
def rotate_cen(ima,imar,angle):
    newIma = pygame.transform.rotate(ima, angle)
    # 校正旋转图片的中心点
    ImaRect = newIma.get_rect(center=imar.center)
    #画框矫正
    newRect = newIma.get_rect()
    pygame.draw.rect(screen, (255, 0, 0), ImaRect, 1)
    pygame.draw.rect(screen, (0, 255, 0), newRect, 1)
    #画框矫正
    return (newIma, ImaRect)
#--------------------------------------------------
pygame.init()  #初始化pygame
size = width, height = 240, 480
color = (255,200,200) #背景颜色
screen = pygame.display.set_mode(size)  #初始化窗口
clock = pygame.time.Clock()
plane = pygame.image.load("plane.png")  #载入飞机图片资源
planerect = plane.get_rect()     #获取矩形区域
screen.fill(color)  #白色背景
screen.blit(plane, planerect)
pygame.display.flip()    #绘制飞机并更新
#--------------------------------------------------
while True:
    r=100
    #clock.tick(300)  #限制fps
    for i in range(0,510):
        #pygame.time.delay(100) 
        x, y = Length2XY(r,i/10)
        print(x,y,240-(r-x)-32,480-y-32)
        x=width-(r-x)-32
        y=height-y-32
        #print(x,y)
        #plt.scatter(x, y)
        #plt.show()
        planerect.move(x, y)
        screen.fill(color)
        newIma, planerect = rotate_cen(plane, planerect,(i/10)/(2*0.25*r)*90) #旋转
        planerect.move(x, y)
        screen.blit(newIma, planerect)
        pygame.display.update()#更新
        
        #pygame.image.save(screen,str(i)+'.jpg') #每帧截图
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    break

pygame.quit()
