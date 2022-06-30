#!/usr/bin/python3
# auther@hy
# 2022年06月14日
import time

import pygame
pygame.init()
# 调用set_mode显示屏幕大小
screen = pygame.display.set_mode((300,400))
# 加载背景图
bg = pygame.image.load("./images/background.png")
# 绘制背景图
screen.blit(bg,(0,0))
# 最后更新背景图
pygame.display.update()
while True:
    time.sleep(1)

pygame.quit()