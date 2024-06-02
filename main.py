import pygame
from game import Game
from player import Player



pygame.init()

screen = pygame.display.set_mode((800,600))
game = Game()

def change_screen_size (screen, size):
    screen = pygame.display.set_mode((size))
    return screen

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255,255,255))

    #starting the game
    #change_screen_size(screen, (1000,800))
    game.draw_board(screen)

    pygame.display.flip()
    
pygame.QUIT()
