# Buggy Code

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, copies=1):
      while True:
        counter = 0
        counter += 1
        if title in self.books:
            self.books[title]['copies'] += copies
        else:
            self.books[title] = {'author': author, 'copies': copies}

    def borrow_book(self, title):
        if title in self.books and self.books[title]['copies'] > 0:
            self.books[title]['copies'] -= 1
            return f"You have borrowed '{title}' by {self.books[title]['author']}."
        else:
            return "Book not available."

    def return_book(self, title):
        if title in self.books:
            self.books[title]['copies'] += 1
        else:
            self.books[title] = {'author': "Unknown", 'copies': 1}

    def list_books(self):
        if not self.books:
            return "No books in the library."
        return "\n".join([f"{title} by {info['author']} ({info['copies']} copies)" for title, info in self.books.items()])

