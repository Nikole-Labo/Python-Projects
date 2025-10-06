# Gomoku – Five in a Row

An implementation of **Gomoku (Five in a Row)** in Python featuring both **console** and **graphical (Tkinter)** user interfaces. The game supports **player vs computer** gameplay, with an AI that can block, attempt to win, and play strategically. It also includes a **unit test suite** for verifying game logic.

---

## 🎯 Features & Functionality

* **Two play modes**

  * Console-based UI (text input)
  * Tkinter GUI with a 15×15 board
* **Human vs AI gameplay**

  * Human plays with `X`
  * Computer plays with `O`
* **AI decision-making**

  * Attempts to win in one move
  * Blocks player’s winning moves
  * Prevents “4 in a row” threats
  * Plays randomly when no immediate strategy is found
* **Game mechanics**

  * Win detection across rows, columns, and diagonals
  * Draw detection when the board is full
  * Restart option after win/loss/draw
* **GUI features**

  * Interactive 15×15 clickable board
  * Score tracking for player vs AI
  * Restart button with alternating first-move advantage
* **Unit tests** ensuring board validation, win conditions, draw detection, AI blocking, and AI winning logic

---

## 🛠 Architecture & Flow

1. **Board (`board.py`)**

   * Maintains grid state and validates moves
   * Detects wins (rows, columns, diagonals) and draws
   * Resets board between games

2. **Service (`service.py`)**

   * Orchestrates game flow and AI strategy
   * Provides methods for blocking, winning, and random AI moves
   * Interfaces between board state and UI

3. **User Interfaces**

   * **Console UI (`ui.py` – `UI` class & console starter)**

     * Text-based play loop with coordinate input
     * Displays board state after each move
   * **GUI (`ui.py` – `GUI` class & gui starter)**

     * Tkinter-based interactive grid
     * Scoreboard and restart functionality

4. **Tests (`tests.py`)**

   * Validates move legality
   * Checks win conditions across all directions
   * Ensures AI correctly blocks or wins when possible
   * Confirms draw detection and board reset

---

## 🚀 Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Nikole-Labo/Python-Projects.git
   cd Python-Projects/Gomoku_Game
   ```

2. Run the console version:

   ```bash
   python start.py
   ```

3. Run the GUI version:

   ```bash
   python start_gui.py
   ```

4. Run tests:

   ```bash
   python -m unittest tests.py
   ```

---
Enjoy playing Gomoku in both console and GUI modes, and challenge the AI that blocks, wins, and keeps track of your scores!
