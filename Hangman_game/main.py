from repository import Repository
from board import Board
from ui import UI

game_repository = Repository("sentences.txt")
game_board = Board(game_repository)
game_ui = UI(game_board)

game_ui.start()
