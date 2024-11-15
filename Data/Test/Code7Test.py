import unittest
from Code7Correct.py import Library  # Replace with the actual file name if different

class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Initialize the library and add some test books
        self.library = Library()
        self.library.add_book("1984", "George Orwell", 3)
        self.library.add_book("To Kill a Mockingbird", "Harper Lee", 2)

    def test_add_book(self):
        # Test adding a new book
        self.library.add_book("Brave New World", "Aldous Huxley", 5)
        books = self.library.list_books()
        self.assertIn("Brave New World by Aldous Huxley (5 copies)", books)

    def test_add_existing_book(self):
        # Test adding copies of an existing book
        self.library.add_book("1984", "George Orwell", 2)
        books = self.library.list_books()
        self.assertIn("1984 by George Orwell (5 copies)", books)

    def test_borrow_book_success(self):
        # Test borrowing a book successfully
        response = self.library.borrow_book("1984")
        self.assertEqual(response, "You have borrowed '1984' by George Orwell.")
        books = self.library.list_books()
        self.assertIn("1984 by George Orwell (4 copies)", books)

    def test_borrow_book_unavailable(self):
        # Test borrowing a book that is not available
        self.library.borrow_book("1984")
        self.library.borrow_book("1984")
        self.library.borrow_book("1984")
        response = self.library.borrow_book("1984")
        self.assertEqual(response, "Book not available.")

    def test_return_book(self):
        # Test returning a book
        self.library.borrow_book("1984")
        self.library.return_book("1984")
        books = self.library.list_books()
        self.assertIn("1984 by George Orwell (4 copies)", books)

    def test_return_book_new_book(self):
        # Test returning a book that is not in the library yet
        self.library.return_book("The Catcher in the Rye")
        books = self.library.list_books()
        self.assertIn("The Catcher in the Rye by Unknown (1 copies)", books)

    def test_list_books_empty(self):
        # Test when there are no books in the library
        empty_library = Library()
        response = empty_library.list_books()
        self.assertEqual(response, "No books in the library.")

    def test_list_books_non_empty(self):
        # Test listing books when there are books in the library
        books = self.library.list_books()
        self.assertIn("1984 by George Orwell (3 copies)", books)
        self.assertIn("To Kill a Mockingbird by Harper Lee (2 copies)", books)

if __name__ == '__main__':
    unittest.main()

