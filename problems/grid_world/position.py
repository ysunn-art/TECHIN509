"""Position representation for grid world navigation."""


class Position:
    """
    Represents a position in a 2D grid.

    Attributes:
        row (int): Row index
        col (int): Column index
    """

    def __init__(self, row, col):
        """
        Initialize a position.

        Args:
            row (int): Row index
            col (int): Column index
        """
        self.row = row
        self.col = col

    def neighbors_4(self):
        """
        Get the four neighboring positions (up, down, left, right).

        Returns:
            tuple: Four Position objects (up, down, left, right)
        """
        up = Position(self.row - 1, self.col)
        down = Position(self.row + 1, self.col)
        left = Position(self.row, self.col - 1)
        right = Position(self.row, self.col + 1)

        return (up, down, left, right)

    def __eq__(self, other):
        """
        Check equality with another Position.

        Args:
            other (Position): Another position object

        Returns:
            bool: True if positions are equal
        """
        if not isinstance(other, Position):
            return False
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        """
        Make Position hashable for use in sets and dicts.

        Returns:
            int: Hash value
        """
        return hash((self.row, self.col))

    def __repr__(self):
        """
        String representation of Position.

        Returns:
            str: String like "(2,3)"
        """
        return f"({self.row},{self.col})"
