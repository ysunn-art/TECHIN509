"""Pathfinding algorithms for grid world navigation."""

from collections import deque
from position import Position


class Pathfinder:
    """
    Pathfinding using Breadth-First Search (BFS).

    Attributes:
        world (GridWorld): The grid world environment
        nodes_expanded (int): Number of nodes explored in last search
    """

    def __init__(self, world):
        """
        Initialize pathfinder for a grid world.

        Args:
            world (GridWorld): The grid world environment
        """
        self.world = world
        self.nodes_expanded = 0

    def find_path(self, start, goal):
        """
        Find shortest path from start to goal using BFS.

        Args:
            start (Position): Starting position
            goal (Position): Goal position

        Returns:
            list or None: List of Position objects from start to goal,
                         or None if no path exists
        """
        # Reset expansion counter
        self.nodes_expanded = 0

        # BFS initialization
        queue = deque([start])
        visited = {start}
        parent = {start: None}

        # BFS loop
        while queue:
            current = queue.popleft()
            self.nodes_expanded += 1

            # Check if we reached the goal
            if current == goal:
                # Reconstruct path by backtracking through parents
                path = []
                node = current
                while node is not None:
                    path.append(node)
                    node = parent[node]
                path.reverse()
                return path

            # Explore neighbors
            for neighbor in current.neighbors_4():
                # Check if neighbor is valid and unvisited
                if (self.world.in_bounds(neighbor) and
                    self.world.passable(neighbor) and
                    neighbor not in visited):

                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        # No path found
        return None
