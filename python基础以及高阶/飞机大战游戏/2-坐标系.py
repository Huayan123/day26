#!/usr/bin/python3
# auther@hy
# 2022年06月14日
import pygame
hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄的坐标是：%d %d"%(hero_rect.x,hero_rect.y))
print("英雄的宽和高是 %d %d"%(hero_rect.width,hero_rect.height))
print("%d %d"%(hero_rect.size))