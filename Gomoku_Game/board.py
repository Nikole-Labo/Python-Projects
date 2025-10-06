from prettytable import PrettyTable


class BoardError(Exception):
    pass


class InputError(Exception):
    pass


class Board:
    def __init__(self, size=15):
        """
        Initialize the Gomoku board.

        :param size: Size of the board (default is 15x15).
        """
        self._size = size
        self._board = [[' ' for _ in range(size)] for _ in range(size)]
        self._moves_made = 0

    def verify_data(self, row, column):
        if not row.isdigit():
            raise InputError("That was not an integer! :(")

    def display_board(self):
        """
        Display the current state of the Gomoku board.
        """
        table = PrettyTable(field_names=[], header=False)
        for row in self._board:
            table.add_row(row)
        return table

    def make_move(self, player, row, col):
        """
        Make a move on the Gomoku board.

        :param player: Player making the move ('X' or 'O').
        :param row: Row index for the move.
        :param col: Column index for the move.
        """
        self._board[row][col] = player
        self._moves_made += 1

    def get_player(self, row, col):
        return self._board[row][col]

    def valid_move(self, row, col):
        """
        Check if a move is valid on the Gomoku board.

        :param row: Row index for the move.
        :param col: Column index for the move.
        :raises BoardError: If the move is invalid.
        :return: True if the move is valid.
        """
        if row < 0 or row > 14 or col < 0 or col > 14:
            raise BoardError("Outside the board! :(")
        if self._board[row][col] != " ":
            raise BoardError("That space is already taken!")
        return True

    def is_draw(self):
        """
        Check if the game is a draw.

        :raises BoardError: If the game is a draw.
        """
        if self._moves_made == 15 * 15:
            raise BoardError("Oh no! It is a draw!")

    def check_row(self, player, row, column, nr):
        """
                Check if a player has won the game.

                :param player: Player to check for a win.
                :param row: Row index for the last move.
                :param column: Column index for the last move.
                :param nr: consecutive_count ideal
                :return: True if the player has won.
        """
        minimum = max(0, column - nr)
        maximum = min(14, column + nr)
        consecutive_count = 0
        for column_check in range(minimum, maximum + 1):
            if self._board[row][column_check] == player:
                consecutive_count += 1
                if consecutive_count == nr:
                    return True
            else:
                consecutive_count = 0

    def check_column(self, player, row, column, nr):
        """
                Check if a player has won the game.

                :param player: Player to check for a win.
                :param row: Row index for the last move.
                :param column: Column index for the last move.
                :param nr: consecutive_count ideal
                :return: True if the player has won.
        """
        minimum = max(0, row - nr)
        maximum = min(14, row + nr)
        consecutive_count = 0
        for row_check in range(minimum, maximum + 1):
            if self._board[row_check][column] == player:
                consecutive_count += 1
                if consecutive_count == nr:
                    return True
            else:
                consecutive_count = 0

    def check_first_diagonal(self, player, row, column, nr):
        """
                Check if a player has won the game.

                :param player: Player to check for a win.
                :param row: Row index for the last move.
                :param column: Column index for the last move.
                :param nr: consecutive_count ideal
                :return: True if the player has won.
        """
        consecutive_count = 0
        for i in range(-nr, nr+1):
            row_check, column_check = row + i, column + i
            if 0 <= row_check < 15 and 0 <= column_check < 15 and self._board[row_check][column_check] == player:
                consecutive_count += 1
                if consecutive_count == nr:
                    return True
            else:
                consecutive_count = 0

    def check_second_diagonal(self, player, row, column, nr):
        """
                Check if a player has won the game.

                :param player: Player to check for a win.
                :param row: Row index for the last move.
                :param column: Column index for the last move.
                :param nr: consecutive_count ideal
                :return: True if the player has won.
        """
        consecutive_count = 0
        for i in range(-nr, nr+1):
            row_check, column_check = row - i, column + i
            if 0 <= row_check < 15 and 0 <= column_check < 15 and self._board[row_check][column_check] == player:
                consecutive_count += 1
                if consecutive_count == nr:
                    return True
            else:
                consecutive_count = 0

    def check_win(self, player, row, column):
        """
        Check if a player has won the game.

        :param player: Player to check for a win.
        :param row: Row index for the last move.
        :param column: Column index for the last move.
        :return: True if the player has won.
        """
        if self.check_row(player, row, column, 5):
            return True
        if self.check_column(player, row, column, 5):
            return True
        if self.check_first_diagonal(player, row, column, 5):
            return True
        if self.check_second_diagonal(player, row, column, 5):
            return True
        return False

    def check_4(self, player, row, column):
        """
        Check if a player has won the game.

        :param player: Player to check for a win.
        :param row: Row index for the last move.
        :param column: Column index for the last move.
        :return: True if the player has won.
        """
        if self.check_row(player, row, column, 4):
            return True
        if self.check_column(player, row, column, 4):
            return True
        if self.check_first_diagonal(player, row, column, 4):
            return True
        if self.check_second_diagonal(player, row, column, 4):
            return True
        return False

    def empty_board(self):
        """
        Reset the Gomoku board to its initial state.
        """
        self._board = [[' ' for _ in range(self._size)] for _ in range(self._size)]
        self._moves_made = 0

    def remove_move(self, row, col):
        """
        Remove a move from the Gomoku board.

        :param row: Row index of the move to be removed.
        :param col: Column index of the move to be removed.
        """
        self._board[row][col] = ' '


