from domain.board import Board
from service.service import GomokuService
from ui.ui import UI

if __name__ == "__main__":
    board = Board(size=15)
    service = GomokuService(board)
    ui = UI(service)
    ui.play_game()

