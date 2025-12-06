import unittest
import sys
sys.path.append('..')
from models.board import Board


class TestCheckWinner(unittest.TestCase):

    def test_horizontal_win_row0(self):
        """Test horizontal win in row 0"""
        board = Board()
        board.grid = [
            ["X", "X", "X"],
            [" ", "O", " "],
            ["O", " ", " "]
        ]
        self.assertEqual(board.check_winner(), "X")

    def test_horizontal_win_row1(self):
        """Test horizontal win in row 1"""
        board = Board()
        board.grid = [
            ["X", " ", "O"],
            ["O", "O", "O"],
            ["X", " ", " "]
        ]
        self.assertEqual(board.check_winner(), "O")

    def test_horizontal_win_row2(self):
        """Test horizontal win in row 2"""
        board = Board()
        board.grid = [
            [" ", "O", "X"],
            ["O", " ", " "],
            ["X", "X", "X"]
        ]
        self.assertEqual(board.check_winner(), "X")

    def test_vertical_win_col0(self):
        """Test vertical win in column 0"""
        board = Board()
        board.grid = [
            ["O", "X", " "],
            ["O", " ", "X"],
            ["O", "X", " "]
        ]
        self.assertEqual(board.check_winner(), "O")

    def test_vertical_win_col1(self):
        """Test vertical win in column 1"""
        board = Board()
        board.grid = [
            ["O", "X", " "],
            [" ", "X", "O"],
            [" ", "X", "O"]
        ]
        self.assertEqual(board.check_winner(), "X")

    def test_vertical_win_col2(self):
        """Test vertical win in column 2"""
        board = Board()
        board.grid = [
            ["X", " ", "O"],
            [" ", "X", "O"],
            ["X", " ", "O"]
        ]
        self.assertEqual(board.check_winner(), "O")

    def test_diagonal_win_top_left_to_bottom_right(self):
        """Test diagonal win from top-left to bottom-right"""
        board = Board()
        board.grid = [
            ["X", "O", " "],
            ["O", "X", " "],
            [" ", "O", "X"]
        ]
        self.assertEqual(board.check_winner(), "X")

    def test_diagonal_win_top_right_to_bottom_left(self):
        """Test diagonal win from top-right to bottom-left"""
        board = Board()
        board.grid = [
            ["X", "O", "O"],
            ["X", "O", " "],
            ["O", "X", "X"]
        ]
        self.assertEqual(board.check_winner(), "O")

    def test_no_winner_empty_board(self):
        """Test empty board has no winner"""
        board = Board()
        self.assertEqual(board.check_winner(), "")

    def test_no_winner_partial_game(self):
        """Test partial game with no winner"""
        board = Board()
        board.grid = [
            ["X", "O", "X"],
            ["O", "X", " "],
            [" ", " ", "O"]
        ]
        self.assertEqual(board.check_winner(), "")

    def test_no_winner_draw(self):
        """Test full board with no winner (draw)"""
        board = Board()
        board.grid = [
            ["X", "O", "X"],
            ["O", "X", "X"],
            ["O", "X", "O"]
        ]
        self.assertEqual(board.check_winner(), "")


if __name__ == "__main__":
    unittest.main()
