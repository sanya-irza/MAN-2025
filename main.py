import pygame
import calculation

pygame.init()
calculation.prepare_maze()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
