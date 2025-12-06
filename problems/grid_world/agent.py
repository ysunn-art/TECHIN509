"""Agent that navigates the grid world."""

from position import Position


class Agent:
    """
    Agent that can move through a GridWorld.

    Attributes:
        world (GridWorld): The grid world environment
        at (Position): Current position of agent
    """

    def __init__(self, world, pos=None):
        """
        Initialize an agent in a grid world.

        Args:
            world (GridWorld): The grid world environment
            pos (Position, optional): Starting position (default: world.start)
        """
        self.world = world
        self.at = pos if pos is not None else world.start

    def can_move_to(self, pos):
        """
        Check if agent can move to a position.

        Args:
            pos (Position): Position to check

        Returns:
            bool: True if position is valid (in bounds and passable)
        """
        return self.world.in_bounds(pos) and self.world.passable(pos)

    def step(self, direction):
        """
        Move agent in specified direction if possible.

        Args:
            direction (str): Direction to move ('up', 'down', 'left', 'right')

        Returns:
            bool: True if move was successful, False otherwise
        """
        # Calculate new position based on direction
        if direction == 'up':
            new_pos = Position(self.at.row - 1, self.at.col)
        elif direction == 'down':
            new_pos = Position(self.at.row + 1, self.at.col)
        elif direction == 'left':
            new_pos = Position(self.at.row, self.at.col - 1)
        elif direction == 'right':
            new_pos = Position(self.at.row, self.at.col + 1)
        else:
            return False  # Invalid direction

        # Check if move is valid
        if self.can_move_to(new_pos):
            self.at = new_pos
            return True
        else:
            return False

    def reset(self, pos):
        """
        Teleport agent to a new position.

        Args:
            pos (Position): New position for agent
        """
        self.at = pos
