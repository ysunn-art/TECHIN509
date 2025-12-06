"""Unit tests for GridWorld class."""

import unittest
import sys
sys.path.append('..')
from position import Position
from grid_world import GridWorld


class TestGridWorld(unittest.TestCase):
    """Test cases for GridWorld class."""

    def setUp(self):
        """Set up test fixtures."""
        self.world = GridWorld(rows=5, cols=5)

    def test_initialization(self):
        """Test grid world initialization."""
        self.assertEqual(self.world.rows, 5)
        self.assertEqual(self.world.cols, 5)
        self.assertEqual(self.world.start, Position(0, 0))
        self.assertEqual(self.world.goal, Position(4, 4))

    def test_in_bounds_valid(self):
        """Test in_bounds for valid positions."""
        self.assertTrue(self.world.in_bounds(Position(0, 0)))
        self.assertTrue(self.world.in_bounds(Position(4, 4)))
        self.assertTrue(self.world.in_bounds(Position(2, 3)))

    def test_in_bounds_invalid(self):
        """Test in_bounds for invalid positions."""
        self.assertFalse(self.world.in_bounds(Position(-1, 0)))
        self.assertFalse(self.world.in_bounds(Position(0, -1)))
        self.assertFalse(self.world.in_bounds(Position(5, 0)))
        self.assertFalse(self.world.in_bounds(Position(0, 5)))

    def test_passable_no_walls(self):
        """Test passable when no walls exist."""
        self.assertTrue(self.world.passable(Position(2, 2)))

    def test_passable_with_wall(self):
        """Test passable with walls."""
        wall_pos = Position(2, 2)
        self.world.place_wall(wall_pos)

        self.assertFalse(self.world.passable(wall_pos))
        self.assertTrue(self.world.passable(Position(2, 3)))

    def test_is_goal(self):
        """Test goal detection."""
        self.assertTrue(self.world.is_goal(Position(4, 4)))
        self.assertFalse(self.world.is_goal(Position(0, 0)))

    def test_place_and_remove_wall(self):
        """Test wall placement and removal."""
        pos = Position(3, 3)

        # Place wall
        self.world.place_wall(pos)
        self.assertIn(pos, self.world.walls)
        self.assertFalse(self.world.passable(pos))

        # Remove wall
        self.world.remove_wall(pos)
        self.assertNotIn(pos, self.world.walls)
        self.assertTrue(self.world.passable(pos))


if __name__ == "__main__":
    unittest.main()
