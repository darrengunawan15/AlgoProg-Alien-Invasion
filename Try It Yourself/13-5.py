# 13-5. Catch
# 13-6. Game Over
import sys
import pygame
import random
from pygame.sprite import Sprite

pygame.init()

screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch")

bg_color = (204, 204, 255)
basket_speed = 2
life = 3
font = pygame.font.Font(None, 36)

class Egg(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/egg.png")
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.y += 1

egg_group = pygame.sprite.Group()

class Basket(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/basket.png")
        self.rect = self.image.get_rect(midbottom=(screen_width // 2, screen_height - 10))

basket = Basket()
 
def spawn_egg():
    x = random.randint(0, screen_width - Egg(0,0).rect.width)
    y = 0
    egg = Egg(x, y)
    egg_group.add(egg)

spawn_egg()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket.rect.left > 0:
        basket.rect.x -= basket_speed
    if keys[pygame.K_RIGHT] and basket.rect.right < screen_width:
        basket.rect.x += basket_speed

    egg_group.update()

    collisions = pygame.sprite.groupcollide(egg_group, [basket], True, False)
    if collisions:
        spawn_egg()

    for egg in egg_group.sprites():
        if egg.rect.top > screen_height:
            egg.kill()
            spawn_egg()
            life -= 1
            if life == 0:
                game_over_text = font.render("Game Over - You missed the egg three times.", True, (0, 0, 0))
                screen.blit(game_over_text, (screen_width // 2 - 250, screen_height // 2))
                pygame.display.flip()
                pygame.time.delay(3000) 
                pygame.quit()
                sys.exit()

    screen.fill(bg_color)
    screen.blit(basket.image, basket.rect)
    egg_group.draw(screen)

    pygame.display.flip()