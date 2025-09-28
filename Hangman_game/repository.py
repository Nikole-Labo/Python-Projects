from errors import SmallWord, NoWords, Duplicate, InputError
import random


class Repository:

    def __init__(self, file_name):
        self.__file_name = file_name
        self.sentences = []
        self.load_file()
        self.save_file()
        self.letters = []

    def restart(self):
        self.letters = []

    def load_file(self):
        """
        Load sentences from a file and populate the sentences list.
        """
        with open(self.__file_name, 'r') as f:
            file_content = f.read() 
            print("File Content:", repr(file_content))
            sentences = file_content.split('\n')
            for sentence in sentences:
                sentence = sentence.strip() 
                if sentence: 
                    print("Read sentence:", repr(sentence)) 
                    self.sentences.append(sentence)
    def check_empty(self, sentence):
        """
        Check if a sentence is empty.

        Raises:
        NoWords: If the sentence is empty.

        param:
        sentence ->string
        """
        if '' == sentence:
            raise NoWords("This was an empty space:(")
        nr = 0
        words = sentence.split(' ')
        for word in words:
            nr += 1
        if nr < 3:
            raise NoWords("That was not a complete sentence")

    def check_small(self, sentence):
        """
        Check if all words in a sentence are long enough.

        Args:
            sentence (str): The sentence to check.

        Raises:
            SmallWord: If any word in the sentence is too short.
        """
        words = sentence.split(' ')
        for word in words:
            if len(word) < 3:
                raise SmallWord("The words were not long enough")

    def check_duplicate(self, sentence):
        """
        Check if a sentence is a duplicate of any existing sentence.

        Args:
            sentence (str): The sentence to check.

        Raises:
            Duplicate: If the sentence is already in the list.
        """
        sentence += '\n'
        for s in self.sentences:
            if s == sentence:
                raise Duplicate("This sentence is already in the list")

    def save_sentence(self, sentence):
        """
        Save a new sentence to the repository.

        Args:
            sentence (str): The sentence to save.
        """
        self.sentences.append(sentence.strip() + '\n')
        self.save_file()

    def save_file(self):
        f = open(self.__file_name, 'w')
        for s in self.sentences:
            f.write(s)
        f.close()

    def choose_sentence(self):
        """
        Choose a random sentence from the repository.

        Returns:
            str: A randomly chosen sentence.
        """
        chosen_sentence = random.choice(self.sentences)
        return chosen_sentence

    def hangman_sentence(self, sentence):
        """
        Transform a sentence into a hangman-style representation.

        Args:
            sentence (str): The sentence to transform.

        Returns:
            str: The transformed sentence.
        """
        new_sentence = ''
        self.letters.append(sentence[0])
        self.letters.append(sentence[len(sentence)-1])
        for i in range(0, len(sentence)-1):
            if sentence[i] == ' ':
                self.letters.append(sentence[i-1])
                self.letters.append(sentence[i+1])
        for letter in sentence:
            if letter not in self.letters and letter != ' ':
                new_sentence += "_"
            else:
                new_sentence += letter
        return new_sentence

    def verify_input(self, user_input):
        """
        Verify if user input is a letter and if it's already been guessed.

        Args:
            user_input (str): The user input to verify.

        Returns:
            bool: True if the input is a new letter, False otherwise.
        """
        if not user_input.isalpha():
            raise InputError("That was not a letter :((")
        if user_input in self.letters:
            return True
        else:
            self.letters.append(user_input)
            return False
