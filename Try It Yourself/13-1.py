# 13-1. Stars
import sys
import pygame

pygame.init()

screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Stars")

star_image = pygame.image.load("images/stars.png")
star_rect = star_image.get_rect()

rows = 6
cols = 6
spacing = 100 
raindrop_speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    for row in range(rows):
        for col in range(cols):
            x = col * spacing
            y = row * spacing
            screen.blit(star_image, (x, y))

    pygame.display.flip()