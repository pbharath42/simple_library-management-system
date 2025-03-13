# Library Management System

class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"{self.book_id} | {self.title} by {self.author} | Available: {self.quantity}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")
    
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("Library Books:")
        print("ID | Title | Author | Available Quantity")
        for book in self.books:
            print(book)
    
    def search_book(self, search_term):
        found_books = [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]
        if not found_books:
            print(f"No books found with the term '{search_term}'.")
        else:
            print("Search Results:")
            for book in found_books:
                print(book)
    
    def delete_book(self, book_id):
        book_to_delete = None
        for book in self.books:
            if book.book_id == book_id:
                book_to_delete = book
                break
        
        if book_to_delete:
            self.books.remove(book_to_delete)
            print(f"Book '{book_to_delete.title}' deleted successfully!")
        else:
            print(f"Book with ID {book_id} not found.")
    
    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.quantity > 0:
                    book.quantity -= 1
                    print(f"You have borrowed '{book.title}'.")
                else:
                    print(f"Sorry, '{book.title}' is currently out of stock.")
                return
        print(f"Book with ID {book_id} not found.")
    
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.quantity += 1
                print(f"You have returned '{book.title}'.")
                return
        print(f"Book with ID {book_id} not found.")

# Main function to interact with the system
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Display All Books")
        print("3. Search for a Book")
        print("4. Delete a Book")
        print("5. Borrow a Book")
        print("6. Return a Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            quantity = int(input("Enter quantity: "))
            new_book = Book(book_id, title, author, quantity)
            library.add_book(new_book)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            search_term = input("Enter book title or author to search: ")
            library.search_book(search_term)

        elif choice == "4":
            book_id = input("Enter book ID to delete: ")
            library.delete_book(book_id)

        elif choice == "5":
            book_id = input("Enter book ID to borrow: ")
            library.borrow_book(book_id)

        elif choice == "6":
            book_id = input("Enter book ID to return: ")
            library.return_book(book_id)

        elif choice == "7":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the system
if __name__ == "__main__":
    main()
