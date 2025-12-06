import random


class Player:
    def __init__(self, symbol: str, random: bool = False):
        self.symbol = symbol
        self.random = random

    def get_move(self) -> tuple:
        """
        Get a valid move from player

        Returns:
        tuple: The row and colum indices to place the player's symbol
        """
        if self.random:
            # Generate a random move
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            print(f"{self.symbol} player chooses randomly: {row}, {col}")
            return row, col
        else:
            # get a move from human player
            while True:
                try:
                    move = input(f"{self.symbol} player, enter your move (row and column, 0-2, separated by a space): ")
                    row, col = map(int, move.split())
                    if row in range(3) and col in range(3):
                        return row, col
                    else:
                        print("Invalid input. Row and column must be between 0 and 2.")
                except ValueError:
                    print("Invalid input. Please enter two numbers separated by a space.")
