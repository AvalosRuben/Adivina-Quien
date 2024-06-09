import character
import game
class Player:
    def __init__(self):
        self.board = [] # List of Characters representing the player's board
        self.turn = False
        self.questions = []
        self.guessed = False
        self.hidden_character = None # The character that the opponent needs to guess
        