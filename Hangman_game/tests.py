import unittest
from unittest.mock import patch
from repository import Repository, NoWords, SmallWord, Duplicate, InputError


class TestRepository(unittest.TestCase):

    def setUp(self):
        self.repo = Repository("test_sentences.txt")

    def test_load_file(self):
        self.repo.load_file()
        self.assertEqual(len(self.repo.sentences), 2) 

    def test_check_empty(self):
        with self.assertRaises(NoWords):
            self.repo.check_empty('')
        with self.assertRaises(NoWords):
            self.repo.check_empty(' ')

    def test_check_small(self):
        with self.assertRaises(SmallWord):
            self.repo.check_small('a bc def')

    def test_check_duplicate(self):
        self.repo.sentences = ['sentence 1\n', 'sentence 2\n']
        with self.assertRaises(Duplicate):
            self.repo.check_duplicate('sentence 1')

    def test_save_sentence(self):
        self.repo.save_sentence('new sentence')
        self.assertIn('new sentence\n', self.repo.sentences)

    def test_choose_sentence(self):
        with patch('random.choice', return_value='random sentence\n'):
            chosen_sentence = self.repo.choose_sentence()
            self.assertEqual(chosen_sentence, 'random sentence\n')

    def test_hangman_sentence(self):
        sentence = 'hello world'
        hangman_style = self.repo.hangman_sentence(sentence)
        self.assertEqual(hangman_style, 'h___o wo__d')

    def test_verify_input(self):
        self.repo.letters = ['a', 'b', 'c']
        self.assertTrue(self.repo.verify_input('a')) 
        self.assertFalse(self.repo.verify_input('d')) 

    def tearDown(self):
        self.repo = None


if __name__ == '__main__':
    unittest.main()
