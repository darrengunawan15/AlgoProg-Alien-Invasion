# 14-2. Target Practice
# 14-3. Challenging Target Practice
import sys
import pygame
import random

pygame.init()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Target Practice")

background_color = (0, 0, 0)
ship_color = (0, 255, 0)
bullet_color = (255, 0, 0)
target_color = (255, 255, 255)

ship_image = pygame.image.load("images/alien.png")
ship_rect = ship_image.get_rect()

ship_width = 50
ship_height = 30
ship_x = 0
ship_y = screen_height // 2 - ship_height // 2
ship_speed = 5

bullet_width = 10
bullet_height = 14
bullet_speed = 2
bullets = []

target_width = 20
target_height = 60
target_x = screen_width - target_width
target_y = screen_height // 2 - target_height // 2
target_speed = 0.1

misses = 3
game_active = False

font = pygame.font.Font(None, 36)
play_button = pygame.Rect(screen_width // 2 - 50, screen_height // 2 - 25, 100, 50)

def reset_game():
    global ship_y, bullets, target_y, misses, game_active
    ship_y = screen_height // 2 - ship_height // 2
    bullets = []
    target_y = screen_height // 2 - target_height // 2
    misses = 0
    game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and game_active:
            if event.key == pygame.K_UP and ship_y > 0:
                ship_y -= ship_speed
            elif event.key == pygame.K_DOWN and ship_y < screen_height - ship_height:
                ship_y += ship_speed
            elif event.key == pygame.K_SPACE:
                bullet = pygame.Rect(ship_x + ship_width, ship_y + ship_height // 2 - bullet_height // 2, bullet_width, bullet_height)
                bullets.append(bullet)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_active:
            if play_button.collidepoint(event.pos):
                reset_game()

    if game_active:
        bullets = [bullet for bullet in bullets if bullet.x < screen_width]
        for bullet in bullets:
            bullet.x += bullet_speed

        target_y += target_speed

        if target_y <= 0 or target_y >= screen_height - target_height:
            target_speed = -target_speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and ship_y > 0:
            ship_y -= ship_speed
        if keys[pygame.K_DOWN] and ship_y < screen_height - ship_height:
            ship_y += ship_speed

        screen.fill(background_color)
        screen.blit(ship_image, (ship_x, ship_y))

        for bullet in bullets:
            pygame.draw.rect(screen, bullet_color, bullet)

        pygame.draw.rect(screen, target_color, (target_x, target_y, target_width, target_height))

        for bullet in bullets:
            if bullet.colliderect(target_x, target_y, target_width, target_height):
                target_y = random.randint(0, screen_height - target_height)
                bullets.remove(bullet)
                target_speed *= 1.5
            elif bullet.x >= screen_width:
                misses += 1
                bullets.remove(bullet)

        misses_text = font.render("Misses: {}".format(misses), True, (255, 255, 255))
        screen.blit(misses_text, (10, 10))

        if misses >= 3:
            game_active = False
            screen.fill(background_color)
            pygame.draw.rect(screen, (255, 0, 0), play_button)
            game_over_text = font.render("Game Over", True, (255, 255, 255))
            screen.blit(game_over_text, (screen_width // 2 - 80, screen_height // 2 - 50))
            play_text = font.render("Play Again", True, (255, 255, 255))
            screen.blit(play_text, (screen_width // 2 - 80, screen_height // 2 + 20))

        pygame.display.flip()

    else:
        screen.fill(background_color)
        pygame.draw.rect(screen, (173, 216, 230), play_button)
        play_text = font.render("Play", True, (255, 255, 255))
        screen.blit(play_text, (screen_width // 2 - 25, screen_height // 2 - 15))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    reset_game()

        pygame.display.flip()
