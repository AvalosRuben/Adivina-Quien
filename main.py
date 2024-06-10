import pygame
import random
from character import Character
from game import Game
from player import Player
from board import Board
from questions import questions
from characters_list import characters

# Screen settings
SCREEN_WIDTH = 1400  # Increased the screen width
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guess Who?")

# Shuffle the characters
random.shuffle(characters)

# Calculate the width and height of each character image
CHARACTER_WIDTH = 100
CHARACTER_HEIGHT = 150

# Calculate the spacing between characters
HORIZONTAL_SPACING = (SCREEN_WIDTH - (6 * CHARACTER_WIDTH)) // 7
VERTICAL_SPACING = (SCREEN_HEIGHT - (4 * CHARACTER_HEIGHT)) // 5

# Create an instance of the game
game = Game(characters)

# Select a random character for the user
selected_character = random.choice(characters)
selected_character_image = pygame.image.load(selected_character.image)
selected_character_image = pygame.transform.scale(selected_character_image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display characters on the screen in a 6x4 grid
    screen.fill(BACKGROUND_COLOR)
    x, y = HORIZONTAL_SPACING, VERTICAL_SPACING
    for character in characters:
        character_image = pygame.image.load(character.image)
        character_image = pygame.transform.scale(character_image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        screen.blit(character_image, (x, y))
        x += CHARACTER_WIDTH + HORIZONTAL_SPACING
        if x > SCREEN_WIDTH - CHARACTER_WIDTH - HORIZONTAL_SPACING:
            x = HORIZONTAL_SPACING
            y += CHARACTER_HEIGHT + VERTICAL_SPACING

    # Display the selected character image below the button for questions
    screen.blit(selected_character_image, (SCREEN_WIDTH - CHARACTER_WIDTH - HORIZONTAL_SPACING, VERTICAL_SPACING))

    # Draw the button for questions more to the right
    pygame.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH - 300, 50, 250, 50))  # Modified position and size of the button
    font = pygame.font.Font(None, 36)
    text_questions = font.render("Questions", True, (255, 255, 255))
    screen.blit(text_questions, (SCREEN_WIDTH - 280, 60))  # Modified position of the text

    pygame.display.flip()

# Quit Pygame
pygame.quit()