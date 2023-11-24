# 12-3. Rocket
import sys
import pygame

pygame.init()

screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rocket")

rocket_image = pygame.image.load("images/rocket.png")
rocket_rect = rocket_image.get_rect()
rocket_rect.center = (screen_width // 2, screen_height // 2)

clock = pygame.time.Clock()

rocket_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and rocket_rect.left > 0:
        rocket_rect.x -= rocket_speed
    if keys[pygame.K_RIGHT] and rocket_rect.right < screen_width:
        rocket_rect.x += rocket_speed
    if keys[pygame.K_UP] and rocket_rect.top > 0:
        rocket_rect.y -= rocket_speed
    if keys[pygame.K_DOWN] and rocket_rect.bottom < screen_height:
        rocket_rect.y += rocket_speed

    screen.fill((255, 255, 255))

    screen.blit(rocket_image, rocket_rect)

    pygame.display.flip()

    clock.tick(60)