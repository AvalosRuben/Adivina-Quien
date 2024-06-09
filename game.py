from character import Character
from player import Player
import characters_images
class Game:
    def __init__(self):
        self.human_player = Player()
        self.computer_player = Player()
        self.characters = []  # Common list of Characters available in the game
        self.current_turn = 'human'  # Can be 'human' or 'computer'
        self.game_state = 'in progress'
        self.remaining_questions = 20  # For example

    def start_game(self):
        # Set up the initial game configuration
        self.assign_hidden_characters()

    def assign_hidden_characters(self):
        # Randomly assigns the hidden characters to both players
        import random
        self.human_player.hidden_character = random.choice(self.characters)
        self.computer_player.hidden_character = random.choice(self.characters)

    def change_turn(self):
        # Switches the turn between the human player and the computer
        self.current_turn = 'computer' if self.current_turn == 'human' else 'human'

    def validate_question(self, question):
        # Validates the player's question
        pass

    def answer_question(self, question):
        # Answers the player's question
        pass

    def mark_characters(self, characteristic, value):
        # Marks the characters that do not match the selected characteristic
        pass

    def guess_character(self, guessed_character):
        # Allows the player to guess the hidden character
        if self.current_turn == 'human':
            if guessed_character == self.computer_player.hidden_character:
                self.game_state = 'human wins'
            else:
                self.game_state = 'computer wins'
        else:
            if guessed_character == self.human_player.hidden_character:
                self.game_state = 'computer wins'
            else:
                self.game_state = 'human wins'