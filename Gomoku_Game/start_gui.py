import tkinter as tk
from domain.board import Board
from service.service import GomokuService
from ui.ui import GUI

if __name__ == "__main__":
    root = tk.Tk()
    board = Board(size=15)
    service = GomokuService(board)
    gui = GUI(root, service)
    root.mainloop()
