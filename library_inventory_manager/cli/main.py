import json
from pathlib import Path
from library_manager.inventory import LibraryInventory

# JSON File Path
JSON_FILE = Path("books.json")

inventory = LibraryInventory()  # Create object


# ---------------------------
# Load books from JSON
# ---------------------------
def load_books():
    if JSON_FILE.exists():
        with open(JSON_FILE, "r") as file:
            try:
                data = json.load(file)
                for book_data in data:
                    new_book = inventory.add_book(
                        book_data["title"],
                        book_data["author"],
                        book_data["isbn"]
                    )
                    new_book.status = book_data.get("status", "available")
            except:
                print("Error loading JSON file!")


# ---------------------------
# Save books to JSON
# ---------------------------
def save_books():
    data = []
    for book in inventory.books:
        data.append({
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "status": book.status
        })

    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ---------------------------
# MENU OPTIONS
# ---------------------------
def menu():
    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book by Title")
    print("4. Search Book by ISBN")
    print("5. Issue a Book")
    print("6. Return a Book")
    print("7. Exit")
    print("======================================")



# ---------------------------
# MAIN PROGRAM LOOP
# ---------------------------
def main():
    load_books()

    while True:
        menu()
        choice = input("Enter your choice: ")

        # 1. Add Book
        if choice == "1":
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")
            inventory.add_book(title, author, isbn)
            save_books()
            print("Book Added Successfully!")

        # 2. View All Books
        elif choice == "2":
            books = inventory.display_all()
            if not books:
                print("\nNo books available.")
            else:
                print("\n----- All Books -----")
                for book in books:
                    print(book)

        # 3. Search by Title
        elif choice == "3":
            title = input("Enter Title to Search: ")
            result = inventory.search_by_title(title)
            if result:
                for book in result:
                    print(book)
            else:
                print("No book found with this title.")

        # 4. Search by ISBN
        elif choice == "4":
            isbn = input("Enter ISBN: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                print(book)
            else:
                print("No book found with this ISBN.")

        # 5. Issue Book
        elif choice == "5":
            isbn = input("Enter ISBN: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                if book.issue():
                    save_books()
                    print("Book Issued Successfully!")
                else:
                    print("Book is already issued.")
            else:
                print("Book not found.")

        # 6. Return Book
        elif choice == "6":
            isbn = input("Enter ISBN: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                book.return_book()
                save_books()
                print("Book Returned Successfully!")
            else:
                print("Book not found.")

        # 7. Exit
        elif choice == "7":
            print("Exiting... Saving Data...")
            save_books()
            break

        else:
            print("Invalid choice! Please try again.")


# Run Program
if __name__ == "__main__":
    main()
