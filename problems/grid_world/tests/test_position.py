"""Unit tests for Position class."""

import unittest
import sys
sys.path.append('..')
from position import Position


class TestPosition(unittest.TestCase):
    """Test cases for Position class."""

    def test_initialization(self):
        """Test position initialization."""
        pos = Position(2, 3)
        self.assertEqual(pos.row, 2)
        self.assertEqual(pos.col, 3)

    def test_neighbors_4(self):
        """Test that neighbors_4 returns correct adjacent positions."""
        pos = Position(2, 3)
        up, down, left, right = pos.neighbors_4()

        self.assertEqual(up, Position(1, 3))      # row - 1
        self.assertEqual(down, Position(3, 3))    # row + 1
        self.assertEqual(left, Position(2, 2))    # col - 1
        self.assertEqual(right, Position(2, 4))   # col + 1

    def test_equality(self):
        """Test position equality comparison."""
        pos1 = Position(2, 3)
        pos2 = Position(2, 3)
        pos3 = Position(3, 2)

        self.assertEqual(pos1, pos2)
        self.assertNotEqual(pos1, pos3)

    def test_equality_with_non_position(self):
        """Test equality with non-Position objects."""
        pos = Position(2, 3)
        self.assertNotEqual(pos, (2, 3))
        self.assertNotEqual(pos, "Position(2,3)")

    def test_hashable(self):
        """Test that Position can be used in sets and as dict keys."""
        pos1 = Position(2, 3)
        pos2 = Position(2, 3)
        pos3 = Position(3, 2)

        # Test in set
        pos_set = {pos1, pos2, pos3}
        self.assertEqual(len(pos_set), 2)  # pos1 and pos2 are same

        # Test as dict key
        pos_dict = {pos1: "A", pos3: "B"}
        self.assertEqual(pos_dict[pos2], "A")  # pos2 same as pos1

    def test_repr(self):
        """Test string representation."""
        pos = Position(2, 3)
        self.assertEqual(repr(pos), "(2,3)")
        self.assertEqual(str(pos), "(2,3)")


if __name__ == "__main__":
    unittest.main()
