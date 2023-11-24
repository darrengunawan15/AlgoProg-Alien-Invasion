# 12-4. Keys
import sys 
import pygame

pygame.init()

screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keys")

font = pygame.font.Font(None, 36)

current_text = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                current_text = ""
            elif event.key == pygame.K_BACKSPACE:
                current_text = current_text[:-1]
            else:
                current_text += event.unicode

    screen.fill((255, 255, 255))
    text_render = font.render(current_text, True, (0, 0, 0)) 
    text_rect = text_render.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(text_render, text_rect)

    pygame.display.flip()