#!/usr/bin/python3
# auther@hy
# 2022年06月14日
import pygame

pygame.init()
screen = pygame.display.set_mode((300,400))
bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
screen.blit(bg,(0,0))
screen.blit(hero,(100,200))
pygame.display.update()
hero_rect = pygame.Rect(100,200,30,50)
clock1 = pygame.time.Clock()
while True:
    clock1.tick(60)
    # 事件的捕获event
    even_list = pygame.event.get()
    if len(even_list) > 0:
        print(even_list)
    hero_rect.y -= 1
    if hero_rect.bottom <= 0:
        hero_rect.y = 400
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    pygame.display.update()
    # 判断事件是否点击了退出
    for even in even_list:
        if even.type == pygame.QUIT:
            pygame.quit()
            # 进程结束
            exit()
