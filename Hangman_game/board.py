import random
from repository import Repository

class Board:

    def __init__(self, repository):
        self.__repository = repository
        self.sentence = ''
        self.transformed_sentence = ''
        self.hangman = ''
        self.mistake = 0

    def write_sentence(self, sentence):
        self.__repository.check_empty(sentence)
        self.__repository.check_small(sentence)
        self.__repository.check_duplicate(sentence)
        self.__repository.save_sentence(sentence)

    def start_game(self):
        self.__repository.restart()
        self.sentence = self.__repository.choose_sentence()
        self.transformed_sentence = self.__repository.hangman_sentence(self.sentence)
        self.hangman = ''
        self.mistake = 0

    def current_state(self):
        return self.transformed_sentence, self.hangman

    def end_game(self):
        if self.hangman == 'hangman' or self.transformed_sentence == self.sentence:
            return True

    def update_hangman(self):
        letter_list = 'hangman'
        self.hangman += letter_list[self.mistake-1]

    def update_status(self, user_input):
        aux_transformed = list(self.transformed_sentence)
        aux = self.sentence
        found = False
        if self.__repository.verify_input(user_input):
            self.mistake += 1
            self.update_hangman()
        for i in range(0, len(aux)-1):
            if aux[i] == user_input:
                aux_transformed[i] = user_input
                found = True
        if not found:
            self.mistake += 1
            self.update_hangman()
        self.transformed_sentence = ''.join(aux_transformed)

    def who_won(self):
        if self.hangman == 'hangman':
            return 'Oh no! You lost! :('
        else:
            return 'Hurray! You won :D'
