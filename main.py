import pygame
from game import Game
from player import Player



pygame.init()

screen = pygame.display.set_mode((800,600))

def change_screen_size (screen, size):
    screen = pygame.display.set_mode((size))
    return screen

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255,255,255))
    pygame.display.flip()
    
pygame.QUIT()
