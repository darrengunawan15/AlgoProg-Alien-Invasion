# 12-5. Sideways Shooter
import pygame
import sys

pygame.init()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sideways Shooter")

background_color = (0, 0, 0)
ship_color = (0, 255, 0)
bullet_color = (255, 0, 0)

ship_image = pygame.image.load("images/alien.png")
ship_rect = ship_image.get_rect()

ship_width = 50
ship_height = 30
ship_x = 0
ship_y = screen_height // 2 - ship_height // 2
ship_speed = 2

bullet_width = 10
bullet_height = 6
bullet_speed = 2
bullets = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship_y -= ship_speed
            elif event.key == pygame.K_DOWN:
                ship_y += ship_speed
            elif event.key == pygame.K_SPACE:
                bullet = pygame.Rect(ship_x + ship_width, ship_y + ship_height // 2 - bullet_height // 2, bullet_width, bullet_height)
                bullets.append(bullet)

    bullets = [bullet for bullet in bullets if bullet.x < screen_width]
    for bullet in bullets:
        bullet.x += bullet_speed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ship_y > 0:
        ship_y -= ship_speed
    if keys[pygame.K_DOWN] and ship_y < screen_height - ship_height:
        ship_y += ship_speed

    screen.fill(background_color)
    screen.blit(ship_image, (ship_x, ship_y))

    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)

    pygame.display.flip()