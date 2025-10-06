import unittest
from domain.board import Board, BoardError
from service.service import GomokuService


class Tests(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()
        self.service = GomokuService(self.test_board)

    def test_make_player_move(self):
        """ Checks if the make_player_move method correctly updates the board with the player's move."""
        self.setUp()
        expected_board = [[' ' for _ in range(15)] for _ in range(15)]
        expected_board[1][1] = 'X'
        self.service.make_player_move(1, 1)
        self.assertEqual(expected_board, self.service.board._board)

    def test_raise_error_outside_the_board(self):
        self.setUp()
        with self.assertRaises(BoardError):self.service.make_player_move(20, 20)

    def test_raise_error_place_already_taken(self):
        self.setUp()
        self.service.make_player_move(1, 1)
        with self.assertRaises(BoardError): self.service.make_player_move(1, 1)

    def test_is_draw(self):
        self.setUp()
        for i in range(15):
            for j in range(15):
                self.service.make_player_move(i, j)
        with self.assertRaises(BoardError): self.service.check_is_draw()

    def test_win_row(self):
        self.setUp()
        for i in range(5):
            self.service.make_player_move(i, 0)
        self.assertEqual(self.service.check_winner('X', 4, 0), True)

    def test_win_column(self):
        self.setUp()
        for i in range(5):
            self.service.make_player_move(0, i)
        self.assertEqual(self.service.check_winner('X', 0, 4), True)

    def test_win_first_diagonal(self):
        self.setUp()
        for i in range(5):
            self.service.make_player_move(i, i)
        self.assertEqual(self.service.check_winner('X', 4, 4), True)

    def test_win_second_diagonal(self):
        self.setUp()
        for i in range(5):
            self.service.make_player_move(i, 5-i-1)
        self.assertEqual(self.service.check_winner('X', 4, 0), True)

    def test_not_win(self):
        """Tests that the check_winner method correctly identifies when there is no win."""
        self.setUp()
        self.service.make_player_move(1, 1)
        self.assertEqual(self.service.check_winner('X', 1, 1), False)

    def test_clear(self):
        """ Checks if the clear_table method resets the board to an empty state."""
        self.setUp()
        for i in range(15):
            for j in range(15):
                self.service.make_player_move(i, j)
        expected_board = [[' ' for _ in range(15)] for _ in range(15)]
        self.service.clear_table()
        self.assertEqual(expected_board, self.service.board._board)


    def test_block_ai1(self):
        """Ensure AI blocks player's potential win"""
        self.setUp()
        for i in range(4):
            self.service.make_player_move(0, i)
        self.assertEqual(self.service.make_ai_block(), (0, 4))

    def test_block_ai2(self):
        """Ensure AI blocks player's potential win"""
        self.setUp()
        for i in range(4):
            self.test_board.make_move('O', 0, i)
        self.assertEqual(self.service.make_ai_block(), (0, 4))

    def test_block_ai_update(self):
        """Ensure AI blocks player's potential win and updates the board"""
        self.setUp()
        x, y = self.service.make_ai_block()
        self.assertEqual(self.service.board._board[x][y], 'O')

    def test_make_ai_win_1(self):
        """Ensure AI wins with a strategy (check_4)"""
        for i in range(4):
            self.service.make_player_move(0, i)
        self.assertEqual(self.service.make_ai_win(), (0, 4))

    def test_make_ai_win_2(self):
        """Ensure AI wins with a strategy (check_win)"""
        for i in range(4):
            self.test_board.make_move('O', 0, i)
        self.assertEqual(self.service.make_ai_win(), (0, 4))

    def test_make_ai_win_3(self):
        """Ensure AI makes a random move when no strategic move is available"""
        x, y = self.service.make_ai_win()
        self.assertTrue(0 <= x <= 14 and 0 <= y <= 14)

    def test_display(self):
        self.setUp()
        self.service.make_player_move(0, 1)
        self.service.print_board()
