"""Unit tests for Pathfinder class."""

import unittest
import sys
sys.path.append('..')
from position import Position
from grid_world import GridWorld
from path import Pathfinder


class TestPathfinder(unittest.TestCase):
    """Test cases for Pathfinder class."""

    def setUp(self):
        """Set up test fixtures."""
        self.world = GridWorld(rows=5, cols=5)
        self.pathfinder = Pathfinder(self.world)

    def test_find_path_straight_line(self):
        """Test finding path in straight line."""
        start = Position(0, 0)
        goal = Position(0, 4)

        path = self.pathfinder.find_path(start, goal)

        self.assertIsNotNone(path)
        self.assertEqual(len(path), 5)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)

    def test_find_path_diagonal(self):
        """Test finding path diagonally (Manhattan distance)."""
        start = Position(0, 0)
        goal = Position(2, 2)

        path = self.pathfinder.find_path(start, goal)

        self.assertIsNotNone(path)
        # Manhattan distance: 2 + 2 = 4, plus start = 5 positions
        self.assertEqual(len(path), 5)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)

    def test_find_path_with_wall_obstacle(self):
        """Test pathfinding around a wall."""
        # Create wall barrier
        self.world.place_wall(Position(1, 1))
        self.world.place_wall(Position(1, 2))
        self.world.place_wall(Position(1, 3))

        start = Position(0, 2)
        goal = Position(2, 2)

        path = self.pathfinder.find_path(start, goal)

        self.assertIsNotNone(path)
        # Must go around the wall
        self.assertGreater(len(path), 3)  # Longer than direct route

        # Verify path doesn't pass through walls
        for pos in path:
            self.assertTrue(self.world.passable(pos))

    def test_find_path_no_solution(self):
        """Test when no path exists (goal completely walled off)."""
        # Wall off goal completely
        goal = Position(2, 2)
        self.world.place_wall(Position(1, 2))
        self.world.place_wall(Position(3, 2))
        self.world.place_wall(Position(2, 1))
        self.world.place_wall(Position(2, 3))

        start = Position(0, 0)
        path = self.pathfinder.find_path(start, goal)

        self.assertIsNone(path)

    def test_find_path_start_equals_goal(self):
        """Test when start and goal are the same."""
        pos = Position(2, 2)
        path = self.pathfinder.find_path(pos, pos)

        self.assertIsNotNone(path)
        self.assertEqual(len(path), 1)
        self.assertEqual(path[0], pos)

    def test_nodes_expanded_tracking(self):
        """Test that nodes_expanded is tracked correctly."""
        start = Position(0, 0)
        goal = Position(1, 1)

        path = self.pathfinder.find_path(start, goal)

        self.assertIsNotNone(path)
        self.assertGreater(self.pathfinder.nodes_expanded, 0)
        # Should not expand more nodes than grid size
        self.assertLessEqual(self.pathfinder.nodes_expanded, 25)

    def test_path_is_connected(self):
        """Test that returned path consists of adjacent positions."""
        start = Position(0, 0)
        goal = Position(4, 4)

        path = self.pathfinder.find_path(start, goal)

        # Check each consecutive pair is adjacent
        for i in range(len(path) - 1):
            curr = path[i]
            next_pos = path[i + 1]

            # Positions should differ by exactly 1 in row OR col (not both)
            row_diff = abs(curr.row - next_pos.row)
            col_diff = abs(curr.col - next_pos.col)

            self.assertTrue(
                (row_diff == 1 and col_diff == 0) or
                (row_diff == 0 and col_diff == 1)
            )


if __name__ == "__main__":
    unittest.main()
