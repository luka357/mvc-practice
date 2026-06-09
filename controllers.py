from models import Book
from views import BookView

class BookController:
    def __init__(self, view):
        self.view = view
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        self.view.show_message("Book added!")

    def complete_book(self, index):
        try:
            self.books[index].completed = True
            self.view.show_message("Marked as read!")
        except IndexError:
            self.view.show_message("Invalid number!")
    
    def show_books(self):
        self.view.show_books(self.books)