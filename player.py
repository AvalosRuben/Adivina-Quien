import character
import game
class Player:
    def __init__(self,name, chosen_character):
        self.name = name
        self.chosen_character = chosen_character #this will be an object from the character class
        