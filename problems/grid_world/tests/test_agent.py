"""Unit tests for Agent class."""

import unittest
import sys
sys.path.append('..')
from position import Position
from grid_world import GridWorld
from agent import Agent


class TestAgent(unittest.TestCase):
    """Test cases for Agent class."""

    def setUp(self):
        """Set up test fixtures."""
        self.world = GridWorld(rows=5, cols=5)
        self.agent = Agent(self.world)

    def test_initialization_default_position(self):
        """Test agent initializes at world start."""
        self.assertEqual(self.agent.at, self.world.start)

    def test_initialization_custom_position(self):
        """Test agent initialization with custom position."""
        custom_pos = Position(2, 3)
        agent = Agent(self.world, pos=custom_pos)
        self.assertEqual(agent.at, custom_pos)

    def test_can_move_to_valid_position(self):
        """Test can_move_to for valid positions."""
        self.assertTrue(self.agent.can_move_to(Position(1, 0)))
        self.assertTrue(self.agent.can_move_to(Position(0, 1)))

    def test_can_move_to_out_of_bounds(self):
        """Test can_move_to for out of bounds positions."""
        self.assertFalse(self.agent.can_move_to(Position(-1, 0)))
        self.assertFalse(self.agent.can_move_to(Position(5, 0)))

    def test_can_move_to_wall(self):
        """Test can_move_to for wall positions."""
        wall_pos = Position(1, 0)
        self.world.place_wall(wall_pos)
        self.assertFalse(self.agent.can_move_to(wall_pos))

    def test_step_down_success(self):
        """Test successful step down."""
        initial_pos = self.agent.at
        result = self.agent.step('down')

        self.assertTrue(result)
        self.assertEqual(self.agent.at, Position(initial_pos.row + 1, initial_pos.col))

    def test_step_right_success(self):
        """Test successful step right."""
        initial_pos = self.agent.at
        result = self.agent.step('right')

        self.assertTrue(result)
        self.assertEqual(self.agent.at, Position(initial_pos.row, initial_pos.col + 1))

    def test_step_up_success(self):
        """Test successful step up."""
        self.agent.reset(Position(2, 2))
        result = self.agent.step('up')

        self.assertTrue(result)
        self.assertEqual(self.agent.at, Position(1, 2))

    def test_step_left_success(self):
        """Test successful step left."""
        self.agent.reset(Position(2, 2))
        result = self.agent.step('left')

        self.assertTrue(result)
        self.assertEqual(self.agent.at, Position(2, 1))

    def test_step_into_wall_fails(self):
        """Test that stepping into wall fails."""
        self.agent.reset(Position(1, 1))
        wall_pos = Position(1, 2)
        self.world.place_wall(wall_pos)

        result = self.agent.step('right')

        self.assertFalse(result)
        self.assertEqual(self.agent.at, Position(1, 1))  # Didn't move

    def test_step_out_of_bounds_fails(self):
        """Test that stepping out of bounds fails."""
        # Agent starts at (0, 0)
        result = self.agent.step('up')

        self.assertFalse(result)
        self.assertEqual(self.agent.at, Position(0, 0))  # Didn't move

    def test_step_invalid_direction(self):
        """Test that invalid direction returns False."""
        initial_pos = self.agent.at
        result = self.agent.step('diagonal')

        self.assertFalse(result)
        self.assertEqual(self.agent.at, initial_pos)

    def test_reset(self):
        """Test agent reset to new position."""
        new_pos = Position(3, 4)
        self.agent.reset(new_pos)
        self.assertEqual(self.agent.at, new_pos)


if __name__ == "__main__":
    unittest.main()
