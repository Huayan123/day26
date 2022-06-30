#!/usr/bin/python3
# auther@hy
# 2022年06月14日
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((300,400))
bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
screen.blit(bg,(0,0))
screen.blit(hero,(100,200))
pygame.display.update()
clock1 = pygame.time.Clock()
i = 0
while True:
    clock1.tick(15)
    i+=1
    print(i)

pygame.quit()