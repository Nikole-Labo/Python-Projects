from unittest.case import TestCase
from A8_2_2.domain.validators_exceptions import BookValidatorException, ClientValidatorException, InputError
from A8_2_2.repository.book_repository import Book_Repository
from A8_2_2.services.book_services import Book_services



import unittest

class TestBookServices(unittest.TestCase):
    def setUp(self):
        self.book_repository = Book_Repository()
        self.book_services = Book_services(self.book_repository)

    def test_add_book_valid(self):
        book_id = "1234"
        self.book_services.add_book(book_id, "The Great Gatsby", "F. Scott Fitzgerald")
        self.assertTrue(self.book_services.find_book_id_services(book_id))

    def test_add_book_existing_id(self):
        self.book_services.add_book("5678", "To Kill a Mockingbird", "Harper Lee")
        with self.assertRaises(BookValidatorException):
            self.book_services.add_book("5678", "New Book", "New Author")

    def test_add_book_invalid_id(self):
        with self.assertRaises(BookValidatorException):
            self.book_services.add_book("abcd", "Invalid Book", "Invalid Author")
        with self.assertRaises(BookValidatorException):
            self.book_services.add_book("12", "Invalid Book", "Invalid Author")

    def test_add_book_empty_title_author(self):
        with self.assertRaises(BookValidatorException):
            self.book_services.add_book("1234", "", "")

    def test_update_book_invalid(self):
        book_id = "5678"
        self.book_services.add_book(book_id, "Another Book", "Another Author")
        with self.assertRaises(BookValidatorException):
            self.book_services.update_book(book_id, "", "New Author")

    def test_delete_book_valid(self):
        book_id = "1234"
        self.book_services.add_book(book_id, "Test Book", "Test Author")
        self.book_services.delete_book(book_id)
        result = self.book_services.find_book_id_services(book_id)
        print("Result:", result)
        self.assertFalse(result)
    def test_delete_book_invalid_id(self):
        with self.assertRaises(InputError):
            self.book_services.delete_book("invalid_id")

    def test_delete_book_nonexistent(self):
        with self.assertRaises(InputError):
            self.book_services.delete_book("9999")

    def test_list_books_with_books(self):
        self.book_services.add_book("1234", "Book 1", "Author 1")
        self.book_services.add_book("5678", "Book 2", "Author 2")
        expected_result = self.book_repository.get_all_books()
        result = self.book_services.list_books()
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
