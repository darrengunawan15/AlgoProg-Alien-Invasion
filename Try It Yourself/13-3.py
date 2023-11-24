# 13-3. Raindrops
import sys
import pygame

pygame.init()

screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Raindrops")

raindrop_image = pygame.image.load("images/rain.png")
raindrop_rect = raindrop_image.get_rect()

horizontal_spacing = 10  
vertical_spacing = 20   

rows = screen_height // (raindrop_rect.height + vertical_spacing)
cols = screen_width // (raindrop_rect.width + horizontal_spacing)

raindrop_positions = [
    (col * (raindrop_rect.width + horizontal_spacing), row * (raindrop_rect.height + vertical_spacing)) for row in range(rows) for col in range(cols)
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    raindrop_positions = [(x, y + 5) for x, y in raindrop_positions]

    screen.fill((0, 0, 0))

    for x, y in raindrop_positions:
        screen.blit(raindrop_image, (x, y))

    pygame.display.flip()