import pygame
from game import Game
from characters_list import characters

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guess Who?")

# Create an instance of the game
game = Game(characters)

# Function to draw the play button
def draw_play_button():
    font = pygame.font.Font(None, 36)
    text_play = font.render("PLAY", True, (0, 0, 0))
    play_rect = text_play.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, play_rect, border_radius=10)
    screen.blit(text_play, play_rect)
    pygame.display.flip()

    return play_rect

# Function to check if the mouse click is within the play button area
def is_inside_play_button(pos, play_rect):
    return play_rect.collidepoint(pos)

# Function to draw the character list
def draw_character_list():
    font = pygame.font.Font(None, 24)
    for i, character in enumerate(game.characters):
        image = pygame.image.load(character.image)
        image_rect = image.get_rect(topleft=(50 + (i % 8) * 100, 50 + (i // 8) * 100))
        screen.blit(image, image_rect)
    pygame.display.flip()


# Main game loop
running = True
while running:
    play_rect = draw_play_button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse click at:", event.pos)  # Print mouse click coordinates
            if is_inside_play_button(event.pos, play_rect):
                game.start_game()
                draw_character_list()

# Quit Pygame
pygame.quit()