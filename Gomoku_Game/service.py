from random import randint
from domain.board import BoardError


class GomokuService:
    def __init__(self, board):
        """
        Initialize GomokuService with the specified Gomoku board.

        :param board: Gomoku board object.
        """
        self.board = board
        self.current_player = 'X'
        self.last_move = [0,0]

    def make_player_move(self, row, col):
        """
        Make a move on the Gomoku board for the current player.

        :param row: Row index for the move.
        :param col: Column index for the move.
        :return: True if the move is successful.
        :raises BoardError: If the move is invalid.
        """
        try:
            self.board.valid_move(row, col)
            self.board.make_move(self.current_player, row, col)
            return True
        except BoardError as e:
            raise e

    def make_ai_block(self):
        """
        Make a move for the AI player.

        :return: Tuple (row, col) representing the AI's move.
        """
        for i in range(15):
            for j in range(15):
                try:
                    if self.board.valid_move(i, j):
                        self.board.make_move('O', i, j)
                        if self.board.check_win('O', i, j):
                            self.last_move = [i, j]
                            return i, j
                        else:
                            self.board.remove_move(i, j)
                except BoardError:
                    pass

        for i in range(15):
            for j in range(15):
                try:
                    if self.board.valid_move(i, j):
                        self.board.make_move('X', i, j)
                        if self.board.check_win('X', i, j):
                            self.board.make_move('O', i, j)
                            self.last_move = [i, j]
                            return i, j
                        else:
                            self.board.remove_move(i, j)
                except BoardError:
                    pass

        for i in range(15):
            for j in range(15):
                try:
                    if self.board.valid_move(i, j):
                        self.board.make_move('X', i, j)
                        if self.board.check_4('X', i, j):
                            self.board.make_move('O', i, j)
                            self.last_move = [i, j]
                            return i, j
                        else:
                            self.board.remove_move(i, j)
                except BoardError:
                    pass
        return self.make_ai_win()

    def get_player_at(self, row, col):
        return self.board.get_player(row, col)

    def check_near_last(self):
        row = self.last_move[0]
        col = self.last_move[1]
        if self.board.valid_move(row, col + 1):
            return row, col + 1
        if self.board.valid_move(row, col - 1):
            return row, col - 1
        if self.board.valid_move(row + 1, col):
            return row + 1, col
        if self.board.valid_move(row - 1, col):
            return row - 1, col
        if self.board.valid_move(row - 1, col - 1):
            return row - 1, col - 1
        if self.board.valid_move(row + 1, col + 1):
            return row + 1, col + 1
        if self.board.valid_move(row + 1, col - 1) :
            return row + 1, col - 1
        if self.board.valid_move(row - 1, col + 1):
            return row - 1, col + 1
        return 0, 0



    def make_ai_win(self):
        """
        Choose a random strategy to place a move for the AI.

        :return: Tuple (row, col) representing the AI's move.
        """

        for i in range(15):
            for j in range(15):
                try:
                    if self.board.valid_move(i, j):
                        self.board.make_move('O', i, j)
                        if self.board.check_4('O', i, j):
                            self.last_move = [i, j]
                            return i, j
                        else:
                            self.board.remove_move(i, j)
                except BoardError:
                    pass

        if not self.last_move == [0,0]:
            try:
                row,col = self.check_near_last()
                if row != 0 and col != 0 :
                    self.board.make_move('O', row, col)
                    self.last_move[0] = row
                    self.last_move[1] = col
                    return row, col
            except BoardError:
                pass



        while True:
            row = randint(0, 14)
            column = randint(0, 14)
            try:
                if self.board.valid_move(row, column):
                    self.board.make_move('O', row, column)
                    self.last_move = [row, column]
                    return row, column
            except BoardError:
                pass

    def clear_table(self):
        """
        Clear the Gomoku board to start a new game.
        """
        self.board.empty_board()

    def check_winner(self, player, row, column):
        """
        Check if a player has won the game.

        :param player: Player to check for a win.
        :param row: Row index for the last move.
        :param column: Column index for the last move.
        :return: True if the player has won.
        """
        return self.board.check_win(player, row, column)

    def print_board(self):
        """
        Display the current state of the Gomoku board.
        """
        table = self.board.display_board()
        return table

    def check_is_draw(self):
        self.board.is_draw()

    def verify_input(self, row, column):
        self.board.verify_data(row, column)
