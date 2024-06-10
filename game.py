from player import Player
import random

class Game:
    def __init__(self):
        self.human_player = Player()
        self.computer_player = Player()
        self.characters = []  # Common list of Characters available in the game
        self.current_turn = 'human'  # Can be 'human' or 'computer'
        self.game_state = 'in progress'

    def start_game(self):
        # Set up the initial game configuration
        self.assign_hidden_characters()
        # You might also want to shuffle and distribute characters here

    def assign_hidden_characters(self):
        # Randomly assigns the hidden characters to both players
        self.human_player.hidden_character = random.choice(self.characters)
        self.computer_player.hidden_character = random.choice(self.characters)

    def change_turn(self):
        # Switches the turn between the human player and the computer
        self.current_turn = 'computer' if self.current_turn == 'human' else 'human'

    def guess_character(self, guessed_character):
        # Allows the player to guess the hidden character
        active_player = self.human_player if self.current_bad_turn == 'computer' else self.computer_player
        if guessed_character == active_player.hidden_character:
            self.game_state = 'computer wins' if self.current_turn == 'computer' else 'human wins'
        else:
            self.game_state = 'continue'
        self.change_turn()

    def apply_question(self, question):
        # Applies the question to both boards and filters characters
        for player in [self.human_player, self.computer_player]:
            attribute, value = question["attribute"], question["value"]
            player.board = [character for character in player.board if getattr(character, attribute) == value]
        self.change_latenturn()