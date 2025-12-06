"""Grid world environment for navigation."""

from position import Position


class GridWorld:
    """
    Represents a 2D grid world with walls, start, and goal positions.

    Attributes:
        rows (int): Number of rows
        cols (int): Number of columns
        walls (set): Set of Position objects representing walls
        start (Position): Starting position
        goal (Position): Goal position
    """

    def __init__(self, rows, cols, walls=None, start=None, goal=None):
        """
        Initialize a grid world.

        Args:
            rows (int): Number of rows
            cols (int): Number of columns
            walls (set, optional): Set of wall positions
            start (Position, optional): Starting position (default: (0, 0))
            goal (Position, optional): Goal position (default: (rows-1, cols-1))
        """
        self.rows = rows
        self.cols = cols
        self.walls = walls if walls is not None else set()
        self.start = start if start is not None else Position(0, 0)
        self.goal = goal if goal is not None else Position(rows - 1, cols - 1)

    def in_bounds(self, pos):
        """
        Check if position is inside the grid.

        Args:
            pos (Position): Position to check

        Returns:
            bool: True if position is within grid boundaries
        """
        return 0 <= pos.row < self.rows and 0 <= pos.col < self.cols

    def passable(self, pos):
        """
        Check if position is not a wall.

        Args:
            pos (Position): Position to check

        Returns:
            bool: True if position is passable (not a wall)
        """
        return pos not in self.walls

    def is_goal(self, pos):
        """
        Check if position is the goal.

        Args:
            pos (Position): Position to check

        Returns:
            bool: True if position is the goal
        """
        return pos == self.goal

    def place_wall(self, pos):
        """
        Add a wall at the specified position.

        Args:
            pos (Position): Position to place wall
        """
        self.walls.add(pos)

    def remove_wall(self, pos):
        """
        Remove wall at the specified position.

        Args:
            pos (Position): Position to remove wall
        """
        self.walls.discard(pos)

    def render(self, path=None, agent=None):
        """
        Print ASCII representation of the grid.

        Legend:
            # = wall
            . = empty space
            S = start
            G = goal
            A = agent
            * = path

        Args:
            path (list, optional): List of Position objects forming a path
            agent (Position, optional): Current agent position
        """
        path_set = set(path) if path is not None else set()

        for row in range(self.rows):
            line = ""
            for col in range(self.cols):
                pos = Position(row, col)

                # Priority: agent > start/goal > path > wall > empty
                if agent is not None and pos == agent:
                    line += "A"
                elif pos == self.start:
                    line += "S"
                elif pos == self.goal:
                    line += "G"
                elif pos in path_set:
                    line += "*"
                elif pos in self.walls:
                    line += "#"
                else:
                    line += "."

            print(line)
