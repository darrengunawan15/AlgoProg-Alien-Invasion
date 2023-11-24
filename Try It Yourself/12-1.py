# 12-1. Blue Sky
import sys
import pygame

pygame.init()

screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Sky")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((135, 206, 235))
    pygame.display.flip()

    clock.tick(60)