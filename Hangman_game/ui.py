from repository import Repository
from board import Board
from errors import NoWords, SmallWord, Duplicate, InputError


class UI:

    def __init__(self, board):
        self.__board = board
        self.exit_flag = False

    def print_menu(self):
        print("_________________________________")
        print("1.add new sentence")
        print("2.play game")
        print("3.exit")
        print("_________________________________")

    def get_input (self, txt="->"):
        return input(txt)

    def choose_option(self, option):
        if option == "1":
            self.add_sentence()
        elif option == "2":
            self.play_game()
        elif option == '3':
            self.exit_flag = True
        else:
            print("invalid choice")

    def add_sentence(self):
        try:
            sentence = self.get_input("Give the new sentence: ")
            self.__board.write_sentence(sentence)
        except NoWords as nw:
            print(nw)
        except SmallWord as sm:
            print(sm)
        except Duplicate as dup:
            print(dup)

    def play_game(self):
        self.__board.start_game()
        while not self.__board.end_game():
            try:
                sentence, hangman = self.__board.current_state()
                print(sentence)
                print(hangman)
                user_input = self.get_input("chose a letter: ")
                self.__board.update_status(user_input)
            except InputError as ve:
                print(ve)
        sentence, hangman = self.__board.current_state()
        print(sentence)
        print(hangman)
        if self.__board.end_game():
            print(self.__board.who_won())


    def start(self):
        while not self.exit_flag:
            self.print_menu()
            option = self.get_input()
            self.choose_option(option)

