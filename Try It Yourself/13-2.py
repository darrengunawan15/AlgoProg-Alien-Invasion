# 13-2. Better Stars
import sys
import pygame
from random import randint

pygame.init()

screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Better Stars")

star_image = pygame.image.load("images/stars.png")
star_rect = star_image.get_rect()

num_of_stars = 20

star_positions = [(randint(0, screen_width - star_rect.width), randint(0, screen_height - star_rect.height)) for i in range(num_of_stars)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    for x, y in star_positions:
        screen.blit(star_image, (x, y))

    pygame.display.flip()