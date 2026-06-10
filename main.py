from views import BookView
from controllers import BookController

def main():
    view = BookView()
    controller = BookController(view)

    while True:
        print("\n1. Add book")
        print("2. Mark as read")
        print("3. Show books")
        print("4. Exit")

        choice = input("Option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            controller.add_book(title, author)
        
        elif choice == "2":
            controller.show_books()
            index = int(input("Book number: ")) - 1
            controller.complete_book(index)

        elif choice == "3":
            controller.show_books()

        elif choice == "4":
            break

        else:
            view.show_message("Invalid option!")   
                     
if __name__ == "__main__":
    main()

