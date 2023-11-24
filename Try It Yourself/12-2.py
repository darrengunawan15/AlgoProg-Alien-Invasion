# 12.2 Game Character
import pygame
from pygame.locals import *

pygame.init()

class GameCharacter(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Character")

character_image_path = "images/cacaca.bmp"
game_character = GameCharacter(character_image_path)

background_color = (211, 153, 155)
screen.fill(background_color)

character_position = (
    screen_width // 2 - game_character.rect.width // 2,
    screen_height // 2 - game_character.rect.height // 2,
)
screen.blit(game_character.image, character_position)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.flip()

pygame.quit()