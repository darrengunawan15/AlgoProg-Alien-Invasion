# 13-4. Steady Rain
import sys
import pygame
from random import randint

pygame.init()

screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Steady Rain")

raindrop_image = pygame.image.load("images/rain.png")
raindrop_rect = raindrop_image.get_rect()

num_raindrops = 100
raindrop_speed = 10

raindrop_positions = [(randint(0, screen_width - raindrop_rect.width), randint(0, screen_height - raindrop_rect.height)) for i in range(num_raindrops)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for i in range(num_raindrops):
        x, y = raindrop_positions[i]
        raindrop_positions[i] = (x, y + raindrop_speed)

        if y > screen_height:
            raindrop_positions[i] = (randint(0, screen_width - raindrop_rect.width), 0)

        screen.fill((0, 0, 20))

    for x, y in raindrop_positions:
        screen.blit(raindrop_image, (x, y))

    pygame.display.flip()