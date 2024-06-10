import random

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.slots = [[None for _ in range(columns)] for _ in range(rows)]

    def generate_board(self, characters):
        random.shuffle(characters)
        # Asumiendo que characters es una lista de personajes que contiene todos los personajes posibles para el juego
        self.grid = [characters[i:i+self.columns] for i in range(0, len(characters), self.columns)]

    def display_board(self):
        # Muestra el estado actual del tablero
        for row in self.grid:
            print(" | ".join(str(character) if character else " " for character in row))