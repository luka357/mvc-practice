class BookView:
    def show_books(self, books):
        if not books:
            print("No books yet")
            return
        
        print("\nYour books:")
        for i, book in enumerate(books, start=1):
            status = "Read" if book.completed else "Not read"
            print(f"{i}. {book.title} - {book.author} - {status}")

    def show_message(self, message):
        print(message)