import pygame
import sys
pygame.init()

pygame.display.set_mode((100, 100))
print("a")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('Forward')
            elif event.key == pygame.K_RIGHT:
                print('Backward')
