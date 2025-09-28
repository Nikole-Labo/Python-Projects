# Hangman – Word Guessing Game

This is a classic console-based implementation of **Hangman**, the word guessing game. Users try to guess a hidden sentence by suggesting letters within a limited number of attempts.

---

## 🎯 Features & Functionality

- Random selection of a secret sentence from a predefined list  
- Display the sentence with blanks (e.g. `c_ _ _s a_e c_ _ e`) and reveal letters as they are guessed  
- Track letters guessed so far and show incorrect guesses  
- Limit number of incorrect guesses (the "hangman" life count)  
- Input validation: ensure user inputs a single letter, not already guessed, within alphabet  
- Option to restart or quit after each game  

---

## 🛠 How it works (modules / flow)

1. **Sentence list loader**  
   Loads a list of valid secret sentences (from file or built-in list).  

2. **Game logic**  
   - Choose a random secret sentence 
   - Maintain sets/arrays: `guessed_letters`, `incorrect_letters`  
   - At each turn:  
     - Prompt user for a letter  
     - Check if letter is in secret word  
     - Reveal positions, or count as wrong guess  
     - Check end conditions: word guessed or max wrong guesses reached  

3. **User interface (console)**  
   - Show current status: revealed letters, wrong guesses, remaining attempts  
   - Prompt user for input  
   - Show win or loss messages  
   - Option to play again  

4. **Utility / helper functions**  
   - Validate user input  
   - Update game state  
   - Render the board (blanks + revealed letters)  


## 🚀 Usage

Run the main script (e.g. `python hangman.py`) and follow the prompts.

Have fun trying to guess the word before you run out of lives!  
