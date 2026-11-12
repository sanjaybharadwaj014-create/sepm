
import unittest


def check_winner(board):
    combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in combinations:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    return None


class TestTicTacToe(unittest.TestCase):

    def test_x_wins(self):
        board = ["X", "X", "X",
                 "O", "O", "",
                 "", "", ""]
        self.assertEqual(check_winner(board), "X")

    def test_o_wins(self):
        board = ["O", "X", "X",
                 "O", "X", "",
                 "O", "", ""]
        self.assertEqual(check_winner(board), "O")

    def test_no_winner(self):
        board = ["X", "O", "X",
                 "O", "X", "O",
                 "O", "X", "O"]
        self.assertIsNone(check_winner(board))

    def test_empty_board(self):
        board = [""] * 9
        self.assertIsNone(check_winner(board))


if __name__ == "__main__":
    unittest.main()
